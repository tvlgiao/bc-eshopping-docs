"""
Generate labeled placeholder PNGs for every screenshot referenced in the docs.

Each placeholder shows:
  - the filename
  - a short human description (caption) so the user knows what to capture
  - sensible dimensions matching the expected screenshot

Usage:
    python scripts/make-placeholders.py
"""

from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "img"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# (filename, width, height, caption)
PLACEHOLDERS: list[tuple[str, int, int, str]] = [
    # Get started
    ("launch-papathemes-widgets-app.jpg", 1280, 720,
        "Screenshot: BigCommerce Apps -> My Apps -> 'Launch' button on the PapaThemes Widgets card"),
    ("install-papathemes-widgets.jpg", 1280, 720,
        "Screenshot: inside the PapaThemes Widgets app, the list of available widgets with their 'Install' buttons"),
    ("custom-widgets-appear.jpg", 1280, 720,
        "Screenshot: Page Builder left-side widget panel showing the new 'Custom Widgets' section after install"),

    # Install theme
    ("my-themes-eshopping.jpg", 1280, 700,
        "Screenshot: Storefront -> My Themes page showing the eShopping theme card"),
    ("upload-theme-button.jpg", 1280, 220,
        "Screenshot: 'Upload theme' button in the top-right corner of the My Themes page"),
    ("current-theme-badge.jpg", 640, 480,
        "Screenshot: the eShopping theme card with the green 'Current Theme' badge across the top"),
    ("make-a-copy.jpg", 640, 480,
        "Screenshot: 'Make a copy' option from the theme card's three-dot (...) more menu"),

    # Choose variant
    ("variation-picker.jpg", 480, 320,
        "Screenshot: 'Theme styles' dropdown at the top of Page Builder with Industrial / AutoParts / Electronics / Packaging options"),
    ("meta-desktop-light.jpg", 600, 400,
        "Screenshot: full home page rendered with the Light variation (sandy/cream, terra accents)"),
    ("meta-desktop-bold.jpg", 600, 400,
        "Screenshot: full home page rendered with the Bold variation (high contrast, sans-serif)"),
    ("meta-desktop-warm.jpg", 600, 400,
        "Screenshot: full home page rendered with the Warm variation (soft beige, brown accents)"),

    # Import demo data
    ("bc-tools-landing.jpg", 1280, 700,
        "Screenshot: https://bc-tools.papathemes.com landing page with the left-side menu"),
    ("import-product.jpg", 1280, 720,
        "Screenshot: BC Tools 'Import Product' page with sample picker + Import button"),
    ("import-widgets.jpg", 1280, 720,
        "Screenshot: BC Tools 'Import Widgets' page with channel selector + page list + Import button"),

    # Theme editor
    ("click-theme-customize.jpg", 1280, 600,
        "Screenshot: 'Customize' button on the eShopping card in My Themes"),
    ("eshopping-color-panel.jpg", 420, 720,
        "Screenshot: Page Builder -> Theme styles -> eShopping -> Colors sub-panel showing every color swatch"),

    # Header / footer / sidebar
    ("footer-industrial.png", 1600, 600,
        "Screenshot: full footer of the Industrial demo (dark, 4 columns, brand strip, copyright bar)"),
    ("footer-autoparts.png", 1600, 600,
        "Screenshot: full footer of the Auto Parts demo (dark, payment icons, 4 columns)"),
    ("footer-packaging.png", 1600, 600,
        "Screenshot: full footer of the Packaging demo (dark green, eco messaging)"),

    ("sidebar-layout.jpg", 380, 900,
        "Screenshot: full left sidebar on a category page (categories tree + filters + promo card)"),

    # Home variants - composed views
    ("home-industrial-composed.png", 1600, 1800,
        "Screenshot: scrolled / composed view of the full Industrial home page (hero + trust + sliders + footer)"),
    ("home-autoparts-composed.png", 1600, 1800,
        "Screenshot: composed view of the full Auto Parts home page (fitment hero + sliders + footer)"),
    ("home-electronics-composed.png", 1600, 1800,
        "Screenshot: composed view of the full Electronics home page (carousel + tabs + brands + blog)"),
    ("home-packaging-composed.png", 1600, 1800,
        "Screenshot: composed view of the full Packaging home page (editorial hero + why + resources + newsletter)"),

    # Packaging widgets / pages
    ("packaging-desktop-hero.png", 1600, 720,
        "Screenshot: Packaging home page hero section, desktop"),
    ("packaging-mobile-375.png", 375, 800,
        "Screenshot: Packaging home page at 375px mobile width"),
    ("packaging-desktop-widgets-why.png", 1600, 480,
        "Screenshot: Packaging 'Why choose us' 4-column callouts widget, desktop"),
    ("packaging-mobile-why-choose.png", 375, 900,
        "Screenshot: Packaging 'Why choose us' widget at 375px mobile width"),
    ("packaging-desktop-widgets-resources.png", 1600, 480,
        "Screenshot: Packaging 'Resources' 3-column links widget"),
    ("packaging-blog-index.png", 1600, 900,
        "Screenshot: Packaging blog index page (post grid)"),
    ("packaging-desktop-widgets-newsletter.png", 1600, 480,
        "Screenshot: Packaging newsletter signup widget with kraft background"),
    ("packaging-mobile-widgets.png", 375, 1200,
        "Screenshot: stacked widgets on Packaging home at 375px mobile"),
    ("packaging-pdp.png", 1600, 1100,
        "Screenshot: Packaging product detail page with gallery + variants + Add-to-Cart"),
    ("packaging-category-page.png", 1600, 1000,
        "Screenshot: Packaging category page (sidebar + grid)"),

    # Product
    ("product-card.jpg", 320, 480,
        "Screenshot: a single product card (image + swatches + title + price + buttons)"),
    ("products-grid.jpg", 800, 600,
        "Screenshot: category page in Grid view"),
    ("products-list.jpg", 800, 600,
        "Screenshot: category page in List view"),
    ("pdp-faq.jpg", 800, 600,
        "Screenshot: PDP FAQ accordion tab open with multiple Q&A items expanded"),
    ("fbt-bundle.jpg", 1000, 400,
        "Screenshot: Frequently Bought Together row on PDP with bundle price + Add bundle button"),

    # Category
    ("category-page.jpg", 1600, 1000,
        "Screenshot: a category page (sidebar + filters + product grid + sort toolbar)"),

    # Brand
    ("brands-az.jpg", 1280, 800,
        "Screenshot: All Brands page in A-Z layout with letter groups + brand logos"),

    # Bulk order
    ("bulk-order-table.jpg", 1200, 700,
        "Screenshot: bulk-order mode table view with rows + qty inputs + Add all to cart"),

    # Cart
    ("cart-free-ship-bar.jpg", 800, 120,
        "Screenshot: free-shipping progress bar at the top of the cart page (with X away message)"),

    # Search
    ("keyword-suggestions.jpg", 800, 500,
        "Screenshot: header search box with the keyword suggestions dropdown open"),

    # Blog
    ("blog-index.jpg", 1280, 800,
        "Screenshot: blog index page with 3-column post grid (featured image + title + excerpt)"),

    # Static pages
    ("about-desktop.jpg", 1280, 1200,
        "Screenshot: full About Us page (banner + story + values + team + CTA)"),
    ("policy-privacy-desktop.jpg", 1280, 1000,
        "Screenshot: Privacy Policy page with header + body text"),
    ("policy-shipping-desktop.jpg", 1280, 1000,
        "Screenshot: Shipping Policy page with header + body text"),
    ("policy-returns-desktop.jpg", 1280, 1000,
        "Screenshot: Returns Policy page with header + body text"),
    ("verify-about-desktop.jpg", 1280, 1000,
        "Screenshot: verified-business / trust page (certifications, badges, value props)"),

    # Widgets
    ("ai-html-generator-editor.jpg", 900, 600,
        "Screenshot: AI HTML Generator (PapaThemes) editor with the Save button"),
    ("widget-settings-panel.jpg", 600, 800,
        "Screenshot: PapaThemes widget Settings panel (3-dot menu -> Settings) with General/Slider sections"),
]


