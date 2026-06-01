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

## Sitewide promo banner

Use the top-banner HTML in **Marketing → Banners** ([see Header & top bar](header-and-topbar.md)) to announce site-wide promos. The examples below are illustrative copy only — adapt them to your own offers (keep text plain; the theme uses inline icons, not emoji):

- **Flash sale**: `24-hour flash sale — 30% off everything with code FLASH30`
- **Restock**: `Back in stock: limited quantities on a popular item — order now`
- **Holiday**: `Holiday shipping cutoff: Dec 18 for ground, Dec 22 for express`

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
