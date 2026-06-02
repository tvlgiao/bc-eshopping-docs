# Home Page — Auto Parts Variant

Live demo: <https://eshopping-autoparts-demo.mybigcommerce.com>

![Auto Parts home page composed view](../img/home-autoparts-composed.png){ loading=lazy }

!!! note "Before you start"
    Theme installed, **AutoParts** variation picked, **AutoParts** product + widget data imported.

The AutoParts variation **already populates** many settings when you pick it (colors, fonts, trust strip, newsletter, promo text, cart goals, and PDP shipping/warranty text). Other features below — popups, Frequently Bought Together, cross-sell, urgency signals, and recent-sales notifications — are theme defaults that are the same in every variation and active out of the box. The recipe below shows what's set automatically, **and how to change each part yourself**.

Every section ends with a **Customize:** line giving the exact place to change it — a Theme Editor field (with its label, id, value format, and default), a Page Builder widget, or a BigCommerce admin location.

The home page renders these sections in this order on the live demo:

1. Hero (Home Page Carousel)
2. Trust strip
3. Featured Products slider
4. New Arrivals slider
5. Products by Category
6. **Why Choose Us** value-prop callout — *"Auto Parts That Fit. Pricing That Drives."* (AI HTML Generator | PapaThemes)
7. **Customer Reviews** social-proof block (AI HTML Generator | PapaThemes)
8. **Resources** guide cards — *"Auto Parts Resources & Guides"* (AI HTML Generator | PapaThemes)
9. Brands carousel
10. Blog posts
11. Newsletter
12. **About** SEO intro — *"Your Complete Auto Parts Source"* (AI HTML Generator | PapaThemes)
13. **Talk to an Expert** contact CTA — *"Talk to an Auto Parts Specialist"* (AI HTML Generator | PapaThemes)

The footer also carries a **Footer tagline** widget (shown on every page, not just the home page).

!!! note "Bestselling slider is enabled but hidden"
    **Show Best Sellers** is on, but the demo store has no bestseller sales data yet, so this slider does **not** appear on the live home page. It starts showing once orders generate bestseller data.

## Section-by-section recipe

### 1. Variation

Theme Editor → **AutoParts**.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSIHRvcCAqKnZhcmlhdGlvbiBkcm9wZG93bioqIChQYWdlIEJ1aWxkZXIgKlRoZW1lIHN0eWxlcyopLiBQaWNrICoqSW5kdXN0cmlhbCoqLCAqKkF1dG8gUGFydHMqKiwgKipFbGVjdHJvbmljcyoqLCBvciAqKlBhY2thZ2luZyoqLiBUaGUgdmFyaWF0aW9uIHN3YXBzIHRoZSB3aG9sZSBjb2xvci9mb250L2NvcHkgcHJlc2V0LiBEZWZhdWx0OiBgQXV0byBQYXJ0c2AgZm9yIHRoaXMgc3RvcmUu-->
<!--te-mock--><div class="te-mock te-mock--styles"><div class="te-mock__hd"><span>Styles</span><span class="te-x">✕</span></div><div class="te-mock__grp">Theme variation</div><div class="te-mock__row"><span class="te-lbl">Industrial</span></div><div class="te-mock__row"><span class="te-lbl">AutoParts</span><span class="te-check">✓</span></div><div class="te-mock__row"><span class="te-lbl">Electronics</span></div><div class="te-mock__row"><span class="te-lbl">Packaging</span></div></div>

### 2. Colors — set automatically by the variation

These values are applied for you when you pick the variation:

<!--te-tbl:fCBDb2xvciB8IFZhbHVlIHwgRmllbGQgaWQgfAp8IC0tLS0tIHwgLS0tLS0gfCAtLS0tLS0tLSB8CnwgUHJpbWFyeSBhY2NlbnQgKFRlcnJhKSB8IGAjZDk3NzA2YCAoYW1iZXIpIHwgYGVzaG9wcGluZy1jb2xvci10ZXJyYWAgfAp8IFByaW1hcnkgYWNjZW50IChsaWdodCkgfCBgI2Y1OWUwYmAgfCBgZXNob3BwaW5nLWNvbG9yLXRlcnJhLWxpZ2h0YCB8CnwgUHJpbWFyeSBhY2NlbnQgKGRhcmspIHwgYCNiNDUzMDlgIHwgYGVzaG9wcGluZy1jb2xvci10ZXJyYS1kYXJrYCB8CnwgUHJpbWFyeSBhY2NlbnQgKHBhbGUpIHwgYCNmZmZiZWJgIHwgYGVzaG9wcGluZy1jb2xvci10ZXJyYS1wYWxlYCB8CnwgRGFya2VzdCBuZXV0cmFsIChCYXJrIDk1MCkgfCBgIzAyMDYxN2AgKGNvb2wgc2xhdGUpIHwgYGVzaG9wcGluZy1jb2xvci1iYXJrLTk1MGAgfAp8IERhcmsgbmV1dHJhbCAoQmFyayA5MDApIHwgYCMwZjE3MmFgIHwgYGVzaG9wcGluZy1jb2xvci1iYXJrLTkwMGAgfAp8IExpZ2h0ZXN0IG5ldXRyYWwgKEJhcmsgNTApIHwgYCNmOGZhZmNgIHwgYGVzaG9wcGluZy1jb2xvci1iYXJrLTUwYCB8CnwgQ3JlYW0gLyBiYWNrZ3JvdW5kIHwgYCNmOGZhZmNgIHwgYGVzaG9wcGluZy1jb2xvci1jcmVhbWAgfAp8IFdoaXRlIHwgYCNmZmZmZmZgIHwgYGVzaG9wcGluZy1jb2xvci13aGl0ZWAgfAp8IFNhbGUgYmFkZ2UgYmFja2dyb3VuZCB8IGAjZGMyNjI2YCB8IGBlc2hvcHBpbmctYmFkZ2Utc2FsZS1iZ2AgfAp8IFN0YWZmLXBpY2sgYmFkZ2UgYmFja2dyb3VuZCB8IGAjYjQ1MzA5YCB8IGBlc2hvcHBpbmctYmFkZ2Utc3RhZmYtYmdgIHwKfCBBY3RpdmUgcmF0aW5nIHN0YXIgfCBgI2Y1OWUwYmAgfCBgZXNob3BwaW5nLXJhdGluZy1zdGFyLWFjdGl2ZWAgfAp8IFNhbGUgcHJpY2UgfCBgI2RjMjYyNmAgfCBgZXNob3BwaW5nLXByaWNlLXNhbGVgIHwKfCBPcmlnaW5hbCAoc3RydWNrLXRocm91Z2gpIHByaWNlIHwgYCM5NGEzYjhgIHwgYGVzaG9wcGluZy1wcmljZS1vcmlnaW5hbGAgfA==-->

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSIGVhY2ggY29sb3IgaXMgaXRzIG93biBmaWVsZCDigJQgZS5nLiAqKlRlcnJhKiogKGlkIGBlc2hvcHBpbmctY29sb3ItdGVycmFgLCBkZWZhdWx0IGAjYmY1YjMzYCksICoqU2FsZSBCYWRnZSBCYWNrZ3JvdW5kKiogKGlkIGBlc2hvcHBpbmctYmFkZ2Utc2FsZS1iZ2ApLCAqKlJhdGluZyBTdGFyIChBY3RpdmUpKiogKGlkIGBlc2hvcHBpbmctcmF0aW5nLXN0YXItYWN0aXZlYCksICoqU2FsZSBQcmljZSoqIChpZCBgZXNob3BwaW5nLXByaWNlLXNhbGVgKS4gRm9ybWF0OiBoZXggY29sb3IuIFBpY2tpbmcgYSBkaWZmZXJlbnQgKip2YXJpYXRpb24qKiByZXNldHMgdGhlIHdob2xlIHBhbGV0dGUgYXQgb25jZS4gKFRoZSB2YWx1ZXMgYWJvdmUgYXJlIHRoaXMgZGVtbydzOyB0aGUgY29uZmlnLWZpbGUgZGVmYXVsdHMgc2hpcHBlZCB3aXRoIHRoZSB0aGVtZSBhcmUgdGhlIEluZHVzdHJpYWwgcGFsZXR0ZS4p-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Primary accent (Terra)</span><span class="te-color"><span class="te-hex">#D97706</span><span class="te-sw" style="background:#d97706"></span></span></div><div class="te-mock__row"><span class="te-lbl">Primary accent (light)</span><span class="te-color"><span class="te-hex">#F59E0B</span><span class="te-sw" style="background:#f59e0b"></span></span></div><div class="te-mock__row"><span class="te-lbl">Primary accent (dark)</span><span class="te-color"><span class="te-hex">#B45309</span><span class="te-sw" style="background:#b45309"></span></span></div><div class="te-mock__row"><span class="te-lbl">Primary accent (pale)</span><span class="te-color"><span class="te-hex">#FFFBEB</span><span class="te-sw" style="background:#fffbeb"></span></span></div><div class="te-mock__row"><span class="te-lbl">Darkest neutral (Bark 950)</span><span class="te-color"><span class="te-hex">#020617</span><span class="te-sw" style="background:#020617"></span></span></div><div class="te-mock__row"><span class="te-lbl">Dark neutral (Bark 900)</span><span class="te-color"><span class="te-hex">#0F172A</span><span class="te-sw" style="background:#0f172a"></span></span></div><div class="te-mock__row"><span class="te-lbl">Lightest neutral (Bark 50)</span><span class="te-color"><span class="te-hex">#F8FAFC</span><span class="te-sw" style="background:#f8fafc"></span></span></div><div class="te-mock__row"><span class="te-lbl">Cream / background</span><span class="te-color"><span class="te-hex">#F8FAFC</span><span class="te-sw" style="background:#f8fafc"></span></span></div><div class="te-mock__row"><span class="te-lbl">White</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Sale badge background</span><span class="te-color"><span class="te-hex">#DC2626</span><span class="te-sw" style="background:#dc2626"></span></span></div><div class="te-mock__row"><span class="te-lbl">Staff-pick badge background</span><span class="te-color"><span class="te-hex">#B45309</span><span class="te-sw" style="background:#b45309"></span></span></div><div class="te-mock__row"><span class="te-lbl">Active rating star</span><span class="te-color"><span class="te-hex">#F59E0B</span><span class="te-sw" style="background:#f59e0b"></span></span></div><div class="te-mock__row"><span class="te-lbl">Sale price</span><span class="te-color"><span class="te-hex">#DC2626</span><span class="te-sw" style="background:#dc2626"></span></span></div><div class="te-mock__row"><span class="te-lbl">Original (struck-through) price</span><span class="te-color"><span class="te-hex">#94A3B8</span><span class="te-sw" style="background:#94a3b8"></span></span></div></div>

### 3. Fonts — set automatically

| Font | Value | Field id |
| ---- | ----- | -------- |
| Body font | Inter (weights 400, 500, 600) | `body-font` |
| Headings font | Inter (weights 600, 700) | `headings-font` |
| Monospace font | IBM Plex Mono (weight 400) | `eshopping-mono-font` |

Root font size is `14px`.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwqIOKGkiAqKkJvZHkgdGV4dCBmb250IGZhbWlseSoqIChpZCBgYm9keS1mb250YCkgYW5kICoqSGVhZGluZyBmb250IGZhbWlseSoqIChpZCBgaGVhZGluZ3MtZm9udGApOyAqKkJvZHkgdGV4dCBmb250IHNpemUqKiAoaWQgYGZvbnRTaXplLXJvb3RgLCBkZWZhdWx0IGAxNGAsIHNlbGVjdCkuIFRoZSBtb25vc3BhY2UgZmFjZSBpcyAqKk1vbm9zcGFjZSBGb250KiogKGlkIGBlc2hvcHBpbmctbW9uby1mb250YCkgdW5kZXIgKmVTaG9wcGluZyBUaGVtZSDihpIgRm9udHMqLiBGb3JtYXQ6IEdvb2dsZS1mb250IHBpY2tlciBmb3IgZmFtaWxpZXM7IHNlbGVjdCBmb3Igcm9vdCBzaXplLiBUaGUgdmFyaWF0aW9uIHNldHMgYWxsIHRocmVlLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Global</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Body text font family</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Heading font family</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Body text font size</span><span class="te-dd"><span class="te-dd__v">14</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Monospace Font</span><span class="te-desc">IBM Plex Mono (weight 400)</span></span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>

### 4. Top banner

Banner colors are set automatically by the variation:

<!--te-tbl:fCBDb2xvciB8IFZhbHVlIHwgRmllbGQgaWQgfAp8IC0tLS0tIHwgLS0tLS0gfCAtLS0tLS0tLSB8CnwgQmFubmVyIGJhY2tncm91bmQgfCBgIzMzNDE1NWAgfCBgZXNob3BwaW5nLWJhbm5lci1iZ2AgfAp8IEJhbm5lciB0ZXh0IHwgYCNjYmQ1ZTFgIHwgYGVzaG9wcGluZy1iYW5uZXItY29sb3JgIHwKfCBCYW5uZXIgbGluayB8IGAjZjU5ZTBiYCB8IGBlc2hvcHBpbmctYmFubmVyLWxpbmtgIHw=-->

The banner *content* (the message) comes from your BigCommerce control panel, not the theme.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoY29sb3JzKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEJhbm5lciog4oaSICoqQmFubmVyIEJhY2tncm91bmQqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItYmdgLCBkZWZhdWx0IGAjM2UzNjI5YCksICoqQmFubmVyIFRleHQgQ29sb3IqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItY29sb3JgLCBkZWZhdWx0IGAjZDVjZWMyYCksICoqQmFubmVyIExpbmsgQ29sb3IqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItbGlua2AsIGRlZmF1bHQgYCNkOTg0NWVgKS4gRm9ybWF0OiBoZXggY29sb3JzLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAobWVzc2FnZSk6KiogQmlnQ29tbWVyY2UgYWRtaW4g4oaSICoqTWFya2V0aW5nIOKGkiBCYW5uZXJzKiouIEFkZC9lZGl0IHRoZSBhbm5vdW5jZW1lbnQgdGV4dCB0aGVyZS4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Banner</div><div class="te-mock__row"><span class="te-lbl">Banner Background</span><span class="te-color"><span class="te-hex">#334155</span><span class="te-sw" style="background:#334155"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner Text Color</span><span class="te-color"><span class="te-hex">#CBD5E1</span><span class="te-sw" style="background:#cbd5e1"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner Link Color</span><span class="te-color"><span class="te-hex">#F59E0B</span><span class="te-sw" style="background:#f59e0b"></span></span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Marketing</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub is-active">Banners</div><div class="te-nav__sub">Coupon codes</div><div class="te-nav__sub">Gift certificates</div><div class="te-nav__sub">Abandoned cart saver</div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 5. Header & search — set automatically by the variation

