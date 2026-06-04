# Urgency Strips & Recent-Sales Toasts

Two lightweight social-proof / scarcity features built into eShopping. The numbers are generated client-side from ranges you configure — they're a friendly UX nudge, not real-time analytics.

## Urgency strips

A pair of short message strips above the Add-to-Cart button that build urgency. They appear on the product page **and** in the Quick View modal:

- **"23 viewing now"** — a number picked from the viewing-count range you set
- **"Bought 14h ago"** — a time picked from the last-order range you set (e.g. `35m ago`, `2d ago`)

On out-of-stock products the "last order" strip is hidden automatically; the view-count strip still shows.

![Urgency strips on the product page — viewing-count + last-order](../img/pdp-urgency.png){ loading=lazy }

### Configure

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIGVTaG9wcGluZyBUaGVtZSDihpIgVXJnZW5jeSBTaWduYWxzIChTb2NpYWwgUHJvb2YpKio6-->

<!--te-tbl:fCBTZXR0aW5nIHwgRWZmZWN0IHwKfCAtLS0tLS0tIHwgLS0tLS0tIHwKfCBTaG93IGxpdmUgdmlldyBjb3VudCB8IFNob3cgLyBoaWRlIHRoZSAidmlld2luZyBub3ciIHN0cmlwIHwKfCBTaG93IGxhc3Qgb3JkZXIgdGltZSB8IFNob3cgLyBoaWRlIHRoZSAiQm91Z2h0IOKApiBhZ28iIHN0cmlwIHwKfCBGYWtlIHZpZXcgY291bnQgcmFuZ2UgfCBUaGUgbG93ZXN0IGFuZCBoaWdoZXN0IHZpZXdlciBudW1iZXIgc2hvd24g4oCUIGUuZy4gYDMsMjVgIHNob3dzIDPigJMyNSB2aWV3ZXJzIHwKfCBMYXN0IG9yZGVyIHRpbWUgcmFuZ2UgfCBUaGUgbG93ZXN0IGFuZCBoaWdoZXN0IG51bWJlciBvZiBob3VycyB1c2VkIGludGVybmFsbHkg4oCUIGUuZy4gYDEsNDhgIGdlbmVyYXRlcyB0aW1lcyBmcm9tICIxIGhvdXIgYWdvIiB1cCB0byAiMiBkYXlzIGFnbyIgKHRoZSB0aGVtZSBmb3JtYXRzIGhvdXJzIGludG8gbWludXRlcywgaG91cnMsIG9yIGRheXMgYXMgYXBwcm9wcmlhdGUpIHw=-->

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFVyZ2VuY3kgU2lnbmFscyAoU29jaWFsIFByb29mKSog4oaSICoqU2hvdyBsaXZlIHZpZXcgY291bnQqKiAoaWQgYGVzaG9wcGluZy11cmdlbmN5LXZpZXctY291bnRgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGB0cnVlYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFVyZ2VuY3kgU2lnbmFscyAoU29jaWFsIFByb29mKSog4oaSICoqU2hvdyBsYXN0IG9yZGVyIHRpbWUqKiAoaWQgYGVzaG9wcGluZy11cmdlbmN5LWxhc3Qtb3JkZXJgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGB0cnVlYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFVyZ2VuY3kgU2lnbmFscyAoU29jaWFsIFByb29mKSog4oaSICoqRmFrZSB2aWV3IGNvdW50IHJhbmdlOiBtaW4sbWF4IChlLmcuIDMsMjUgPSBzaG93IDPigJMyNSB2aWV3ZXJzKSoqIChpZCBgZXNob3BwaW5nLXVyZ2VuY3ktdmlldy1yYW5nZWApLiBGb3JtYXQ6IGNvbW1hLXNlcGFyYXRlZCBgbWluLG1heGAuIERlZmF1bHQ6IGAzLDI1YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFVyZ2VuY3kgU2lnbmFscyAoU29jaWFsIFByb29mKSog4oaSICoqTGFzdCBvcmRlciB0aW1lIHJhbmdlOiBtaW4sbWF4IGhvdXJzIGFnbyAoZS5nLiAxLDQ4ID0gMeKAkzQ4IGhvdXJzIGFnbykqKiAoaWQgYGVzaG9wcGluZy11cmdlbmN5LW9yZGVyLXJhbmdlYCkuIEZvcm1hdDogY29tbWEtc2VwYXJhdGVkIGBtaW4sbWF4YCAoaG91cnMpLiBEZWZhdWx0OiBgMSw0OGAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Urgency Signals (Social…</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show live view count</span><span class="te-desc">Show / hide the &quot;viewing now&quot; strip</span></span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show last order time</span><span class="te-desc">Show / hide the &quot;Bought … ago&quot; strip</span></span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Fake view count range: min,max (e.g. 3,25 = show 3–25 viewers)</span><span class="te-desc">The lowest and highest viewer number shown — e.g. 3,25 shows 3–25 viewers</span></span><span class="te-tx">3,25</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Last order time range: min,max hours ago (e.g. 1,48 = 1–48 hours ago)</span><span class="te-desc">1–48 hours (default)</span></span><span class="te-tx">1,48</span></div></div>

Turn both strips off to hide them entirely.

---

## Recent-sales toasts

Small pop-up toasts at the bottom of the screen showing recent purchase activity, for social proof. They never appear on the cart or checkout pages. Once a visitor closes a toast, no more toasts are shown for the rest of that browsing session.

![Recent-sales toast on the storefront — thumbnail, product, time](../img/recent-sales-toast.png){ loading=lazy }

### Configure

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIGVTaG9wcGluZyBUaGVtZSDihpIgUmVjZW50IFNhbGVzIFBvcHVwKio6-->

<!--te-tbl:fCBTZXR0aW5nIHwgT3B0aW9ucyAvIEZvcm1hdCB8IEVmZmVjdCB8CnwgLS0tLS0tLSB8IC0tLS0tLS0tLS0tLS0tLS0gfCAtLS0tLS0gfAp8IFNob3cgb24gcGFnZXMgfCBPZmYg4oCUIGRvbid0IHNob3cgwrcgQWxsIHBhZ2VzIMK3IEhvbWVwYWdlIG9ubHkgwrcgUHJvZHVjdCBwYWdlcyBvbmx5IMK3IENhdGVnb3J5IHBhZ2VzIG9ubHkgfCBXaGVyZSB0aGUgdG9hc3RzIG1heSBhcHBlYXIgfAp8IFBvcHVwIHRpbWluZyB8IEZvdXIgY29tbWEtc2VwYXJhdGVkIHNlY29uZHM6IGRlbGF5LCBzaG93IGR1cmF0aW9uLCBwYXVzZSBiZXR3ZWVuLCBtYXggcG9wdXBzIOKAlCBlLmcuIGA1LDUsMTUsNWAgfCBDb250cm9scyB3aGVuIGFuZCBob3cgb2Z0ZW4gdG9hc3RzIGFwcGVhciB8CnwgUHJvZHVjdHMgfCBMaXN0IG9mIGBJRC1vci1TS1VcfGxvY2F0aW9uXHx0aW1lQWdvYCBlbnRyaWVzLCBjb21tYS1zZXBhcmF0ZWQgfCBUaGUgcHJvZHVjdHMgYW5kIGxhYmVscyBlYWNoIHRvYXN0IHNob3dzIHw=-->

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFJlY2VudCBTYWxlcyBQb3B1cCog4oaSICoqU2hvdyBvbiBwYWdlcyoqIChpZCBgZXNob3BwaW5nLXJlY2VudC1zYWxlcy1wYWdlc2ApLiBGb3JtYXQ6IHNlbGVjdCDigJQgYG5vbmVgIChPZmYg4oCUIGRvbid0IHNob3cpIMK3IGBhbGxgIMK3IGBob21lYCDCtyBgcHJvZHVjdGAgwrcgYGNhdGVnb3J5YC4gRGVmYXVsdDogYGFsbGAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFJlY2VudCBTYWxlcyBQb3B1cCog4oaSICoqUG9wdXAgdGltaW5nOiBkZWxheSwgc2hvdyBkdXJhdGlvbiwgcGF1c2UgYmV0d2VlbiwgbWF4IHBvcHVwcyAoc2Vjb25kcywgY29tbWEtc2VwYXJhdGVkKS4gRS5nLiA1LDUsMTUsNSoqIChpZCBgZXNob3BwaW5nLXJlY2VudC1zYWxlcy10aW1pbmdgKS4gRm9ybWF0OiBjb21tYS1zZXBhcmF0ZWQgYGRlbGF5LHNob3dfZHVyYXRpb24scGF1c2VfYmV0d2VlbixtYXhfcG9wdXBzYCAoc2Vjb25kcykuIERlZmF1bHQ6IGA1LDUsMTUsNWAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFJlY2VudCBTYWxlcyBQb3B1cCog4oaSICoqUHJvZHVjdHMgKElEIG9yIFNLVXxsb2NhdGlvbnx0aW1lQWdvLCBjb21tYS1zZXBhcmF0ZWQpKiogKGlkIGBlc2hvcHBpbmctcmVjZW50LXNhbGVzLWl0ZW1zYCkuIEZvcm1hdDogY29tbWEtc2VwYXJhdGVkIGVudHJpZXMsIGVhY2ggcGlwZS1zZXBhcmF0ZWQgYElELW9yLVNLVXxsb2NhdGlvbnx0aW1lQWdvYC4gRGVmYXVsdDogYDc3fENhbGlmb3JuaWF8MiBob3VycyBhZ28sNzh8VGV4YXN8MzUgbWluIGFnbyw3OXxGbG9yaWRhfDQgaG91cnMgYWdvLDgwfE5ldyBZb3JrfDEgaG91ciBhZ28sODF8T3JlZ29ufDYgaG91cnMgYWdvYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Recent Sales Popup</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show on pages</span><span class="te-desc">Off — don't show · All pages · Homepage only · Product pages only · Category pages only</span></span><span class="te-dd"><span class="te-dd__v">all</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Popup timing: delay, show duration, pause between, max popups (seconds, comma-separated). E.g. 5,5,15,5</span><span class="te-tx">5,5,15,5</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Products (ID or SKU|location|timeAgo, comma-separated)</span><span class="te-desc">List of ID-or-SKU|location|timeAgo entries, comma-separated</span></span><span class="te-tx">77|California|2 hours ago,78|Texas|3…</span></div></div>

Set **Show on pages** to "Off — don't show" to disable.

### How the data is sourced

Each toast shows a product you list in the **Products** setting, using the location and time you enter for that entry (for example `77|California|2 hours ago`). If the **Products** field is empty — or none of the listed products can be found — the theme falls back to your catalog automatically, in order: **best sellers → featured products → new arrivals** (the first that returns products wins). Fallback items show a generated time and **no location** (just *"Someone just purchased …"*); locations only appear for products you enter yourself.

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
