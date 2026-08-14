#!/usr/bin/env python3
"""Remove the hardcoded gtag from the site, once GTM is carrying the tags.

Run AFTER the marketing partner has published GA4, the Ads conversion linker,
the tel: click conversion and the thank-you form conversion into GTM-P526Z2L9.

The two halves have to land in the same window. Publish GTM without removing
this and every pageview and conversion counts twice; remove this before GTM is
live and the site measures nothing at all, silently, while Ads smart bidding
keeps spending against a signal that stopped arriving.

That is what the preflight is for: it reads the live container and refuses to
touch anything unless the tags are actually in it. It is not a formality. The
container was inspected on 2026-08-12 and its tag array was empty.

Dry run by default. Pass --apply to write.

    python3 tools/strip_gtag.py              # report only
    python3 tools/strip_gtag.py --apply      # write the changes
    python3 tools/strip_gtag.py --force      # skip the GTM preflight (don't)
"""
import os, re, sys, glob, json, urllib.request

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GTM_ID   = "GTM-P526Z2L9"
GA4_ID   = "G-39ZPTZ73DK"
ADS_ID   = "AW-18096983407"
PHONE_LB = "4xQWCNa0wdwcEO-aqLVD"
FORM_LB  = "01S8CJac9d4cEO-aqLVD"

# The async loader plus the inline config script that follows it, and the
# comment above it. Three comment wordings are in use across the 98 pages -
# "Google Ads / gtag", "Google tag (gtag.js)", and one on 404.html that names
# the GA4 id inline. Missing a variant leaves a comment claiming the page
# routes to Ads and GA4 when it no longer does, which is how the next person
# reading this file gets misled.
GTAG_BLOCK = re.compile(
    r'[ \t]*<!-- Google (?:Ads / gtag|tag \(gtag\.js\))[^>]*-->\s*'
    r'|[ \t]*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*'
    r'<script>.*?</script>\s*',
    re.S)
ONCLICK  = re.compile(r'\s*onclick="return gb_(?:callConversion|bookingClick)\(\);"')

GB_FUNCS = ("gb_callConversion", "gb_bookingClick")


def _comment_start(src, i):
    """Walk back from i over the comment lines that introduce the function, so
    the explanation goes out with the thing it explains."""
    while True:
        line_start = src.rfind("\n", 0, i - 1) + 1 if i else 0
        if line_start >= i:
            return i
        line = src[line_start:i].strip()
        if line.startswith("//"):
            i = line_start
        elif line.endswith("*/"):
            open_at = src.rfind("/*", 0, i)
            if open_at == -1:
                return i
            i = src.rfind("\n", 0, open_at) + 1
        else:
            return i


def strip_function(src, name):
    """Remove `function name() { ... }` by COUNTING BRACES, not by regex.

    The regex this replaces was `.*?\\n[ \\t]*\\}\\n` non-greedy, which stops at
    the first closing brace sitting alone on a line - and gb_callConversion has
    one, the inner `if (typeof gtag === "function") { ... }`. It cut the
    function in half and left `return true; }` at the top level, so script.js
    became a syntax error and every scripted feature on the site would have
    died silently: menu, gallery, hero video, the lot. Grepping for the
    function name said it was gone. `node --check` said otherwise.
    """
    pattern = re.compile(r'function\s+' + re.escape(name) + r'\s*\(\s*\)\s*\{')
    removed = 0
    while True:
        m = pattern.search(src)
        if not m:
            return src, removed
        n = len(src)
        j = m.end() - 1          # sitting on the opening brace
        depth = 0
        while j < n:
            ch = src[j]
            if ch in "\"'`":     # skip string literals, braces inside don't count
                quote, j = ch, j + 1
                while j < n and src[j] != quote:
                    j += 2 if src[j] == "\\" else 1
                j += 1
            elif src.startswith("//", j):
                j = src.find("\n", j)
                if j == -1:
                    j = n
            elif src.startswith("/*", j):
                k = src.find("*/", j)
                j = n if k == -1 else k + 2
            elif ch == "{":
                depth += 1
                j += 1
            elif ch == "}":
                depth -= 1
                j += 1
                if depth == 0:
                    break
            else:
                j += 1
        if depth != 0:
            raise SystemExit(f"unbalanced braces around {name} - refusing to guess")
        start = _comment_start(src, m.start())
        end = j
        while end < n and src[end] in " \t":
            end += 1
        if end < n and src[end] == "\n":
            end += 1
        src = src[:start] + src[end:]
        removed += 1

# The same-origin endpoint the web container's Google tag points at. In a
# server-side setup this is the thing that proves the container is really
# wired up, because the Ads conversion tags live in the SERVER container and
# never appear in gtm.js at all.
TAGGING_URL = "guildbuildersgroup.com/edge"


