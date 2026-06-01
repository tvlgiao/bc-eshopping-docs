# Home Page — Electronics Variant

Live demo: <https://eshopping-electronics-demo.mybigcommerce.com>

![Electronics home page composed view](../img/home-electronics-composed.png){ loading=lazy }

!!! note "Before you start"
    Theme installed, **Electronics** variation picked, **Electronics** product + widget data imported.

The Electronics variation **already populates** most settings (colors, fonts, trust strip, newsletter, promo, cart goal, PDP shipping). Recipe below shows what's set automatically + what to override.

!!! info "What actually renders on the live home page"
    In order, top to bottom: **Hero** → **Trust strip** → **Featured Products** → **New Arrivals** → **Products by Category** → **value-prop callout** (HTML widget) → **Brands carousel** → **Blog posts** → **Newsletter** → **about block** (HTML widget). The two HTML widgets are placed via Page Builder by the demo widget import — not from theme settings.

## Section-by-section recipe

### 1. Variation

Theme Editor → **Electronics**.

### 2. Colors — set automatically

The Electronics variation applies these colors for you:

| Color | Value |
| ----- | ----- |
| Primary accent | `#3b82f6` (electric blue) |
| Primary accent (dark) | `#2563eb` |
| Primary accent (light) | `#60a5fa` |
| Primary accent (pale) | `#eff6ff` |
| Darkest neutral | `#09090b` (zinc) |
| Dark neutral | `#18181b` |
| Light neutral | `#fafafa` |
| Cream | `#fafafa` |
| Sale badge background | `#dc2626` |
| Staff pick badge background | `#d97706` |
| Active rating star | `#f59e0b` |
| Sale price | `#dc2626` |
| Original (struck-through) price | `#94a3b8` |

### 3. Fonts — set automatically

| Font | Value |
| ---- | ----- |
| Body font | Inter (weights 400, 500, 600) |
| Headings font | Space Grotesk (weights 500, 700) |
| Mono font | IBM Plex Mono (weight 400) |

### 4. Top banner

**Marketing → Banners → Create**. HTML (*example copy — replace with your own*):

```html
<div data-banner-carousel style="text-align:center">
  <div>⚡ Free shipping on $99+ orders</div>
  <div>New GPU drop incoming — <a href="/gpus">join the waitlist</a></div>
  <div>Trade in your old phone — up to $400 off</div>
</div>
```

Banner colors set by variation:

| Banner color | Value |
| ------------ | ----- |
| Banner background | `#3f3f46` |
| Banner text | `#d4d4d8` |
| Banner link | `#60a5fa` |

### 5. Header

| Setting | Value |
| ------- | ----- |
| Top bar background | `#09090b` |
| Top bar text | `#a1a1aa` |
| Nav background | `#ffffff` |
| Nav text | `#52525b` |
| Nav search button | `#3b82f6` |
| Search typing phrases | `Search for laptops & monitors...`, `Find headphones & speakers...`, `Browse keyboards & mice...`, `Discover cables & adapters...` |
| Voice search | On |
| Welcome text | (empty in the demo) |

### 6. Hero

Use the built-in hero:

1. **Storefront → Home Page Carousel** → upload 3 slides (1920 × 700).
2. eShopping → Homepage → turn on **Show hero**.
3. Turn on **Show carousel**.
4. Mobile fixed height (BC carousel setting) — `420`.

Slide ideas (*suggestions only*):

| Slide | Image | Heading | CTA |
| :---: | ----- | ------- | --- |
| 1 | Gaming laptop hero | Power. Anywhere. | Shop laptops → /laptops |
| 2 | Wireless headphones | Sound that disappears | Shop audio → /audio |
| 3 | 4K monitor stack | Studio-grade displays | Shop monitors → /monitors |

### 7. Trust strip — variation default

**Show trust strip** is on. The variation fills in four items (title + description each):

- **Authorized Dealer** — Genuine products with full manufacturer warranty
- **Free Shipping** — On all orders over $99
- **Easy Returns** — 30-day hassle-free returns
- **Tech Support** — Expert assistance 7 days a week

### 8. Featured Products

