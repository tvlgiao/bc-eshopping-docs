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

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIGVTaG9wcGluZyBUaGVtZSDihpIgTmV3c2xldHRlciBQb3B1cCoqOg==-->

<!--te-tbl:fCBGaWVsZCB8IFdoYXQgeW91IGVudGVyIHwgRXhhbXBsZSB8CnwgLS0tLS0gfCAtLS0tLS0tLS0tLS0tLSB8IC0tLS0tLS0gfAp8ICoqTmV3c2xldHRlciBDb250ZW50IOKAlCBUaXRsZVx8RGVzY3JpcHRpb24qKiB8IEEgdGl0bGUgYW5kIGEgZGVzY3JpcHRpb24sIHNlcGFyYXRlZCBieSBgXHxgLiBMZWF2ZSBlbXB0eSB0byBkaXNhYmxlLiB8IGBHZXQgMTAlIG9mZiB5b3VyIGZpcnN0IG9yZGVyXHxQbHVzIG1vbnRobHkgcHJvZHVjdCB0aXBzLCBubyBzcGFtLmAgfAp8ICoqU2hvdyBhZnRlciAoc2Vjb25kcykgXHwgUmVwZWF0IGV2ZXJ5IChkYXlzKSoqIHwgRGVsYXkgaW4gc2Vjb25kcywgdGhlbiByZS1zaG93IGZyZXF1ZW5jeSBpbiBkYXlzLCBzZXBhcmF0ZWQgYnkgYFx8YCB8IGAyMFx8MTRgID0gd2FpdCAyMCBzLCBzaG93IGFnYWluIGFmdGVyIDE0IGRheXMgfA==-->

| Setting | Default | Effect |
| ------- | ------- | ------ |
| Delay (seconds) | 20 | Seconds before the popup appears (counts from page load). If left blank, falls back to 5. |
| Re-show frequency (days) | 14 | Days until the popup may re-show after the user closes it. If left blank, falls back to 0 = once per browser session. |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIE5ld3NsZXR0ZXIgUG9wdXAqIOKGkiAqKk5ld3NsZXR0ZXIgQ29udGVudCDigJQgVGl0bGV8RGVzY3JpcHRpb24gKGxlYXZlIGVtcHR5IHRvIGRpc2FibGUpKiogKGlkIGBlc2hvcHBpbmctcG9wdXAtbmwtdGV4dGApLiBGb3JtYXQ6IHBpcGUtc2VwYXJhdGVkIGBUaXRsZXxEZXNjcmlwdGlvbmAuIERlZmF1bHQ6IGBHZXQgMTAlIE9mZiBZb3VyIEZpcnN0IE9yZGVyfFNpZ24gdXAgZm9yIG91ciBuZXdzbGV0dGVyIGFuZCByZWNlaXZlIGFuIGV4Y2x1c2l2ZSBkaXNjb3VudCBjb2RlLmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIE5ld3NsZXR0ZXIgUG9wdXAqIOKGkiAqKlNob3cgYWZ0ZXIgKHNlY29uZHMpIHwgUmVwZWF0IGV2ZXJ5IChkYXlzKS4gRS5nLiAyMHwxNCA9IHdhaXQgMjBzLCBzaG93IGFnYWluIGFmdGVyIDE0IGRheXMqKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1ubC1vcHRzYCkuIEZvcm1hdDogcGlwZS1zZXBhcmF0ZWQgYGRlbGF5X3NlY29uZHN8ZnJlcV9kYXlzYC4gRGVmYXVsdDogYDIwfDE0YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Newsletter Popup</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Newsletter Content — Title|Description (leave empty to disable)</span><span class="te-desc">After N seconds</span></span><span class="te-tx">Get 10% Off Your First Order|Sign up…</span></div><div class="te-mock__row"><span class="te-lbl">Show after (seconds) | Repeat every (days). E.g. 20|14 = wait 20s, show again after 14 days</span><span class="te-tx">20|14</span></div></div>

Leave the content box empty to disable.

---

## Promotion popup

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIGVTaG9wcGluZyBUaGVtZSDihpIgUHJvbW90aW9uIFBvcHVwKio6-->

