# Popups (Newsletter / Promotion / Exit-Intent)

eShopping ships 3 popup types managed by one priority queue — only one popup is visible at a time. After it closes, the next eligible popup in the queue may show. Each popup type has its own independent re-show frequency cap, so (for example) a promotion popup and a newsletter popup can both appear in the same visit, one after the other.

| Popup | Trigger | Use it for |
| ----- | ------- | ---------- |
| **Newsletter** | After N seconds | First-visit email capture |
| **Promotion** | After N seconds, optional date range | Sale / restock / coupon-code announcement |
| **Exit-intent** | Mouse leaves viewport (desktop) / inactivity timer (mobile) | Last-chance discount |

When more than one popup is eligible at the same moment, **exit-intent has the highest priority, then promotion, then newsletter.**

Each popup is configured in the Theme Editor with **two single-line, pipe-delimited (`|`) text inputs**: one for the **content** (title, description, etc.) and one for the **behaviour** (timing and how often it re-shows). You type pipe-separated values into a single box — for example `Title|Description` — rather than filling in a multi-field form.

All three popups live under the same **eShopping Theme** panel in the Theme Editor, as sub-headings — they are not separate top-level panels.

---

## Newsletter popup

**Theme Editor → eShopping Theme → Newsletter Popup**:

| Field | What you enter | Example |
| ----- | -------------- | ------- |
| **Newsletter Content — Title\|Description** | A title and a description, separated by `\|`. Leave empty to disable. | `Get 10% off your first order\|Plus monthly product tips, no spam.` |
| **Show after (seconds) \| Repeat every (days)** | Delay in seconds, then re-show frequency in days, separated by `\|` | `20\|14` = wait 20 s, show again after 14 days |

| Setting | Default | Effect |
| ------- | ------- | ------ |
| Delay (seconds) | 20 | Seconds before the popup appears (counts from page load). If left blank, falls back to 5. |
| Re-show frequency (days) | 14 | Days until the popup may re-show after the user closes it. If left blank, falls back to 0 = once per browser session. |

Leave the content box empty to disable.

---

## Promotion popup

**Theme Editor → eShopping Theme → Promotion Popup**:

| Field | What you enter | Example |
| ----- | -------------- | ------- |
| **Promo Content — Title\|Description\|Coupon Code\|Button Text\|Button URL** | A title, description, coupon code, button text and button link, separated by `\|`. Leave empty to disable. | `Spring Sale\|Get 15% off your entire order with the code below.\|SPRING15\|Shop Now\|/` |
| **Show after (seconds) \| Repeat every (days) \| Start date \| End date** | Delay, re-show frequency, and an optional start/end date, separated by `\|` | `5\|3\|\|` = wait 5 s, every 3 days, no date limit |

| Setting | Default | Effect |
| ------- | ------- | ------ |
| Delay (seconds) | 5 | Seconds before appearing |
| Re-show frequency (days) | 3 | 0 = once per browser session; greater than 0 = days between shows |
| Start date / end date | empty | Dates in `YYYY-MM-DD` form. Popup hides outside the range. Empty = no restriction |

Leave the content box empty to disable.

---

## Exit-intent popup

**Theme Editor → eShopping Theme → Exit Intent Popup**:

| Field | What you enter | Example |
| ----- | -------------- | ------- |
| **Exit Content — Title\|Description\|Coupon Code\|Button Text\|Button URL** | A title, description, coupon code, button text and button link, separated by `\|`. Leave empty to disable. | `Wait! Don't Go Empty-Handed\|Here's a special 10% discount just for you.\|STAY10\|Claim Discount\|/` |
| **Type (discount/newsletter/custom) \| Mobile timeout (seconds) \| Repeat every (days)** | A style keyword, mobile timeout in seconds, and re-show frequency in days, separated by `\|` | `discount\|45\|1` = Discount style, 45 s mobile timeout, re-show after 1 day |

| Setting | Allowed | Effect |
| ------- | ------- | ------ |
| Style | `discount` · `newsletter` · `custom` | **discount** shows a coupon code with a one-click *copy code* button; **newsletter** shows an email signup form; **custom** shows just the text and button |
| Mobile timeout (seconds) | number (default 45) | Inactivity-timer length for mobile (mouse-leave isn't available on touch). Falls back to 45 if blank. |
| Re-show frequency (days) | number (default 1) | 0 = once per browser session; greater than 0 = days between shows |

On desktop, the popup triggers when the cursor moves toward the top of the browser viewport. On mobile it triggers after the inactivity (mobile timeout) period.

**Choosing the `newsletter` style** turns the exit popup into the same email signup form as the Newsletter popup — submissions go to your store's newsletter subscribe action. The `discount` style shows the coupon code with a one-click button that copies the code to the visitor's clipboard.

Leave the content box empty to disable.

---

## Where popups appear

- Popups **never show on the cart or checkout pages**.
- A popup **waits until any open drawer, mobile filter sheet, or modal is closed** before it appears.
- The re-show frequency is tracked in the **visitor's own browser**, so clearing site data (or using a different browser/device) resets it. A frequency of **0** means the popup shows at most **once per browser session**.

---

## Disabling all popups

Set **all three content boxes to empty**. Popups never render.

---

## Z-index conflicts

Popups use a high z-index. If a 3rd-party widget (chat bubble, video lightbox) renders above them, add a CSS override to lower the 3rd-party z-index. Apply the rule via **Storefront → My Themes → Customize → Advanced → Edit Theme Files** (custom CSS), or inject a `<style>` tag through **Storefront → Script Manager**.

---

## Demo store setup (all four stores)

All four demo stores (Industrial, AutoParts, Packaging, Electronics) ship with the **same** popup configuration:

| Popup | Content | Behaviour |
| ----- | ------- | --------- |
| **Newsletter** | Title *Get 10% Off Your First Order*, description *Sign up for our newsletter and receive an exclusive discount code.* | Delay 20 s, re-show every 14 days |
| **Promotion** | Title *Spring Sale*, description *Get 15% off your entire order with the code below.*, coupon *SPRING15*, button *Shop Now* → `/` | Delay 5 s, re-show every 3 days, no date range |
| **Exit-intent** | Title *Wait! Don't Go Empty-Handed*, description *Here's a special 10% discount just for you.*, coupon *STAY10*, button *Claim Discount* → `/` | Style *Discount*, mobile timeout 45 s, re-show every 1 day |

You can adapt these per store — change the copy, coupon codes, timing, or the exit-intent style — but the shipped demos do not vary popup content between stores.

---

## Next

- [Urgency strips & recent-sales toasts](urgency-and-recent-sales.md)
- [Promotions / free-shipping bar](promotions.md)
