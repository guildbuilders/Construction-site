"""Ad 4 - before/after statics, 1080x1350 (4:5 Meta feed).

Two versions: a bathroom (side-by-side, portrait sources) and a kitchen
(stacked, landscape sources). Both framing choices were arrived at by looking
at renders, not by reasoning about the numbers.
"""
from PIL import Image, ImageDraw
from gbads import *

W, H = 1080, 1350

def build(pair, headline, place, layout="side", fb=0.5, fa=0.5, out="ad4.png"):
    c = Image.new("RGB", (W, H), NAVY)

    if layout == "side":
        hw = W // 2
        c.paste(fit_crop(load(f"{pair}-before.webp"), hw, H, fb), (0, 0))
        c.paste(fit_crop(load(f"{pair}-after.webp"), W - hw, H, fa), (hw, 0))
        d = ImageDraw.Draw(c)
        d.rectangle([hw - 2, 0, hw + 1, H], fill=GOLD)
        fpill = font("heavy", 26)
        pill(d, (34, 54), "BEFORE", NAVY, WHITE, fpill)
        pill(d, (hw + 30, 54), "AFTER", GOLD, NAVY, fpill)
        scrim(c, 820)
        d = ImageDraw.Draw(c)
        hsize, lead, base = 60, 72, 1150
    else:
        # 500px panels framed at 0.7. Full 1.6-ratio panels were tried and
        # rejected: they leave nowhere for the text except over the island.
        ph = 500
        c.paste(fit_crop(load(f"{pair}-before.webp"), W, ph, fb), (0, 0))
        c.paste(fit_crop(load(f"{pair}-after.webp"), W, ph, fa), (0, ph + 4))
        d = ImageDraw.Draw(c)
        d.rectangle([0, ph, W, ph + 3], fill=GOLD)
        fpill = font("heavy", 26)
        pill(d, (34, 40), "BEFORE", NAVY, WHITE, fpill)
        pill(d, (34, ph + 44), "AFTER", GOLD, NAVY, fpill)
        hsize, lead, base = 52, 62, 1168

    fh = font("bold", hsize)
    lines = wrap(d, headline, fh, W - 128)
    top = base - lead * len(lines)
    for i, ln in enumerate(lines):
        d.text((60, top + i * lead), ln, font=fh, fill=WHITE)
    ls_text(d, (60, top - 50), place.upper(), font("demi", 24), GOLD_H, 4.0)

    logo_lockup(c, d, 1266)
    c.save(out, quality=95)
    print("wrote", out, layout)

if __name__ == "__main__":
    build("ba-orchidia", "From builder-grade tub to daily luxury spa.",
          "Camino de Orchidia, Encinitas", "side", out="ad4_primary.png")
    # NOTE: ba-tynebourne-* is misnamed. It is a KITCHEN pair, and the kitchen
    # is Kingsfield Court, not Tynebourne Circle. Do not rename the files:
    # kitchen-remodel-a.html (the Google Ads landing page) loads them by name.
    build("ba-tynebourne", "From dark and dated to the best room in the house.",
          "Kingsfield Court, San Diego", "stack", fb=0.7, fa=0.7, out="ad4_variant.png")