<!--te-tbl:fCBGaWVsZCB8IFdoYXQgeW91IGVudGVyIHwgRXhhbXBsZSB8CnwgLS0tLS0gfCAtLS0tLS0tLS0tLS0tLSB8IC0tLS0tLS0gfAp8ICoqUHJvbW8gQ29udGVudCDigJQgVGl0bGVcfERlc2NyaXB0aW9uXHxDb3Vwb24gQ29kZVx8QnV0dG9uIFRleHRcfEJ1dHRvbiBVUkwqKiB8IEEgdGl0bGUsIGRlc2NyaXB0aW9uLCBjb3Vwb24gY29kZSwgYnV0dG9uIHRleHQgYW5kIGJ1dHRvbiBsaW5rLCBzZXBhcmF0ZWQgYnkgYFx8YC4gTGVhdmUgZW1wdHkgdG8gZGlzYWJsZS4gfCBgU3ByaW5nIFNhbGVcfEdldCAxNSUgb2ZmIHlvdXIgZW50aXJlIG9yZGVyIHdpdGggdGhlIGNvZGUgYmVsb3cuXHxTUFJJTkcxNVx8U2hvcCBOb3dcfC9gIHwKfCAqKlNob3cgYWZ0ZXIgKHNlY29uZHMpIFx8IFJlcGVhdCBldmVyeSAoZGF5cykgXHwgU3RhcnQgZGF0ZSBcfCBFbmQgZGF0ZSoqIHwgRGVsYXksIHJlLXNob3cgZnJlcXVlbmN5LCBhbmQgYW4gb3B0aW9uYWwgc3RhcnQvZW5kIGRhdGUsIHNlcGFyYXRlZCBieSBgXHxgIHwgYDVcfDNcfFx8YCA9IHdhaXQgNSBzLCBldmVyeSAzIGRheXMsIG5vIGRhdGUgbGltaXQgfA==-->

| Setting | Default | Effect |
| ------- | ------- | ------ |
| Delay (seconds) | 5 | Seconds before appearing |
| Re-show frequency (days) | 3 | 0 = once per browser session; greater than 0 = days between shows |
| Start date / end date | empty | Dates in `YYYY-MM-DD` form. Popup hides outside the range. Empty = no restriction |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb21vdGlvbiBQb3B1cCog4oaSICoqUHJvbW8gQ29udGVudCDigJQgVGl0bGV8RGVzY3JpcHRpb258Q291cG9uIENvZGV8QnV0dG9uIFRleHR8QnV0dG9uIFVSTCAobGVhdmUgZW1wdHkgdG8gZGlzYWJsZSkqKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1wcm9tby10ZXh0YCkuIEZvcm1hdDogcGlwZS1zZXBhcmF0ZWQgYFRpdGxlfERlc2NyaXB0aW9ufENvdXBvbkNvZGV8QnV0dG9uVGV4dHxCdXR0b25VUkxgLiBEZWZhdWx0OiBgU3ByaW5nIFNhbGV8R2V0IDE1JSBvZmYgeW91ciBlbnRpcmUgb3JkZXIgd2l0aCB0aGUgY29kZSBiZWxvdy58U1BSSU5HMTV8U2hvcCBOb3d8L2Au-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb21vdGlvbiBQb3B1cCog4oaSICoqU2hvdyBhZnRlciAoc2Vjb25kcykgfCBSZXBlYXQgZXZlcnkgKGRheXMpIHwgU3RhcnQgZGF0ZSB8IEVuZCBkYXRlLiBFLmcuIDV8M3x8ID0gd2FpdCA1cywgZXZlcnkgMyBkYXlzLCBubyBkYXRlIGxpbWl0KiogKGlkIGBlc2hvcHBpbmctcG9wdXAtcHJvbW8tb3B0c2ApLiBGb3JtYXQ6IHBpcGUtc2VwYXJhdGVkIGBkZWxheV9zZWNvbmRzfGZyZXFfZGF5c3xzdGFydF9kYXRlfGVuZF9kYXRlYCAoZGF0ZXMgYFlZWVktTU0tRERgLCBibGFuayA9IG5vIGxpbWl0KS4gRGVmYXVsdDogYDV8M3x8YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Promotion Popup</div><div class="te-mock__row"><span class="te-lbl">Promo Content — Title|Description|Coupon Code|Button Text|Button URL (leave empty to disable)</span><span class="te-tx">Spring Sale|Get 15% off your entire …</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show after (seconds) | Repeat every (days) | Start date | End date. E.g. 5|3|| = wait 5s, every 3 days, no date limit</span><span class="te-desc">Delay in seconds, then re-show frequency in days, separated by |</span></span><span class="te-tx">5|3||</span></div></div>

