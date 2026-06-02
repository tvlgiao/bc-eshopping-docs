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

Set in **Theme Editor → Products → Image sizes**:

| Setting | id | Used for | Default |
| ------- | -- | -------- | ------- |
| Main product images | `product_size` | Main gallery image | `1500x1500` |
| Thumbnail image in product page | `productview_thumb_size` | Gallery thumbnails | `100x100` |
| Zoomed image | `zoom_size` | Lightbox zoom | `2000x2000` |
| Image in gallery view | `productgallery_size` | Card sliders (product grid and sliders) | `1500x1500` |

These settings tell the theme the maximum render size; BigCommerce downscales each uploaded photo to fit.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqSW1hZ2Ugc2l6ZXMqKiAoaGVhZGluZykg4oaSIHRoZSBmaWVsZCBhYm92ZS4gRWFjaCBpcyBhbiBpbWFnZS1kaW1lbnNpb24gcGlja2VyOiBjaG9vc2UgKk9wdGltaXplZCBmb3IgdGhlbWUqIG9yICpTcGVjaWZ5IGRpbWVuc2lvbnMqIGFuZCBlbnRlciBgV0lEVEh4SEVJR0hUYCAoZS5nLiBgMTUwMHgxNTAwYCkuIEZvcm1hdDogYFd4SGAgaW4gcGl4ZWxzLg0=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodGhlIHBob3RvcyB0aGVtc2VsdmVzKToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgQ2F0YWxvZyDihpIgUHJvZHVjdHMg4oaSIChwcm9kdWN0KSDihpIgSW1hZ2VzLiAoTm90IGEgdGhlbWUgc2V0dGluZy4pIFRoZSBnYWxsZXJ5LCB0aHVtYm5haWwgc3RyaXAgYW5kIGxpZ2h0Ym94IGFyZSBhdXRvbWF0aWMg4oCUIHRoZXJlIGlzICoqbm8qKiBUaGVtZSBFZGl0b3IgdG9nZ2xlIGZvciB0aGUgdGh1bWJuYWlsIGxheW91dCwgbGlnaHRib3ggb3Igem9vbTsgdGhleSByZW5kZXIgZnJvbSB5b3VyIHVwbG9hZGVkIGltYWdlcy4N-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Image sizes</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>


!!! warning "Always upload large, square images"
    Upload high-resolution square PNG/JPG (e.g. 1500×1500). BigCommerce can downscale for thumbnails and product cards but cannot upscale. A square shape avoids cropping surprises across the gallery and card layouts.

### Videos