| Setting | Value | Field id |
| ------- | ----- | -------- |
| Top bar background | `#020617` | `eshopping-topbar-bg` |
| Top bar text | `#94a3b8` | `eshopping-topbar-color` |
| Nav background | `#ffffff` | `eshopping-nav-bg` |
| Nav text | `#475569` | `eshopping-nav-color` |
| Nav search button | `#d97706` | `eshopping-nav-search-btn` |
| Search box typing phrases | Search for brake pads… · Find oil filters & fluids… · Browse suspension parts… · Discover lighting & accessories… | `eshopping-search-typing-phrases` |
| Enable voice search | ✅ On | `eshopping-search-voice` |
| Welcome text | *(empty)* | `eshopping-welcome-text` |

!!! tip "Welcome text"
    The welcome text field ships empty. Add your own short line (for example, *Find parts for your vehicle in seconds*) if you want one in the top bar.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoaGVhZGVyIGNvbG9ycyk6KiogVGhlbWUgRWRpdG9yIOKGkiAqZVNob3BwaW5nIFRoZW1lIOKGkiBIZWFkZXIqIOKGkiAqKlRvcGJhciBCYWNrZ3JvdW5kKiogKGlkIGBlc2hvcHBpbmctdG9wYmFyLWJnYCksICoqVG9wYmFyIFRleHQqKiAoaWQgYGVzaG9wcGluZy10b3BiYXItY29sb3JgKSwgKipOYXZpZ2F0aW9uIEJhY2tncm91bmQqKiAoaWQgYGVzaG9wcGluZy1uYXYtYmdgKSwgKipOYXZpZ2F0aW9uIFRleHQqKiAoaWQgYGVzaG9wcGluZy1uYXYtY29sb3JgKSwgKipTZWFyY2ggQnV0dG9uKiogKGlkIGBlc2hvcHBpbmctbmF2LXNlYXJjaC1idG5gKS4gRm9ybWF0OiBoZXggY29sb3JzLiAoQWxzbyAqKlNob3cgUGhvbmUgaW4gVG9wYmFyKiogLyAqKlNob3cgQWRkcmVzcyBpbiBUb3BiYXIqKiwgaWRzIGBlc2hvcHBpbmctdG9wYmFyLXNob3ctcGhvbmVgIC8gYGVzaG9wcGluZy10b3BiYXItc2hvdy1hZGRyZXNzYCwgb24vb2ZmLik=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2VsY29tZSB0ZXh0KToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhlYWRlciog4oaSICoqV2VsY29tZSBUZXh0KiogKGlkIGBlc2hvcHBpbmctd2VsY29tZS10ZXh0YCkuIEZvcm1hdDogcGxhaW4gdGV4dC4gRGVmYXVsdDogKihlbXB0eSkqLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodm9pY2Ugc2VhcmNoKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNlYXJjaCog4oaSICoqRW5hYmxlIHZvaWNlIHNlYXJjaCoqIChpZCBgZXNob3BwaW5nLXNlYXJjaC12b2ljZWApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYE9uYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodHlwaW5nIHBocmFzZXMpOioqIFRoZW1lIEVkaXRvciDihpIgKmVTaG9wcGluZyBUaGVtZSDihpIgU2VhcmNoKiDihpIgKipUeXBpbmcgcGhyYXNlcyAocGlwZSB8IHNlcGFyYXRlZCkqKiAoaWQgYGVzaG9wcGluZy1zZWFyY2gtdHlwaW5nLXBocmFzZXNgKS4gRWFjaCBwaHJhc2Ugcm90YXRlcyBpbiB0aGUgc2VhcmNoIHBsYWNlaG9sZGVyLiBGb3JtYXQ6IHBocmFzZXMgc2VwYXJhdGVkIGJ5IGB8YC4gRGVmYXVsdCAoQXV0b1BhcnRzKTogYFNlYXJjaCBmb3IgYnJha2UgcGFkcy4uLnxGaW5kIG9pbCBmaWx0ZXJzICYgZmx1aWRzLi4ufEJyb3dzZSBzdXNwZW5zaW9uIHBhcnRzLi4ufERpc2NvdmVyIGxpZ2h0aW5nICYgYWNjZXNzb3JpZXMuLi5gLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Header</div><div class="te-mock__row"><span class="te-lbl">Topbar Background</span><span class="te-color"><span class="te-hex">#020617</span><span class="te-sw" style="background:#020617"></span></span></div><div class="te-mock__row"><span class="te-lbl">Topbar Text</span><span class="te-color"><span class="te-hex">#94A3B8</span><span class="te-sw" style="background:#94a3b8"></span></span></div><div class="te-mock__row"><span class="te-lbl">Navigation Background</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Navigation Text</span><span class="te-color"><span class="te-hex">#475569</span><span class="te-sw" style="background:#475569"></span></span></div><div class="te-mock__row"><span class="te-lbl">Search Button</span><span class="te-color"><span class="te-hex">#D97706</span><span class="te-sw" style="background:#d97706"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Welcome Text</span><span class="te-desc">(empty)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__grp">Search</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Enable voice search</span><span class="te-desc">✅ On</span></span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Typing phrases (pipe | separated)</span><span class="te-tx">Search for brake pads</span></div></div>

### 6. Hero (Home Page Carousel)

The built-in **Home Page Carousel** is enabled. The slides themselves come from the store's Home Page Carousel — the theme does not require a fixed slide size; use a wide landscape image (JPG or WebP, e.g. ~1920 × 700) and keep all slides the same dimensions.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2xpZGVzKToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipTdG9yZWZyb250IOKGkiBIb21lIFBhZ2UgQ2Fyb3VzZWwqKi4gQWRkL2VkaXQvcmVvcmRlciBzbGlkZXMsIGltYWdlcywgaGVhZGluZ3MsIGFuZCBidXR0b24gbGlua3MgdGhlcmUuIChOb3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY2Fyb3VzZWwgYmVoYXZpb3VyKToqKiBUaGVtZSBFZGl0b3Ig4oaSICpIb21lIFBhZ2UqIChzdGFuZGFyZCBDb3JuZXJzdG9uZSBwYW5lbCkg4oaSICoqU2hvdyBjYXJvdXNlbCoqIChpZCBgaG9tZXBhZ2Vfc2hvd19jYXJvdXNlbGAsIGRlZmF1bHQgYE9uYCksICoqU2hvdyBDYXJvdXNlbCBBcnJvd3MqKiAoaWQgYGhvbWVwYWdlX3Nob3dfY2Fyb3VzZWxfYXJyb3dzYCwgZGVmYXVsdCBgT25gKSwgKipTaG93IENhcm91c2VsIFBsYXkvUGF1c2UgQnV0dG9uKiogKGlkIGBob21lcGFnZV9zaG93X2Nhcm91c2VsX3BsYXlfcGF1c2VfYnV0dG9uYCwgZGVmYXVsdCBgT25gKSwgcGx1cyB0aGUgY2Fyb3VzZWwgY29sb3IgZmllbGRzIChgY2Fyb3VzZWwtdGl0bGUtY29sb3JgLCBgY2Fyb3VzZWwtYXJyb3ctY29sb3JgLCBgY2Fyb3VzZWwtZG90LWNvbG9yYCwg4oCmKS4gRm9ybWF0OiBvbi9vZmYgdG9nZ2xlcyArIGhleCBjb2xvcnMu-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub is-active">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Homepage</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show carousel</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show Carousel Arrows</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show Carousel Play/Pause Button</span><span class="te-cb is-on"></span></div></div>

!!! note "There is no separate \"Show hero\" toggle"
    The hero is the BigCommerce Home Page Carousel, gated entirely by **Show carousel** (`homepage_show_carousel`) in the standard **Home Page** panel — there is no `eshopping-show-hero` setting.

!!! tip "Slide ideas (suggestions only)"
    The demo's actual slides come from the Home Page Carousel. If you're building your own, these work well for an auto-parts catalog:

    | Slide | Heading | CTA |
    | :---: | ------- | --- |
    | 1 | **Performance parts. Built for the long haul.** | `Shop the catalog` |
    | 2 | **Find parts for your ride** | `Fitment lookup` |
    | 3 | **Same-day shipping on orders before 2pm** | `Shop now` |

### 7. Trust strip — variation default

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IFRydXN0IFN0cmlwKiogaXMgb24uIEZvdXIgaXRlbXMsIGVhY2ggYSB0aXRsZSBhbmQgYSBkZXNjcmlwdGlvbjo=-->

| Title | Description |
| ----- | ----------- |
| OEM Quality Parts | Genuine & aftermarket parts you can trust |
| Fast Shipping | Same-day dispatch on in-stock items |
| Free Returns | Easy 30-day return policy |
| Expert Support | ASE-certified advisors available |

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IFRydXN0IFN0cmlwKiogKGlkIGBlc2hvcHBpbmctc2hvdy10cnVzdC1zdHJpcGApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYE9uYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoaXRlbXMpOioqIFRoZW1lIEVkaXRvciDihpIgKmVTaG9wcGluZyBUaGVtZSDihpIgVHJ1c3QgU3RyaXAqIOKGkiAqKlRydXN0IFN0cmlwIEl0ZW1zKiogKGlkIGBlc2hvcHBpbmctdHJ1c3QtdGV4dGApLiBUaGUgc3RyaXAgYWx3YXlzIHNob3dzIGV4YWN0bHkgKio0IGZpeGVkIGljb25zKio7IHRoZSB0ZXh0IGNvbWVzIGZyb20gdGhpcyBmaWVsZCBhcyAqKjQgdGl0bGUvZGVzY3JpcHRpb24gcGFpcnMqKiA9IDggcGlwZS1zZXBhcmF0ZWQgc2VnbWVudHMgaW4gb3JkZXIgYFRpdGxlMXxEZXNjMXxUaXRsZTJ8RGVzYzJ8VGl0bGUzfERlc2MzfFRpdGxlNHxEZXNjNGAuIERlZmF1bHQgKEF1dG9QYXJ0cyk6IGBPRU0gUXVhbGl0eSBQYXJ0c3xHZW51aW5lICYgYWZ0ZXJtYXJrZXQgcGFydHMgeW91IGNhbiB0cnVzdHxGYXN0IFNoaXBwaW5nfFNhbWUtZGF5IGRpc3BhdGNoIG9uIGluLXN0b2NrIGl0ZW1zfEZyZWUgUmV0dXJuc3xFYXN5IDMwLWRheSByZXR1cm4gcG9saWN5fEV4cGVydCBTdXBwb3J0fEFTRS1jZXJ0aWZpZWQgYWR2aXNvcnMgYXZhaWxhYmxlYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Trust Strip</span><span class="te-cb is-on"></span></div><div class="te-mock__grp">Trust Strip</div><div class="te-mock__row"><span class="te-lbl">Trust Strip Items</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">4 fixed icons</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">4 title/description pairs</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### 8. Featured Products

eShopping Theme → Homepage Sections → **Show Featured Products** is on. The slider shows products you flag as *Featured* in BigCommerce.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IEZlYXR1cmVkIFByb2R1Y3RzKiogKGlkIGBlc2hvcHBpbmctc2hvdy1mZWF0dXJlZGApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYE9uYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY291bnQpOioqIFRoZW1lIEVkaXRvciDihpIgKkhvbWUgUGFnZSogKHN0YW5kYXJkIENvcm5lcnN0b25lIHBhbmVsKSDihpIgKipOdW1iZXIgb2YgRmVhdHVyZWQgUHJvZHVjdHMqKiAoaWQgYGhvbWVwYWdlX2ZlYXR1cmVkX3Byb2R1Y3RzX2NvdW50YCkuIEZvcm1hdDogc2VsZWN0Lg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggcHJvZHVjdHMpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKkNhdGFsb2cg4oaSIFByb2R1Y3RzKiog4oaSIGVkaXQgYSBwcm9kdWN0IOKGkiBtYXJrIGl0ICoqRmVhdHVyZWQqKi4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Featured Products</span><span class="te-cb is-on"></span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Homepage</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Number of Featured Products</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 9. New Arrivals

eShopping Theme → Homepage Sections → **Show New Arrivals** is on. Recently added products render here automatically.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IE5ldyBBcnJpdmFscyoqIChpZCBgZXNob3BwaW5nLXNob3ctbmV3YCkuIEZvcm1hdDogb24vb2ZmLiBEZWZhdWx0OiBgT25gLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY291bnQpOioqIFRoZW1lIEVkaXRvciDihpIgKkhvbWUgUGFnZSog4oaSICoqTnVtYmVyIG9mIE5ldyBQcm9kdWN0cyoqIChpZCBgaG9tZXBhZ2VfbmV3X3Byb2R1Y3RzX2NvdW50YCkuIEZvcm1hdDogc2VsZWN0Lg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show New Arrivals</span><span class="te-cb is-on"></span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Homepage</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Number of New Products</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>

### 10. Bestselling Products

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IEJlc3QgU2VsbGVycyoqIGlzIG9uLg==-->

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IEJlc3QgU2VsbGVycyoqIChpZCBgZXNob3BwaW5nLXNob3ctYmVzdHNlbGxpbmdgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGBPbmAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Best Sellers</span><span class="te-cb is-on"></span></div></div>

!!! warning "Won't appear until you have sales data"
    The toggle is enabled, but the demo store has no bestseller / sales data yet, so the Bestselling slider does **not** appear on the live home page. It will show once the store accumulates sales and bestseller data.

### 11. Products by Category

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IENhdGVnb3JpZXMqKiBpcyBvbi4gUHJvZHVjdHMtYnktQ2F0ZWdvcnkgY29uZmlndXJhdGlvbjo=-->

