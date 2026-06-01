# Cart Page

The eShopping cart has two surfaces:

1. **Cart drawer** — a slide-in panel from the right edge that opens after the shopper adds an item to the cart (from the product page, quick view, or product listings). Products with options open quick view first, then the drawer slides in once the item is added.
2. **Cart page** (`/cart.php`) — the full-page view when the user clicks **View cart**.

Both show the same line-items and totals. The cart page also has an order-summary sidebar with the goal bar and a cross-sell section below the items; the cart drawer shows the goal bar and cross-sell too.

!!! note "Logged-out shoppers"
    If your store is set to hide prices from guests, the **goal bar** and the **You May Also Like** cross-sell are hidden for visitors who are not signed in. They appear once the shopper signs in — or if your store shows prices to guests.

## Cart goal bar

A theme-driven progress bar that rewards customers as their **cart subtotal** grows. It is **multi-tier**: you define a series of dollar milestones, and each milestone shows a marker on the bar plus a labelled reward (e.g. free shipping, a discount, a free gift). As the subtotal passes each milestone, that marker is ticked off.

The bar appears at the top of the order-summary sidebar on the cart page and in the cart drawer.

### Configure the tiers

**Theme Editor → eShopping Theme → Cart Goal Bar → Goal items (amount|icon|label, comma-separated)**

Enter a comma-separated list of tiers. Each tier is three parts joined by a pipe (`|`):

```
amount|icon|label
```

- **amount** — the cart subtotal (in your store currency) that unlocks this tier.
- **icon** — an optional icon keyword (see below).
- **label** — the reward text shown under the marker.

Example (the Industrial demo default):

```
50|shipping|Free Shipping,100|discount|10% Off,150|gift|Free Gift
```

This renders three milestones at $50, $100, and $150. The bar fills toward the highest tier and ticks off each marker as the subtotal reaches it.

!!! info "Supported icon keywords"
    `shipping`, `discount`, `gift`, `check`, `bag`, `star`. The icon part is optional — if you omit it, write the tier as `amount|label` (two parts).

### Messages shown to the shopper

The bar text updates automatically:

- Before the top tier is reached: *"$X away from {label}!"* — where `$X` (the formatted currency amount) is bolded and is the amount left until the next milestone, and `{label}` is that milestone's reward.
- Once every tier is unlocked: *"You've unlocked all rewards!"*

These messages are built into the theme. The reward labels come from the **Goal items** field; the surrounding text ("away from" and "You've unlocked all rewards!") is fixed in the theme code.

!!! note
    The goal bar is based on **dollar subtotal**, not item count. To turn it off entirely, clear the **Goal items** field.

## Cross-sell ("You May Also Like")

Both the cart page and the cart drawer can show a **You May Also Like** section. It pulls BigCommerce **related products** for the items currently in the cart — that is, the related products you assign to each product (or the store's automatic related products) — aggregated across all cart items and de-duplicated so nothing already in the cart is suggested.

The heading text **You May Also Like** comes from the theme's language strings and can be edited there.

### Configure the counts

**Theme Editor → eShopping Theme → Cart Cross-sell → Cross-sell products (page,drawer — 0 = off)**

This field takes **two numbers separated by a comma**:

- The **first** number is how many products to show on the **cart page**.
- The **second** number is how many to show in the **cart drawer**.

Example (the demo default for all four stores):

```
6,4
```

Set either number to `0` to turn that surface's cross-sell off.

## Widget area below the cart

The cart **page** exposes one widget region, which renders **below the cart items and the cross-sell section**. You can drop an **HTML Widget** here from the BigCommerce page-builder / widget tools to add custom content — for example a short value-prop list:

```html
<ul>
  <li>Free shipping on qualifying orders</li>
  <li>30-day no-questions returns</li>
  <li>Volume pricing on bulk orders</li>
</ul>
```

!!! note
    This widget area exists on the cart **page only**. The cart **drawer** does not accept HTML widgets.

## Cart goal bar — demo store values

The four demo stores all ship with a populated multi-tier goal bar and the same cross-sell counts (`6,4`):

| Variant | Goal bar tiers |
| ------- | -------------- |
| Industrial | `50|shipping|Free Shipping,100|discount|10% Off,150|gift|Free Gift` |
| Auto Parts | `50|shipping|Free Shipping,100|discount|10% Off,200|gift|Free Gift` |
| Packaging | `75|shipping|Free Shipping,150|discount|10% Off,300|gift|Free Samples` |
| Electronics | `30|shipping|Free Shipping,75|discount|5% Off,150|gift|Free Accessory` |

---

## Next

- [Search & keyword suggestions](search.md)
- [Blog](blog.md)
- [Static pages (About / Privacy / Returns)](static-pages.md)
