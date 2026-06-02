# Promotions & Discounts

Promotions are powered by **BigCommerce → Marketing → Promotions**, not by the theme. eShopping just renders the messages and badges. This page is a quick guide to the promos that work best with the theme.

## Free-shipping progress bar

See [Cart page → Cart goal bar](cart.md#cart-goal-bar).

## Coupon-code field

The cart page shows an **Apply coupon code** link in the order-summary box, below the totals. Clicking it reveals a field where customers can enter a code from any promotion of type **Coupon Code**.

!!! note
    This in-cart coupon link appears when your store has the multi-coupon cart UI enabled in BigCommerce. Otherwise, customers enter coupon codes at checkout.

## Bundle discount (FBT)

If you've set a **Visual Bundle Discount %** in [Frequently Bought Together](product-fbt.md), be aware that this figure is **display-only** — it shows a "You save" amount on the PDP but does **not** apply at checkout. To make the discount real, create a matching cart-level promotion (`Spend $X get Y% off`) in BigCommerce so it actually deducts at checkout.

## Sale badge on PDP / cards

eShopping reads the difference between **Original price** and **Sale price** in BigCommerce. If you've set a sale price, a sale badge appears automatically on every card and PDP — as long as **Show product sale badges** (Theme Editor → Products) is not set to **None**.

| Field on product | What |
| ---------------- | ---- |
| **Price** | The normal selling price |
| **Sale price** | Lower price → triggers the sale badge |
| **MSRP / Retail price** | Comparison price shown as struck-through |

Badge style and position is set in **Theme Editor → Products → Show product sale badges** (within the **Product sale badges** section) — choose **None**, **Top left**, **Diagonal**, or **Burst**. You can also set the **Badge text color**, **Badge color**, and **Badge hover color** in the same section.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqU2hvdyBwcm9kdWN0IHNhbGUgYmFkZ2VzKiogKGlkIGBwcm9kdWN0X3NhbGVfYmFkZ2VzYCkuIEZvcm1hdDogc2VsZWN0IOKAlCBgbm9uZWAgwrcgYHRvcGxlZnRgIMK3IGBzYXNoYCAoRGlhZ29uYWwpIMK3IGBidXJzdGAuIERlZmF1bHQ6IGB0b3BsZWZ0YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqQmFkZ2UgdGV4dCBjb2xvcioqIChpZCBgY29sb3JfdGV4dF9wcm9kdWN0X3NhbGVfYmFkZ2VzYCkuIEZvcm1hdDogY29sb3IuIERlZmF1bHQ6IGAjZmZmZmZmYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqQmFkZ2UgY29sb3IqKiAoaWQgYGNvbG9yX2JhZGdlX3Byb2R1Y3Rfc2FsZV9iYWRnZXNgKS4gRm9ybWF0OiBjb2xvci4gRGVmYXVsdDogYCNiZjViMzNgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSICoqQmFkZ2UgaG92ZXIgY29sb3IqKiAoaWQgYGNvbG9yX2hvdmVyX3Byb2R1Y3Rfc2FsZV9iYWRnZXNgKS4gRm9ybWF0OiBjb2xvci4gRGVmYXVsdDogYCM5OTNmMWZgLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show product sale badges</span><span class="te-dd"><span class="te-dd__v">topleft</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Badge text color</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Badge color</span><span class="te-color"><span class="te-hex">#BF5B33</span><span class="te-sw" style="background:#bf5b33"></span></span></div><div class="te-mock__row"><span class="te-lbl">Badge hover color</span><span class="te-color"><span class="te-hex">#993F1F</span><span class="te-sw" style="background:#993f1f"></span></span></div></div>

## Sitewide promo banner

Use the top-banner HTML in **Marketing → Banners** ([see Header & top bar](header-and-topbar.md)) to announce site-wide promos. The examples below are illustrative copy only — adapt them to your own offers (keep text plain; the theme uses inline icons, not emoji):

- **Flash sale**: `24-hour flash sale — 30% off everything with code FLASH30`
- **Restock**: `Back in stock: limited quantities on a popular item — order now`
- **Holiday**: `Holiday shipping cutoff: Dec 18 for ground, Dec 22 for express`

There is also a **sidebar promo card** — a small heading/description/button block rendered in the category sidebar — driven entirely by a theme setting:

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNpZGViYXIgUHJvbW8gQ2FyZCog4oaSICoqU2lkZWJhciBQcm9tbyBUZXh0KiogKGlkIGBlc2hvcHBpbmctcHJvbW8tdGV4dGApLiBGb3JtYXQ6IHBpcGUtc2VwYXJhdGVkIGBIZWFkaW5nfERlc2NyaXB0aW9ufEJ1dHRvbiBMYWJlbHxVUkxgLiBEZWZhdWx0OiBgRnJlZSBTaGlwcGluZyAkNTAwK3xGcmVlIGdyb3VuZCBzaGlwcGluZyBvbiBxdWFsaWZ5aW5nIG9yZGVycy58U2hvcCBOb3d8L3NoaXBwaW5nL2Au-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Sidebar Promo Card</div><div class="te-mock__row"><span class="te-lbl">Sidebar Promo Text</span><span class="te-tx">Free Shipping $500+|Free ground ship…</span></div></div>

## Newsletter signup → first-order coupon

A common flow: newsletter popup offers 10% off; user signs up; you email them a coupon code.

1. **Marketing → Promotions → Create** — type **Coupon Code**, single-use, **10% off whole cart**.
2. Configure the popup ([Popups → Newsletter](popups.md#newsletter-popup)) with the coupon code in the text:

   ```
   Get 10% off your first order — your code: WELCOME10
   ```

3. (Optional) Set up Mailchimp/Klaviyo to push the subscriber list to your ESP and trigger an automated welcome email.

## Volume pricing / quantity discounts

BigCommerce supports tiered pricing per product or per customer group:

1. Catalog → Products → edit the product → **Pricing** tab.
2. Add **Bulk pricing rules** (e.g. ≥10 = 5% off, ≥100 = 15% off).
3. eShopping displays a price table below the price on the PDP automatically.

For B2B stores, also see **Customers → Customer groups** to create a *Wholesale* group with its own pricing tier.

---

## Next

- [Update guide](../update.md)
- [FAQs](../faqs.md)