Leave the content box empty to disable.

---

## Exit-intent popup

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIGVTaG9wcGluZyBUaGVtZSDihpIgRXhpdCBJbnRlbnQgUG9wdXAqKjo=-->

| Field | What you enter | Example |
| ----- | -------------- | ------- |
| **Exit Content — Title\|Description\|Coupon Code\|Button Text\|Button URL** | A title, description, coupon code, button text and button link, separated by `\|`. Leave empty to disable. | `Wait! Don't Go Empty-Handed\|Here's a special 10% discount just for you.\|STAY10\|Claim Discount\|/` |
| **Type (discount/newsletter/custom) \| Mobile timeout (seconds) \| Repeat every (days)** | A style keyword, mobile timeout in seconds, and re-show frequency in days, separated by `\|` | `discount\|45\|1` = Discount style, 45 s mobile timeout, re-show after 1 day |

| Setting | Allowed | Effect |
| ------- | ------- | ------ |
| Style | `discount` · `newsletter` · `custom` | **discount** shows a coupon code with a one-click *copy code* button; **newsletter** shows an email signup form; **custom** shows just the text and button |
| Mobile timeout (seconds) | number (default 45) | Inactivity-timer length for mobile (mouse-leave isn't available on touch). Falls back to 45 if blank. |
| Re-show frequency (days) | number (default 1) | 0 = once per browser session; greater than 0 = days between shows |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEV4aXQgSW50ZW50IFBvcHVwKiDihpIgKipFeGl0IENvbnRlbnQg4oCUIFRpdGxlfERlc2NyaXB0aW9ufENvdXBvbiBDb2RlfEJ1dHRvbiBUZXh0fEJ1dHRvbiBVUkwgKGxlYXZlIGVtcHR5IHRvIGRpc2FibGUpKiogKGlkIGBlc2hvcHBpbmctcG9wdXAtZXhpdC10ZXh0YCkuIEZvcm1hdDogcGlwZS1zZXBhcmF0ZWQgYFRpdGxlfERlc2NyaXB0aW9ufENvdXBvbkNvZGV8QnV0dG9uVGV4dHxCdXR0b25VUkxgLiBEZWZhdWx0OiBgV2FpdCEgRG9uJ3QgR28gRW1wdHktSGFuZGVkfEhlcmUncyBhIHNwZWNpYWwgMTAlIGRpc2NvdW50IGp1c3QgZm9yIHlvdS58U1RBWTEwfENsYWltIERpc2NvdW50fC9gLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEV4aXQgSW50ZW50IFBvcHVwKiDihpIgKipUeXBlIChkaXNjb3VudC9uZXdzbGV0dGVyL2N1c3RvbSkgfCBNb2JpbGUgdGltZW91dCAoc2Vjb25kcykgfCBSZXBlYXQgZXZlcnkgKGRheXMpLiBFLmcuIGRpc2NvdW50fDQ1fDEqKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1leGl0LW9wdHNgKS4gRm9ybWF0OiBwaXBlLXNlcGFyYXRlZCBgdHlwZXxtb2JpbGVfdGltZW91dF9zZWNvbmRzfGZyZXFfZGF5c2AgKHR5cGUgPSBgZGlzY291bnRgIMK3IGBuZXdzbGV0dGVyYCDCtyBgY3VzdG9tYCkuIERlZmF1bHQ6IGBkaXNjb3VudHw0NXwxYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Exit Intent Popup</div><div class="te-mock__row"><span class="te-lbl">Exit Content — Title|Description|Coupon Code|Button Text|Button URL (leave empty to disable)</span><span class="te-tx">Wait! Don't Go Empty-Handed|Here's a…</span></div><div class="te-mock__row"><span class="te-lbl">Type (discount/newsletter/custom) | Mobile timeout (seconds) | Repeat every (days). E.g. discount|45|1</span><span class="te-tx">discount|45|1</span></div></div>

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
