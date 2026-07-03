# Adding new photos (keep the site fast)

The site shows small, fast-loading copies of each photo in the galleries,
and the full-resolution original only when a visitor clicks to enlarge.
A helper script keeps this automatic so you never have to think about it.

## The 3-step routine for new photos

1. **Add your photo files** (the full-size `.webp` originals) into this
   folder, just like before.

2. **Add the image to the page HTML** using a normal tag, e.g.:

   ```html
   <img src="myphoto.webp" alt="Short description" class="gallery-image" loading="lazy" />
   ```

   (Use `src="myphoto.webp"` — the full-size name. The script fixes it up.)

3. **Run the optimizer**: double-click **`optimize-images.command`** in
   Finder (or run `python3 optimize-images.py` in Terminal).

   It will:
   - create a small web copy `myphoto-1000.webp` for any new photos, and
   - rewrite the page so it loads the small copy, while the click-to-enlarge
     lightbox still shows your full-size original.

Then upload the folder to Cloudflare as usual.

## Good to know

- **Your originals are never changed or deleted.** The script only *adds*
  `-1000` copies and edits the HTML.
- **Safe to run anytime.** Running it again skips photos that are already
  done — it won't duplicate work or double-process anything.
- **What to upload:** upload the whole folder (originals + the `-1000`
  copies). The originals power the zoom view; the `-1000` copies make
  browsing fast.
- **Quality:** web copies are max 1000px wide at quality 80 — visually
  identical at the size they're shown. Adjust `THUMB_WIDTH` / `THUMB_QUALITY`
  at the top of `optimize-images.py` if you ever want larger/sharper copies.

## Requirements

The script uses `cwebp` (installed at `~/.local/bin/cwebp`) and Python 3
(built into macOS). Both are already set up on this Mac.
