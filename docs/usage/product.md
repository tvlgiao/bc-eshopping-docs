# Product Page (PDP)

The Product Detail Page is the most important page on your storefront — most stores see 60-80% of sessions touch it. eShopping's PDP is composed of these zones:

```
┌─────────────────────────────────────────────────────────────┐
│ Breadcrumbs                                                  │
├─────────────────────┬────────────────────────────────────────┤
│                     │  Brand · Title · SKU · Rating          │
│   Image gallery     │  Price · Stock badge · Urgency strip   │
│   (thumbnail strip  │  Variants (color/size swatches)        │
│    + main image     │  Quantity · Add to Cart                │
│    + lightbox zoom) │  Wishlist · Compare                    │
│                     │  Shipping icon strip (3 items)         │
├─────────────────────┴────────────────────────────────────────┤
│ Frequently Bought Together  (bundle 1-3 items, optional %)   │
├──────────────────────────────────────────────────────────────┤
│ Tabs: Description · Videos · Specs · Warranty · FAQ · Reviews│
├──────────────────────────────────────────────────────────────┤
│ Related products                                            │
├──────────────────────────────────────────────────────────────┤
│ Mobile sticky Add-to-Cart (mobile only, on scroll)           │
└──────────────────────────────────────────────────────────────┘
```

This page covers each zone. For the **product card** that appears in sliders and category grids, see [Product card](product-card.md).

---

## Image gallery

The gallery shows the main image with a **vertical thumbnail strip to the left** on desktop, switching to a **horizontal strip below** on mobile. There is one thumbnail per uploaded product image, so the strip grows with the number of photos you add. Click the main image for a fullscreen lightbox with zoom (mouse-wheel or pinch).

### Image sizes

Set in **Theme Editor → Products → Image Sizes**:

| Setting | Used for |
| ------- | -------- |
| Main product images | Main gallery image |
| Thumbnail image in product page | Gallery thumbnails |
| Zoomed image | Lightbox zoom |
| Image in gallery view | Card sliders (product grid and sliders) |

These settings tell the theme the maximum render size; BigCommerce downscales each uploaded photo to fit.

!!! warning "Always upload large, square images"
    Upload high-resolution square PNG/JPG (e.g. 1500×1500). BigCommerce can downscale for thumbnails and product cards but cannot upscale. A square shape avoids cropping surprises across the gallery and card layouts.

### Videos

