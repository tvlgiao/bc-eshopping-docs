"""Move latest GIF from user's Downloads/, convert to PNG via PIL, save in docs/img/.

Usage:
    python scripts/harvest-cap.py <source-filename.gif> <target-name>
    # e.g.
    python scripts/harvest-cap.py my-themes-eshopping.gif my-themes-eshopping.jpg

If <target-name> ends in .jpg or .jpeg => save as JPEG (RGB).
If <target-name> ends in .png         => save as PNG.
"""
from __future__ import annotations
import sys
from pathlib import Path
from PIL import Image

DOWNLOADS = Path.home() / "Downloads"
OUT = Path(__file__).resolve().parent.parent / "docs" / "img"

def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__); return 2
    src_name, dst_name = sys.argv[1], sys.argv[2]
    src = DOWNLOADS / src_name
    if not src.exists():
        print(f"NOT FOUND: {src}"); return 1
    dst = OUT / dst_name

    img = Image.open(src)
    # GIFs may be palette mode; convert to RGB so JPEG works + PNG loses nothing.
    if img.mode != "RGB":
        img = img.convert("RGB")
    ext = dst.suffix.lower()
    if ext in (".jpg", ".jpeg"):
        img.save(dst, "JPEG", quality=90)
    else:
        img.save(dst, "PNG")
    # Clean up the original download.
    try: src.unlink()
    except OSError: pass
    print(f"OK -> {dst}  ({dst.stat().st_size} bytes)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
