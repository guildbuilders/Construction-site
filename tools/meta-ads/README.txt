GUILD BUILDERS - META AD BUILD SCRIPTS
tools/meta-ads/

Regenerates every Meta ad from the site's own photo library. Lives in tools/
so it is version controlled but never uploaded: .assetsignore excludes
"tools" and "tools/**" from the Cloudflare deploy.

An earlier copy of these scripts was written to a system temp directory and
macOS deleted it within days. That is why they live in the repo now.

RUN (from inside this folder)

    python3 make_logo.py     # only if newguild_keyed.png is missing
    python3 ad4.py           # two before/after statics, 1080x1350
    python3 ad5.py           # six carousel cards, 1080x1080
    python3 ad1_reel.py      # 15s vertical reel, 1080x1920

Output lands here and is gitignored. Export to JPG at quality 92 for upload
and keep the deliverables in ~/Desktop/Guild Meta Ads/.

FILES
    gbads.py            palette, fonts, cropping, scrims, logo lockup
    ad4.py ad5.py       the statics
    ad1_reel.py         the reel (pipes raw frames to bundled ffmpeg)
    make_logo.py        keys the transparent wordmark out of the mockup
    newguild_keyed.png  the usable transparent logo
    newguild-source.png the mockup it was keyed from

REQUIREMENTS
    Pillow, numpy, imageio_ffmpeg. All already installed system-wide.
    Photos are read from the repo root, resolved relative to this folder.

THINGS THAT WILL BITE YOU
  - ba-tynebourne-* is a KITCHEN pair and the kitchen is KINGSFIELD COURT.
    Do not rename or delete: kitchen-remodel-a.html loads those files.
  - westwood is engineered QUARTZ. brava, kingsfield, poole are QUARTZITE.
    The site draws this distinction explicitly, so do not generalise it.
  - newguild-source.png is a MOCKUP with a baked-in background and no
    transparency. make_logo.py keys it. The result works on dark grounds only.
  - Scrims must reach solid, not just 76%, or the wordmark washes out.
  - Every ad needs CA Lic #1154614 (B&P 7027.4). Never say "bonded", and
    never "insured" without naming the type.
  - No em dashes in any ad copy.
