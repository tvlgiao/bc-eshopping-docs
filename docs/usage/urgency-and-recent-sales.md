# Urgency Strips & Recent-Sales Toasts

Two lightweight social-proof / scarcity features built into eShopping. The numbers are generated client-side from ranges you configure — they're a friendly UX nudge, not real-time analytics.

## Urgency strips

A pair of short message strips above the Add-to-Cart button that build urgency. They appear on the product page **and** in the Quick View modal:

- **"23 viewing now"** — a number picked from the viewing-count range you set
- **"Bought 14h ago"** — a time picked from the last-order range you set (e.g. `35m ago`, `2d ago`)

On out-of-stock products the "last order" strip is hidden automatically; the view-count strip still shows.

### Configure

**Theme Editor → eShopping Theme → Urgency Signals (Social Proof)**:

| Setting | Effect |
| ------- | ------ |
| Show live view count | Show / hide the "viewing now" strip |
| Show last order time | Show / hide the "Bought … ago" strip |
| Fake view count range | The lowest and highest viewer number shown — e.g. `3,25` shows 3–25 viewers |
| Last order time range | The lowest and highest number of hours used internally — e.g. `1,48` generates times from "1 hour ago" up to "2 days ago" (the theme formats hours into minutes, hours, or days as appropriate) |

Turn both strips off to hide them entirely.

---

## Recent-sales toasts

Small pop-up toasts at the bottom of the screen showing recent purchase activity, for social proof. They never appear on the cart or checkout pages. Once a visitor closes a toast, no more toasts are shown for the rest of that browsing session.

### Configure

**Theme Editor → eShopping Theme → Recent Sales Popup**:

| Setting | Options / Format | Effect |
| ------- | ---------------- | ------ |
| Show on pages | Off — don't show · All pages · Homepage only · Product pages only · Category pages only | Where the toasts may appear |
| Popup timing | Four comma-separated seconds: delay, show duration, pause between, max popups — e.g. `5,5,15,5` | Controls when and how often toasts appear |
| Products | List of `ID-or-SKU\|location\|timeAgo` entries, comma-separated | The products and labels each toast shows |

Set **Show on pages** to "Off — don't show" to disable.

### How the data is sourced

Each toast shows a product you list in the **Products** setting, using the location and time you enter for that entry (for example `77|California|2 hours ago`). If you leave the time blank on an entry — or if no products are listed and the best-seller fallback is used — a random time is generated. Locations are not auto-randomized; they come from what you type.

There's no order tracking — the toasts are designed for social-proof UX, not analytics. If you want to swap to real-order data, that's a customization beyond the built-in scope; email <contact@papathemes.com>.

## How the demo stores are configured

All four demo stores (Industrial, AutoParts, Packaging, Electronics) use the same setup:

| Setting | Value (all four stores) |
| ------- | ----------------------- |
| Show live view count | On |
| Show last order time | On |
| View count range | 3–25 viewers (default) |
| Last order time range | 1–48 hours (default) |
| Recent-sales toasts | On — All pages |

> **Merchant tip:** these urgency tactics suit consumer-facing catalogs best. For a strictly B2B catalog you may prefer to turn the view-count and last-order strips off, since B2B buyers tend to be driven more by spec, price, and account terms.

### Notes & gotchas

- Both features pause when the browser tab is hidden or backgrounded, and resume when it's visible again.
- A visitor can dismiss a toast with its close button; the dismissal is remembered for the rest of the session.
- All toast and strip text is translatable through your store's language settings.

---

## Next

- [Popups (Newsletter / Promo / Exit-intent)](popups.md)
- [Promotions / free-shipping bar](promotions.md)
