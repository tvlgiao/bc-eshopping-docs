# Home Page — Packaging Variant

Live demo: <https://eshopping-packaging-demo.mybigcommerce.com>

![Packaging home page composed view](../img/home-packaging-composed.png){ loading=lazy }

![Packaging home hero (desktop)](../img/packaging-desktop-hero.png){ loading=lazy }
![Packaging mobile 375 view](../img/packaging-mobile-375.png){ loading=lazy }

!!! note "Before you start"
    Theme installed, **Packaging** variation picked, **Packaging** product + widget data imported.

The Packaging variation **already populates** most settings (colors, fonts, trust strip, newsletter, promo, SEO text, cart goal, PDP info, popups). The recipe below shows what's set automatically and how the live demo home page is composed.

!!! info "How the live demo home page is composed, top to bottom"
    1. Hero (BigCommerce Home Page Carousel)
    2. Trust strip
    3. Featured Products slider
    4. New Arrivals slider
    5. Products by Category
    6. Value-prop callout (HTML Widget — *Page Builder*)
    7. Customer Reviews carousel (HTML Widget — *Page Builder*)
    8. Packaging Resources & Guides (HTML Widget — *Page Builder*)
    9. Brands carousel
    10. Blog posts
    11. Newsletter
    12. About block (HTML Widget — *Page Builder*)
    13. Talk to an Expert CTA bar (HTML Widget — *Page Builder*)

## Section-by-section recipe

### 1. Variation

Theme Editor → **Packaging**.

### 2. Colors — set automatically

These values are applied for you when you pick the variation:

| Color | Value |
| ----- | ----- |
| Primary accent | `#059669` (emerald) |
| Primary accent (dark) | `#047857` |
| Primary accent (light) | `#34d399` |
| Primary accent (pale) | `#ecfdf5` |
| Darkest neutral | `#0c0a09` (warm stone) |
| Dark neutral | `#1c1917` |
| Lightest neutral | `#fafaf9` |
| Cream / background | `#fafaf9` |
| Sale badge background | `#dc2626` |
| Staff-pick badge background | `#059669` |
| Active rating star | `#f59e0b` |
| Sale price | `#dc2626` |
| Original (struck-through) price | `#a8a29e` |

### 3. Fonts — set automatically

| Font | Value |
| ---- | ----- |
| Body font | DM Sans (weights 400, 500) |
| Headings font | DM Sans (weights 600, 700) |
| Mono font | IBM Plex Mono (weight 400) |

### 4. Top banner

Banner colors set by the variation:

| Color | Value |
| ----- | ----- |
| Banner background | `#44403c` |
| Banner text | `#d6d3d1` |
| Banner link | `#34d399` |

!!! tip "Banner content"
    The banner colors ship with the variation, but the banner message itself is created under **Marketing → Banners**. Add your own carbon-neutral / bulk-quote messaging there.

### 5. Header

| Setting | Value |
| ------- | ----- |
| Top bar background | `#0c0a09` |
| Top bar text | `#a8a29e` |
| Nav background | `#ffffff` |
| Nav text | `#57534e` |
| Nav search button | `#059669` |
| Search box typing phrases | Search for shipping boxes… / Find bubble wrap & packing… / Browse tape & labels… / Discover mailer bags & envelopes… |
| Voice search | On |
| Welcome text | *(empty in the demo — leave blank or add your own)* |

### 6. Hero

The demo uses the built-in hero driven by the BigCommerce Home Page Carousel:

1. In your BigCommerce admin, open the **Home Page Carousel** (in the Storefront area) and upload your slides.
2. The variation already turns on **Show hero** and the BigCommerce carousel.

!!! tip "Slide ideas (suggestions only)"
    These are starting points, not demo content:

    | Slide | Image | Heading | Sub | CTA |
    | :---: | ----- | ------- | --- | --- |
    | 1 | Lifestyle shot of recyclable boxes | **Packaging that protects more than products.** | Recyclable, compostable, beautiful. | `Shop the catalog` → /catalog |
    | 2 | Stack of mailers with kraft texture | **Custom-printed mailers** | From 25 units. Turnaround in 7 days. | `Start a quote` → /quote |

### 7. Trust strip — variation default (enabled)

**Show trust strip** is on. The variation fills in four trust items, each with a title and description:

- **Bulk Pricing** — Volume discounts on all packaging supplies
- **Same-Day Ship** — Orders placed by 2pm ship today
- **Free Samples** — Try before you buy on select items
- **Expert Support** — Packaging specialists available Mon-Fri

### 8. Featured Products — enabled

**Show featured products** is on. The Featured Products slider appears on the live demo, populated from products flagged as Featured in the catalog.

### 9. Bestselling — enabled (will not display without sales data)

**Show bestselling** is turned on. However, the demo store has no bestseller sales data yet, so the Bestselling slider **does not appear** on the live home page. It will display automatically once the store accumulates order/sales history.

### 10. New Arrivals — enabled

**Show new arrivals** is on. The New Arrivals slider appears on the live demo.

### 11. Products by Category — enabled

**Show products by category** is on. Configuration as shipped:

| Setting | Value |
| ------- | ----- |
| Category IDs | *Empty* — automatically uses the first top-level categories, limited to the first grid number (3 for this variation). Set specific Category IDs to control which categories appear. |
| Grid layout (per breakpoint) | `3, 4, 6` |
| Active tab | **Featured** |
| Tabs shown | Bestselling, Featured, New |
| Show reviews | Off |

### 12. Value-prop callout (HTML Widget — Page Builder)

Below the Products by Category section, the demo renders an **HTML Widget** (added via Page Builder, imported with the demo widget data — **not** a theme setting). Heading: *"Packaging That Protects. Pricing That Scales."*.

This block is the first of three HTML Widgets that sit directly **below Products by Category** (this one appears first).

### 12b. Customer Reviews (HTML Widget — Page Builder)

The second HTML Widget below Products by Category is a scrollable carousel of **12 customer testimonials**, each with a 5-star rating, quote, reviewer name/role, and a "Verified" tag. Like the others, it's imported with the demo widget data — **not** a theme setting. It appears directly after the value-prop callout.

### 12c. Packaging Resources & Guides (HTML Widget — Page Builder)

The third HTML Widget below Products by Category, headed *"Packaging Resources & Guides"*, shows three guide cards that link to blog posts:

- **How to Choose the Right Box Size**
- **Bubble Wrap vs. Foam Peanuts vs. Air Pillows**
- **Shipping Label Best Practices**

It's imported with the demo widget data — **not** a theme setting — and appears after the Customer Reviews carousel.

### 13. Brands carousel — enabled

The homepage brands limit is `12`, so the Brands carousel appears on the live demo.

### 14. Blog

The homepage blog posts count is `3`.

![Packaging blog index](../img/packaging-blog-index.png){ loading=lazy }

### 15. Newsletter — variation default

**Show newsletter** is on. The variation sets the heading and description:

- Heading: Subscribe for *Packaging Deals*
- Description: Bulk offers, new product alerts, and industry tips delivered to your inbox.

### 16. About block (HTML Widget — Page Builder)

Below the newsletter, the demo renders a second **HTML Widget** (added via Page Builder, imported with the demo widget data — **not** a theme setting). Heading: *"Your Complete Shipping Supplies Source"*.

This block is the first of two HTML Widgets directly **below Newsletter** (this one appears first).

### 16b. Talk to an Expert (HTML Widget — Page Builder)

The second HTML Widget below the newsletter renders a dark CTA bar with the heading *"Need help choosing packaging? Talk to a Packaging Specialist"*. It includes a **Request a Quote** button linking to `/contact-us/` and a phone number, **(800) 555-0123**. Like the About block, it's imported with the demo widget data — **not** a theme setting — and appears directly after it.

### 17. SEO text — pre-filled but hidden

The variation **pre-fills** the SEO text below, but the **Show SEO text** toggle is **off**, so it does **not** display on the live demo. Turn the toggle on if you want it shown.

```
Packaging & Shipping Supplies|Your one-stop shop for professional packaging materials. From corrugated boxes and bubble wrap to tape, mailer bags, and shipping labels.|Competitive bulk pricing, same-day shipping, and expert guidance to help you find the right packaging solutions for your business.
```

### 18. Sidebar / cart / PDP — variation defaults

| Setting | Value |
| ------- | ----- |
| Sidebar promo | Title "Free Shipping $300+", description "Free ground shipping on qualifying packaging orders.", button "Shop Supplies" linking to /shipping/ |
| Cart goal milestones | $75 → Free Shipping, $150 → 10% Off, $300 → Free Samples |
| PDP shipping info | Free Shipping (on orders over $300), Bulk Pricing (volume discounts available), Same-Day Ship (orders by 2pm) |
| PDP warranty | What's Covered, What's Not Covered, How to Claim, Satisfaction Guarantee |
| Frequently Bought Together | 2 products, 0% bundle discount |
| Cross-sell counts | 6 / 4 |

### 19. Popups — variation defaults

| Popup | Content |
| ----- | ------- |
| Newsletter popup | "Get 10% Off Your First Order" — "Sign up for our newsletter and receive an exclusive discount code." (shows after 20s, reappears every 14 days) |
| Promo popup | "Spring Sale" — "Get 15% off your entire order with the code below." Code `SPRING15`, button "Shop Now" → / (shows after 5s, every 3 days) |
| Exit-intent popup | "Wait! Don't Go Empty-Handed" — "Here's a special 10% discount just for you." Code `STAY10`, button "Claim Discount" → / (discount style, every 45 days, once per session) |

### 20. Urgency & social proof — variation defaults

| Setting | Value |
| ------- | ----- |
| Show "viewing now" count | On |
| Show "last ordered" time | On |
| Recent-sales notifications | On all pages — California (2 hours ago), Texas (35 min ago), Florida (4 hours ago), New York (1 hour ago), Oregon (6 hours ago) |

---

## Mobile preview

The Packaging demo is heavy on widgets — preview at 375 px to verify nothing breaks. Use the device-switcher at the top of Page Builder.

![Packaging mobile widget stack](../img/packaging-mobile-widgets.png){ loading=lazy }

---

## Final check

Compare to <https://eshopping-packaging-demo.mybigcommerce.com>.

---

## Next

- [Product page](product.md)
- [Static pages (About / Privacy / Returns)](static-pages.md)