**Show featured products** is on. The Featured Products slider renders on the live home page.

### 9. Bestselling

**Show bestselling** is on, but the demo has **no bestseller sales data**, so the bestselling slider does **not** appear on the live home page. It will only show once products have recorded sales.

### 10. New Arrivals

**Show new arrivals** is on. The New Arrivals slider renders on the live home page.

### 11. Products by Category tabs

**Show products by category** is on. Demo configuration:

| Setting | Value |
| ------- | ----- |
| Category IDs | *(empty)* — auto-uses all top-level categories |
| Grid columns | `3,4,6` |
| Active tab | Featured |
| Show Bestselling tab | ✅ |
| Show Featured tab | ✅ |
| Show New Arrivals tab | ✅ |
| Show Top Rated tab | ❌ (off) |

### 12. Brands carousel

12 brand logos shown on the home page. The demo uses fictional brand names (TechNova, PixelCraft, AudioWave, etc.) — replace them with your own brands.

### 13. Blog

Home page blog posts: `3`. Add at least 3 posts with featured images.

### 14. Value-prop callout (HTML widget)

A Page Builder **HTML Widget** placed in the region **below Products by Category**, with the heading **Tech That Performs. Pricing That Powers Up.** It arrives with the demo widget import — it is not a theme setting.

### 15. Newsletter — variation default

The variation sets the heading **Stay Ahead in *Tech*** with the description "Product launches, exclusive deals, and expert reviews delivered weekly."

### 16. About block (HTML widget)

A Page Builder **HTML Widget** placed in the region **below the Newsletter**, with the heading **Your Complete Consumer Electronics Source.** Like the callout above, it comes from the demo widget import — not a theme setting.

### 17. SEO text — pre-filled but hidden

The variation **pre-fills** this SEO block, but the **Show SEO text** toggle is **off**, so it is **not displayed** on the demo home page. Turn the toggle on if you want it to appear.

- **Title:** Electronics & Tech Accessories
- **Paragraph 1:** Discover the latest in technology — laptops, monitors, headphones, keyboards, cables, hubs, chargers, and storage devices from top brands.
- **Paragraph 2:** Authorized dealer with manufacturer warranties, competitive pricing, and expert tech support to help you make the right choice.

### 18. Marketing features to turn on

| Setting | Value |
| ------- | ----- |
| Frequently Bought Together count | `2` |
| Frequently Bought Together discount | `0`% |
| Urgency: view count | ✅ |
| Urgency: last order | ✅ |
| Recent sales pages | All pages |
| Newsletter popup | Heading "Get 10% Off Your First Order", description "Sign up for our newsletter and receive an exclusive discount code." |
| Promo popup | Heading "Spring Sale", description "Get 15% off your entire order with the code below.", code `SPRING15`, button "Shop Now", link `/` |
| Exit popup | Heading "Wait! Don't Go Empty-Handed", description "Here's a special 10% discount just for you.", code `STAY10`, button "Claim Discount", link `/` |
| Exit popup options | Type `discount`, after 45 seconds, show once per session |

See [Urgency + recent sales](urgency-and-recent-sales.md), [Popups](popups.md), [FBT](product-fbt.md).

### 19. Sidebar promo / cart goal / PDP shipping & warranty (variation defaults)

| Setting | Value |
| ------- | ----- |
| Sidebar promo | Heading "Free Shipping $99+", text "Free shipping on all electronics orders over $99.", button "Shop Deals", link `/shipping/` |
| Cart goals | Free Shipping at $30, 5% Off at $75, Free Accessory at $150 |
| PDP shipping notes | "Free Shipping" — on orders over $99; "Manufacturer Warranty" — full coverage included; "30-Day Returns" — hassle-free policy |
| PDP warranty | "What's Covered", "What's Not Covered", "How to Claim", "Extended Protection" (four blocks, pre-filled) |

---

## Final check

Compare to <https://eshopping-electronics-demo.mybigcommerce.com>.

---

## Next

- [Product page](product.md)
- [Frequently Bought Together](product-fbt.md)
- [Packaging →](home-packaging.md)
</content>
</invoke>