<!--te-tbl:fCBTZXR0aW5nIHwgVmFsdWUgfCBGaWVsZCBpZCB8CnwgLS0tLS0tLSB8IC0tLS0tIHwgLS0tLS0tLS0gfAp8IENhdGVnb3J5IElEcyB8ICooZW1wdHkg4oCUIGF1dG8tZGV0ZWN0cyB0b3AtbGV2ZWwgY2F0ZWdvcmllcywgc2hvd2luZyB0aGUgZmlyc3QgMyBwZXIgdGhlIGdyaWQpKiB8IGBlc2hvcHBpbmctcGJjc3QtY2F0SURzYCB8CnwgR3JpZCBsYXlvdXQgfCBgMyw0LDZgIOKAlCAzIGNhdGVnb3JpZXMgKHRhYnMpLCA0IHByb2R1Y3RzIGVhY2gsIHVwIHRvIDYgc3ViY2F0ZWdvcmllcyB8IGBlc2hvcHBpbmctcGJjc3QtZ3JpZGAgfAp8IERlZmF1bHQgYWN0aXZlIHRhYiB8IEZlYXR1cmVkIHwgYGVzaG9wcGluZy1wYmNzdC1hY3RpdmVgIHwKfCBTaG93IEJlc3RzZWxsaW5nIHRhYiB8IOKchSBPbiB8IGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1iZXN0c2VsbGluZ2AgfAp8IFNob3cgRmVhdHVyZWQgdGFiIHwg4pyFIE9uIHwgYGVzaG9wcGluZy1wYmNzdC1zaG93LWZlYXR1cmVkYCB8CnwgU2hvdyBOZXcgdGFiIHwg4pyFIE9uIHwgYGVzaG9wcGluZy1wYmNzdC1zaG93LW5ld2AgfAp8IFNob3cgUmV2aWV3cyB0YWIgKHRoZSAiVG9wIFJhdGVkIiB0YWIpIHwg4p2MIE9mZiB8IGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1yZXZpZXdzYCB8-->

!!! note "Category IDs left empty on purpose"
    With no IDs entered, the section automatically pulls top-level categories — no need to look up or type any IDs.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IENhdGVnb3JpZXMqKiAoaWQgYGVzaG9wcGluZy1zaG93LWNhdGVnb3JpZXNgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGBPbmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggY2F0ZWdvcmllcyk6KiogVGhlbWUgRWRpdG9yIOKGkiAqZVNob3BwaW5nIFRoZW1lIOKGkiBQcm9kdWN0cyBieSBDYXRlZ29yeSog4oaSICoqQ2F0ZWdvcnkgSURzIChjb21tYSBzZXBhcmF0ZWQsIGxlYXZlIGVtcHR5IGZvciBhdXRvLWRldGVjdCkqKiAoaWQgYGVzaG9wcGluZy1wYmNzdC1jYXRJRHNgKS4gRm9ybWF0OiBjb21tYS1zZXBhcmF0ZWQgY2F0ZWdvcnkgSURzOyBlbXB0eSA9IGF1dG8tZGV0ZWN0LiBEZWZhdWx0OiAqKGVtcHR5KSou-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoZ3JpZCk6Kiogc2FtZSBzZWN0aW9uIOKGkiAqKkdyaWQgbGF5b3V0OiBjYXRlZ29yaWVzLHByb2R1Y3RzLHN1YmNhdGVnb3JpZXMgKGUuZy4gMyw0LDYpKiogKGlkIGBlc2hvcHBpbmctcGJjc3QtZ3JpZGApLiBGb3JtYXQ6IHRocmVlIGNvbW1hLXNlcGFyYXRlZCBudW1iZXJzIGBkLHQsc2AgPSBudW1iZXIgb2YgKipjYXRlZ29yaWVzICh0YWJzKSoqLCAqKnByb2R1Y3RzIHBlciBjYXRlZ29yeSoqLCBhbmQgKipzdWJjYXRlZ29yaWVzKiogc2hvd24uIERlZmF1bHQ6IGAzLDQsNmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoYWN0aXZlIHRhYik6Kiogc2FtZSBzZWN0aW9uIOKGkiAqKkRlZmF1bHQgYWN0aXZlIHRhYioqIChpZCBgZXNob3BwaW5nLXBiY3N0LWFjdGl2ZWApLiBGb3JtYXQ6IHNlbGVjdCDigJQgYGZlYXR1cmVkYCwgYGJlc3RzZWxsaW5nYCwgYG5ld2VzdGAsIG9yIGBhdmdjdXN0b21lcnJldmlld2AgKFRvcCBSYXRlZCkuIERlZmF1bHQ6IGBmZWF0dXJlZGAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodGFiIHRvZ2dsZXMpOioqIHNhbWUgc2VjdGlvbiDihpIgKipTaG93IEJlc3RzZWxsaW5nIHRhYioqIChpZCBgZXNob3BwaW5nLXBiY3N0LXNob3ctYmVzdHNlbGxpbmdgLCBkZWZhdWx0IGBPbmApLCAqKlNob3cgRmVhdHVyZWQgdGFiKiogKGlkIGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1mZWF0dXJlZGAsIGRlZmF1bHQgYE9uYCksICoqU2hvdyBOZXcgdGFiKiogKGlkIGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1uZXdgLCB0aGVtZSBkZWZhdWx0IGBPZmZgIOKAlCBgT25gIGZvciB0aGUgQXV0b1BhcnRzIGRlbW8pLCAqKlNob3cgUmV2aWV3cyB0YWIqKiAoaWQgYGVzaG9wcGluZy1wYmNzdC1zaG93LXJldmlld3NgLCBkZWZhdWx0IGBPZmZgKS4gRm9ybWF0OiBvbi9vZmYu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Categories</span><span class="te-cb is-on"></span></div><div class="te-mock__grp">Products by Category</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Category IDs (comma separated, leave empty for auto-detect)</span><span class="te-desc">(empty — auto-detects top-level categories, showing the first 3 per the grid)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Grid layout: categories,products,subcategories (e.g. 3,4,6)</span><span class="te-desc">3,4,6 — 3 categories (tabs), 4 products each, up to 6 subcategories</span></span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">categories (tabs)</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">products per category</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">subcategories</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Default active tab</span><span class="te-dd"><span class="te-dd__v">featured</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show Bestselling tab</span><span class="te-desc">✅ On</span></span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show Featured tab</span><span class="te-desc">✅ On</span></span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show New tab</span><span class="te-desc">✅ On</span></span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Show Reviews tab</span><span class="te-desc">❌ Off</span></span><span class="te-cb"></span></div></div>

### 12. Why Choose Us — marketing block (Page Builder)

