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
