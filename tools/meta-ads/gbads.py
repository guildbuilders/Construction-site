"""Shared helpers for the Guild Builders Meta ad creative.

Every ad is generated from the website's own photo library, so the source of
truth for imagery is the repo below, not this folder.
"""
from PIL import Image, ImageDraw, ImageFont
import os


# this file lives at <repo>/tools/meta-ads/, so the photo library is two up
REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
NAVY   = (26, 36, 59)
GOLD   = (198, 169, 97)
GOLD_H = (236, 211, 119)
WHITE  = (252, 252, 252)
LICENSE = "CA Lic #1154614"

AV  = "/System/Library/Fonts/Avenir Next.ttc"
AVC = "/System/Library/Fonts/Avenir Next Condensed.ttc"
IDX = {"bold": 0, "demi": 2, "medium": 5, "regular": 7, "heavy": 8}

def font(weight="bold", size=48, cond=False):
    return ImageFont.truetype(AVC if cond else AV, size, index=IDX[weight])

def load(name):
    return Image.open(os.path.join(REPO, name)).convert("RGB")

def fit_crop(im, w, h, focus=0.5):
    """Cover-crop to exactly w x h. focus 0..1 slides the kept window."""
    sr, tr = im.width / im.height, w / h
    if sr > tr:
        nw = int(round(im.height * tr))
        x = int((im.width - nw) * focus)
        im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(round(im.width / tr))
        y = int((im.height - nh) * focus)
        im = im.crop((0, y, im.width, y + nh))
    return im.resize((w, h), Image.LANCZOS)

def ls_text(d, xy, text, f, fill, tracking=0, anchor_right=False):
    total = sum(d.textlength(c, font=f) + tracking for c in text) - tracking
    x, y = xy
    if anchor_right:
        x -= total
    for c in text:
        d.text((x, y), c, font=f, fill=fill)
        x += d.textlength(c, font=f) + tracking
    return total

def scrim(base, top_y, color=NAVY, max_a=252, solid_from=0.74):
    """Gradient to SOLID colour over the last stretch. The solid tail matters:
    a gradient that only reaches ~76% lets the photo show through and washes
    out the wordmark."""
    h = base.height - top_y
    ov = Image.new("RGBA", (base.width, h))
    dd = ImageDraw.Draw(ov)
    for i in range(h):
        t = min(1.0, (i / max(h - 1, 1)) / solid_from)
        dd.line([(0, i), (base.width, i)], fill=color + (int(max_a * (t ** 1.25)),))
    base.paste(Image.alpha_composite(
        base.crop((0, top_y, base.width, base.height)).convert("RGBA"), ov).convert("RGB"),
        (0, top_y))

def pill(d, xy, text, bg, fg, f, padx=26, pady=13, tracking=3):
    w = sum(d.textlength(c, font=f) + tracking for c in text) - tracking
    asc, desc = f.getmetrics()
    x, y = xy
    d.rounded_rectangle([x, y, x + w + padx * 2, y + asc + pady * 2], radius=6, fill=bg)
    ls_text(d, (x + padx, y + pady - (desc // 6)), text, f, fg, tracking)
    return w + padx * 2

LOGO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "newguild_keyed.png")

def wordmark(h):
    lg = Image.open(LOGO).convert("RGBA")
    r = h / lg.height
    return lg.resize((int(lg.width * r), h), Image.LANCZOS)

def logo_lockup(canvas, d, y_center, x_left=60, height=104):
    lg = wordmark(height)
    canvas.paste(lg, (x_left, int(y_center - height / 2)), lg)
    f = font("demi", 25)
    asc, _ = f.getmetrics()
    ls_text(d, (canvas.width - 60, int(y_center - asc / 2) + 2), LICENSE, f,
            GOLD, 1.6, anchor_right=True)

def wrap(d, text, f, max_w, tracking=0):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if sum(d.textlength(c, font=f) + tracking for c in t) - tracking <= max_w or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines
