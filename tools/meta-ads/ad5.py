"""Ad 5 - educational carousel, six cards at 1080x1080.

The guide's Card 3 (pull-out drawers) and Card 4 (concealed trash) were
dropped: no such photos exist in the 1057-image library. Pantry and bar were
substituted rather than faking them.

Material names are per-project and must not be generalised: westwood is
engineered QUARTZ; brava, kingsfield and poole are QUARTZITE.
"""
from PIL import Image, ImageDraw
from gbads import *

S = 1080

CARDS = [
    ("westwood5-2000.webp",   "01", "Waterfall quartz island",      "Stone that wraps the edge to the floor",
     "Westwood Drive, Carlsbad", 0.25),
    ("kingsfield4-2000.webp", "02", "Contrasting island cabinetry", "Navy base against warm white oak",
     "Kingsfield Court, San Diego", 0.35),
    ("poole8-2000.webp",      "03", "Concealed pantry storage",     "Full-height doors, nothing on show",
     "Poole Street, La Jolla", 0.5),
    ("caminito4-2000.webp",   "04", "Built-in wine and bar storage", "Glass uppers, refrigerated below",
     "Caminito Ocean Cove, Encinitas", 0.42),
    ("miracle1-2000.webp",    "05", "Concealed refrigerator",       "Panelled to match the cabinetry",
     "Miracle Drive, San Diego", 0.12),
]

def photo_card(src, num, title, sub, place, focus, out):
    c = fit_crop(load(src), S, S, focus)
    scrim(c, 470, max_a=250)
    d = ImageDraw.Draw(c)

    ft, fs, fp = font("bold", 57), font("medium", 29), font("demi", 22)
    lines = wrap(d, title, ft, S - 130)

    addr_y  = 924
    sub_y   = addr_y - 44
    title_y = sub_y - 8 - 66 * len(lines)
    rule_y  = title_y - 30
    num_y   = rule_y - 44

    ls_text(d, (48, num_y), num, font("heavy", 26), GOLD_H, 3)
    d.rectangle([48, rule_y, 48 + 74, rule_y + 3], fill=GOLD)
    for i, ln in enumerate(lines):
        d.text((48, title_y + i * 66), ln, font=ft, fill=WHITE)
    d.text((48, sub_y), sub, font=fs, fill=(226, 228, 233))
    ls_text(d, (48, addr_y), place.upper(), fp, GOLD_H, 3.4)

    ls_text(d, (S - 44, S - 44), LICENSE, font("demi", 21), GOLD, 1.4, anchor_right=True)
    c.save(out, quality=95); print("wrote", out)

def end_card(out):
    c = Image.new("RGB", (S, S), NAVY)
    d = ImageDraw.Draw(c)
    for x0, y0, w, h in [(48,48,96,3),(48,48,3,96),
                         (S-48-96,S-51,96,3),(S-51,S-48-96,3,96)]:
        d.rectangle([x0, y0, x0+w, y0+h], fill=GOLD)

    lg = wordmark(250)
    c.paste(lg, ((S - lg.width) // 2, 176), lg)

    ft = font("bold", 62)
    lines = wrap(d, "Which layout fits your home?", ft, S - 200)
    y = 500
    for ln in lines:
        d.text(((S - d.textlength(ln, font=ft)) / 2, y), ln, font=ft, fill=WHITE); y += 72

    fs = font("medium", 31)
    sub = "Free in-home design consultation"
    d.text(((S - d.textlength(sub, font=fs)) / 2, y + 14), sub, font=fs, fill=(214, 218, 226))

    fb = font("demi", 30); bt = "SEE THE FULL GALLERY"
    bw = sum(d.textlength(ch, font=fb) + 3 for ch in bt) - 3
    bx0, by0 = (S - bw - 84) / 2, y + 100
    d.rounded_rectangle([bx0, by0, bx0 + bw + 84, by0 + 78], radius=8, fill=GOLD)
    ls_text(d, (bx0 + 42, by0 + 22), bt, fb, NAVY, 3)

    fl = font("demi", 24)
    lw = sum(d.textlength(ch, font=fl) + 1.4 for ch in LICENSE) - 1.4
    ls_text(d, ((S - lw) / 2, S - 76), LICENSE, fl, GOLD, 1.4)
    c.save(out, quality=95); print("wrote", out)

if __name__ == "__main__":
    for i, (src, num, title, sub, place, f) in enumerate(CARDS, 1):
        photo_card(src, num, title, sub, place, f, f"ad5_card{i}.png")
    end_card("ad5_card6.png")
