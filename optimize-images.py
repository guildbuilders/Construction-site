#!/usr/bin/env python3
"""
optimize-images.py  —  Guild Builders site image optimizer

What it does (safe + idempotent, run it as often as you like):
  1. For every full-size NAME.webp, creates a small NAME-1000.webp web copy
     (max 1000px wide) if it doesn't already exist. Your originals are
     never modified.
  2. Rewrites the gallery/home <img> tags in the .html files so the page
     loads the small -1000 copy, while remembering the full-size original
     in a data-full="..." attribute (used by the click-to-enlarge lightbox).

Typical workflow for NEW photos:
  - Drop the new NAME.webp file(s) into this folder.
  - Add a normal tag in the HTML, e.g.
        <img src="NAME.webp" alt="..." class="gallery-image" loading="lazy" />
  - Run this script (double-click optimize-images.command, or:
        python3 optimize-images.py
    ).
  - Upload the folder to Cloudflare.

Requires the cwebp tool (installed at ~/.local/bin/cwebp).
"""

import os
import re
import shutil
import subprocess
import sys

# --- Tunables -------------------------------------------------------------
THUMB_WIDTH = 1000      # max width of the web copy, in pixels
THUMB_QUALITY = 80      # WebP quality 0-100 (80 = visually lossless for photos)
SUFFIX = "-1000"        # naming suffix for the web copies
# Only these CSS classes get rewritten (logos etc. are left alone):
GALLERY_CLASSES = ("gallery-image", "home-photo")
# -------------------------------------------------------------------------

HERE = os.path.dirname(os.path.abspath(__file__))


def find_cwebp():
    for cand in (
        os.path.expanduser("~/.local/bin/cwebp"),
        shutil.which("cwebp") or "",
    ):
        if cand and os.path.exists(cand):
            return cand
    sys.exit("ERROR: cwebp not found. Expected at ~/.local/bin/cwebp")


def image_width(path):
    """Return pixel width via macOS 'sips', or None if it can't be read."""
    try:
        out = subprocess.run(
            ["sips", "-g", "pixelWidth", path],
            capture_output=True, text=True, check=True,
        ).stdout
        m = re.search(r"pixelWidth:\s*(\d+)", out)
        return int(m.group(1)) if m else None
    except Exception:
        return None


def is_original(name):
    """True for full-size source webp (not one of our generated copies)."""
    return name.endswith(".webp") and not name.endswith(SUFFIX + ".webp")


def generate_thumbnails(cwebp):
    made, skipped = 0, 0
    originals = sorted(f for f in os.listdir(HERE) if is_original(f))
    for fname in originals:
        stem = fname[:-len(".webp")]
        thumb = f"{stem}{SUFFIX}.webp"
        thumb_path = os.path.join(HERE, thumb)
        if os.path.exists(thumb_path):
            skipped += 1
            continue
        src = os.path.join(HERE, fname)
        w = image_width(src)
        cmd = [cwebp, "-q", str(THUMB_QUALITY)]
        # only downscale; never upscale a smaller source
        if w is None or w > THUMB_WIDTH:
            cmd += ["-resize", str(THUMB_WIDTH), "0"]
        cmd += [src, "-o", thumb_path]
        subprocess.run(cmd, capture_output=True, check=True)
        made += 1
        print(f"  thumb: {thumb}")
    print(f"Thumbnails: {made} created, {skipped} already existed.")
    return made


# Matches a single <img ...> tag
IMG_RE = re.compile(r"<img\b[^>]*?/?>", re.IGNORECASE | re.DOTALL)
SRC_RE = re.compile(r'src\s*=\s*"([^"]+)"', re.IGNORECASE)
CLASS_RE = re.compile(r'class\s*=\s*"([^"]*)"', re.IGNORECASE)


def rewrite_img(tag):
    cls = CLASS_RE.search(tag)
    if not cls or not any(c in cls.group(1).split() for c in GALLERY_CLASSES):
        return tag                       # not a gallery image; leave alone
    if "data-full=" in tag:
        return tag                       # already processed
    srcm = SRC_RE.search(tag)
    if not srcm:
        return tag
    src = srcm.group(1)
    if not src.endswith(".webp") or src.endswith(SUFFIX + ".webp"):
        return tag                       # already a -1000 src, or not webp
    stem = src[:-len(".webp")]
    thumb = f"{stem}{SUFFIX}.webp"
    if not os.path.exists(os.path.join(HERE, thumb)):
        return tag                       # no thumb yet; don't break the page
    # point src at the thumbnail and remember the original for the lightbox
    new_tag = tag.replace(srcm.group(0), f'src="{thumb}" data-full="{src}"', 1)
    return new_tag


def rewrite_html():
    changed_files = 0
    for fname in sorted(os.listdir(HERE)):
        if not fname.endswith(".html"):
            continue
        path = os.path.join(HERE, fname)
        with open(path, "r", encoding="utf-8") as fh:
            html = fh.read()
        new_html = IMG_RE.sub(lambda m: rewrite_img(m.group(0)), html)
        if new_html != html:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_html)
            changed_files += 1
            print(f"  updated: {fname}")
    print(f"HTML: {changed_files} file(s) updated.")


def main():
    print("Guild Builders image optimizer")
    cwebp = find_cwebp()
    print("1/2  Generating web-sized copies...")
    generate_thumbnails(cwebp)
    print("2/2  Updating <img> tags in HTML...")
    rewrite_html()
    print("Done. Review changes, then upload the folder to Cloudflare.")


if __name__ == "__main__":
    main()
