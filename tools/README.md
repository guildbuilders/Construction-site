# Site generators

These build the individual project pages and wire them into the galleries,
the city pages and the sitemap. They are NOT part of the deployed site -
`.assetsignore` keeps `tools/` out of the Cloudflare upload.

## Usage

    cd tools
    python3 build_projects.py     # writes/refreshes every project page
    python3 wire_projects.py      # gallery links, city cards, sitemap entries

`build_projects.py` holds the kitchen projects and imports the bathroom and
whole-home lists. Each project is a dict: page, project, city, city_page,
prefix, photos, anchor, blurb, hero_sub, specs, body, plus optional
hero_photo / hero_pos / related / gallery_h2 / kind.

## Before you rebuild: `--check`

    python3 build_projects.py --check

Builds every page in memory and reports which existing ones a real run would
change, without writing anything. Exit 0 means nothing would move; exit 1 lists
the pages that would.

Run it after editing `build_projects.py`, and after any change to the shared
head, footer or asset versions. **A page you did not intend to touch showing up
as CHANGED means the template has drifted from the live pages.** That is not
theoretical: this template sat at the pre-swap head for weeks, and a rebuild on
2026-08-28 would have put the stripped `gtag.js` layer back on all 42 project
pages (double counting every Ads conversion), reverted the Stape custom loader
to the plain googletagmanager one, rolled `style.css` and `script.js` backwards
and dropped `tracking.js` entirely.

## Where the shared chrome comes from

The project pages do not carry their own copy of the site chrome. At build time
`build_projects.py` lifts these out of `index.html` (`REFERENCE`):

- the Stape custom loader block and its `noscript` counterpart
- `style.css?v=`, `script.js?v=` and `tracking.js?v=`

So the way to change them on the project pages is to change them on
`index.html` and rebuild. Do not paste a second copy into the generator: a
second copy is exactly what drifted. If an extraction fails, or if `index.html`
is found to carry a hardcoded `gtag.js` layer, the build stops rather than
shipping a wrong head.

## Rules the scripts enforce

- Spec counts must be EVEN. An odd count strands the last item alone in the
  two-column strip; the build fails rather than shipping it.
- `kind` is "kitchen", "bathroom" or "fullhome" and drives titles, schema
  serviceType, headings, service-page links and back-links.
- `hero_photo` overrides which photo leads the page; `hero_pos` sets its crop
  (both carry through to the city-page card).
- Bump CSS/JS version query strings after editing style.css or landing.css,
  or the edge serves stale files.

## Site gotchas

- Cloudflare serves this site WITHOUT .html. `/kitchens-cabinets` is 200;
  `/kitchens-cabinets.html` 307s to it. Always link and list the
  extensionless form.
- Never advertise "bonded", and never say "insured" without naming the type
  of insurance - B&P 7027.4.