Product videos are **YouTube videos**, not uploaded files. Add them in **Catalog → Products → (product) → Videos** by pasting a YouTube URL (or video ID). They do not appear inside the image gallery — they render in the dedicated **Videos** tab below the gallery (see [Tabs](#pdp-tabs)).


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgQ2F0YWxvZyDihpIgUHJvZHVjdHMg4oaSIChwcm9kdWN0KSDihpIgVmlkZW9zLiAoTm90IGEgdGhlbWUgc2V0dGluZyDigJQgdGhlIFZpZGVvcyB0YWIgYXBwZWFycyBhdXRvbWF0aWNhbGx5IHdoZW4gdGhlIHByb2R1Y3QgaGFzIGF0IGxlYXN0IG9uZSB2aWRlby4pDQ==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>


### 360-degree images

BigCommerce's product image system supports 360-degree image sequences. Upload a sequence of images and BigCommerce's gallery renders a 360 viewer. For full setup steps, see [BigCommerce's 360-degree image guide](https://support.bigcommerce.com/s/article/Adding-Products-v3#image-360).

---

## Title, brand, SKU, rating

These come straight from the product record (Catalog → Products → edit). Brand is shown only if you've assigned one. Rating shows the average of all approved reviews.


<!--te-src:PiAqKkN1c3RvbWl6ZSAodGhlIGRhdGEpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiBDYXRhbG9nIOKGkiBQcm9kdWN0cyDihpIgKHByb2R1Y3QpIOKAlCBOYW1lLCBTS1UsIEJyYW5kLCBXZWlnaHQsIERpbWVuc2lvbnMuIChOb3QgdGhlbWUgc2V0dGluZ3Mg4oCUIHRoZXkgZGlzcGxheSB0aGUgcHJvZHVjdCByZWNvcmQuKQ0=-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>


To **show or hide product weight / dimensions**:

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIFByb2R1Y3RzIOKGkiBEaXNwbGF5IHNldHRpbmdzKio6DQ==-->

| Setting | id | Effect | Default |
| ------- | -- | ------ | ------- |
| Show product weight | `show_product_weight` | Show weight under the title | `true` |
| Show product dimensions | `show_product_dimensions` | Show H×W×D under the title | `false` |


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqU2hvdyBwcm9kdWN0IHdlaWdodCoqIC8gKipTaG93IHByb2R1Y3QgZGltZW5zaW9ucyoqIChjaGVja2JveGVzLCB1bmRlciB0aGUgKkRpc3BsYXkgc2V0dGluZ3MqIGhlYWRpbmcpLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdHM6IHdlaWdodCBgdHJ1ZWAsIGRpbWVuc2lvbnMgYGZhbHNlYC4N-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show product weight</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Show product dimensions</span><span class="te-cb"></span></div></div>


---

## Price + sale badges

eShopping shows:

- **Sale price** (or regular if no sale) in the Terra colour
- **Original price** struck-through to the right (only if on sale)
- **Sale badge** as a coloured pill on the image (see below)


<!--te-src:PiAqKkN1c3RvbWl6ZSAodGhlIHByaWNlcyk6KiogQmlnQ29tbWVyY2UgYWRtaW4g4oaSIENhdGFsb2cg4oaSIFByb2R1Y3RzIOKGkiAocHJvZHVjdCkg4oaSIFByaWNpbmcg4oCUIERlZmF1bHQgUHJpY2UsIFNhbGUgUHJpY2UsIE1TUlAgLyBSZXRhaWwgcHJpY2UuIChOb3QgdGhlbWUgc2V0dGluZ3MuKSBUaGUgc2FsZSBwcmljZS9zdHJ1Y2stdGhyb3VnaCBvcmlnaW5hbCBhcmUgZHJpdmVuIGVudGlyZWx5IGJ5IHlvdXIgUHJpY2luZyBmaWVsZHMuDQ==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>


When you set an **MSRP / retail price** on the product, the theme also shows the retail price with a label. You can override that label with the **Product price label (retail)** text setting (id `pdp-retail-price-label`, default empty → uses the built-in label) under **Theme Editor → Products → Product sale badges**. There is no automatic "You save $X" calculation — the theme simply displays the retail price you entered.

Configure the badge in **Theme Editor → Products → Product sale badges**:

| Setting | id | Options | Default |
| ------- | -- | ------- | ------- |
| **Show product sale badges** | `product_sale_badges` | `None` (none) / `Top Left` (topleft) / `Diagonal` (sash) / `Burst` (burst) | `topleft` |
| **Product sale badge label** | `pdp_sale_badge_label` | text — the text in the badge (e.g. `SALE`); empty → built-in default | empty |
| **Badge color** | `color_badge_product_sale_badges` | colour picker — badge background | (theme) |
| **Badge text color** | `color_text_product_sale_badges` | colour picker — badge text | (theme) |


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqUHJvZHVjdCBzYWxlIGJhZGdlcyoqIChoZWFkaW5nKSDihpIgZmllbGRzIGFib3ZlLiBCYWRnZSBzdHlsZSBpcyBhIGRyb3Bkb3duOyBsYWJlbCBpcyBwbGFpbiB0ZXh0OyBjb2xvdXJzIGFyZSBwaWNrZXJzLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Product sale badges</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>


For the **"Sold out"** badge (same heading):

| Setting | id | Effect | Default |
| ------- | -- | ------ | ------- |
| **Show product sold-out badges** | `product_sold_out_badges` | Badge style: `None` / `Top Left` / `Diagonal` / `Burst` | `none` (off) |
| **Product sold out badge label** | `pdp_sold_out_label` | e.g. `Sold out`; empty → built-in default | empty |


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqUHJvZHVjdCBzYWxlIGJhZGdlcyoqIOKGkiAqKlNob3cgcHJvZHVjdCBzb2xkLW91dCBiYWRnZXMqKiAvICoqUHJvZHVjdCBzb2xkIG91dCBiYWRnZSBsYWJlbCoqLiBUaGUgc29sZC1vdXQgYmFkZ2UgaXMgKipvZmYgYnkgZGVmYXVsdCoqIChgbm9uZWApLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Product sale badges</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show product sold-out badges</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Product sold out badge label</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">off by default</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>


### Staff Pick badge colour

eShopping renders a **Staff Pick** badge on certain product cards. There is no merchant-facing toggle to enable it per product and no custom-badge value field — only the styling is controlled, by two colour pickers in the **eShopping Theme** section:

<!--te-tbl:fCBTZXR0aW5nIHwgaWQgfCBFZmZlY3QgfA0KfCAtLS0tLS0tIHwgLS0gfCAtLS0tLS0gfA0KfCAqKlN0YWZmIFBpY2sgQmFkZ2UgQmFja2dyb3VuZCoqIHwgYGVzaG9wcGluZy1iYWRnZS1zdGFmZi1iZ2AgfCBCYWRnZSBiYWNrZ3JvdW5kIGNvbG91ciB8DQp8ICoqU3RhZmYgUGljayBCYWRnZSBUZXh0KiogfCBgZXNob3BwaW5nLWJhZGdlLXN0YWZmLXRleHRgIHwgQmFkZ2UgdGV4dCBjb2xvdXIgfA0=-->


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKlN0YWZmIFBpY2sgQmFkZ2UgQmFja2dyb3VuZCoqIC8gKipTdGFmZiBQaWNrIEJhZGdlIFRleHQqKiAoY29sb3VyIHBpY2tlcnMpLiBUaGVzZSBvbmx5IHJlc3R5bGUgdGhlIGJhZGdlIOKAlCB0aGVyZSBpcyBubyBzZXR0aW5nIHRvIGNob29zZSAqd2hpY2gqIHByb2R1Y3RzIHNob3cgaXQuDQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Staff Pick Badge Background</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Staff Pick Badge Text</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>


---

## Variants — swatches

Color / size variants appear as **swatches** if you've set them up in **Catalog → Product Options & SKUs**:

- **Color swatches** — for option type "Swatch (Color)". The theme renders them as colour circles.
- **Image swatches** — for option type "Swatch (Image)". The theme renders the option image.
- **Rectangle text swatches** — for "Rectangle list" options (size: S / M / L). Rendered as text pills.


<!--te-src:PiAqKkN1c3RvbWl6ZSAodGhlIHZhcmlhbnRzKToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgQ2F0YWxvZyDihpIgUHJvZHVjdCBPcHRpb25zICYgU0tVcyAoc2hhcmVkIG9wdGlvbnMpIG9yIHRoZSBwcm9kdWN0J3MgKipWYXJpYXRpb25zKiogdGFiLiAoTm90IGEgdGhlbWUgc2V0dGluZyDigJQgc3dhdGNoIGNvbG91cnMvaW1hZ2VzIGNvbWUgZnJvbSB5b3VyIG9wdGlvbiB2YWx1ZXMuKQ0=-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Product Options &amp; SKUs</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>


The swatch sizes shown are styled by the theme. The only configurable image dimension is **Product swatch images** (id `swatch_option_size`, default `22x22`) under **Theme Editor → Products → Image sizes**, which controls the source resolution of image swatches.


<!--te-src:PiAqKkN1c3RvbWl6ZSAoc3dhdGNoIGltYWdlIHJlc29sdXRpb24pOioqIFRoZW1lIEVkaXRvciDihpIgKlByb2R1Y3RzKiDihpIgKipQcm9kdWN0IHN3YXRjaCBpbWFnZXMqKi4gRm9ybWF0OiBgV3hIYCBwaXhlbHMuIERlZmF1bHQ6IGAyMngyMmAuIChGb3IgdGV4dHVyZSBzd2F0Y2hlcyBCaWdDb21tZXJjZSBjYXBzIHNvdXJjZSBpbWFnZXMgYXQgYDE1MHgxNTBgLikN-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Product swatch images</span><span class="te-tx">22x22</span></div></div>


To **show swatch names beside the swatch** (e.g. "Black" next to a black swatch), check **Show product swatch names** (id `show_product_swatch_names`) in the Products panel.


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqU2hvdyBwcm9kdWN0IHN3YXRjaCBuYW1lcyoqIChjaGVja2JveCwgdW5kZXIgKkRpc3BsYXkgc2V0dGluZ3MqKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGB0cnVlYC4N-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show product swatch names</span><span class="te-cb is-on"></span></div></div>


---

## Add to Cart + sticky mobile ATC

The **Add to Cart** button is always visible on desktop. On mobile, when the user scrolls past it, a sticky bottom bar appears with **price + ATC**.

Toggle the mobile sticky ATC:


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKlNob3cgTW9iaWxlIFN0aWNreSBBZGQgdG8gQ2FydCoqIChjaGVja2JveCwgdW5kZXIgdGhlICpQcm9kdWN0IFBhZ2UgKFBEUCkqIGhlYWRpbmc7IGlkIGBlc2hvcHBpbmctcGRwLXNob3ctbW9iaWxlLWF0Y2ApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYHRydWVgLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show Mobile Sticky Add to Cart</span><span class="te-cb is-on"></span></div></div>


### Quick payment buttons

When BigCommerce's express-checkout providers (PayPal, Apple Pay, etc.) are enabled in your store, the theme can render their quick-payment buttons beneath Add to Cart.


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqU2hvdyBxdWljayBwYXltZW50IGJ1dHRvbnMqKiAoY2hlY2tib3gsIHVuZGVyICpEaXNwbGF5IHNldHRpbmdzKjsgaWQgYHNob3dfcXVpY2tfcGF5bWVudF9idXR0b25zYCkuIEZvcm1hdDogb24vb2ZmLiBEZWZhdWx0OiBgdHJ1ZWAuIFRoZSBidXR0b25zIHRoZW1zZWx2ZXMgY29tZSBmcm9tIHRoZSBwYXltZW50IHByb3ZpZGVycyB5b3UgZW5hYmxlIGluIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiBTZXR0aW5ncyDihpIgUGF5bWVudHMg4oCUIGNvbG91cnMvc2hhcGVzL2xhYmVscyBhcmUgdHVuZWQgdW5kZXIgVGhlbWUgRWRpdG9yIOKGkiAqUGF5bWVudCBidXR0b25zKi4N-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show quick payment buttons</span><span class="te-cb is-on"></span></div></div>


### Compare

The **Add to compare** control lets shoppers queue products into a compare panel.


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqU2hvdyBwcm9kdWN0IGNvbXBhcmUqKiAoY2hlY2tib3gsIHVuZGVyICpEaXNwbGF5IHNldHRpbmdzKjsgaWQgYHNob3dfY29tcGFyZWApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYHRydWVgLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show product compare</span><span class="te-cb is-on"></span></div></div>


---

## Shipping text + Warranty text { #shipping-text-warranty-text }

These are two separate settings in the **eShopping Theme** section, under the *Product Page (PDP)* heading, and they appear in different places.

**PDP Shipping Text** (id `eshopping-pdp-shipping-text`) produces the **3-item icon strip** shown under the Add-to-Cart button. It is a single field made of exactly **three `Title|Description` pairs** (6 pipe-separated segments — `Title1|Desc1|Title2|Desc2|Title3|Desc3`). The strip always renders three fixed icon cards (truck, shield, clock); extra segments are ignored.

```
Free Shipping|on orders over $500|1-Year Warranty|included with purchase|30-Day Returns|hassle-free policy
```

Plain text only — HTML and links are **not** supported (each segment is inserted as plain text via `textContent`). The strip is hidden entirely if the field is empty.


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKlBEUCBTaGlwcGluZyBUZXh0KiogKHRleHQgaW5wdXQsIHVuZGVyICpQcm9kdWN0IFBhZ2UgKFBEUCkqOyBpZCBgZXNob3BwaW5nLXBkcC1zaGlwcGluZy10ZXh0YCkuIEZvcm1hdDogYFRpdGxlMXxEZXNjMXxUaXRsZTJ8RGVzYzJ8VGl0bGUzfERlc2MzYCAocGlwZS1kZWxpbWl0ZWQsIDYgc2VnbWVudHMpLiBEZWZhdWx0IChiYXNlKTogYEZyZWUgU2hpcHBpbmd8b24gb3JkZXJzIG92ZXIgJDUwMHwxLVllYXIgV2FycmFudHl8aW5jbHVkZWQgd2l0aCBwdXJjaGFzZXwzMC1EYXkgUmV0dXJuc3xoYXNzbGUtZnJlZSBwb2xpY3lgLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">PDP Shipping Text</span><span class="te-tx">Free Shipping|on orders over $500|1-…</span></div></div>


**PDP Warranty Text** (id `eshopping-pdp-warranty-text`) is a separate field that fills the **4-card grid inside the Warranty tab** (not the strip under the ATC). It is made of exactly **four `Title|Description` pairs** (8 pipe segments). The grid always renders four fixed cards.

```
What's Covered|...|What's Not Covered|...|How to Claim|...|Extended Warranty|...
```


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKlBEUCBXYXJyYW50eSBUZXh0KiogKHRleHQgaW5wdXQsIHVuZGVyICpQcm9kdWN0IFBhZ2UgKFBEUCkqOyBpZCBgZXNob3BwaW5nLXBkcC13YXJyYW50eS10ZXh0YCkuIEZvcm1hdDogYFRpdGxlMXxEZXNjMXxUaXRsZTJ8RGVzYzJ8VGl0bGUzfERlc2MzfFRpdGxlNHxEZXNjNGAgKHBpcGUtZGVsaW1pdGVkLCA4IHNlZ21lbnRzKS4gUGxhaW4gdGV4dCBvbmx5LiBOb3RlOiB0aGUgd2FycmFudHkgKnRhYiogb25seSBhcHBlYXJzIHdoZW4gdGhlIHByb2R1Y3QgaGFzIFdhcnJhbnR5IEluZm9ybWF0aW9uIChDYXRhbG9nIOKGkiBQcm9kdWN0cyDihpIgZWRpdCDihpIgV2FycmFudHkgSW5mb3JtYXRpb24pOyB0aGlzIGZpZWxkIG9ubHkgZmlsbHMgdGhlIGNhcmQgZ3JpZCBpbnNpZGUgdGhhdCB0YWIuDQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">PDP Warranty Text</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>


---

## Tabs (Description · Videos · Specs · Warranty · FAQ · Reviews) { #pdp-tabs }

The tabs appear below the gallery. Most toggles live in **Theme Editor → Products → Display settings**:

| Setting | id | Effect | Default |
| ------- | -- | ------ | ------- |
| Show product description tabs | `show_product_details_tabs` | Show the tab strip at all | `true` |
| Show product reviews | `show_product_reviews` | Add the **Reviews** tab (only renders when the product has reviews) | `true` |
| Product custom fields in tabs | `show_custom_fields_tabs` | Show a **Specifications** tab with ALL of the product's custom fields rendered as a 2-column table | `true` |


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqU2hvdyBwcm9kdWN0IGRlc2NyaXB0aW9uIHRhYnMqKiAvICoqU2hvdyBwcm9kdWN0IHJldmlld3MqKiAvICoqUHJvZHVjdCBjdXN0b20gZmllbGRzIGluIHRhYnMqKiAoY2hlY2tib3hlcywgdW5kZXIgKkRpc3BsYXkgc2V0dGluZ3MqKS4gRm9ybWF0OiBvbi9vZmYuDQ==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAobnVtYmVyIG9mIHJldmlld3MpOioqIFRoZW1lIEVkaXRvciDihpIgKlByb2R1Y3RzKiDihpIgKipOdW1iZXIgb2YgcHJvZHVjdCByZXZpZXdzKiogKGRyb3Bkb3duIDHigJMxMjsgaWQgYHByb2R1Y3RwYWdlX3Jldmlld3NfY291bnRgOyBzaG93biBvbmx5IHdoZW4gKlNob3cgcHJvZHVjdCByZXZpZXdzKiBpcyBvbikuIERlZmF1bHQ6IGA5YC4N-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show product description tabs</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Show product reviews</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Product custom fields in tabs</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Number of product reviews</span><span class="te-tx">9</span></div></div>


The **FAQ** tab is toggled separately in the **eShopping Theme** section with the **Show FAQ Tab** setting (a built-in ask-a-question form — see [Product FAQ](product-faq.md)).


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKlNob3cgRkFRIFRhYioqIChjaGVja2JveCwgdW5kZXIgKlByb2R1Y3QgUGFnZSAoUERQKSo7IGlkIGBlc2hvcHBpbmctcGRwLXNob3ctZmFxLXRhYmApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYHRydWVgLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show FAQ Tab</span><span class="te-cb is-on"></span></div></div>


The **Warranty** tab is rendered automatically when the product has warranty text (Catalog → Products → edit → Warranty Information). Inside the warranty tab the theme shows a 4-card grid of warranty highlights (set the four title/description pairs in the **PDP Warranty Text** field — id `eshopping-pdp-warranty-text`, in the *eShopping Theme* section under *Product Page (PDP)*), plus an area below the cards where you can drop a widget — either on every product (region `product_below_warranty--global`) or on one specific product (region `product_below_warranty`).


<!--te-src:PiAqKkN1c3RvbWl6ZSAod2lkZ2V0IGJlbG93IHRoZSB3YXJyYW50eSBjYXJkcyk6KiogUGFnZSBCdWlsZGVyIOKGkiBvcGVuIGEgcHJvZHVjdCBwYWdlIOKGkiBkcm9wIGFuIEhUTUwgLyBBY2NvcmRpb24gLyBCYW5uZXIgd2lkZ2V0IGludG8gdGhlICoqQmVsb3cgd2FycmFudHkqKiByZWdpb24uIFVzZSB0aGUgZ2xvYmFsIHBsYWNlbWVudCBmb3IgYWxsIHByb2R1Y3RzIG9yIHRoZSBwYWdlLXNwZWNpZmljIHBsYWNlbWVudCBmb3Igb25lIHByb2R1Y3QuDQ==-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>


The **Videos** tab is rendered automatically when the product has videos uploaded.

### Adding "Shipping & Returns" or other content to every PDP

eShopping provides a widget area that renders BELOW the tabs (not inside them) on every PDP. Drop any HTML / Accordion / Banner widget there. There's also a matching area for content on a single product.

### Customizing the Specifications tab label

Use the **Product custom fields tab label** text setting (id `pdp-custom-fields-tab-label`) to override the tab title. Leave it empty to use the default ("Specifications").


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqUHJvZHVjdCBjdXN0b20gZmllbGRzIHRhYiBsYWJlbCoqICh0ZXh0IGlucHV0LCB1bmRlciAqRGlzcGxheSBzZXR0aW5ncyo7IHNob3duIG9ubHkgd2hlbiAqUHJvZHVjdCBjdXN0b20gZmllbGRzIGluIHRhYnMqIGlzIG9uKS4gRm9ybWF0OiBwbGFpbiB0ZXh0LiBEZWZhdWx0OiBlbXB0eSAo4oaSICJTcGVjaWZpY2F0aW9ucyIpLiBUaGUgY3VzdG9tLWZpZWxkICp2YWx1ZXMqIGNvbWUgZnJvbSBCaWdDb21tZXJjZSBhZG1pbiDihpIgQ2F0YWxvZyDihpIgUHJvZHVjdHMg4oaSIChwcm9kdWN0KSDihpIgQ3VzdG9tIEZpZWxkcy4N-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Product custom fields tab label</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>


---

## Frequently Bought Together (FBT)

A bundle widget that appears above the tab strip (between the image/info section and the tabs), showing the current product + 1–3 frequently-paired products with an optional bundle discount. See full guide: [Frequently Bought Together](product-fbt.md).

Quick toggles (**Theme Editor → eShopping Theme**, under the *Frequently Bought Together* heading):

| Setting | id | Effect | Default |
| ------- | -- | ------ | ------- |
| FBT Products Count | `eshopping-fbt-count` | dropdown `Off — don't show` (0) / `1` / `2` / `3` — number of paired products | `2` |
| Visual Bundle Discount % | `eshopping-fbt-discount-percent` | text — e.g. `10` for 10% off the bundle | `0` |


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKkZCVCBQcm9kdWN0cyBDb3VudCoqIChkcm9wZG93bjsgYDBgIGhpZGVzIHRoZSB3aG9sZSBGQlQgYmxvY2spIGFuZCAqKlZpc3VhbCBCdW5kbGUgRGlzY291bnQgJSoqICh0ZXh0IGlucHV0OyBudW1iZXIgb25seSwgbm8gYCVgIHNpZ24pLiBEZWZhdWx0czogY291bnQgYDJgLCBkaXNjb3VudCBgMGAuIFRoZSBwYWlyZWQgcHJvZHVjdHMgY29tZSBmcm9tIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiBDYXRhbG9nIOKGkiBQcm9kdWN0cyDihpIgKHByb2R1Y3QpIOKGkiBSZWxhdGVkIFByb2R1Y3RzLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">FBT Products Count</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Visual Bundle Discount %</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>


---

## Related products

Below the tabs the PDP shows a single **Related products** slider. Related products come from the product's Related Products list in BigCommerce — automatic (by category) by default, or manually curated per product in **Catalog → Products**. The slider only renders when the product has related products.

| Setting | id | Effect | Default |
| ------- | -- | ------ | ------- |
| **Product page (related products)** | `productpage_related_products_count` | How many to show; set to `0` to hide the slider | `10` |


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqUHJvZHVjdCBwYWdlIChyZWxhdGVkIHByb2R1Y3RzKSoqIChudW1iZXIgaW5wdXQsIHVuZGVyIHRoZSAqTnVtYmVyIG9mIHByb2R1Y3RzIGRpc3BsYXllZCogaGVhZGluZzsgaWQgYHByb2R1Y3RwYWdlX3JlbGF0ZWRfcHJvZHVjdHNfY291bnRgKS4gRm9ybWF0OiBpbnRlZ2VyIChgMGAgaGlkZXMpLiBEZWZhdWx0OiBgMTBgLiBUaGUgcHJvZHVjdCBsaXN0IGl0c2VsZiBjb21lcyBmcm9tIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiBDYXRhbG9nIOKGkiBQcm9kdWN0cyDihpIgKHByb2R1Y3QpIOKGkiBSZWxhdGVkIFByb2R1Y3RzLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Product page (related products)</span><span class="te-tx">10</span></div></div>


### Customers Also Viewed

The theme also has a **Customers Also Viewed** module, controlled by the **Product page (customers also viewed products)** count (id `productpage_similar_by_views_count`). When a product has **no** related products, the PDP falls back to the standard tab layout, where this module appears as a "Customers Also Viewed" carousel.


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqUHJvZHVjdCBwYWdlIChjdXN0b21lcnMgYWxzbyB2aWV3ZWQgcHJvZHVjdHMpKiogKG51bWJlciBpbnB1dCwgdW5kZXIgKk51bWJlciBvZiBwcm9kdWN0cyBkaXNwbGF5ZWQqOyBpZCBgcHJvZHVjdHBhZ2Vfc2ltaWxhcl9ieV92aWV3c19jb3VudGApLiBGb3JtYXQ6IGludGVnZXIgKGAwYCBoaWRlcykuIERlZmF1bHQ6IGAxMGAuIFRoaXMgbGlzdCBpcyBnZW5lcmF0ZWQgYnkgQmlnQ29tbWVyY2UgZnJvbSBzdG9yZS13aWRlIHZpZXcgYmVoYXZpb3VyIOKAlCB0aGVyZSBpcyBubyBtYW51YWwgcHJvZHVjdCBsaXN0IHRvIGVkaXQuDQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Product page (customers also viewed products)</span><span class="te-tx">10</span></div></div>


!!! note "Cross-sell is a cart feature"
    Cross-sell products are shown in the **cart / cart drawer**, not on the PDP — controlled by the **Cross-sell products (page,drawer — 0 = off)** field (id `eshopping-crosssell-count`, default `6,4`) under **Theme Editor → eShopping Theme → Cart Cross-sell**. The value is two numbers `page,drawer` (count on the cart page, count in the cart drawer). There is **no** recently-viewed slider on the product page (Customers Also Viewed is based on view behaviour, not the visitor's own recent history).

---

## Urgency strips

Two short message strips that build social proof. Configure them in the **eShopping Theme** section, under the *Urgency Signals (Social Proof)* heading:

| Setting | id | Effect | Default |
| ------- | -- | ------ | ------- |
| **Show live view count** | `eshopping-urgency-view-count` | Shows "X viewing now" using a random number in the range below (the exact wording is editable in the theme's language file) | `true` |
| **Fake view count range: min,max** | `eshopping-urgency-view-range` | `min,max` — the range for the viewer count | `3,25` |
| **Show last order time** | `eshopping-urgency-last-order` | Shows a "last order …" message using a random time in the range below | `true` |
| **Last order time range: min,max hours ago** | `eshopping-urgency-order-range` | `min,max` in **hours** ago | `1,48` |


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKlNob3cgbGl2ZSB2aWV3IGNvdW50KiogLyAqKlNob3cgbGFzdCBvcmRlciB0aW1lKiogKGNoZWNrYm94ZXMpLCAqKkZha2UgdmlldyBjb3VudCByYW5nZSoqIC8gKipMYXN0IG9yZGVyIHRpbWUgcmFuZ2UqKiAodGV4dCBpbnB1dHMpLiBGb3JtYXQgZm9yIHRoZSByYW5nZXM6IHR3byBpbnRlZ2VycyBgbWluLG1heGAgKGNvbW1hLXNlcGFyYXRlZDsgdGhlIG9yZGVyIHJhbmdlIGlzIGluIGhvdXJzKS4gRGVmYXVsdHM6IHZpZXcgcmFuZ2UgYDMsMjVgLCBvcmRlciByYW5nZSBgMSw0OGAsIGJvdGggdG9nZ2xlcyBgdHJ1ZWAuDQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show live view count</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show last order time</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Fake view count range</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Last order time range</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>


The last-order message adapts its units automatically — it can read as minutes, hours, or days ago depending on the random value.

These are randomized client-side per session — they're not tracked analytics.

---

## Quick view button

The product card in sliders + category grids has a **Quick View** button. Clicking it opens a modal showing the PDP without leaving the page. Toggle it in **Theme Editor → Products → Display settings**:

- **Show quickview button on product cards** (id `show_product_quick_view`)


<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqU2hvdyBxdWlja3ZpZXcgYnV0dG9uIG9uIHByb2R1Y3QgY2FyZHMqKiAoY2hlY2tib3gsIHVuZGVyICpEaXNwbGF5IHNldHRpbmdzKjsgaWQgYHNob3dfcHJvZHVjdF9xdWlja192aWV3YCkuIEZvcm1hdDogb24vb2ZmLg0=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show quickview button on product cards</span><span class="te-cb"></span></div></div>


---

## Stock availability & rating bars (automatic)

- **Stock badge / availability message** comes straight from the product record — BigCommerce admin → Catalog → Products → (product) → Inventory (stock level, "Stock Level Display") and the availability text. (Not a theme setting; there is no Theme Editor toggle for the PDP availability line.)
- **Review rating bars** (the 5-star breakdown in the Reviews tab) are rendered automatically from the product's approved reviews — no setting. Reviews are managed in BigCommerce admin → Products → Product Reviews. The Reviews tab and its count are gated by **Show product reviews** / **Number of product reviews** (see [Tabs](#pdp-tabs)).

---

## Product page settings in the demo stores

All four demo stores (Industrial, Auto Parts, Electronics, Packaging) use the **same** PDP configuration. The only thing that differs between them is the copy in the shipping/warranty fields:

<!--te-tbl:fCBTZXR0aW5nIHwgaWQgfCBWYWx1ZSAoYWxsIGZvdXIgZGVtb3MpIHwNCnwgLS0tLS0tLSB8IC0tIHwgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSB8DQp8IEZCVCBQcm9kdWN0cyBDb3VudCB8IGBlc2hvcHBpbmctZmJ0LWNvdW50YCB8IGAyYCB8DQp8IFZpc3VhbCBCdW5kbGUgRGlzY291bnQgJSB8IGBlc2hvcHBpbmctZmJ0LWRpc2NvdW50LXBlcmNlbnRgIHwgYDBgIChubyBidW5kbGUgZGlzY291bnQpIHwNCnwgU2hvdyBsaXZlIHZpZXcgY291bnQgfCBgZXNob3BwaW5nLXVyZ2VuY3ktdmlldy1jb3VudGAgfCDinIUgKHJhbmdlIGAzLDI1YCkgfA0KfCBTaG93IGxhc3Qgb3JkZXIgdGltZSB8IGBlc2hvcHBpbmctdXJnZW5jeS1sYXN0LW9yZGVyYCB8IOKchSAocmFuZ2UgYDEsNDhgKSB8DQ==-->

Each store fills its own **PDP Shipping Text** (`eshopping-pdp-shipping-text`) and **PDP Warranty Text** (`eshopping-pdp-warranty-text`) with industry-appropriate copy (e.g. Auto Parts uses a "Fitment Guarantee", Packaging uses "Bulk Pricing" / "Same-Day Ship"), but the structural settings above are identical. See the per-block defaults in [How to customize each section](#shipping-text-warranty-text) above.

![Packaging PDP example](../img/packaging-pdp.png){ loading=lazy }

---

## Next

- [Product card style](product-card.md)
- [Frequently Bought Together](product-fbt.md)
- [Product FAQ](product-faq.md)
- [Category page →](category.md)
