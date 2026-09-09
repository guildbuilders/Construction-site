"""Ad 1 - 15s Transformation Reel, 1080x1920, built entirely from stills.

Landscape sources sit in a 675px band over a blurred navy backdrop rather than
being cropped to 9:16, which would discard ~65% of each photo's width.
No audio, no motion footage: this is a photo-motion reel, not the whip-pan
demo the Andromeda guide describes.
"""
import subprocess, imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFilter
from gbads import *

W, H, FPS, SECS = 1080, 1920, 30, 15
TOTAL = FPS * SECS
BAND_Y, BAND_H = 470, 675          # keeps text clear of the Reels UI overlays
ADDR = "Kingsfield Court, San Diego"

SEGS = [
    dict(img="ba-tynebourne-before.webp", s=0.0,  e=3.5,  z=(1.00, 1.07),
         pill="BEFORE", cap="Your kitchen still looks like this."),
    dict(img="ba-tynebourne-after.webp",  s=3.5,  e=7.0,  z=(1.07, 1.00),
         pill="AFTER",  cap="Until our design-build team steps in."),
    dict(img="kingsfield5-2000.webp",     s=7.0,  e=10.0, z=(1.00, 1.06),
         pill=None,     cap="Structural changes. Custom cabinetry. Quartzite counters."),
    dict(img="kingsfield1-2000.webp",     s=10.0, e=13.0, z=(1.06, 1.00),
         pill=None,     cap="One team from design through final inspection."),
]
END_S = 13.0

def backdrop(img):
    small = fit_crop(img, 216, 384)
    b = small.filter(ImageFilter.GaussianBlur(9)).resize((W, H), Image.LANCZOS)
    return Image.blend(b, Image.new("RGB", (W, H), NAVY), 0.62)

def text_layer(seg):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    if seg["pill"]:
        f = font("heavy", 30)
        bg, fg = (NAVY, WHITE) if seg["pill"] == "BEFORE" else (GOLD, NAVY)
        pill(d, (56, BAND_Y - 76), seg["pill"], bg, fg, f)
    ls_text(d, (56, BAND_Y + BAND_H + 56), ADDR.upper(), font("demi", 26), GOLD_H, 4.0)
    fc = font("bold", 62)
    y = BAND_Y + BAND_H + 108
    for ln in wrap(d, seg["cap"], fc, W - 112):
        d.text((56, y), ln, font=fc, fill=WHITE); y += 74
    return lay

def end_frame():
    c = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(c)
    for x0, y0, w, h in [(64,470,110,3),(64,470,3,110),
                         (W-64-110,H-473,110,3),(W-67,H-580,3,110)]:
        d.rectangle([x0, y0, x0+w, y0+h], fill=GOLD)
    lg = wordmark(300)
    c.paste(lg, ((W - lg.width)//2, 610), lg)
    ft = font("bold", 70)
    for i, ln in enumerate(["Kitchen and bath", "remodels"]):
        d.text(((W - d.textlength(ln, font=ft))/2, 990 + i*82), ln, font=ft, fill=WHITE)
    fs = font("medium", 36)
    sub = "Free in-home design consultation"
    d.text(((W - d.textlength(sub, font=fs))/2, 1172), sub, font=fs, fill=(214,218,226))
    fb = font("demi", 32); bt = "TAP TO BOOK"
    bw = sum(d.textlength(ch, font=fb)+3 for ch in bt) - 3
    bx, by = (W - bw - 96)/2, 1258
    d.rounded_rectangle([bx, by, bx+bw+96, by+86], radius=9, fill=GOLD)
    ls_text(d, (bx+48, by+25), bt, fb, NAVY, 3)
    fl = font("demi", 28)
    lw = sum(d.textlength(ch, font=fl)+1.4 for ch in LICENSE) - 1.4
    ls_text(d, ((W - lw)/2, 1410), LICENSE, fl, GOLD, 1.4)
    return c

def main(out="Ad1_Transformation_Reel_1080x1920.mp4"):
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen(
        [ff, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
         "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-preset", "slow",
         "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out],
        stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    cache = {s["img"]: (load(s["img"]), None, text_layer(s)) for s in SEGS}
    cache = {k: (src, backdrop(src), txt) for k, (src, _, txt) in cache.items()}
    endc = end_frame()
    prev = endc

    for n in range(TOTAL):
        t = n / FPS
        if t >= END_S:
            k = min(1.0, (t - END_S) / 0.4)
            frame = endc if k >= 1.0 else Image.blend(prev, endc, k)
        else:
            seg = next(s for s in SEGS if s["s"] <= t < s["e"])
            src, bg, txt = cache[seg["img"]]
            p = (t - seg["s"]) / (seg["e"] - seg["s"])
            z = seg["z"][0] + (seg["z"][1] - seg["z"][0]) * p
            zw, zh = int(BAND_H * z * (W / BAND_H)), int(BAND_H * z)
            fg = fit_crop(src, zw, zh)
            left, top = (zw - W)//2, (zh - BAND_H)//2
            fg = fg.crop((left, top, left + W, top + BAND_H))
            frame = bg.copy()
            frame.paste(fg, (0, BAND_Y))
            d = ImageDraw.Draw(frame)
            d.rectangle([0, BAND_Y - 3, W, BAND_Y - 1], fill=GOLD)
            d.rectangle([0, BAND_Y + BAND_H + 1, W, BAND_Y + BAND_H + 3], fill=GOLD)
            frame = Image.alpha_composite(frame.convert("RGBA"), txt).convert("RGB")
            if 3.5 <= t < 3.60:
                a = 1 - (t - 3.5) / 0.10
                frame = Image.blend(frame, Image.new("RGB", (W, H), "white"), a * 0.75)
            prev = frame
        proc.stdin.write(frame.tobytes())

    proc.stdin.close()
    err = proc.stderr.read().decode()
    print(err[-1500:] if proc.wait() != 0 else f"wrote {out}")

if __name__ == "__main__":
    main()