Product videos are **YouTube videos**, not uploaded files. Add them in **Catalog → Products → (product) → Videos** by pasting a YouTube URL (or video ID). They do not appear inside the image gallery — they render in the dedicated **Videos** tab below the gallery (see [Tabs](#pdp-tabs)).

### 360-degree images

BigCommerce's product image system supports 360-degree image sequences. Upload a sequence of images and BigCommerce's gallery renders a 360 viewer. For full setup steps, see [BigCommerce's 360-degree image guide](https://support.bigcommerce.com/s/article/Adding-Products-v3#image-360).

---

## Title, brand, SKU, rating

These come straight from the product record (Catalog → Products → edit). Brand is shown only if you've assigned one. Rating shows the average of all approved reviews.

To **hide product weight or dimensions**:

**Theme Editor → Products → Display settings**:

| Setting | Effect |
| ------- | ------ |
| Show product weight | Show weight under the title |
| Show product dimensions | Show H×W×D under the title |

---

## Price + sale badges

eShopping shows:

- **Sale price** (or regular if no sale) in the Terra colour
- **Original price** struck-through to the right (only if on sale)
- **Sale badge** as a coloured pill on the image (see below)

When you set an **MSRP / retail price** on the product, the theme also shows the retail price with a label (default `MSRP:`). You can override that label with the **Product price label (retail)** text setting under **Theme Editor → Products → Product Sale Badges**. There is no automatic "You save $X" calculation — the theme simply displays the retail price you entered.

Configure the badge in **Theme Editor → Products → Product Sale Badges**:

| Setting | Options | Effect |
| ------- | ------- | ------ |
| **Show product sale badges** | `None` / `Top Left` / `Diagonal` / `Burst` | Choose the badge style/position (or turn it off) |
| **Product sale badge label** | text | The text shown in the badge (e.g. `SALE`). If left empty, the theme falls back to its built-in default |
| **Badge color** | colour picker | Badge background |
| **Badge text color** | colour picker | Badge text |

For the **"Sold out"** badge:

| Setting | Effect |
| ------- | ------ |
| **Show product sold-out badges** | Choose the badge style (or `None`) |
| **Product sold out badge label** | e.g. `Sold out` |

### Staff Pick badge colour

eShopping renders a **Staff Pick** badge on certain product cards. There is no merchant-facing toggle to enable it per product and no custom-badge value field — the styling is controlled by two colour pickers in **Theme Editor → eShopping Theme → Colors**:

| Setting | Effect |
| ------- | ------ |
| **Staff Pick Badge Background** | Badge background colour |
| **Staff Pick Badge Text** | Badge text colour |

---

## Variants — swatches

Color / size variants appear as **swatches** if you've set them up in **Catalog → Product Options & SKUs**:

- **Color swatches** — for option type "Swatch (Color)". The theme renders them as colour circles.
- **Image swatches** — for option type "Swatch (Image)". The theme renders the option image.
- **Rectangle text swatches** — for "Rectangle list" options (size: S / M / L). Rendered as text pills.

The swatch sizes shown are styled by the theme. The only configurable image dimension is **Product swatch images** (default `22x22`) under **Theme Editor → Products → Image Sizes**, which controls the source resolution of image swatches.

To **show swatch names beside the swatch** (e.g. "Black" next to a black swatch), check **Show product swatch names** in the Products panel.

---

## Add to Cart + sticky mobile ATC

The **Add to Cart** button is always visible on desktop. On mobile, when the user scrolls past it, a sticky bottom bar appears with **price + ATC**.

Toggle the mobile sticky ATC:

**Theme Editor → eShopping Theme → Product Page (PDP) → Show Mobile Sticky Add to Cart**.

---

## Shipping text + Warranty text

These are two separate settings in **Theme Editor → eShopping Theme → Product Page (PDP)**, and they appear in different places.

**PDP Shipping Text** produces the **3-item icon strip** shown under the Add-to-Cart button. It is a single field made of three `Title|Description` pairs separated by pipes (`|`):

```
Free Shipping|on orders over $500|1-Year Warranty|included with purchase|30-Day Returns|hassle-free policy
```

That renders as three icon cards. Plain text only — HTML and links are **not** supported (the text is inserted as plain text).

**PDP Warranty Text** is a separate field that fills the **4-card grid inside the Warranty tab** (not the strip under the ATC). It is made of four `Title|Description` pairs:

```
What's Covered|...|What's Not Covered|...|How to Claim|...|Extended Warranty|...
```

---

## Tabs (Description · Videos · Specs · Warranty · FAQ · Reviews) { #pdp-tabs }

The tabs appear below the gallery. Most toggles live in **Theme Editor → Products → Display settings**:

| Setting | Effect |
| ------- | ------ |
| Show product description tabs | Show the tab strip at all |
| Show product reviews | Add the **Reviews** tab (only renders when the product has reviews) |
| Product custom fields in tabs | Show a **Specifications** tab with ALL of the product's custom fields rendered as a 2-column table |

The **FAQ** tab is toggled separately under **Theme Editor → eShopping Theme → Product Page (PDP)** with the **Show FAQ Tab** setting (a built-in ask-a-question form — see [Product FAQ](product-faq.md)).

The **Warranty** tab is rendered automatically when the product has warranty text (Catalog → Products → edit → Warranty Information). Inside the warranty tab the theme shows a 4-card grid of warranty highlights (set the four title/description pairs in the **PDP Warranty Text** field under **Theme Editor → eShopping Theme → Product Page (PDP)**), plus an area below the cards where you can drop a widget — either on every product or on one specific product.

The **Videos** tab is rendered automatically when the product has videos uploaded.

### Adding "Shipping & Returns" or other content to every PDP

eShopping provides a widget area that renders BELOW the tabs (not inside them) on every PDP. Drop any HTML / Accordion / Banner widget there. There's also a matching area for content on a single product.

### Customizing the Specifications tab label

Use the **Product custom fields tab label** text setting (Theme Editor → Products → Display settings) to override the tab title. Leave it empty to use the default ("Specifications").

---

## Frequently Bought Together (FBT)

A bundle widget that appears above the tab strip (between the image/info section and the tabs), showing the current product + 1–3 frequently-paired products with an optional bundle discount. See full guide: [Frequently Bought Together](product-fbt.md).

Quick toggles (**Theme Editor → eShopping Theme → Frequently Bought Together**):

| Setting | Effect |
| ------- | ------ |
| FBT Products Count | `0` (off) / `1` / `2` / `3` — number of paired products |
| Visual Bundle Discount % | e.g. `10` for 10% off the bundle |

---

## Related products

Below the tabs the PDP shows a single **Related products** slider. Related products come from the product's Related Products list in BigCommerce — automatic (by category) by default, or manually curated per product in **Catalog → Products**. The slider only renders when the product has related products.

| Setting | Effect |
| ------- | ------ |
| **Product page (related products)** (Theme Editor → Products → Number of products displayed) | How many to show; set to `0` to hide the slider |

### Customers Also Viewed

The theme also has a **Customers Also Viewed** module, controlled by the **Product page (customers also viewed products)** count under **Theme Editor → Products → Number of products displayed**. When a product has **no** related products, the PDP falls back to the standard tab layout, where this module appears as a "Customers Also Viewed" carousel.

!!! note "Cross-sell is a cart feature"
    Cross-sell products are shown in the **cart**, not on the PDP. There is **no** recently-viewed slider on the product page (Customers Also Viewed is based on view behaviour, not the visitor's own recent history).

---

## Urgency strips

Two short message strips that build social proof. Configure them in **Theme Editor → eShopping Theme → Urgency Signals (Social Proof)**:

| Setting | Effect | Default |
| ------- | ------ | ------- |
| **Show live view count** | Shows "X viewing now" using a random number in the range below (the exact wording is editable in the theme's language file) | — |
| **Fake view count range** | `min,max` — the range for the viewer count | `3,25` |
| **Show last order time** | Shows a "last order …" message using a random time in the range below | — |
| **Last order time range** | `min,max` in **hours** ago | `1,48` |

The last-order message adapts its units automatically — it can read as minutes, hours, or days ago depending on the random value.

These are randomized client-side per session — they're not tracked analytics.

---

## Quick view button

The product card in sliders + category grids has a **Quick View** button. Clicking it opens a modal showing the PDP without leaving the page. Toggle it in **Theme Editor → Products → Display settings**:

- **Show quickview button on product cards** ✅

---

## Product page settings in the demo stores

All four demo stores (Industrial, Auto Parts, Electronics, Packaging) use the **same** PDP configuration. The only thing that differs between them is the copy in the shipping/warranty fields:

| Setting | Value (all four demos) |
| ------- | ---------------------- |
| FBT Products Count | `2` |
| Visual Bundle Discount % | `0` (no bundle discount) |
| Show live view count | ✅ |
| Show last order time | ✅ |

Each store fills its own **PDP Shipping Text** and **PDP Warranty Text** with industry-appropriate copy (e.g. Auto Parts uses a "Fitment Guarantee", Packaging uses "Bulk Pricing"), but the structural settings above are identical.

![Packaging PDP example](../img/packaging-pdp.png){ loading=lazy }

---

## Next

- [Product card style](product-card.md)
- [Frequently Bought Together](product-fbt.md)
- [Product FAQ](product-faq.md)
- [Category page →](category.md)
