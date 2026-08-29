#!/usr/bin/env python3
"""Wire every generated project page into the gallery, its city page and the
sitemap. Driven off build_projects.PROJECTS so the link list can never drift
out of step with the pages themselves.
"""
import os, re, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_projects import PROJECTS, SITE

CARD_BLURB = {p["page"]: p["blurb"] for p in PROJECTS}


def link_for(p):
    """The gallery detail link. Written and checked through the same function so
    the idempotency guard can never drift from what is emitted again."""
    return f'<a href="{p["page"][:-5]}" class="project-detail-link">See how we built it &rarr;</a>'


def wire():
    os.chdir(SITE)

    # ---- gallery: one detail link per project, photos untouched ----
    for f, kind in (("kitchens-cabinets.html", "kitchen"), ("bathrooms.html", "bathroom"),
                    ("full-home-renovations.html", "fullhome")):
      s = open(f, encoding="utf-8").read()
      added = 0
      for p in [q for q in PROJECTS if q.get("kind", "kitchen") == kind]:
        # Match the href actually written below, which is extensionless. Testing
        # for p["page"] here looked for the .html form, which this script never
        # writes, so the guard could not see its own output and every run added
        # another link. By the time it was noticed all 39 projects carried nine
        # copies apiece, 351 tags where 39 belong.
        if link_for(p) in s:
            continue
        anchor = p["anchor"].split("#")[1]
        pat = re.compile(rf'(<section id="{anchor}"[^>]*>\s*<div class="container">\s*)'
                         rf'<p class="section-label">[^<]*</p>(\s*<h2>[^<]*</h2>\s*)')
        m = pat.search(s)
        if not m:
            print(f"  !! anchor not found: {anchor}"); continue
        s = (s[:m.start()]
             + m.group(1)
             + f'<p class="section-label">{p["project"]} &middot; {p["city"]}</p>'
             + m.group(2)
             + link_for(p) + '\n\n        '
             + s[m.end():])
        added += 1
      open(f, "w", encoding="utf-8").write(s)
      want = [q for q in PROJECTS if q.get("kind", "kitchen") == kind]
      present = sum(1 for p in want if link_for(p) in s)
      print(f"{f}: +{added} links, {present}/{len(want)} present")

    # ---- city pages ----
    # A house with a whole-home page would otherwise show three cards on its
    # city page - kitchen, bathrooms and whole home. Show only the whole-home
    # card there; the other two stay linked from their galleries and from the
    # whole-home page itself.
    superseded = {q["project"] for q in PROJECTS if q.get("kind") == "fullhome"}
    by_city = defaultdict(list)
    for p in PROJECTS:
        if p.get("kind", "kitchen") != "fullhome" and p["project"] in superseded:
            continue
        by_city[p["city_page"]].append(p)

    def card(p, note=""):
        Label = {"bathroom": "Bathroom Remodel", "fullhome": "Whole Home Renovation"}.get(
            p.get("kind", "kitchen"), "Kitchen Remodel")
        first = p.get("hero_photo", list(p["photos"])[0])
        pos = f' style="object-position: {p["hero_pos"]}"' if p.get("hero_pos") else ""
        return (f'\n        <a class="city-project" href="{p["page"][:-5]}">\n'
                f'          <img src="{p["prefix"]}{first}-1000.webp" alt="{p["project"]} &mdash; {Label.lower()} in {p["city"]}" loading="lazy"{pos} />\n'
                f'          <div class="city-project-body">\n'
                f'            <h3>{p["project"]} &mdash; {Label}{note}</h3>\n'
                f'            <p>{CARD_BLURB[p["page"]]}</p>\n'
                f'            <span class="city-project-cta">See the project &rarr;</span>\n'
                f'          </div>\n        </a>\n')

    def write_city(cf, heading, cards, n):
        t = open(cf, encoding="utf-8").read()
        t = re.sub(r'    <section class="section">\s*<div class="container">\s*'
                   r'<p class="section-label">Recent Work</p>.*?</section>\n\n', '', t, flags=re.S)
        block = ('    <section class="section">\n      <div class="container">\n'
                 '        <p class="section-label">Recent Work</p>\n'
                 f'        <h2>{heading}</h2>\n{cards}\n      </div>\n    </section>\n\n')
        i = t.rindex('    <section class="section section-alt">')
        open(cf, "w", encoding="utf-8").write(t[:i] + block + t[i:])
        print(f"  {cf}: {n} project(s)")

    for cf, items in sorted(by_city.items()):
        city = items[0]["city"]
        write_city(cf, f"Recent Projects in {city}",
                   "".join(card(p) for p in items), len(items))

    # Del Mar shows neighbouring Carmel Valley work, labelled as such
    cv = by_city.get("carmel-valley.html", [])
    if cv:
        write_city("del-mar.html", "Recent Work Near Del Mar",
                   "".join(card(p, " in Carmel Valley") for p in cv), len(cv))

    # ---- sitemap ----
    sm = open("sitemap.xml", encoding="utf-8").read()
    # Two traps here, both of the same family as the gallery guard above: the
    # guard has to match what is actually in the file, and the insertion point
    # has to exist.
    #
    # 1. Guard on the <loc> alone, not on the whole <url> element. Entries
    #    written by hand carry a <lastmod> and the ones written here do not,
    #    so comparing whole elements never matches an existing entry and every
    #    run would append the same URLs again.
    # 2. Insert before </urlset>, not after a named page. This anchored on
    #    ".../kitchens-cabinets.html" and went silently dead the moment the
    #    sitemap was converted to extensionless URLs - `add` was computed
    #    correctly and then thrown away by a replace that matched nothing.
    def url_for(p):
        return f'https://guildbuildersgroup.com/{p["page"][:-5]}'
    add = "".join(f'  <url><loc>{url_for(p)}</loc></url>\n'
                  for p in PROJECTS if f'<loc>{url_for(p)}</loc>' not in sm)
    if add:
        assert "</urlset>" in sm, "sitemap.xml has no </urlset> to insert before"
        sm = sm.replace("</urlset>", add + "</urlset>")
        open("sitemap.xml", "w", encoding="utf-8").write(sm)
    print("sitemap urls:", sm.count("<url>"))


if __name__ == "__main__":
    wire()
