"""Key the transparent wordmark out of newguild.png.

newguild.png is a PRESENTATION MOCKUP: the wordmark embossed on a textured
navy ground, RGB with no alpha. This lifts it to a usable transparent asset.
The result only composites correctly on DARK grounds. If a real transparent
logo ever arrives from the designer, drop it in as newguild_keyed.png instead
and delete this script.
"""
from PIL import Image
import numpy as np, os

_HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(_HERE, "newguild-source.png")
if not os.path.exists(SRC):
    SRC = "/Users/omershapan/Desktop/newguild.png"
OUT = os.path.join(_HERE, "newguild_keyed.png")

im = Image.open(SRC).convert("RGB").crop((285, 328, 984, 906))
a = np.asarray(im).astype(float)
lum = a.max(axis=2)
alpha = np.clip((lum - 80) / (145 - 80), 0, 1)   # opaque by 145 so it is not washed
rgb = np.clip(a * 1.30, 0, 255)                  # lift the gold for small sizes
Image.fromarray(np.dstack([rgb, alpha * 255]).astype("uint8")).save(OUT)
print("wrote", OUT)