def preflight():
    """Read the live container and confirm it carries what the gtag block does."""
    url = f"https://www.googletagmanager.com/gtm.js?id={GTM_ID}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        js = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    except Exception as e:
        return False, [f"could not fetch the container: {e}"], []

    missing, warnings = [], []

    # Hard requirement 1: the container actually carries tags.
    m = re.search(r'"tags":\s*\[(.*?)\]\s*,\s*"predicates"', js, re.S)
    if m and not m.group(1).strip():
        missing.append("the container's tag array is empty")

    # Hard requirement 2: something in there measures. Either the GA4 id is
    # configured in the web container the old way, or there is a Google tag
    # pointing at our own tagging endpoint, which is the server-side way.
    if GA4_ID not in js and TAGGING_URL not in js:
        missing.append(
            f"no GA4 config ({GA4_ID}) and no server_container_url "
            f"({TAGGING_URL}) - nothing in this container measures anything")

    # Soft: with a server-side setup the Ads conversion tags live in the
    # server container and are invisible here, so their absence is not proof
    # of anything. Worth printing, not worth blocking on.
    for needle, label in (
        (ADS_ID,   f"Ads config ({ADS_ID})"),
        (PHONE_LB, f"phone conversion label ({PHONE_LB})"),
        (FORM_LB,  f"form conversion label ({FORM_LB})"),
    ):
        if needle not in js:
            warnings.append(f"{label} not in the web container "
                            f"- expected if it lives in the server container")

    return (not missing), missing, warnings


def main():
    apply_ = "--apply" in sys.argv
    force  = "--force" in sys.argv
    os.chdir(SITE)

    ok, missing, warnings = preflight()
    print(f"GTM preflight on {GTM_ID}: {'PASS' if ok else 'FAIL'}")
    for m in missing:
        print(f"   missing: {m}")
    for w in warnings:
        print(f"   note   : {w}")
    if not ok and not force:
        print("\nRefusing to run. Removing the gtag now would leave the site with no\n"
              "GA4, no Ads conversions and gb_callConversion undefined, and nothing on\n"
              "the page would look wrong. Publish the container first.")
        return 1
    if not ok and force:
        print("\n--force given, proceeding against a container that is not ready.")

    pages = sorted(f for f in glob.glob("*.html") + glob.glob("blog/*.html"))
    stats = dict(pages=0, blocks=0, onclicks=0, gbfunc=0, untouched=0)

    for f in pages:
        s = open(f, encoding="utf-8").read()
        o = s
        s, n_block   = GTAG_BLOCK.subn("", s)
        s, n_click   = ONCLICK.subn("", s)
        n_func = 0
        for name in GB_FUNCS:
            s, k = strip_function(s, name)
            n_func += k
        if s == o:
            stats["untouched"] += 1
            continue
        # the GTM container must survive; it is the whole point of the swap
        if GTM_ID not in s:
            print(f"  !! {f}: GTM snippet would be lost, skipping")
            continue
        stats["pages"] += 1
        stats["blocks"] += n_block
        stats["onclicks"] += n_click
        stats["gbfunc"] += n_func
        if apply_:
            open(f, "w", encoding="utf-8").write(s)

    # gb_callConversion also lives in script.js, for the 94 non-landing pages
    js = open("script.js", encoding="utf-8").read()
    js2, n_js = js, 0
    for name in GB_FUNCS:
        js2, k = strip_function(js2, name)
        n_js += k
    if apply_ and n_js:
        open("script.js", "w", encoding="utf-8").write(js2)

    # a changed script.js needs a new query string or caches keep the old one
    bumped = 0
    if apply_ and n_js:
        cur = re.search(r'script\.js\?v=(\d+)', open(pages[0], encoding="utf-8").read())
        if cur:
            old, new = int(cur.group(1)), int(cur.group(1)) + 1
            for f in pages:
                t = open(f, encoding="utf-8").read()
                t2 = t.replace(f"script.js?v={old}", f"script.js?v={new}")
                if t2 != t:
                    open(f, "w", encoding="utf-8").write(t2)
                    bumped += 1
            print(f"script.js cache-buster: v{old} -> v{new} on {bumped} pages")

    print(f"\n{'APPLIED' if apply_ else 'DRY RUN'}")
    print(f"  pages changed        : {stats['pages']}")
    print(f"  gtag blocks removed  : {stats['blocks']}")
    print(f"  onclick handlers     : {stats['onclicks']}")
    print(f"  gb_callConversion    : {stats['gbfunc']} in pages, {n_js} in script.js")
    print(f"  pages already clean  : {stats['untouched']}")
    if not apply_:
        print("\nNothing written. Re-run with --apply.")
    else:
        print("\nNow verify real traffic: drive the page in headless Chrome and count\n"
              "/g/collect beacons and Ads conversion hits. A page that greps clean can\n"
              "still be sending nothing, which is how the GA4 gap survived a full audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