def _font(size: int):
    """Try common Windows fonts then fall back to PIL default."""
    candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def wrap_text(text: str, font, max_width: int, draw) -> list[str]:
    words = text.split()
    lines, cur = [], ""
    for w in words:
        candidate = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), candidate, font=font)
        width = bbox[2] - bbox[0]
        if width <= max_width:
            cur = candidate
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make_one(filename: str, width: int, height: int, caption: str):
    img = Image.new("RGB", (width, height), color=(245, 241, 235))
    draw = ImageDraw.Draw(img)

    # Border
    draw.rectangle([0, 0, width - 1, height - 1], outline=(180, 165, 145), width=2)

    # Big diagonal "PLACEHOLDER" stripes
    stripe = (235, 228, 218)
    spacing = 40
    for x in range(-height, width, spacing):
        draw.line([(x, 0), (x + height, height)], fill=stripe, width=2)

    title = "PLACEHOLDER  •  REPLACE WITH REAL SCREENSHOT"
    title_font = _font(max(16, min(28, width // 40)))
    caption_font = _font(max(13, min(20, width // 60)))
    meta_font = _font(max(11, min(16, width // 80)))

    # Vertical center stack
    margin = 32
    inner_w = width - 2 * margin

    title_lines = wrap_text(title, title_font, inner_w, draw)
    caption_lines = wrap_text(caption, caption_font, inner_w, draw)
    meta_line = f"{filename}  ·  {width}x{height}"
    meta_lines = wrap_text(meta_line, meta_font, inner_w, draw)

    line_h_t = (draw.textbbox((0, 0), "Ag", font=title_font)[3] -
                draw.textbbox((0, 0), "Ag", font=title_font)[1]) + 6
    line_h_c = (draw.textbbox((0, 0), "Ag", font=caption_font)[3] -
                draw.textbbox((0, 0), "Ag", font=caption_font)[1]) + 6
    line_h_m = (draw.textbbox((0, 0), "Ag", font=meta_font)[3] -
                draw.textbbox((0, 0), "Ag", font=meta_font)[1]) + 4

    total_h = (
        len(title_lines) * line_h_t
        + 14
        + len(caption_lines) * line_h_c
        + 14
        + len(meta_lines) * line_h_m
    )
    y = (height - total_h) // 2

    def draw_lines(lines, font, color, line_h):
        nonlocal y
        for ln in lines:
            bbox = draw.textbbox((0, 0), ln, font=font)
            w = bbox[2] - bbox[0]
            draw.text(((width - w) // 2, y), ln, fill=color, font=font)
            y += line_h

    draw_lines(title_lines, title_font, (60, 40, 25), line_h_t)
    y += 14
    draw_lines(caption_lines, caption_font, (95, 75, 55), line_h_c)
    y += 14
    draw_lines(meta_lines, meta_font, (140, 120, 100), line_h_m)

    out = OUT_DIR / filename
    if filename.lower().endswith((".jpg", ".jpeg")):
        img.save(out, "JPEG", quality=88)
    else:
        img.save(out, "PNG")
    return out


def main() -> int:
    written = 0
    skipped_existing = 0
    # Default: do NOT overwrite existing files. Real screenshots that have
    # been dropped in over a placeholder must survive a re-run of this script.
    # Pass --force to regenerate every placeholder anyway.
    import sys
    overwrite = "--force" in sys.argv
    for filename, w, h, caption in PLACEHOLDERS:
        target = OUT_DIR / filename
        if target.exists() and not overwrite:
            skipped_existing += 1
            continue
        make_one(filename, w, h, caption)
        written += 1
    print(f"Wrote {written} placeholder(s) to {OUT_DIR}")
    if skipped_existing:
        print(f"Skipped {skipped_existing} (already exists)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
