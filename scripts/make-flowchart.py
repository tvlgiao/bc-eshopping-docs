"""Render the get-started 5-step flowchart as a PNG.

Strategy: draw at 2x scale, downscale with LANCZOS for crisp edges + smooth
anti-aliased curves. Number badges straddle the card's top border so the
label area stays uncrowded and vertically centered.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(__file__).resolve().parent.parent / "docs" / "img" / "flow-get-started.png"
OUT.parent.mkdir(parents=True, exist_ok=True)


def _font(size: int, bold: bool = False):
    candidates = (
        ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf"]
        if bold
        else ["C:/Windows/Fonts/segoeui.ttf", "C:/Windows/Fonts/arial.ttf"]
    )
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


STEPS = [
    ("1", "Install theme"),
    ("2", "Pick variant"),
    ("3", "Install PapaThemes\nWidgets app"),
    ("4", "Import demo\nproducts + widgets"),
    ("5", "Customize in\nPage Builder"),
]

# --- Layout (logical pixels, will render at 2x then downsample) ----------
W, H = 1700, 320
BOX_W, BOX_H = 280, 170
BADGE_R = 26
GAP = (W - BOX_W * len(STEPS)) // (len(STEPS) + 1)
BOX_TOP = (H - BOX_H) // 2 + 10  # +10 so badge has room above

# --- Palette --------------------------------------------------------------
BG = (250, 248, 244)
CARD_BG = (255, 255, 255)
CARD_BORDER = (215, 195, 180)        # warm grey-terra
CARD_SHADOW = (180, 150, 130, 60)    # soft warm shadow
BADGE_BG = (191, 91, 51)             # terra
BADGE_TEXT = (255, 255, 255)
LABEL = (40, 30, 24)                 # bark
ARROW = (191, 91, 51)                # terra (match badge)

SCALE = 2
W2, H2 = W * SCALE, H * SCALE

img = Image.new("RGB", (W2, H2), BG)
shadow_layer = Image.new("RGBA", (W2, H2), (0, 0, 0, 0))
shadow_draw = ImageDraw.Draw(shadow_layer)
d = ImageDraw.Draw(img)

num_font = _font(34 * SCALE, bold=True)
txt_font = _font(22 * SCALE)


def _sx(v: int) -> int:
    return v * SCALE


def text_size(text: str, font):
    bbox = d.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_box(x: int, num: str, label: str) -> None:
    x0, y0 = _sx(x), _sx(BOX_TOP)
    x1, y1 = _sx(x + BOX_W), _sx(BOX_TOP + BOX_H)

    # Soft drop shadow (offset down a few px)
    shadow_draw.rounded_rectangle(
        [x0 + _sx(2), y0 + _sx(6), x1 + _sx(2), y1 + _sx(6)],
        radius=_sx(16),
        fill=CARD_SHADOW,
    )

    # Card
    d.rounded_rectangle(
        [x0, y0, x1, y1], radius=_sx(16),
        fill=CARD_BG, outline=CARD_BORDER, width=_sx(2),
    )

    # Centered numbered badge straddling top border
    cx = (x0 + x1) // 2
    cy = y0
    r = _sx(BADGE_R)
    # White ring to lift badge off the border
    d.ellipse([cx - r - _sx(3), cy - r - _sx(3), cx + r + _sx(3), cy + r + _sx(3)],
              fill=BG)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BADGE_BG)
    d.text((cx, cy), num, fill=BADGE_TEXT, font=num_font, anchor="mm")

    # Label — vertically center the full block in the card body
    lines = label.split("\n")
    line_h = text_size("Ag", txt_font)[1] + _sx(6)
    total_h = line_h * len(lines) - _sx(6)
    body_top = y0 + r + _sx(8)              # below the badge
    body_h = y1 - body_top
    ty = body_top + (body_h - total_h) // 2
    for ln in lines:
        lw, _h = text_size(ln, txt_font)
        d.text((cx - lw / 2, ty), ln, fill=LABEL, font=txt_font)
        ty += line_h


def draw_arrow(x_from: int, x_to: int) -> None:
    y = _sx(BOX_TOP + BOX_H // 2)
    x0, x1 = _sx(x_from + 8), _sx(x_to - 8)
    head = _sx(14)
    # Shaft
    d.line([(x0, y), (x1 - head + _sx(2), y)], fill=ARROW, width=_sx(3))
    # Arrowhead
    d.polygon([(x1 - head, y - _sx(9)), (x1 - head, y + _sx(9)), (x1, y)],
              fill=ARROW)


# --- Composite ------------------------------------------------------------
# Blur shadow then paste before drawing cards on top
shadow_blur = shadow_layer.filter(ImageFilter.GaussianBlur(radius=_sx(6)))
img.paste(shadow_blur, (0, 0), shadow_blur)

for i, (num, label) in enumerate(STEPS):
    x = GAP + i * (BOX_W + GAP)
    draw_box(x, num, label)
    if i > 0:
        x_prev = GAP + (i - 1) * (BOX_W + GAP) + BOX_W
        draw_arrow(x_prev, x)

# Downsample for crisp edges
final = img.resize((W, H), Image.LANCZOS)
final.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT}  ({OUT.stat().st_size} bytes)")
