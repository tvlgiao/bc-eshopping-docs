"""Render the eShopping header-structure mockup as a JPG.

Replaces the ASCII diagram in header-and-topbar.md with a real layout mock:
three stacked strips (Top Banner / Top Bar / Main Nav) drawn as representative
UI, with circled-number guides on the left and height annotations on the right.

Drawn at 2x then downscaled (LANCZOS) for crisp edges. Palette uses the
eShopping design tokens (terra accent, bark neutrals, cream background).
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(__file__).resolve().parent.parent / "docs" / "img" / "header-structure.jpg"
OUT.parent.mkdir(parents=True, exist_ok=True)


def _font(size, bold=False):
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


# --- Palette (eShopping tokens) ------------------------------------------
BG = (250, 248, 244)          # cream
CARD_BORDER = (215, 195, 180)  # warm grey-terra
SHADOW = (180, 150, 130, 70)
TERRA = (191, 91, 51)
TERRA_DK = (150, 66, 36)
BARK_900 = (38, 30, 24)
BARK_600 = (110, 98, 86)
BARK_300 = (170, 156, 142)
TOPBAR_BG = (244, 239, 232)
WHITE = (255, 255, 255)
PILL_BORDER = (205, 192, 178)

SCALE = 2


def sx(v):
    return int(v * SCALE)


# --- Geometry (logical px) -----------------------------------------------
W, H = 1360, 360
CARD_X0, CARD_X1 = 80, 1120
GUTTER_X = 1150           # right annotations
BAND_TOP = 34
B1_H, B2_H, B3_H = 64, 84, 116
RADIUS = 18

img = Image.new("RGB", (sx(W), sx(H)), BG)
shadow_layer = Image.new("RGBA", (sx(W), sx(H)), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow_layer)
d = ImageDraw.Draw(img)

f_band = _font(sx(20), bold=True)
f_body = _font(sx(16))
f_small = _font(sx(13))
f_logo = _font(sx(19), bold=True)
f_badge = _font(sx(18), bold=True)
f_anno = _font(sx(15))
f_anno_b = _font(sx(15), bold=True)


def text_wh(t, font):
    b = d.textbbox((0, 0), t, font=font)
    return b[2] - b[0], b[3] - b[1]


def band_rect(top, height):
    return sx(CARD_X0), sx(top), sx(CARD_X1), sx(top + height)


def rounded_top(x0, y0, x1, y1, fill):
    d.rounded_rectangle([x0, y0, x1, y1], radius=sx(RADIUS), fill=fill)
    d.rectangle([x0, y0 + sx(RADIUS), x1, y1], fill=fill)


def rounded_bottom(x0, y0, x1, y1, fill):
    d.rounded_rectangle([x0, y0, x1, y1], radius=sx(RADIUS), fill=fill)
    d.rectangle([x0, y0, x1, y1 - sx(RADIUS)], fill=fill)


def badge(cx, cy, num):
    r = sx(17)
    d.ellipse([cx - r - sx(3), cy - r - sx(3), cx + r + sx(3), cy + r + sx(3)], fill=BG)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=TERRA)
    d.text((cx, cy), num, fill=WHITE, font=f_badge, anchor="mm")


def annotation(top, height, label):
    cy = sx(top + height // 2)
    # connector tick
    d.line([sx(CARD_X1 + 8), cy, sx(GUTTER_X - 8), cy], fill=BARK_300, width=sx(1))
    d.text((sx(GUTTER_X), cy), label, fill=BARK_600, font=f_anno, anchor="lm")


def magnifier(cx, cy, col):
    r = sx(8)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=sx(2))
    d.line([cx + sx(6), cy + sx(6), cx + sx(12), cy + sx(12)], fill=col, width=sx(2))


def heart(cx, cy, col):
    rr = sx(5)
    d.ellipse([cx - sx(8), cy - sx(6), cx - sx(8) + 2 * rr, cy - sx(6) + 2 * rr], outline=col, width=sx(2))
    d.ellipse([cx + sx(8) - 2 * rr, cy - sx(6), cx + sx(8), cy - sx(6) + 2 * rr], outline=col, width=sx(2))
    d.polygon([cx - sx(9), cy - sx(1), cx + sx(9), cy - sx(1), cx, cy + sx(11)], outline=col, width=sx(2))


def bag(cx, cy, col):
    w, h = sx(18), sx(16)
    d.rounded_rectangle([cx - w // 2, cy - h // 2 + sx(3), cx + w // 2, cy + h // 2 + sx(3)],
                        radius=sx(3), outline=col, width=sx(2))
    d.arc([cx - sx(6), cy - h // 2 - sx(4), cx + sx(6), cy - h // 2 + sx(8)], 180, 360, fill=col, width=sx(2))


# --- Soft drop shadow -----------------------------------------------------
sd.rounded_rectangle([sx(CARD_X0 + 2), sx(BAND_TOP + 8),
                      sx(CARD_X1 + 2), sx(BAND_TOP + B1_H + B2_H + B3_H + 8)],
                     radius=sx(RADIUS), fill=SHADOW)
blur = shadow_layer.filter(ImageFilter.GaussianBlur(radius=sx(7)))
img.paste(blur, (0, 0), blur)

# === Band 1 — Top Banner (terra promo strip) =============================
t = BAND_TOP
x0, y0, x1, y1 = band_rect(t, B1_H)
rounded_top(x0, y0, x1, y1, TERRA)
# subtle darker inset line bottom
d.text((sx(CARD_X0 + 28), sx(t + B1_H // 2)), "Free shipping on all orders over $99",
       fill=WHITE, font=f_body, anchor="lm")
lbl = "Top Banner"
lw, _ = text_wh(lbl, f_small)
d.text((sx(CARD_X1 - 24), sx(t + B1_H // 2)), "promo / announcement",
       fill=(255, 226, 214), font=f_small, anchor="rm")
badge(sx(CARD_X0), sx(t + B1_H // 2), "1")
annotation(t, B1_H, "content-height")

# === Band 2 — Top Bar (utility strip) ====================================
t = BAND_TOP + B1_H
x0, y0, x1, y1 = band_rect(t, B2_H)
d.rectangle([x0, y0, x1, y1], fill=TOPBAR_BG)
d.line([x0, y0, x1, y0], fill=CARD_BORDER, width=sx(1))
d.text((sx(CARD_X0 + 28), sx(t + B2_H // 2)), "Welcome to our store",
       fill=BARK_900, font=f_body, anchor="lm")
links = "Pages   ·   Address   ·   Phone   ·   Account   ·   Currency   ·   Social"
d.text((sx(CARD_X1 - 24), sx(t + B2_H // 2)), links, fill=BARK_600, font=f_small, anchor="rm")
badge(sx(CARD_X0), sx(t + B2_H // 2), "2")
annotation(t, B2_H, "54 px")

# === Band 3 — Main Nav (logo + nav + search + icons) =====================
t = BAND_TOP + B1_H + B2_H
x0, y0, x1, y1 = band_rect(t, B3_H)
rounded_bottom(x0, y0, x1, y1, WHITE)
d.line([x0, y0, x1, y0], fill=CARD_BORDER, width=sx(1))
d.rounded_rectangle([x0, y0, x1, y1], radius=sx(RADIUS), outline=CARD_BORDER, width=sx(1))
cy = sx(t + B3_H // 2)
# logo block
lg_x0 = sx(CARD_X0 + 28)
d.rounded_rectangle([lg_x0, cy - sx(20), lg_x0 + sx(96), cy + sx(20)], radius=sx(8), fill=TERRA)
d.text((lg_x0 + sx(48), cy), "LOGO", fill=WHITE, font=f_logo, anchor="mm")
# nav links
nav_x = lg_x0 + sx(96) + sx(40)
d.text((nav_x, cy), "Shop      Brands      About      Contact", fill=BARK_900, font=f_body, anchor="lm")
# search pill
sp_x1 = sx(CARD_X1 - 150)
sp_x0 = sp_x1 - sx(240)
d.rounded_rectangle([sp_x0, cy - sx(17), sp_x1, cy + sx(17)], radius=sx(17),
                    outline=PILL_BORDER, width=sx(2), fill=BG)
magnifier(sp_x0 + sx(20), cy, BARK_600)
d.text((sp_x0 + sx(40), cy), "Search products", fill=BARK_300, font=f_small, anchor="lm")
# wishlist + cart icons
heart(sx(CARD_X1 - 96), cy, BARK_900)
bag(sx(CARD_X1 - 48), cy, BARK_900)
badge(sx(CARD_X0), cy, "3")
annotation(t, B3_H, "grows to logo")

# --- Export ---------------------------------------------------------------
final = img.resize((W, H), Image.LANCZOS)
final.save(OUT, "JPEG", quality=92, optimize=True)
print(f"wrote {OUT}  ({OUT.stat().st_size} bytes)")
