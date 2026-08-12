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

# the async loader plus the inline config script that follows it
GTAG_BLOCK = re.compile(
    r'[ \t]*<!-- Google Ads / gtag -->\s*'
    r'|[ \t]*<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*'
    r'<script>.*?</script>\s*',
    re.S)
ONCLICK  = re.compile(r'\s*onclick="return gb_callConversion\(\);"')
GB_FUNC  = re.compile(r'\n?[ \t]*function gb_callConversion\(\)\s*\{.*?\n[ \t]*\}\n', re.S)


def preflight():
    """Read the live container and confirm it carries what the gtag block does."""
    url = f"https://www.googletagmanager.com/gtm.js?id={GTM_ID}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        js = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    except Exception as e:
        return False, [f"could not fetch the container: {e}"]

    missing = [label for needle, label in (
        (GA4_ID,   f"GA4 config ({GA4_ID})"),
        (ADS_ID,   f"Ads config ({ADS_ID})"),
        (PHONE_LB, f"phone conversion label ({PHONE_LB})"),
        (FORM_LB,  f"form conversion label ({FORM_LB})"),
    ) if needle not in js]

    m = re.search(r'"tags":\s*\[(.*?)\]\s*,\s*"predicates"', js, re.S)
    if m and not m.group(1).strip():
        missing.append("the container's tag array is empty")
    return (not missing), missing


def main():
    apply_ = "--apply" in sys.argv
    force  = "--force" in sys.argv
    os.chdir(SITE)

    ok, missing = preflight()
    print(f"GTM preflight on {GTM_ID}: {'PASS' if ok else 'FAIL'}")
    for m in missing:
        print(f"   missing: {m}")
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
        s, n_func    = GB_FUNC.subn("\n", s)
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
    js2, n_js = GB_FUNC.subn("\n", js)
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