Below the Products-by-Category section, the value-prop callout — heading *"Auto Parts That Fit. Pricing That Drives."* with an eyebrow *"Why Choose Us"* and feature cards (Verified Fitment, Fast Bulk Fulfillment, OEM & Performance). This is an **AI HTML Generator | PapaThemes** widget, not a theme setting.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIgKCoqU3RvcmVmcm9udCDihpIgTXkgVGhlbWVzIOKGkiBDdXN0b21pemUqKikg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgZWRpdCB0aGUgKipIVE1MIENvbnRlbnQqKiBmaWVsZCAod2lkZ2V0IHNjaGVtYSBpZCBgY29udGVudGAsIHR5cGUgYGNvZGVgL2h0bWwpIOKGkiAqKlNhdmUqKi4gU2VlIFtXaHkgQ2hvb3NlIFVzXSh3aWRnZXRzLXBhcGF0aGVtZXMubWQjd2h5LWNob29zZS11cykgZm9yIGEgY2xlYW4gY29weS1wYXN0ZSB0ZW1wbGF0ZSBhbmQgdGhlIHZlcmJhdGltIGRlbW8gSFRNTC4gUmVnaW9uIMK3IHNvcnQ6IGBob21lX2JlbG93X3Byb2R1Y3RzX2J5X2NhdGVnb3J5YCDCtyAwLg==-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (AutoParts) — Why Choose Us, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-z5x8wwcc {
        --papathemes-ai-widget-z5x8wwcc-white: #ffffff;
        --papathemes-ai-widget-z5x8wwcc-cream: #f8fafc;
        --papathemes-ai-widget-z5x8wwcc-bark-100: #f1f5f9;
        --papathemes-ai-widget-z5x8wwcc-bark-200: #e2e8f0;
        --papathemes-ai-widget-z5x8wwcc-bark-400: #94a3b8;
        --papathemes-ai-widget-z5x8wwcc-bark-500: #64748b;
        --papathemes-ai-widget-z5x8wwcc-bark-700: #334155;
        --papathemes-ai-widget-z5x8wwcc-bark-800: #1e293b;
        --papathemes-ai-widget-z5x8wwcc-bark-900: #0f172a;
        --papathemes-ai-widget-z5x8wwcc-terra: #d97706;
        --papathemes-ai-widget-z5x8wwcc-terra-light: #f59e0b;
        --papathemes-ai-widget-z5x8wwcc-terra-dark: #b45309;
        --papathemes-ai-widget-z5x8wwcc-terra-pale: #fffbeb;
        --papathemes-ai-widget-z5x8wwcc-accent: #f59e0b;
        --papathemes-ai-widget-z5x8wwcc-accent-soft: #fef3c7;
        --papathemes-ai-widget-z5x8wwcc-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-z5x8wwcc-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-z5x8wwcc *,
    .papathemes-ai-widget-z5x8wwcc *::before,
    .papathemes-ai-widget-z5x8wwcc *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-z5x8wwcc-section {
        padding: 32px 20px 0;
    }
    
    .papathemes-ai-widget-z5x8wwcc-card {
        background: var(--papathemes-ai-widget-z5x8wwcc-white);
        border: 1px solid var(--papathemes-ai-widget-z5x8wwcc-bark-100);
        border-radius: 8px;
        overflow: hidden;
    }
    
    .papathemes-ai-widget-z5x8wwcc-inner {
        display: grid;
        grid-template-columns: 1fr 1fr;
        min-height: 360px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-visual {
        position: relative;
        background:
            linear-gradient(135deg, var(--papathemes-ai-widget-z5x8wwcc-bark-900) 0%, var(--papathemes-ai-widget-z5x8wwcc-bark-800) 100%);
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.04) inset;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        min-height: 260px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-visual::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse 70% 100% at 90% 50%, rgba(245, 158, 11, 0.14), transparent 70%),
            radial-gradient(ellipse 40% 60% at 0% 0%, rgba(255, 255, 255, 0.04), transparent 60%);
        pointer-events: none;
    }
    
    .papathemes-ai-widget-z5x8wwcc-visual::after {
        content: "";
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
        background-size: 40px 40px;
        opacity: 0.5;
        pointer-events: none;
    }
    
    .papathemes-ai-widget-z5x8wwcc-stats {
        position: relative;
        z-index: 2;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        padding: 36px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-stat {
        text-align: center;
        padding: 18px;
        background: rgba(255, 255, 255, .06);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, .08);
    }
    
    .papathemes-ai-widget-z5x8wwcc-stat-num {
        font-family: var(--papathemes-ai-widget-z5x8wwcc-font-heading);
        font-size: 28px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-z5x8wwcc-cream);
        line-height: 1;
        margin-bottom: 3px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-stat-num span {
        color: var(--papathemes-ai-widget-z5x8wwcc-accent);
    }
    
    .papathemes-ai-widget-z5x8wwcc-stat-label {
        font-family: var(--papathemes-ai-widget-z5x8wwcc-font-body);
        font-size: 10px;
        color: var(--papathemes-ai-widget-z5x8wwcc-bark-400);
        text-transform: uppercase;
        letter-spacing: .08em;
        font-weight: 600;
    }
    
    .papathemes-ai-widget-z5x8wwcc-content {
        padding: 36px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .papathemes-ai-widget-z5x8wwcc-eyebrow {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: var(--papathemes-ai-widget-z5x8wwcc-font-body);
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: .14em;
        font-weight: 700;
        color: var(--papathemes-ai-widget-z5x8wwcc-bark-700);
        margin-bottom: 10px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-eyebrow::before {
        content: "";
        width: 24px;
        height: 2px;
        background: var(--papathemes-ai-widget-z5x8wwcc-accent);
    }
    
    .papathemes-ai-widget-z5x8wwcc-heading {
        font-family: var(--papathemes-ai-widget-z5x8wwcc-font-heading);
        font-size: 20px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-z5x8wwcc-bark-900);
        margin-bottom: 14px;
        line-height: 1.25;
    }
    
    .papathemes-ai-widget-z5x8wwcc-heading em {
        font-style: italic;
        font-weight: 400;
        color: var(--papathemes-ai-widget-z5x8wwcc-bark-500);
    }
    
    .papathemes-ai-widget-z5x8wwcc-desc {
        font-family: var(--papathemes-ai-widget-z5x8wwcc-font-body);
        font-size: 12px;
        color: var(--papathemes-ai-widget-z5x8wwcc-bark-500);
        line-height: 1.7;
        margin-bottom: 24px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-features {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-feat {
        display: flex;
        gap: 12px;
        align-items: flex-start;
    }
    
    .papathemes-ai-widget-z5x8wwcc-feat-icon {
        width: 38px;
        height: 38px;
        border-radius: 6px;
        background: var(--papathemes-ai-widget-z5x8wwcc-accent-soft);
        border: 1px solid var(--papathemes-ai-widget-z5x8wwcc-bark-200);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--papathemes-ai-widget-z5x8wwcc-accent);
        flex-shrink: 0;
    }
    
    .papathemes-ai-widget-z5x8wwcc-feat-icon svg {
        width: 17px;
        height: 17px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-feat-title {
        font-family: var(--papathemes-ai-widget-z5x8wwcc-font-body);
        font-size: 12px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-z5x8wwcc-bark-800);
        margin-bottom: 1px;
    }
    
    .papathemes-ai-widget-z5x8wwcc-feat-desc {
        font-family: var(--papathemes-ai-widget-z5x8wwcc-font-body);
        font-size: 11px;
        color: var(--papathemes-ai-widget-z5x8wwcc-bark-500);
        line-height: 1.45;
    }
    
    @media (max-width: 1023px) {
        .papathemes-ai-widget-z5x8wwcc-inner {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-z5x8wwcc-section {
            padding: 24px 10px 0;
        }
    
        .papathemes-ai-widget-z5x8wwcc-stats {
            padding: 24px;
            gap: 12px;
        }
    
        .papathemes-ai-widget-z5x8wwcc-content {
            padding: 24px;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-z5x8wwcc">
        <div class="papathemes-ai-widget-z5x8wwcc-section">
            <div class="papathemes-ai-widget-z5x8wwcc-card">
                <div class="papathemes-ai-widget-z5x8wwcc-inner">
                    <div class="papathemes-ai-widget-z5x8wwcc-visual">
                        <div class="papathemes-ai-widget-z5x8wwcc-stats">
                            <div class="papathemes-ai-widget-z5x8wwcc-stat">
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-num">15<span>+</span></div>
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-label">YEARS IN AUTO PARTS</div>
                            </div>
                            <div class="papathemes-ai-widget-z5x8wwcc-stat">
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-num">3,500<span>+</span></div>
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-label">AUTO SKUS</div>
                            </div>
                            <div class="papathemes-ai-widget-z5x8wwcc-stat">
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-num">8M<span>+</span></div>
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-label">Orders Shipped</div>
                            </div>
                            <div class="papathemes-ai-widget-z5x8wwcc-stat">
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-num">99<span>%</span></div>
                                <div class="papathemes-ai-widget-z5x8wwcc-stat-label">Customer Satisfaction</div>
                            </div>
                        </div>
                    </div>
                    <div class="papathemes-ai-widget-z5x8wwcc-content">
                        <div class="papathemes-ai-widget-z5x8wwcc-eyebrow">Why Choose Us</div>
                        <h2 data-localized="1" data-localized="1" class="papathemes-ai-widget-z5x8wwcc-heading">Auto Parts That Fit. <em>Pricing That Drives.</em></h2>
                        <p class="papathemes-ai-widget-z5x8wwcc-desc">From OEM replacements to performance upgrades — every part is verified for fitment and stocked for fast dispatch to keep vehicles on the road.</p>
                        <div class="papathemes-ai-widget-z5x8wwcc-features">
                            <div class="papathemes-ai-widget-z5x8wwcc-feat">
                                <div class="papathemes-ai-widget-z5x8wwcc-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16zM12 4.15 18.4 7.8 12 11.45 5.6 7.8 12 4.15zM5 9.5l6 3.43v6.94l-6-3.43V9.5zm8 10.37v-6.94l6-3.43v6.94l-6 3.43z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-z5x8wwcc-feat-title">Verified Fitment</div>
                                    <div class="papathemes-ai-widget-z5x8wwcc-feat-desc">Every part cross-checked against year/make/model so you order right the first time.</div>
                                </div>
                            </div>
                            <div class="papathemes-ai-widget-z5x8wwcc-feat">
                                <div class="papathemes-ai-widget-z5x8wwcc-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2a3 3 0 0 0 6 0h6a3 3 0 0 0 6 0h2v-5l-3-4zM6 18.5A1.5 1.5 0 1 1 7.5 17 1.5 1.5 0 0 1 6 18.5zm13.5-9 1.96 2.5H17V9.5h2.5zM18 18.5A1.5 1.5 0 1 1 19.5 17 1.5 1.5 0 0 1 18 18.5z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-z5x8wwcc-feat-title">Fast Bulk Fulfillment</div>
                                    <div class="papathemes-ai-widget-z5x8wwcc-feat-desc">Same-day dispatch on stock items and shop pricing trusted by 9,000+ repair shops and enthusiasts.</div>
                                </div>
                            </div>
                            <div class="papathemes-ai-widget-z5x8wwcc-feat">
                                <div class="papathemes-ai-widget-z5x8wwcc-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66.95-2.3c.48.17.98.3 1.34.3C19 20 22 3 22 3c-1 2-8 2.25-13 3.25S2 11.5 2 13.5s1.75 3.75 1.75 3.75C7 8 17 8 17 8z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-z5x8wwcc-feat-title">OEM & Performance</div>
                                    <div class="papathemes-ai-widget-z5x8wwcc-feat-desc">Genuine OEM replacements alongside trusted aftermarket performance brands.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    ```
### 13. Customer Reviews — marketing block (Page Builder)

The social-proof block (heading *"Customer Reviews"*) sits directly below Why Choose Us. Also an **AI HTML Generator | PapaThemes** widget.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZCDihpIgKipTYXZlKiouIFNlZSBbQ3VzdG9tZXIgUmV2aWV3c10od2lkZ2V0cy1wYXBhdGhlbWVzLm1kI2N1c3RvbWVyLXJldmlld3MpIGZvciB0aGUgZXhhY3QgSFRNTC4gUmVnaW9uIMK3IHNvcnQ6IGBob21lX2JlbG93X3Byb2R1Y3RzX2J5X2NhdGVnb3J5YCDCtyAxLg==-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (AutoParts) — Customer Reviews, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-pkg1 {
        --papathemes-ai-widget-pkg1-white: #ffffff;
        --papathemes-ai-widget-pkg1-bark-50: #f8fafc;
        --papathemes-ai-widget-pkg1-bark-100: #eef1f5;
        --papathemes-ai-widget-pkg1-bark-200: #e2e8f0;
        --papathemes-ai-widget-pkg1-bark-300: #cbd5e1;
        --papathemes-ai-widget-pkg1-bark-400: #94a3b8;
        --papathemes-ai-widget-pkg1-bark-500: #64748b;
        --papathemes-ai-widget-pkg1-bark-600: #475569;
        --papathemes-ai-widget-pkg1-bark-700: #334155;
        --papathemes-ai-widget-pkg1-bark-800: #1e293b;
        --papathemes-ai-widget-pkg1-bark-900: #0f172a;
        --papathemes-ai-widget-pkg1-terra: #3b82f6;
        --papathemes-ai-widget-pkg1-gold: #f59e0b;
        --papathemes-ai-widget-pkg1-gold-soft: #fef3c7;
        --papathemes-ai-widget-pkg1-success: #16a34a;
        --papathemes-ai-widget-pkg1-success-soft: #ecfdf5;
        --papathemes-ai-widget-pkg1-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-pkg1-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-pkg1 *,
    .papathemes-ai-widget-pkg1 *::before,
    .papathemes-ai-widget-pkg1 *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-pkg1-section {
        padding: 32px 20px 0;
    }
    
    /* ── Section header: eyebrow + title + 'view all' link ─────────────────── */
    .papathemes-ai-widget-pkg1-header {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        gap: 16px;
        margin-bottom: 18px;
        padding-bottom: 16px;
        border-bottom: 1px solid var(--papathemes-ai-widget-pkg1-bark-200);
    }
    
    .papathemes-ai-widget-pkg1-header-left {
        display: flex;
        flex-direction: column;
        gap: 6px;
        min-width: 0;
    }
    
    .papathemes-ai-widget-pkg1-eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.16em;
        color: var(--papathemes-ai-widget-pkg1-bark-500);
    }
    
    .papathemes-ai-widget-pkg1-eyebrow::before {
        content: "";
        display: inline-block;
        width: 18px;
        height: 1px;
        background: var(--papathemes-ai-widget-pkg1-bark-400);
    }
    
    .papathemes-ai-widget-pkg1-title {
        font-family: var(--papathemes-ai-widget-pkg1-font-heading);
        font-size: 22px;
        font-weight: 700;
        color: var(--papathemes-ai-widget-pkg1-bark-900);
        letter-spacing: -0.02em;
        line-height: 1.2;
    }
    
    .papathemes-ai-widget-pkg1-viewall {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 11px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-pkg1-bark-600);
        text-decoration: none;
        padding: 8px 14px;
        border: 1px solid var(--papathemes-ai-widget-pkg1-bark-200);
        border-radius: 999px;
        transition: all .2s ease;
        flex-shrink: 0;
    }
    
    .papathemes-ai-widget-pkg1-viewall:hover {
        color: var(--papathemes-ai-widget-pkg1-bark-900);
        border-color: var(--papathemes-ai-widget-pkg1-bark-400);
        background: var(--papathemes-ai-widget-pkg1-bark-50);
    }
    
    .papathemes-ai-widget-pkg1-viewall svg {
        width: 12px;
        height: 12px;
    }
    
    /* ── Hero summary strip — restrained ecommerce palette ─────────────────── */
    .papathemes-ai-widget-pkg1-hero {
        display: grid;
        grid-template-columns: 280px 1fr 220px;
        gap: 28px;
        align-items: stretch;
        padding: 22px 26px;
        background: var(--papathemes-ai-widget-pkg1-white);
        border: 1px solid var(--papathemes-ai-widget-pkg1-bark-200);
        border-radius: 8px;
        margin-bottom: 16px;
    }
    
    @media (max-width: 1100px) {
        .papathemes-ai-widget-pkg1-hero {
            grid-template-columns: 1fr;
            gap: 20px;
        }
    }
    
    /* Cell 1 — rating hero */
    .papathemes-ai-widget-pkg1-rating-hero {
        display: flex;
        flex-direction: column;
        gap: 8px;
        justify-content: center;
        padding-right: 28px;
        border-right: 1px solid var(--papathemes-ai-widget-pkg1-bark-100);
    }
    
    @media (max-width: 1100px) {
        .papathemes-ai-widget-pkg1-rating-hero {
            padding-right: 0;
            padding-bottom: 16px;
            border-right: none;
            border-bottom: 1px solid var(--papathemes-ai-widget-pkg1-bark-100);
        }
    }
    
    .papathemes-ai-widget-pkg1-rating-row {
        display: flex;
        align-items: baseline;
        gap: 12px;
    }
    
    .papathemes-ai-widget-pkg1-rating-big {
        font-family: var(--papathemes-ai-widget-pkg1-font-heading);
        font-size: 52px;
        font-weight: 700;
        color: var(--papathemes-ai-widget-pkg1-bark-900);
        letter-spacing: -0.04em;
        line-height: 1;
    }
    
    .papathemes-ai-widget-pkg1-rating-out {
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 13px;
        color: var(--papathemes-ai-widget-pkg1-bark-500);
        font-weight: 500;
    }
    
    .papathemes-ai-widget-pkg1-stars {
        display: inline-flex;
        gap: 2px;
        color: var(--papathemes-ai-widget-pkg1-gold);
    }
    
    .papathemes-ai-widget-pkg1-stars svg {
        width: 16px;
        height: 16px;
    }
    
    .papathemes-ai-widget-pkg1-rating-rank {
        display: inline-block;
        font-family: var(--papathemes-ai-widget-pkg1-font-heading);
        font-size: 12px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-pkg1-bark-700);
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 2px;
    }
    
    .papathemes-ai-widget-pkg1-rating-count {
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 12px;
        color: var(--papathemes-ai-widget-pkg1-bark-500);
    }
    
    /* Cell 2 — distribution */
    .papathemes-ai-widget-pkg1-dist {
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: 6px;
        justify-content: center;
    }
    
    .papathemes-ai-widget-pkg1-dist-row {
        display: grid;
        grid-template-columns: 38px 1fr 36px 50px;
        align-items: center;
        gap: 12px;
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 12px;
        color: var(--papathemes-ai-widget-pkg1-bark-600);
    }
    
    .papathemes-ai-widget-pkg1-dist-label {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        font-weight: 700;
        color: var(--papathemes-ai-widget-pkg1-bark-700);
        font-size: 12px;
    }
    
    .papathemes-ai-widget-pkg1-dist-label svg {
        width: 11px;
        height: 11px;
        color: var(--papathemes-ai-widget-pkg1-gold);
    }
    
    .papathemes-ai-widget-pkg1-dist-bar {
        position: relative;
        height: 8px;
        background: var(--papathemes-ai-widget-pkg1-bark-100);
        border-radius: 2px;
        overflow: hidden;
    }
    
    .papathemes-ai-widget-pkg1-dist-fill {
        display: block;
        height: 100%;
        background: var(--papathemes-ai-widget-pkg1-gold);
        border-radius: inherit;
    }
    
    .papathemes-ai-widget-pkg1-dist-pct {
        text-align: right;
        font-weight: 700;
        color: var(--papathemes-ai-widget-pkg1-bark-700);
        font-variant-numeric: tabular-nums;
        font-size: 12px;
    }
    
    .papathemes-ai-widget-pkg1-dist-count {
        text-align: right;
        color: var(--papathemes-ai-widget-pkg1-bark-400);
        font-variant-numeric: tabular-nums;
        font-size: 11px;
    }
    
    /* Cell 3 — trust badges */
    .papathemes-ai-widget-pkg1-badges {
        display: flex;
        flex-direction: column;
        gap: 10px;
        justify-content: center;
        padding-left: 28px;
        border-left: 1px solid var(--papathemes-ai-widget-pkg1-bark-100);
    }
    
    @media (max-width: 1100px) {
        .papathemes-ai-widget-pkg1-badges {
            padding-left: 0;
            padding-top: 16px;
            border-left: none;
            border-top: 1px solid var(--papathemes-ai-widget-pkg1-bark-100);
            flex-direction: row;
            flex-wrap: wrap;
        }
    }
    
    .papathemes-ai-widget-pkg1-badge {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 12px;
        color: var(--papathemes-ai-widget-pkg1-bark-600);
        font-weight: 500;
    }
    
    .papathemes-ai-widget-pkg1-badge strong {
        font-weight: 700;
        color: var(--papathemes-ai-widget-pkg1-bark-900);
    }
    
    .papathemes-ai-widget-pkg1-badge-icon {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 24px;
        height: 24px;
        border-radius: 4px;
        flex-shrink: 0;
        background: var(--papathemes-ai-widget-pkg1-bark-50);
        color: var(--papathemes-ai-widget-pkg1-bark-700);
        border: 1px solid var(--papathemes-ai-widget-pkg1-bark-200);
    }
    
    .papathemes-ai-widget-pkg1-badge-icon svg {
        width: 12px;
        height: 12px;
    }
    
    /* ── Carousel ─────────────────────────────────────────────────────────── */
    .papathemes-ai-widget-pkg1-carousel-wrap {
        position: relative;
        min-width: 0;
    }
    
    .papathemes-ai-widget-pkg1-scroll {
        display: flex;
        gap: 16px;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        scrollbar-width: none;
        padding: 4px 0;
    }
    
    .papathemes-ai-widget-pkg1-scroll::-webkit-scrollbar {
        display: none;
    }
    
    .papathemes-ai-widget-pkg1-arrow {
        display: none;
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: var(--papathemes-ai-widget-pkg1-white);
        border: 1px solid var(--papathemes-ai-widget-pkg1-bark-200);
        cursor: pointer;
        z-index: 3;
        align-items: center;
        justify-content: center;
        padding: 0;
        transition: all .2s ease;
        color: var(--papathemes-ai-widget-pkg1-bark-700);
    }
    
    .papathemes-ai-widget-pkg1-arrow svg {
        width: 18px;
        height: 18px;
    }
    
    .papathemes-ai-widget-pkg1-arrow:hover {
        border-color: var(--papathemes-ai-widget-pkg1-bark-400);
        color: var(--papathemes-ai-widget-pkg1-bark-900);
        box-shadow: 0 2px 8px rgba(15, 23, 42, .08);
    }
    
    .papathemes-ai-widget-pkg1-arrow--prev {
        left: -16px;
    }
    
    .papathemes-ai-widget-pkg1-arrow--next {
        right: -16px;
    }
    
    @media (min-width: 768px) {
        .papathemes-ai-widget-pkg1-arrow {
            display: flex;
        }
    }
    
    /* ── Review card — restrained ecommerce ───────────────────────────────── */
    .papathemes-ai-widget-pkg1-review {
        min-width: 240px;
        max-width: 260px;
        flex-shrink: 0;
        scroll-snap-align: start;
        background: var(--papathemes-ai-widget-pkg1-white);
        border: 1px solid var(--papathemes-ai-widget-pkg1-bark-200);
        border-radius: 8px;
        padding: 18px 16px 14px;
        transition: border-color .2s ease, box-shadow .2s ease;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
    }
    
    .papathemes-ai-widget-pkg1-review:hover {
        border-color: var(--papathemes-ai-widget-pkg1-bark-400);
        box-shadow: 0 4px 16px rgba(15, 23, 42, .06);
    }
    
    /* Subtle faded quote mark — top-left, neutral */
    .papathemes-ai-widget-pkg1-quote-bg {
        position: absolute;
        top: 4px;
        left: 10px;
        font-family: Georgia, 'Times New Roman', serif;
        font-size: 60px;
        line-height: 1;
        color: var(--papathemes-ai-widget-pkg1-bark-100);
        pointer-events: none;
        user-select: none;
        font-weight: 700;
        z-index: 0;
    }
    
    .papathemes-ai-widget-pkg1-r-meta {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 8px;
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-pkg1-r-stars {
        display: flex;
        gap: 2px;
        color: var(--papathemes-ai-widget-pkg1-gold);
    }
    
    .papathemes-ai-widget-pkg1-r-stars svg {
        width: 13px;
        height: 13px;
    }
    
    .papathemes-ai-widget-pkg1-r-ago {
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 10px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        color: var(--papathemes-ai-widget-pkg1-bark-400);
    }
    
    .papathemes-ai-widget-pkg1-r-text {
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 13px;
        color: var(--papathemes-ai-widget-pkg1-bark-800);
        line-height: 1.55;
        margin-bottom: 14px;
        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
        overflow: hidden;
        position: relative;
        z-index: 1;
        flex: 1;
        font-weight: 500;
    }
    
    .papathemes-ai-widget-pkg1-r-author {
        display: flex;
        align-items: center;
        gap: 10px;
        padding-top: 12px;
        border-top: 1px solid var(--papathemes-ai-widget-pkg1-bark-100);
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-pkg1-avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: var(--papathemes-ai-widget-pkg1-font-heading);
        font-weight: 700;
        font-size: 12px;
        color: #ffffff;
        letter-spacing: 0.02em;
        flex-shrink: 0;
    }
    
    .papathemes-ai-widget-pkg1-r-id {
        display: flex;
        flex-direction: column;
        min-width: 0;
        flex: 1;
    }
    
    .papathemes-ai-widget-pkg1-r-name {
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 13px;
        font-weight: 700;
        color: var(--papathemes-ai-widget-pkg1-bark-900);
        display: inline-flex;
        align-items: center;
        gap: 5px;
        line-height: 1.3;
    }
    
    .papathemes-ai-widget-pkg1-r-check {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background: var(--papathemes-ai-widget-pkg1-success);
        color: #ffffff;
        flex-shrink: 0;
    }
    
    .papathemes-ai-widget-pkg1-r-check svg {
        width: 9px;
        height: 9px;
    }
    
    .papathemes-ai-widget-pkg1-r-role {
        font-family: var(--papathemes-ai-widget-pkg1-font-body);
        font-size: 11px;
        color: var(--papathemes-ai-widget-pkg1-bark-500);
        margin-top: 2px;
    }
    
    @media (max-width: 900px) {
        .papathemes-ai-widget-pkg1-hero {
            padding: 18px;
        }
    
        .papathemes-ai-widget-pkg1-rating-big {
            font-size: 48px;
        }
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-pkg1-section {
            padding: 24px 10px 0;
        }
    
        .papathemes-ai-widget-pkg1-review {
            min-width: 240px;
        }
    
        .papathemes-ai-widget-pkg1-quote-bg {
            font-size: 64px;
        }
    
        .papathemes-ai-widget-pkg1-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 12px;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-pkg1">
        <div class="papathemes-ai-widget-pkg1-section">
            <header class="papathemes-ai-widget-pkg1-header">
                <div class="papathemes-ai-widget-pkg1-header-left">
                    <span class="papathemes-ai-widget-pkg1-eyebrow">Reviews</span>
                    <h2 class="papathemes-ai-widget-pkg1-title">Customer Reviews</h2>
                </div>
                <a href="#reviews" class="papathemes-ai-widget-pkg1-viewall" aria-label="View all reviews">
                    View all 2,400
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
                </a>
            </header>
            <section class="papathemes-ai-widget-pkg1-hero" aria-label="Rating summary">
                <div class="papathemes-ai-widget-pkg1-rating-hero">
                    <div class="papathemes-ai-widget-pkg1-rating-row">
                        <span class="papathemes-ai-widget-pkg1-rating-big">4.8</span>
                        <span class="papathemes-ai-widget-pkg1-rating-out">out of 5</span>
                    </div>
                    <div class="papathemes-ai-widget-pkg1-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                    <span class="papathemes-ai-widget-pkg1-rating-count">Based on 2,400+ verified reviews</span>
                </div>
                <ul class="papathemes-ai-widget-pkg1-dist">
                        <li class="papathemes-ai-widget-pkg1-dist-row">
                            <span class="papathemes-ai-widget-pkg1-dist-label">5 <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></span>
                            <span class="papathemes-ai-widget-pkg1-dist-bar"><span class="papathemes-ai-widget-pkg1-dist-fill" style="width:78%"></span></span>
                            <span class="papathemes-ai-widget-pkg1-dist-pct">78%</span>
                            <span class="papathemes-ai-widget-pkg1-dist-count">1,872</span>
                        </li>
                        <li class="papathemes-ai-widget-pkg1-dist-row">
                            <span class="papathemes-ai-widget-pkg1-dist-label">4 <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></span>
                            <span class="papathemes-ai-widget-pkg1-dist-bar"><span class="papathemes-ai-widget-pkg1-dist-fill" style="width:18%"></span></span>
                            <span class="papathemes-ai-widget-pkg1-dist-pct">18%</span>
                            <span class="papathemes-ai-widget-pkg1-dist-count">432</span>
                        </li>
                        <li class="papathemes-ai-widget-pkg1-dist-row">
                            <span class="papathemes-ai-widget-pkg1-dist-label">3 <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></span>
                            <span class="papathemes-ai-widget-pkg1-dist-bar"><span class="papathemes-ai-widget-pkg1-dist-fill" style="width:3%"></span></span>
                            <span class="papathemes-ai-widget-pkg1-dist-pct">3%</span>
                            <span class="papathemes-ai-widget-pkg1-dist-count">72</span>
                        </li>
                        <li class="papathemes-ai-widget-pkg1-dist-row">
                            <span class="papathemes-ai-widget-pkg1-dist-label">2 <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></span>
                            <span class="papathemes-ai-widget-pkg1-dist-bar"><span class="papathemes-ai-widget-pkg1-dist-fill" style="width:1%"></span></span>
                            <span class="papathemes-ai-widget-pkg1-dist-pct">1%</span>
                            <span class="papathemes-ai-widget-pkg1-dist-count">24</span>
                        </li>
                        <li class="papathemes-ai-widget-pkg1-dist-row">
                            <span class="papathemes-ai-widget-pkg1-dist-label">1 <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></span>
                            <span class="papathemes-ai-widget-pkg1-dist-bar"><span class="papathemes-ai-widget-pkg1-dist-fill" style="width:1%"></span></span>
                            <span class="papathemes-ai-widget-pkg1-dist-pct"><1%</span>
                            <span class="papathemes-ai-widget-pkg1-dist-count">0</span>
                        </li>
                </ul>
                <div class="papathemes-ai-widget-pkg1-badges">
                    <div class="papathemes-ai-widget-pkg1-badge">
                        <span class="papathemes-ai-widget-pkg1-badge-icon"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span>
                        <span><strong>98%</strong> recommend</span>
                    </div>
                    <div class="papathemes-ai-widget-pkg1-badge">
                        <span class="papathemes-ai-widget-pkg1-badge-icon"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L4 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-8-3z"/></svg></span>
                        <span><strong>100%</strong> verified</span>
                    </div>
                    <div class="papathemes-ai-widget-pkg1-badge">
                        <span class="papathemes-ai-widget-pkg1-badge-icon"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M17.65 6.35A7.958 7.958 0 0012 4a8 8 0 108 8h-2a6 6 0 11-1.76-4.24L13 11h7V4l-2.35 2.35z"/></svg></span>
                        <span><strong>87%</strong> reorder</span>
                    </div>
                </div>
            </section>
            <div class="papathemes-ai-widget-pkg1-carousel-wrap">
                <button type="button" class="papathemes-ai-widget-pkg1-arrow papathemes-ai-widget-pkg1-arrow--prev" data-dir="prev" aria-label="Previous reviews">
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/></svg>
                </button>
                <button type="button" class="papathemes-ai-widget-pkg1-arrow papathemes-ai-widget-pkg1-arrow--next" data-dir="next" aria-label="Next reviews">
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/></svg>
                </button>
                <div class="papathemes-ai-widget-pkg1-scroll">
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">2 days ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Switched our entire parts ordering here. Faster fitment lookups and far fewer wrong-part returns.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #334155, #1e293b)">DM</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Dana M.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Shop Owner</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 week ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">The performance suspension kit arrived complete with hardware. Install was clean and the ride is night-and-day.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">EK</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Erin K.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">DIY Builder</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">2 weeks ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">OEM brake parts arrive on time, every time. Shop pricing keeps our margin healthy.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">RT</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Ray T.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Service Manager</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">3 weeks ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Right-spec sensors and gaskets cut my diagnostic time noticeably. Reordering by VIN is effortless.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #334155, #1e293b)">SP</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Sofia P.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Mechanic</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 month ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Performance intake shipped same day before a track event. Saved my weekend.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">JL</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Jordan L.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Car Enthusiast</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 month ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Maintenance parts arrive ready to install. No more lost time chasing fitment.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #1e293b, #0f172a)">MA</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Marcus A.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Fleet Manager</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">2 months ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">The eco mailers and paper void fill let us drop plastic entirely. Our customers love the sustainable switch.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #1e293b, #0f172a)">NB</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Nina B.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Subscription Box Founder</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">2 months ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Double-wall cartons hold up across multiple carrier hand-offs. Breakage on heavy SKUs is basically gone.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #334155, #1e293b)">CT</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Carlos T.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">3PL Operations</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">3 months ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Consistent board strength and accurate dimensions. We can plan pallet loads without surprises.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #64748b, #475569)">HW</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Hannah W.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Retail Buyer</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">3 months ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Poly mailers are light, tough, and cheap to ship. Exactly what I needed to scale my store.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">TV</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Tom V.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Dropship Seller</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">4 months ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Their team helped me spec the right cushioning for fragile glassware. Damage claims dropped to near zero.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #64748b, #475569)">GR</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Grace R.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Logistics Coordinator</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">5 months ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Bulk tape and box bundles ship fast and the quality is consistent. Our go-to supplier now.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #1e293b, #0f172a)">PD</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Priya D.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Shop Owner</span>
                            </div>
                        </footer>
                    </article>
                </div>
            </div>
        </div>
    </div>
    
    <script>
    (function(){
        var id = 'pkg1';
        var gap = 16;
        var root = document.querySelector('.papathemes-ai-widget-' + id);
        if (!root) return;
        var track = root.querySelector('.papathemes-ai-widget-' + id + '-scroll');
        if (!track) return;
        var prev = root.querySelector('[data-dir="prev"]');
        var next = root.querySelector('[data-dir="next"]');
        var cardW = function(){ var c = track.querySelector('.papathemes-ai-widget-' + id + '-review'); return c ? c.offsetWidth + gap : 260; };
        if (prev) prev.onclick = function(){ track.scrollBy({ left: -cardW(), behavior: 'smooth' }); };
        if (next) next.onclick = function(){ track.scrollBy({ left: cardW(), behavior: 'smooth' }); };
    })();
    </script>
    ```
### 14. Resources — marketing block (Page Builder)

The guide-cards block (heading *"Auto Parts Resources & Guides"*, with cards *How to Find the Right Fitment*, *OEM vs Aftermarket: When to Choose*, *DIY Repair Safety & Tools*) follows Customer Reviews. Also an **AI HTML Generator | PapaThemes** widget.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZCDihpIgKipTYXZlKiouIFNlZSBbUmVzb3VyY2VzXSh3aWRnZXRzLXBhcGF0aGVtZXMubWQjcmVzb3VyY2VzKSBmb3IgdGhlIGV4YWN0IEhUTUwuIFJlZ2lvbiDCtyBzb3J0OiBgaG9tZV9iZWxvd19wcm9kdWN0c19ieV9jYXRlZ29yeWAgwrcgMi4=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (AutoParts) — Resources, paste into the widget's HTML Content field"

    ```html
    
    <style>
    .papathemes-ai-widget-sg5va1rw {
        --papathemes-ai-widget-sg5va1rw-white: #ffffff;
        --papathemes-ai-widget-sg5va1rw-bark-100: #f1f5f9;
        --papathemes-ai-widget-sg5va1rw-bark-500: #64748b;
        --papathemes-ai-widget-sg5va1rw-bark-800: #1e293b;
        --papathemes-ai-widget-sg5va1rw-bark-900: #0f172a;
        --papathemes-ai-widget-sg5va1rw-terra: #d97706;
        --papathemes-ai-widget-sg5va1rw-terra-dark: #b45309;
        --papathemes-ai-widget-sg5va1rw-terra-pale: #fffbeb;
        --papathemes-ai-widget-sg5va1rw-forest-700: #15803d;
        --papathemes-ai-widget-sg5va1rw-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-sg5va1rw-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-sg5va1rw *,
    .papathemes-ai-widget-sg5va1rw *::before,
    .papathemes-ai-widget-sg5va1rw *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-sg5va1rw-section {
        padding: 32px 20px 0;
    }
    
    .papathemes-ai-widget-sg5va1rw-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    
    .papathemes-ai-widget-sg5va1rw-header-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .papathemes-ai-widget-sg5va1rw-sec-icon {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        background: var(--papathemes-ai-widget-sg5va1rw-terra-pale);
        color: var(--papathemes-ai-widget-sg5va1rw-terra);
    }
    
    .papathemes-ai-widget-sg5va1rw-sec-icon svg {
        width: 18px;
        height: 18px;
    }
    
    .papathemes-ai-widget-sg5va1rw-title {
        font-family: var(--papathemes-ai-widget-sg5va1rw-font-heading);
        font-size: 18px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-sg5va1rw-bark-900);
    }
    
    .papathemes-ai-widget-sg5va1rw-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 20px;
    }
    
    .papathemes-ai-widget-sg5va1rw-card-link {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    
    .papathemes-ai-widget-sg5va1rw-card {
        background: var(--papathemes-ai-widget-sg5va1rw-white);
        border: 1px solid var(--papathemes-ai-widget-sg5va1rw-bark-100);
        border-radius: 8px;
        overflow: hidden;
        transition: all .35s;
    }
    
    a.papathemes-ai-widget-sg5va1rw-card-link .papathemes-ai-widget-sg5va1rw-card {
        cursor: pointer;
    }
    
    a.papathemes-ai-widget-sg5va1rw-card-link .papathemes-ai-widget-sg5va1rw-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 20px rgba(15, 13, 10, .08);
        border-color: transparent;
    }
    
    .papathemes-ai-widget-sg5va1rw-thumb {
        aspect-ratio: 16/9;
        position: relative;
        display: block;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        background-color: #f8fafc;
    }
    
    .papathemes-ai-widget-sg5va1rw-thumb img {
        width: 100%;
        height: 100%;
        /* cover + 4:3 ratio = uniform card visuals across stores:
           - packaging square product photos crop minimally (~12% top/bottom)
           - electronics 16:9 hero images crop slightly on sides (~12%)
           - subject usually centered → safe crop for both
           Eliminates the "different image sizes inside same-size frames" bug
           caused by object-fit: contain + variable source ratios. */
        object-fit: cover;
        opacity: 0;
        transition: opacity 0.3s ease-in-out;
    }
    
    .papathemes-ai-widget-sg5va1rw-thumb img.papathemes-ai-widget-sg5va1rw-loaded {
        opacity: 1;
    }
    
    .papathemes-ai-widget-sg5va1rw-type {
        position: absolute;
        top: 10px;
        left: 10px;
        padding: 3px 9px;
        background: rgba(0, 0, 0, .45);
        backdrop-filter: blur(6px);
        border-radius: 4px;
        font-family: var(--papathemes-ai-widget-sg5va1rw-font-body);
        font-size: 8px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: .06em;
        color: #fff;
        display: flex;
        align-items: center;
        gap: 4px;
        z-index: 2;
    }
    
    .papathemes-ai-widget-sg5va1rw-type svg {
        width: 10px;
        height: 10px;
    }
    
    .papathemes-ai-widget-sg5va1rw-body {
        padding: 18px;
    }
    
    .papathemes-ai-widget-sg5va1rw-body h3 {
        font-family: var(--papathemes-ai-widget-sg5va1rw-font-body);
        font-size: 13px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-sg5va1rw-bark-800);
        margin-bottom: 4px;
        line-height: 1.3;
        transition: color .2s;
    }
    
    a.papathemes-ai-widget-sg5va1rw-card-link .papathemes-ai-widget-sg5va1rw-card:hover .papathemes-ai-widget-sg5va1rw-body h3 {
        color: var(--papathemes-ai-widget-sg5va1rw-terra-dark);
    }
    
    .papathemes-ai-widget-sg5va1rw-body p {
        font-family: var(--papathemes-ai-widget-sg5va1rw-font-body);
        font-size: 11px;
        color: var(--papathemes-ai-widget-sg5va1rw-bark-500);
        line-height: 1.5;
    }
    
    @media (max-width: 1023px) {
        .papathemes-ai-widget-sg5va1rw-grid {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-sg5va1rw-section {
            padding: 24px 10px 0;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-sg5va1rw">
        <div class="papathemes-ai-widget-sg5va1rw-section">
            <div class="papathemes-ai-widget-sg5va1rw-header">
                <div class="papathemes-ai-widget-sg5va1rw-header-left">
                    <div class="papathemes-ai-widget-sg5va1rw-sec-icon">
                        <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-5 2v6l-2.5-1.5L8 10V4h5zM6 20V4h.01L6 20h12V4l.01 16H6z"/></svg>
                    </div>
                    <h2 class="papathemes-ai-widget-sg5va1rw-title">Auto Parts Resources &amp; Guides</h2>
                </div>
            </div>
            <div class="papathemes-ai-widget-sg5va1rw-grid">
                <a href="https://eshopping-autoparts-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-sg5va1rw-card-link">
                    <div class="papathemes-ai-widget-sg5va1rw-card">
                        <div class="papathemes-ai-widget-sg5va1rw-thumb">
                            <img
                                class="papathemes-ai-widget-sg5va1rw-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-u0mz3ww2uj/product_images/uploaded_images/autoparts-fitment-guide.jpg?v=1779872254"
                                width="640"
                                height="360"
                                alt="Auto parts catalog"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-sg5va1rw-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-sg5va1rw-body">
                            <h3>How to Find the Right Fitment</h3>
                            <p>Year/make/model and VIN verification to order the right part the first time.</p>
                        </div>
                    </div>
                </a>
                <a href="https://eshopping-autoparts-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-sg5va1rw-card-link">
                    <div class="papathemes-ai-widget-sg5va1rw-card">
                        <div class="papathemes-ai-widget-sg5va1rw-thumb">
                            <img
                                class="papathemes-ai-widget-sg5va1rw-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-u0mz3ww2uj/product_images/uploaded_images/autoparts-oem-vs-aftermarket.jpg?v=1779872265"
                                width="640"
                                height="360"
                                alt="OEM and aftermarket parts"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-sg5va1rw-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-sg5va1rw-body">
                            <h3>OEM vs Aftermarket: When to Choose</h3>
                            <p>Trade-offs between genuine OEM and trusted aftermarket performance brands.</p>
                        </div>
                    </div>
                </a>
                <a href="https://eshopping-autoparts-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-sg5va1rw-card-link">
                    <div class="papathemes-ai-widget-sg5va1rw-card">
                        <div class="papathemes-ai-widget-sg5va1rw-thumb">
                            <img
                                class="papathemes-ai-widget-sg5va1rw-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-u0mz3ww2uj/product_images/uploaded_images/autoparts-diy-repair-safety.jpg?v=1779872276"
                                width="640"
                                height="360"
                                alt="DIY auto repair tools"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-sg5va1rw-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-sg5va1rw-body">
                            <h3>DIY Repair Safety &amp; Tools</h3>
                            <p>Essential tools and safety gear for confident at-home auto repair work.</p>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
    
    <script>
    (function(){
        var id = 'sg5va1rw';
        var root = document.querySelector('.papathemes-ai-widget-' + id);
        if (!root) return;
        var images = root.querySelectorAll('img[data-src]');
        var imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    var img = entry.target;
                    var src = img.getAttribute('data-src');
                    if (src) {
                        img.src = src;
                        img.removeAttribute('data-src');
                        img.addEventListener('load', function() {
                            img.classList.add('papathemes-ai-widget-' + id + '-loaded');
                        });
                        imageObserver.unobserve(img);
                    }
                }
            });
        }, { rootMargin: '50px' });
        images.forEach(function(img) {
            imageObserver.observe(img);
        });
    })();
    </script>
    ```
### 15. Brands carousel

eShopping Theme → Homepage Sections → **Homepage Brands Limit**: `12`. Square / transparent-PNG logos at a consistent size sit evenly in the carousel.

<!--te-src:PiAqKkN1c3RvbWl6ZSAobGltaXQpOioqIFRoZW1lIEVkaXRvciDihpIgKmVTaG9wcGluZyBUaGVtZSDihpIgSG9tZXBhZ2UgU2VjdGlvbnMqIOKGkiAqKkhvbWVwYWdlIEJyYW5kcyBMaW1pdCoqIChpZCBgZXNob3BwaW5nLWhvbWVwYWdlLWJyYW5kcy1saW1pdGApLiBGb3JtYXQ6IG51bWJlciAobWF4IGJyYW5kcyBzaG93bikuIERlZmF1bHQ6IGAxMmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAobG9nb3MpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKkNhdGFsb2cg4oaSIEJyYW5kcyoqLiBBZGQgYnJhbmRzIGFuZCB1cGxvYWQgZWFjaCBicmFuZCdzIGxvZ28gaW1hZ2UgdGhlcmUuIChOb3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Homepage Brands Limit</span><span class="te-dd"><span class="te-dd__v">12</span><span class="te-dd__b">▾</span></span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub is-active">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 16. Blog posts

Blog posts count: `3`. Posts come from **Storefront → Blog**.

<!--te-src:PiAqKkN1c3RvbWl6ZSAocG9zdHMpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKlN0b3JlZnJvbnQg4oaSIEJsb2cqKi4gV3JpdGUvcHVibGlzaCBwb3N0cyB0aGVyZS4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub is-active">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 17. Newsletter — variation default

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IE5ld3NsZXR0ZXIqKiBpcyBvbi4gVGhlIGhlYWRpbmcgYW5kIGRlc2NyaXB0aW9uICh0aGUgYDxlbT5gIHdyYXBzIHRoZSBpdGFsaWMgZW1waGFzaXMpOg==-->

- **Heading:** Get *Parts Updates* & Deals
- **Description:** New arrivals, fitment guides, and exclusive discounts delivered weekly.

The signup writes to **Customers → Subscribers**.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IE5ld3NsZXR0ZXIqKiAoaWQgYGVzaG9wcGluZy1zaG93LW5ld3NsZXR0ZXJgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGBPbmAuIChBbHNvIHJlcXVpcmVzIHRoZSBzdG9yZS1sZXZlbCAqU2hvdyBuZXdzbGV0dGVyKiBzZXR0aW5nIHRvIGJlIG9uLik=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodGV4dCk6Kiogc2FtZSBzZWN0aW9uIOKGkiAqKk5ld3NsZXR0ZXIgU2lnbnVwIFRleHQqKiAoaWQgYGVzaG9wcGluZy1uZXdzbGV0dGVyLXRleHRgKS4gRm9ybWF0OiBgSGVhZGluZ3xEZXNjcmlwdGlvbmAsIHNwbGl0IG9uIGEgc2luZ2xlIGB8YC4gVGhlICoqaGVhZGluZyBzdXBwb3J0cyBpbmxpbmUgSFRNTCoqIChlLmcuIGA8ZW0+4oCmPC9lbT5gKTsgdGhlIGRlc2NyaXB0aW9uIGlzIHBsYWluIHRleHQuIERlZmF1bHQgKEF1dG9QYXJ0cyk6IGBHZXQgPGVtPlBhcnRzIFVwZGF0ZXM8L2VtPiAmIERlYWxzfE5ldyBhcnJpdmFscywgZml0bWVudCBndWlkZXMsIGFuZCBleGNsdXNpdmUgZGlzY291bnRzIGRlbGl2ZXJlZCB3ZWVrbHkuYA==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Newsletter</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Newsletter Signup Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">heading supports inline HTML</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### 18. About — marketing block (Page Builder)

Below the Newsletter, the SEO intro block (heading *"Your Complete Auto Parts Source"*). An **AI HTML Generator | PapaThemes** widget.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZCDihpIgKipTYXZlKiouIFNlZSBbQWJvdXRdKHdpZGdldHMtcGFwYXRoZW1lcy5tZCNhYm91dCkgZm9yIHRoZSBleGFjdCBIVE1MLiBSZWdpb24gwrcgc29ydDogYGhvbWVfYmVsb3dfbmV3c2xldHRlcmAgwrcgMC4=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (AutoParts) — About, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-k83ixx3j {
        --papathemes-ai-widget-k83ixx3j-white: #ffffff;
        --papathemes-ai-widget-k83ixx3j-bark-100: #f1f5f9;
        --papathemes-ai-widget-k83ixx3j-bark-600: #475569;
        --papathemes-ai-widget-k83ixx3j-bark-900: #0f172a;
        --papathemes-ai-widget-k83ixx3j-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-k83ixx3j-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 32px 20px 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-k83ixx3j *,
    .papathemes-ai-widget-k83ixx3j *::before,
    .papathemes-ai-widget-k83ixx3j *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-k83ixx3j-section {
        background: var(--papathemes-ai-widget-k83ixx3j-white);
        border: 1px solid var(--papathemes-ai-widget-k83ixx3j-bark-100);
        border-radius: 8px;
        padding: 32px;
    }
    
    .papathemes-ai-widget-k83ixx3j-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .papathemes-ai-widget-k83ixx3j-title {
        font-family: var(--papathemes-ai-widget-k83ixx3j-font-heading);
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--papathemes-ai-widget-k83ixx3j-bark-900);
        text-align: center;
        margin-bottom: 16px;
        line-height: 1.3;
    }
    
    .papathemes-ai-widget-k83ixx3j-text {
        font-family: var(--papathemes-ai-widget-k83ixx3j-font-body);
        font-size: 0.86rem;
        color: var(--papathemes-ai-widget-k83ixx3j-bark-600);
        line-height: 1.8;
        max-width: 860px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 12px;
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-k83ixx3j {
            margin: 24px 10px 0;
        }
    
        .papathemes-ai-widget-k83ixx3j-section {
            padding: 24px 18px;
        }
    
        .papathemes-ai-widget-k83ixx3j-title {
            font-size: 1.15rem;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-k83ixx3j">
        <div class="papathemes-ai-widget-k83ixx3j-section">
            <div class="papathemes-ai-widget-k83ixx3j-container">
                <h2 class="papathemes-ai-widget-k83ixx3j-title">Your Complete Auto Parts Source</h2>
                <p class="papathemes-ai-widget-k83ixx3j-text">We supply the OEM and performance parts that keep mechanics, fleets, and enthusiasts moving. Our catalog spans engine, brake, suspension, electrical, body, and accessory parts — verified for fitment and stocked for fast, predictable reordering.</p>
                <p class="papathemes-ai-widget-k83ixx3j-text">From routine maintenance to performance upgrades, every part is chosen for fitment accuracy and quality. Browse trusted OEM and aftermarket brands used by thousands of shops and DIY builders every day.</p>
            </div>
        </div>
    </div>
    ```
### 19. Talk to an Expert — marketing block (Page Builder)

Directly below About, the contact CTA (heading *"Need help finding the right part? Talk to an Auto Parts Specialist"*). An **AI HTML Generator | PapaThemes** widget.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZCDihpIgKipTYXZlKiouIFNlZSBbVGFsayB0byBhbiBFeHBlcnRdKHdpZGdldHMtcGFwYXRoZW1lcy5tZCN0YWxrLXRvLWFuLWV4cGVydCkgZm9yIHRoZSBleGFjdCBIVE1MLiBSZWdpb24gwrcgc29ydDogYGhvbWVfYmVsb3dfbmV3c2xldHRlcmAgwrcgMS4=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (AutoParts) — Talk to an Expert, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-lkaloss0 {
        --papathemes-ai-widget-lkaloss0-white: #ffffff;
        --papathemes-ai-widget-lkaloss0-cream: #f8fafc;
        --papathemes-ai-widget-lkaloss0-bark-200: #cbd5e1;
        --papathemes-ai-widget-lkaloss0-bark-300: #cbd5e1;
        --papathemes-ai-widget-lkaloss0-bark-400: #94a3b8;
        --papathemes-ai-widget-lkaloss0-bark-700: #334155;
        --papathemes-ai-widget-lkaloss0-bark-800: #1e293b;
        --papathemes-ai-widget-lkaloss0-bark-900: #0f172a;
        --papathemes-ai-widget-lkaloss0-bark-950: #060912;
        --papathemes-ai-widget-lkaloss0-terra: #d97706;
        --papathemes-ai-widget-lkaloss0-terra-dark: #b45309;
        --papathemes-ai-widget-lkaloss0-terra-light: #f59e0b;
        --papathemes-ai-widget-lkaloss0-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-lkaloss0-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-lkaloss0 *,
    .papathemes-ai-widget-lkaloss0 *::before,
    .papathemes-ai-widget-lkaloss0 *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-lkaloss0-bar {
        margin: 32px 20px 0;
        background:
            linear-gradient(135deg, var(--papathemes-ai-widget-lkaloss0-bark-900) 0%, var(--papathemes-ai-widget-lkaloss0-bark-800) 100%);
        border: 1px solid rgba(255, 255, 255, 0.06);
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.04) inset, 0 12px 36px rgba(2, 6, 18, 0.35);
        border-radius: 14px;
        padding: 30px 36px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 28px;
        position: relative;
        overflow: hidden;
    }
    
    .papathemes-ai-widget-lkaloss0-bar::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse 60% 90% at 92% 50%, rgba(217, 119, 6, 0.18), transparent 70%),
            radial-gradient(ellipse 40% 60% at 0% 0%, rgba(255, 255, 255, 0.04), transparent 60%);
        pointer-events: none;
    }
    
    .papathemes-ai-widget-lkaloss0-bar::after {
        content: "";
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
        background-size: 40px 40px;
        opacity: 0.5;
        pointer-events: none;
    }
    
    .papathemes-ai-widget-lkaloss0-left {
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-lkaloss0-heading {
        font-family: var(--papathemes-ai-widget-lkaloss0-font-heading);
        font-size: 17px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-lkaloss0-white);
        margin-bottom: 6px;
        letter-spacing: -0.01em;
    }
    
    .papathemes-ai-widget-lkaloss0-heading em {
        font-style: italic;
        font-weight: 400;
        // Hardcoded warm gold accent — universal premium signal, decoupled from
        // per-store terra-light (renders blue on Electronics #60a5fa).
        color: #fbbf24;
    }
    
    .papathemes-ai-widget-lkaloss0-desc {
        font-family: var(--papathemes-ai-widget-lkaloss0-font-body);
        font-size: 13px;
        line-height: 1.55;
        color: var(--papathemes-ai-widget-lkaloss0-bark-300);
        max-width: 60ch;
    }
    
    .papathemes-ai-widget-lkaloss0-btns {
        display: flex;
        gap: 10px;
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-lkaloss0-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 12px 24px;
        border-radius: 8px;
        font-family: var(--papathemes-ai-widget-lkaloss0-font-heading);
        font-size: 13px;
        font-weight: 600;
        text-decoration: none;
        transition: all .25s cubic-bezier(.16, 1, .3, 1);
        letter-spacing: 0.01em;
        border: none;
        cursor: pointer;
    }
    
    .papathemes-ai-widget-lkaloss0-btn svg {
        width: 15px;
        height: 15px;
        transition: transform .3s;
    }
    
    .papathemes-ai-widget-lkaloss0-btn--terra {
        background: var(--papathemes-ai-widget-lkaloss0-terra);
        color: var(--papathemes-ai-widget-lkaloss0-white);
    }
    
    .papathemes-ai-widget-lkaloss0-btn--terra:hover {
        background: var(--papathemes-ai-widget-lkaloss0-terra-dark);
        color: var(--papathemes-ai-widget-lkaloss0-white);
        box-shadow: 0 6px 24px rgba(217, 119, 6, .35);
        transform: translateY(-1px);
        text-decoration: none;
    }
    
    .papathemes-ai-widget-lkaloss0-btn--terra:hover svg {
        transform: translateX(3px);
    }
    
    .papathemes-ai-widget-lkaloss0-btn--ghost {
        border: 1px solid rgba(255, 255, 255, 0.22);
        color: var(--papathemes-ai-widget-lkaloss0-white);
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(8px);
    }
    
    .papathemes-ai-widget-lkaloss0-btn--ghost:hover {
        border-color: rgba(255, 255, 255, 0.45);
        color: var(--papathemes-ai-widget-lkaloss0-white);
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-1px);
        text-decoration: none;
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-lkaloss0-bar {
            margin-left: 10px;
            margin-right: 10px;
            flex-direction: column;
            text-align: center;
            padding: 28px 24px;
        }
    
        .papathemes-ai-widget-lkaloss0-btns {
            flex-direction: column;
            width: 100%;
        }
    
        .papathemes-ai-widget-lkaloss0-btn {
            justify-content: center;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-lkaloss0">
        <div class="papathemes-ai-widget-lkaloss0-bar">
            <div class="papathemes-ai-widget-lkaloss0-left">
                <h3 class="papathemes-ai-widget-lkaloss0-heading">Need help finding the right part? <em>Talk to an Auto Parts Specialist</em></h3>
                <p class="papathemes-ai-widget-lkaloss0-desc">Our specialists verify fitment by year, make, model, and VIN so you order right the first time. Call or chat anytime.</p>
            </div>
            <div class="papathemes-ai-widget-lkaloss0-btns">
                <a href="/contact-us/" class="papathemes-ai-widget-lkaloss0-btn papathemes-ai-widget-lkaloss0-btn--terra">
                    Request a Quote
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
                </a>
                <a href="tel:18005550123" class="papathemes-ai-widget-lkaloss0-btn papathemes-ai-widget-lkaloss0-btn--ghost">
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                    (800) 555-0123
                </a>
            </div>
        </div>
    </div>
    ```
### 20. Footer tagline — marketing block (Page Builder)

The footer carries a small tagline widget (this demo: *"eShopping Autoparts Demo — OEM & aftermarket auto parts for every make and model."*). It lives in a **global** region, so it shows on every page. Also an **AI HTML Generator | PapaThemes** widget.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBmb290ZXIgdGFnbGluZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZCDihpIgKipTYXZlKiouIFNlZSBbRm9vdGVyIHRhZ2xpbmVdKHdpZGdldHMtcGFwYXRoZW1lcy5tZCNmb290ZXItdGFnbGluZSkgZm9yIHRoZSBleGFjdCBIVE1MLiBSZWdpb246IGBlc2hvcHBpbmdfZm9vdGVyX2Rlc2NyaXB0aW9uLS1nbG9iYWxgIChwbGFjZWQgb24gZXZlcnkgcGFnZSku-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (AutoParts) — Footer tagline, paste into the widget's HTML Content field"

    ```html
    <span class="eshopping-footer-desc-text">eShopping Autoparts Demo — OEM & aftermarket auto parts for every make and model.</span>
    ```
!!! note "Five home widgets + footer tagline"
    The AutoParts demo home page has **five** content blocks built with the **AI HTML Generator | PapaThemes** widget (Why Choose Us, Customer Reviews, Resources, About, Talk to an Expert), plus a **sixth** widget for the footer tagline. They require the PapaThemes app and arrive with the demo widget import, not the theme settings. See the [PapaThemes marketing blocks reference](widgets-papathemes.md) for the full set.

## Beyond the home page

These AutoParts settings drive other pages and on-site widgets. The promo card, cart goals, and PDP text below are set by the **variation**; Frequently Bought Together, cross-sell, urgency signals, and pop-ups are **theme defaults** (the same in every variation) and active out of the box.

### Sidebar promo card

- **Text:** Free Shipping $250+ — Free ground shipping on qualifying parts orders.
- **Button:** Shop Parts → `/shipping/`

This is the sidebar promo card (shown on category, brand, and search pages), not the top banner.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNpZGViYXIgUHJvbW8gQ2FyZCog4oaSICoqU2lkZWJhciBQcm9tbyBUZXh0KiogKGlkIGBlc2hvcHBpbmctcHJvbW8tdGV4dGApLiBGb3JtYXQ6IGBIZWFkaW5nfFN1YnRleHR8QnV0dG9uIGxhYmVsfEJ1dHRvbiBVUkxgLCBzcGxpdCBvbiBgfGAgKDQgc2VnbWVudHMpLiBEZWZhdWx0IChBdXRvUGFydHMpOiBgRnJlZSBTaGlwcGluZyAkMjUwK3xGcmVlIGdyb3VuZCBzaGlwcGluZyBvbiBxdWFsaWZ5aW5nIHBhcnRzIG9yZGVycy58U2hvcCBQYXJ0c3wvc2hpcHBpbmcvYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Sidebar Promo Card</div><div class="te-mock__row"><span class="te-lbl">Sidebar Promo Text</span><span class="te-tx">Free Shipping $250+|Free ground ship…</span></div></div>

### Cart free-shipping / reward goals

Progress goals shown in the cart drawer:

| Threshold | Reward |
| --------- | ------ |
| $50 | Free Shipping |
| $100 | 10% Off |
| $200 | Free Gift |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENhcnQgR29hbCBCYXIqIOKGkiAqKkdvYWwgaXRlbXMgKGFtb3VudHxpY29ufGxhYmVsLCBjb21tYS1zZXBhcmF0ZWQpKiogKGlkIGBlc2hvcHBpbmctY2FydC1nb2FsLWl0ZW1zYCkuIEZvcm1hdDogYSAqKmNvbW1hLXNlcGFyYXRlZCoqIGxpc3Qgb2YgZ29hbHM7IGVhY2ggZ29hbCBpcyBgYW1vdW50fGljb258bGFiZWxgICh0aGUgaWNvbiBpcyBvbmUgb2YgYHNoaXBwaW5nYCwgYGRpc2NvdW50YCwgYGdpZnRgKS4gRGVmYXVsdCAoQXV0b1BhcnRzKTogYDUwfHNoaXBwaW5nfEZyZWUgU2hpcHBpbmcsMTAwfGRpc2NvdW50fDEwJSBPZmYsMjAwfGdpZnR8RnJlZSBHaWZ0YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Cart Goal Bar</div><div class="te-mock__row"><span class="te-lbl">Goal items (amount|icon|label, comma-separated)</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">comma-separated</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### Cart cross-sell ("You May Also Like")

A "You May Also Like" cross-sell block appears in the cart: up to **6** items on the full cart page and up to **4** items in the slide-out cart drawer.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENhcnQgQ3Jvc3Mtc2VsbCog4oaSICoqQ3Jvc3Mtc2VsbCBwcm9kdWN0cyAocGFnZSxkcmF3ZXIg4oCUIDAgPSBvZmYpKiogKGlkIGBlc2hvcHBpbmctY3Jvc3NzZWxsLWNvdW50YCkuIEZvcm1hdDogdHdvIGNvbW1hLXNlcGFyYXRlZCBudW1iZXJzIGBwYWdlLGRyYXdlcmAgKHNldCBlaXRoZXIgdG8gYDBgIHRvIGhpZGUgdGhhdCBwbGFjZW1lbnQpLiBEZWZhdWx0OiBgNiw0YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Cart Cross-sell</div><div class="te-mock__row"><span class="te-lbl">Cross-sell products (page,drawer — 0 = off)</span><span class="te-tx">6,4</span></div></div>

### Product page (PDP)

Shipping / warranty strip:

| Title | Detail |
| ----- | ------ |
| Free Shipping | on parts orders over $250 |
| Fitment Guarantee | verified compatibility |
| 30-Day Returns | no-hassle policy |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb2R1Y3QgUGFnZSAoUERQKSog4oaSICoqUERQIFNoaXBwaW5nIFRleHQqKiAoaWQgYGVzaG9wcGluZy1wZHAtc2hpcHBpbmctdGV4dGApLiBGb3JtYXQ6IGBUaXRsZXxEZXRhaWxgIHBhaXJzIHNwbGl0IG9uIGB8YCDigJQgMyBwYWlycyA9IDYgc2VnbWVudHMgaW4gb3JkZXIgYFRpdGxlMXxEZXRhaWwxfFRpdGxlMnxEZXRhaWwyfFRpdGxlM3xEZXRhaWwzYC4gRGVmYXVsdCAoQXV0b1BhcnRzKTogYEZyZWUgU2hpcHBpbmd8b24gcGFydHMgb3JkZXJzIG92ZXIgJDI1MHxGaXRtZW50IEd1YXJhbnRlZXx2ZXJpZmllZCBjb21wYXRpYmlsaXR5fDMwLURheSBSZXR1cm5zfG5vLWhhc3NsZSBwb2xpY3lgLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Product Page (PDP)</div><div class="te-mock__row"><span class="te-lbl">PDP Shipping Text</span><span class="te-tx">Free Shipping|on parts orders over $…</span></div></div>

Warranty accordion (4-card grid):

| Section | Content |
| ------- | ------- |
| What's Covered | Manufacturing defects, material failures, and premature wear under normal vehicle use. |
| What's Not Covered | Damage from improper installation, racing, off-road abuse, or normal wear items. |
| How to Claim | Contact us with your order number and part details for quick resolution. |
| Extended Warranty | Upgrade to our extended coverage plan for added peace of mind. |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb2R1Y3QgUGFnZSAoUERQKSog4oaSICoqUERQIFdhcnJhbnR5IFRleHQqKiAoaWQgYGVzaG9wcGluZy1wZHAtd2FycmFudHktdGV4dGApLiBGb3JtYXQ6IGBTZWN0aW9ufENvbnRlbnRgIHBhaXJzIHNwbGl0IG9uIGB8YCDigJQgdGhlIGRlbW8gdXNlcyA0IHBhaXJzID0gOCBzZWdtZW50cy4gRGVmYXVsdCAoQXV0b1BhcnRzKTogYFdoYXQncyBDb3ZlcmVkfOKApnxXaGF0J3MgTm90IENvdmVyZWR84oCmfEhvdyB0byBDbGFpbXzigKZ8RXh0ZW5kZWQgV2FycmFudHl84oCmYC4gKEFsc286ICoqU2hvdyBGQVEgVGFiKiosIGlkIGBlc2hvcHBpbmctcGRwLXNob3ctZmFxLXRhYmAsIGFuZCAqKlNob3cgTW9iaWxlIFN0aWNreSBBZGQgdG8gQ2FydCoqLCBpZCBgZXNob3BwaW5nLXBkcC1zaG93LW1vYmlsZS1hdGNgLCBib3RoIG9uL29mZi4p-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Product Page (PDP)</div><div class="te-mock__row"><span class="te-lbl">PDP Warranty Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show FAQ Tab</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show Mobile Sticky Add to Cart</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

**Frequently Bought Together:** shows `2` products, discount `0%`.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEZyZXF1ZW50bHkgQm91Z2h0IFRvZ2V0aGVyKiDihpIgKipGQlQgUHJvZHVjdHMgQ291bnQqKiAoaWQgYGVzaG9wcGluZy1mYnQtY291bnRgLCBzZWxlY3QgYDBgL2AxYC9gMmAvYDNgOyBgMGAgPSBvZmY7IGRlZmF1bHQgYDJgKSBhbmQgKipWaXN1YWwgQnVuZGxlIERpc2NvdW50ICUqKiAoaWQgYGVzaG9wcGluZy1mYnQtZGlzY291bnQtcGVyY2VudGAsIGEgbnVtYmVyIHVzZWQgZm9yIGEgKmRpc3BsYXktb25seSogYnVuZGxlIGRpc2NvdW50OyBkZWZhdWx0IGAwYCkuIEZvcm1hdDogc2VsZWN0ICsgbnVtYmVyLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Frequently Bought Toget…</div><div class="te-mock__row"><span class="te-lbl">FBT Products Count</span><span class="te-dd"><span class="te-dd__v">2</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Visual Bundle Discount %</span><span class="te-dd"><span class="te-dd__v">0</span><span class="te-dd__b">▾</span></span></div></div>

### Urgency & social proof

- **Live view count** and **last order time** are both on.
- **Recent sales pop-ups** show on **all pages**, cycling through demo sales from California, Texas, Florida, New York, and Oregon.

!!! note "Where these appear & how the numbers are generated"
    The "people viewing" and "last ordered" signals render on **product pages**, not the home page. The figures are **simulated from configured ranges** (viewer counts and last-order hours) — not real-time analytics.

<!--te-src:PiAqKkN1c3RvbWl6ZSAodXJnZW5jeSk6KiogVGhlbWUgRWRpdG9yIOKGkiAqZVNob3BwaW5nIFRoZW1lIOKGkiBVcmdlbmN5IFNpZ25hbHMgKFNvY2lhbCBQcm9vZikqIOKGkiAqKlNob3cgbGl2ZSB2aWV3IGNvdW50KiogKGlkIGBlc2hvcHBpbmctdXJnZW5jeS12aWV3LWNvdW50YCwgZGVmYXVsdCBgT25gKSBhbmQgKipTaG93IGxhc3Qgb3JkZXIgdGltZSoqIChpZCBgZXNob3BwaW5nLXVyZ2VuY3ktbGFzdC1vcmRlcmAsIGRlZmF1bHQgYE9uYCkuIFRoZSByYW5nZXMgYXJlICoqRmFrZSB2aWV3IGNvdW50IHJhbmdlOiBtaW4sbWF4KiogKGlkIGBlc2hvcHBpbmctdXJnZW5jeS12aWV3LXJhbmdlYCwgZGVmYXVsdCBgMywyNWApIGFuZCAqKkxhc3Qgb3JkZXIgdGltZSByYW5nZTogbWluLG1heCBob3VycyBhZ28qKiAoaWQgYGVzaG9wcGluZy11cmdlbmN5LW9yZGVyLXJhbmdlYCwgZGVmYXVsdCBgMSw0OGApLiBGb3JtYXQ6IG9uL29mZiArIGBtaW4sbWF4YCBudW1iZXIgcGFpcnMu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAocmVjZW50IHNhbGVzIHBvcC11cHMpOioqIFRoZW1lIEVkaXRvciDihpIgKmVTaG9wcGluZyBUaGVtZSDihpIgUmVjZW50IFNhbGVzIFBvcHVwKiDihpIgKipTaG93IG9uIHBhZ2VzKiogKGlkIGBlc2hvcHBpbmctcmVjZW50LXNhbGVzLXBhZ2VzYCwgc2VsZWN0IGBub25lYC9gYWxsYC9gaG9tZWAvYHByb2R1Y3RgL2BjYXRlZ29yeWA7IGRlZmF1bHQgYGFsbGApLCAqKlBvcHVwIHRpbWluZzogZGVsYXksIHNob3cgZHVyYXRpb24sIHBhdXNlIGJldHdlZW4sIG1heCBwb3B1cHMqKiAoaWQgYGVzaG9wcGluZy1yZWNlbnQtc2FsZXMtdGltaW5nYCwgZGVmYXVsdCBgNSw1LDE1LDVgKSwgYW5kICoqUHJvZHVjdHMgKElEIG9yIFNLVXxsb2NhdGlvbnx0aW1lQWdvLCBjb21tYS1zZXBhcmF0ZWQpKiogKGlkIGBlc2hvcHBpbmctcmVjZW50LXNhbGVzLWl0ZW1zYCkuIEZvcm1hdDogZWFjaCBzYWxlIGlzIGBwcm9kdWN0SUR8bG9jYXRpb258dGltZUFnb2AsIHNhbGVzIGNvbW1hLXNlcGFyYXRlZC4gRGVmYXVsdDogYDc3fENhbGlmb3JuaWF8MiBob3VycyBhZ28sNzh8VGV4YXN8MzUgbWluIGFnbyw3OXxGbG9yaWRhfDQgaG91cnMgYWdvLDgwfE5ldyBZb3JrfDEgaG91ciBhZ28sODF8T3JlZ29ufDYgaG91cnMgYWdvYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Urgency Signals (Social…</div><div class="te-mock__row"><span class="te-lbl">Show live view count</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show last order time</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Fake view count range: min,max</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Last order time range: min,max hours ago</span><span class="te-cb"></span></div><div class="te-mock__grp">Recent Sales Popup</div><div class="te-mock__row"><span class="te-lbl">Show on pages</span><span class="te-tx">all</span></div><div class="te-mock__row"><span class="te-lbl">Popup timing: delay, show duration, pause between, max popups</span><span class="te-tx">5,5,15,5</span></div><div class="te-mock__row"><span class="te-lbl">Products (ID or SKU|location|timeAgo, comma-separated)</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### Pop-ups

**Newsletter pop-up:**

- **Text:** Get 10% Off Your First Order — Sign up for our newsletter and receive an exclusive discount code.
- **Options:** shows after 20 seconds; reappears after 14 days.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIE5ld3NsZXR0ZXIgUG9wdXAqIOKGkiAqKk5ld3NsZXR0ZXIgQ29udGVudCDigJQgVGl0bGV8RGVzY3JpcHRpb24qKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1ubC10ZXh0YDsgbGVhdmUgZW1wdHkgdG8gZGlzYWJsZTsgZm9ybWF0IGBUaXRsZXxEZXNjcmlwdGlvbmApIGFuZCAqKlNob3cgYWZ0ZXIgKHNlY29uZHMpIHwgUmVwZWF0IGV2ZXJ5IChkYXlzKSoqIChpZCBgZXNob3BwaW5nLXBvcHVwLW5sLW9wdHNgOyBmb3JtYXQgYHNlY29uZHN8ZGF5c2ApLiBEZWZhdWx0OiBgR2V0IDEwJSBPZmYgWW91ciBGaXJzdCBPcmRlcnxTaWduIHVwIGZvciBvdXIgbmV3c2xldHRlciBhbmQgcmVjZWl2ZSBhbiBleGNsdXNpdmUgZGlzY291bnQgY29kZS5gIGFuZCBgMjB8MTRgLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Newsletter Popup</div><div class="te-mock__row"><span class="te-lbl">Newsletter Content — Title|Description</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show after (seconds) | Repeat every (days)</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

**Promo pop-up:**

- **Heading:** Spring Sale
- **Body:** Get 15% off your entire order with the code below.
- **Code:** `SPRING15`
- **Button:** Shop Now → `/`
- **Options:** shows after 5 seconds; reappears after 3 days.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb21vdGlvbiBQb3B1cCog4oaSICoqUHJvbW8gQ29udGVudCDigJQgVGl0bGV8RGVzY3JpcHRpb258Q291cG9uIENvZGV8QnV0dG9uIFRleHR8QnV0dG9uIFVSTCoqIChpZCBgZXNob3BwaW5nLXBvcHVwLXByb21vLXRleHRgOyBsZWF2ZSBlbXB0eSB0byBkaXNhYmxlKSBhbmQgKipTaG93IGFmdGVyIChzZWNvbmRzKSB8IFJlcGVhdCBldmVyeSAoZGF5cykgfCBTdGFydCBkYXRlIHwgRW5kIGRhdGUqKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1wcm9tby1vcHRzYCkuIERlZmF1bHQ6IGBTcHJpbmcgU2FsZXxHZXQgMTUlIG9mZiB5b3VyIGVudGlyZSBvcmRlciB3aXRoIHRoZSBjb2RlIGJlbG93LnxTUFJJTkcxNXxTaG9wIE5vd3wvYCBhbmQgYDV8M3x8YCAobm8gZGF0ZSBsaW1pdHMpLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Promotion Popup</div><div class="te-mock__row"><span class="te-lbl">Promo Content — Title|Description|Coupon Code|Button Text|Button URL</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show after (seconds) | Repeat every (days) | Start date | End date</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

**Exit-intent pop-up:**

- **Heading:** Wait! Don't Go Empty-Handed
- **Body:** Here's a special 10% discount just for you.
- **Code:** `STAY10`
- **Button:** Claim Discount → `/`
- **Options:** discount type. On desktop it triggers when the cursor leaves the top of the window; on mobile after 45 seconds of inactivity. It reappears at most once per day.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEV4aXQgSW50ZW50IFBvcHVwKiDihpIgKipFeGl0IENvbnRlbnQg4oCUIFRpdGxlfERlc2NyaXB0aW9ufENvdXBvbiBDb2RlfEJ1dHRvbiBUZXh0fEJ1dHRvbiBVUkwqKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1leGl0LXRleHRgOyBsZWF2ZSBlbXB0eSB0byBkaXNhYmxlKSBhbmQgKipUeXBlIChkaXNjb3VudC9uZXdzbGV0dGVyL2N1c3RvbSkgfCBNb2JpbGUgdGltZW91dCAoc2Vjb25kcykgfCBSZXBlYXQgZXZlcnkgKGRheXMpKiogKGlkIGBlc2hvcHBpbmctcG9wdXAtZXhpdC1vcHRzYCkuIERlZmF1bHQ6IGBXYWl0ISBEb24ndCBHbyBFbXB0eS1IYW5kZWR8SGVyZSdzIGEgc3BlY2lhbCAxMCUgZGlzY291bnQganVzdCBmb3IgeW91LnxTVEFZMTB8Q2xhaW0gRGlzY291bnR8L2AgYW5kIGBkaXNjb3VudHw0NXwxYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Exit Intent Popup</div><div class="te-mock__row"><span class="te-lbl">Exit Content — Title|Description|Coupon Code|Button Text|Button URL</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Type (discount/newsletter/custom) | Mobile timeout (seconds) | Repeat every (days)</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

---

## Final check

Click **Save → Publish**. Open the storefront in a private browser window. Compare to <https://eshopping-autoparts-demo.mybigcommerce.com>.

---

## Next

- [Product page](product.md)
- [Category page](category.md)
- [Electronics →](home-electronics.md)
