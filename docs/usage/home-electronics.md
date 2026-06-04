# Home Page — Electronics Variant

Live demo: <https://eshopping-electronics-demo.mybigcommerce.com>

![Electronics home page composed view](../img/home-electronics-composed.png){ loading=lazy }

!!! note "Before you start"
    Theme installed, **Electronics** variation picked, **Electronics** product + widget data imported.

The Electronics variation **already populates** most settings (colors, fonts, trust strip, newsletter, promo, cart goal, PDP shipping). Recipe below shows what's set automatically + what to override — and, for every section, **how to change it yourself**.

!!! info "What actually renders on the live home page"
    In order, top to bottom: **Hero carousel** → **Trust strip** → **Featured Products** → **New Arrivals** → **Products by Category** → **Why Choose Us** (AI HTML Generator) → **Customer Reviews** (AI HTML Generator) → **Resources** (AI HTML Generator) → **Brands carousel** → **Blog posts** → **Newsletter** → **About** (AI HTML Generator) → **Talk to an Expert** (AI HTML Generator) → footer (with **Footer tagline** widget).

    The **five** home AI HTML Generator widgets (Why Choose Us, Customer Reviews, Resources, About, Talk to an Expert) plus the **Footer tagline** widget are placed via Page Builder by the demo widget import — they are **not** theme settings, and require the **PapaThemes** app to be installed. See [Demo marketing blocks](widgets-papathemes.md) for what each one is and its exact HTML.

!!! info "Where settings live in the Theme Editor"
    Storefront → **My Themes** → **Customize**. Almost every eShopping setting below sits in one flat panel: **Theme Editor → eShopping Theme**. The carousel toggle is under **Theme Editor → Homepage**; the body/heading fonts are under **Theme Editor → Global**. Most toggles set `force_reload`, so the preview reloads when you change them.

## Section-by-section recipe

### 1. Variation

Theme Editor → **Electronics**.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqVmFyaWF0aW9ucyoqIGRyb3Bkb3duICh0b3Agb2YgdGhlIHBhbmVsKSDihpIgcGljayBhIHZhcmlhdGlvbi4gU3dpdGNoaW5nIHZhcmlhdGlvbnMgcmUtYXBwbGllcyB0aGF0IHZhcmlhdGlvbidzIGJ1bmRsZWQgY29sb3JzLCBmb250cywgYW5kIGNvcHkuIChOb3QgYSBzaW5nbGUgZmllbGQg4oCUIGl0IGlzIHRoZSB2YXJpYXRpb24gc2VsZWN0b3IgaXRzZWxmLik=-->
<!--te-mock--><div class="te-mock te-mock--styles"><div class="te-mock__hd"><span>Styles</span><span class="te-x">✕</span></div><div class="te-mock__grp">Theme variation</div><div class="te-mock__row"><span class="te-lbl">Industrial</span></div><div class="te-mock__row"><span class="te-lbl">AutoParts</span></div><div class="te-mock__row"><span class="te-lbl">Electronics</span><span class="te-check">✓</span></div><div class="te-mock__row"><span class="te-lbl">Packaging</span></div></div>

### 2. Colors — set automatically

The Electronics variation applies these colors for you:

<!--te-tbl:fCBDb2xvciB8IFRoZW1lIEVkaXRvciBmaWVsZCAoZVNob3BwaW5nIFRoZW1lKSB8IFZhbHVlIHwKfCAtLS0tLSB8IC0tLS0tIHwgLS0tLS0gfAp8IFByaW1hcnkgYWNjZW50IHwgKipUZXJyYSoqIChgZXNob3BwaW5nLWNvbG9yLXRlcnJhYCkgfCBgIzNiODJmNmAgKGVsZWN0cmljIGJsdWUpIHwKfCBQcmltYXJ5IGFjY2VudCAoZGFyaykgfCAqKlRlcnJhIChkYXJrKSoqIChgZXNob3BwaW5nLWNvbG9yLXRlcnJhLWRhcmtgKSB8IGAjMjU2M2ViYCB8CnwgUHJpbWFyeSBhY2NlbnQgKGxpZ2h0KSB8ICoqVGVycmEgKGxpZ2h0KSoqIChgZXNob3BwaW5nLWNvbG9yLXRlcnJhLWxpZ2h0YCkgfCBgIzYwYTVmYWAgfAp8IFByaW1hcnkgYWNjZW50IChwYWxlKSB8ICoqVGVycmEgKHBhbGUpKiogKGBlc2hvcHBpbmctY29sb3ItdGVycmEtcGFsZWApIHwgYCNlZmY2ZmZgIHwKfCBEYXJrZXN0IG5ldXRyYWwgfCBgZXNob3BwaW5nLWNvbG9yLWJhcmstOTUwYCB8IGAjMDkwOTBiYCAoemluYykgfAp8IERhcmsgbmV1dHJhbCB8IGBlc2hvcHBpbmctY29sb3ItYmFyay05MDBgIHwgYCMxODE4MWJgIHwKfCBMaWdodCBuZXV0cmFsIHwgYGVzaG9wcGluZy1jb2xvci1iYXJrLTUwYCB8IGAjZmFmYWZhYCB8CnwgQ3JlYW0gfCBgZXNob3BwaW5nLWNvbG9yLWNyZWFtYCB8IGAjZmFmYWZhYCB8CnwgU2FsZSBiYWRnZSBiYWNrZ3JvdW5kIHwgYGVzaG9wcGluZy1iYWRnZS1zYWxlLWJnYCB8IGAjZGMyNjI2YCB8CnwgU3RhZmYgcGljayBiYWRnZSBiYWNrZ3JvdW5kIHwgYGVzaG9wcGluZy1iYWRnZS1zdGFmZi1iZ2AgfCBgI2Q5NzcwNmAgfAp8IEFjdGl2ZSByYXRpbmcgc3RhciB8IGBlc2hvcHBpbmctcmF0aW5nLXN0YXItYWN0aXZlYCB8IGAjZjU5ZTBiYCB8CnwgU2FsZSBwcmljZSB8IGBlc2hvcHBpbmctcHJpY2Utc2FsZWAgfCBgI2RjMjYyNmAgfAp8IE9yaWdpbmFsIChzdHJ1Y2stdGhyb3VnaCkgcHJpY2UgfCBgZXNob3BwaW5nLXByaWNlLW9yaWdpbmFsYCB8IGAjOTRhM2I4YCB8-->

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSIHRoZSBjb2xvciBzd2F0Y2hlcyAoZS5nLiAqKlRlcnJhKiosIGBlc2hvcHBpbmctY29sb3ItdGVycmFgKSDigJQgZWFjaCBvcGVucyBhIGNvbG9yIHBpY2tlci4gRm9ybWF0OiBoZXgvcmdiL2hzbC4gVGhlbWUgZGVmYXVsdCAoZ2VuZXJpYywgbm9uLWVsZWN0cm9uaWNzKTogYCNiZjViMzNgLiBUaGUgRWxlY3Ryb25pY3MgdmFyaWF0aW9uIG92ZXJyaWRlcyBpdCB0byBgIzNiODJmNmAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Terra</span><span class="te-color"><span class="te-hex">#3B82F6</span><span class="te-sw" style="background:#3b82f6"></span></span></div><div class="te-mock__row"><span class="te-lbl">Terra (dark)</span><span class="te-color"><span class="te-hex">#2563EB</span><span class="te-sw" style="background:#2563eb"></span></span></div><div class="te-mock__row"><span class="te-lbl">Terra (light)</span><span class="te-color"><span class="te-hex">#60A5FA</span><span class="te-sw" style="background:#60a5fa"></span></span></div><div class="te-mock__row"><span class="te-lbl">Terra (pale)</span><span class="te-color"><span class="te-hex">#EFF6FF</span><span class="te-sw" style="background:#eff6ff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Darkest neutral</span><span class="te-color"><span class="te-hex">#09090B</span><span class="te-sw" style="background:#09090b"></span></span></div><div class="te-mock__row"><span class="te-lbl">Dark neutral</span><span class="te-color"><span class="te-hex">#18181B</span><span class="te-sw" style="background:#18181b"></span></span></div><div class="te-mock__row"><span class="te-lbl">Light neutral</span><span class="te-color"><span class="te-hex">#FAFAFA</span><span class="te-sw" style="background:#fafafa"></span></span></div><div class="te-mock__row"><span class="te-lbl">Cream</span><span class="te-color"><span class="te-hex">#FAFAFA</span><span class="te-sw" style="background:#fafafa"></span></span></div><div class="te-mock__row"><span class="te-lbl">Sale badge background</span><span class="te-color"><span class="te-hex">#DC2626</span><span class="te-sw" style="background:#dc2626"></span></span></div><div class="te-mock__row"><span class="te-lbl">Staff pick badge background</span><span class="te-color"><span class="te-hex">#D97706</span><span class="te-sw" style="background:#d97706"></span></span></div><div class="te-mock__row"><span class="te-lbl">Active rating star</span><span class="te-color"><span class="te-hex">#F59E0B</span><span class="te-sw" style="background:#f59e0b"></span></span></div><div class="te-mock__row"><span class="te-lbl">Sale price</span><span class="te-color"><span class="te-hex">#DC2626</span><span class="te-sw" style="background:#dc2626"></span></span></div><div class="te-mock__row"><span class="te-lbl">Original (struck-through) price</span><span class="te-color"><span class="te-hex">#94A3B8</span><span class="te-sw" style="background:#94a3b8"></span></span></div></div>

### 3. Fonts — set automatically

| Font | Theme Editor field | Value |
| ---- | ----- | ----- |
| Body font | **Body text font family** (`body-font`, under *Global*) | Inter (weights 400, 500, 600) |
| Headings font | **Heading font family** (`headings-font`, under *Global*) | Space Grotesk (weights 500, 700) |
| Mono font | **Monospace Font** (`eshopping-mono-font`, under *eShopping Theme*) | IBM Plex Mono (weight 400) |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqR2xvYmFsKiog4oaSICoqQm9keSB0ZXh0IGZvbnQgZmFtaWx5KiogLyAqKkhlYWRpbmcgZm9udCBmYW1pbHkqKiwgYW5kIFRoZW1lIEVkaXRvciDihpIgKiplU2hvcHBpbmcgVGhlbWUqKiDihpIgKipNb25vc3BhY2UgRm9udCoqLiBGb3JtYXQ6IHBpY2sgZnJvbSB0aGUgZm9udCBkcm9wZG93biAoR29vZ2xlL3dlYi1zYWZlIGZhbWlsaWVzKS4gVGhlbWUgZGVmYXVsdHM6IGJvZHkgYFNvdXJjZSBTYW5zIDNgLCBoZWFkaW5ncyBgUGxheWZhaXIgRGlzcGxheWAsIG1vbm8gYElCTSBQbGV4IE1vbm9gLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Global</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Body text font family</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Heading font family</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Monospace Font</span><span class="te-desc">Theme Editor field</span></span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>

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

<!--te-tbl:fCBCYW5uZXIgY29sb3IgfCBUaGVtZSBFZGl0b3IgZmllbGQgfCBWYWx1ZSB8CnwgLS0tLS0tLS0tLS0tIHwgLS0tLS0gfCAtLS0tLSB8CnwgQmFubmVyIGJhY2tncm91bmQgfCBgZXNob3BwaW5nLWJhbm5lci1iZ2AgfCBgIzNmM2Y0NmAgfAp8IEJhbm5lciB0ZXh0IHwgYGVzaG9wcGluZy1iYW5uZXItY29sb3JgIHwgYCNkNGQ0ZDhgIHwKfCBCYW5uZXIgbGluayB8IGBlc2hvcHBpbmctYmFubmVyLWxpbmtgIHwgYCM2MGE1ZmFgIHw=-->

<!--te-src:PiAqKkN1c3RvbWl6ZSAoY29udGVudCk6KiogQmlnQ29tbWVyY2UgYWRtaW4g4oaSICoqTWFya2V0aW5nIOKGkiBCYW5uZXJzKiog4oaSIGNyZWF0ZS9lZGl0IGEgYmFubmVyIGZvciAqSG9tZSBQYWdlKiBsb2NhdGlvbi4gKE5vdCBhIHRoZW1lIHNldHRpbmcg4oCUIHRoZSBiYW5uZXIgSFRNTCBsaXZlcyBpbiBCQywgbm90IHRoZSBUaGVtZSBFZGl0b3IuKQ==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY29sb3JzKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSIHRoZSBiYW5uZXIgY29sb3Igc3dhdGNoZXMgKGBlc2hvcHBpbmctYmFubmVyLWJnYCwgYGVzaG9wcGluZy1iYW5uZXItY29sb3JgLCBgZXNob3BwaW5nLWJhbm5lci1saW5rYCkuIEZvcm1hdDogaGV4L3JnYi9oc2wu-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Marketing</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub is-active">Banners</div><div class="te-nav__sub">Coupon codes</div><div class="te-nav__sub">Gift certificates</div><div class="te-nav__sub">Abandoned cart saver</div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Banner background</span><span class="te-color"><span class="te-hex">#3F3F46</span><span class="te-sw" style="background:#3f3f46"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner text</span><span class="te-color"><span class="te-hex">#D4D4D8</span><span class="te-sw" style="background:#d4d4d8"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner link</span><span class="te-color"><span class="te-hex">#60A5FA</span><span class="te-sw" style="background:#60a5fa"></span></span></div></div>

### 5. Header

| Setting | Theme Editor field (eShopping Theme) | Value |
| ------- | ----- | ----- |
| Top bar background | `eshopping-topbar-bg` | `#09090b` |
| Top bar text | `eshopping-topbar-color` | `#a1a1aa` |
| Nav background | `eshopping-nav-bg` | `#ffffff` |
| Nav text | `eshopping-nav-color` | `#52525b` |
| Nav search button | `eshopping-nav-search-btn` | `#3b82f6` |
| Search typing phrases | **Typing phrases (pipe \| separated)** (`eshopping-search-typing-phrases`) | `Search for laptops & monitors...`, `Find headphones & speakers...`, `Browse keyboards & mice...`, `Discover cables & adapters...` |
| Voice search | **Enable voice search** (`eshopping-search-voice`) | On |
| Welcome text | **Welcome Text** (`eshopping-welcome-text`) | (empty in the demo) |

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2VhcmNoIHBsYWNlaG9sZGVyIHBocmFzZXMpOioqIFRoZW1lIEVkaXRvciDihpIgKiplU2hvcHBpbmcgVGhlbWUqKiDihpIgKipUeXBpbmcgcGhyYXNlcyAocGlwZSB8IHNlcGFyYXRlZCkqKi4gRm9ybWF0OiBhIHNpbmdsZSBzdHJpbmcgb2YgcGhyYXNlcyBzZXBhcmF0ZWQgYnkgYHxgOyB0aGUgc2VhcmNoIGJveCBjeWNsZXMgdGhyb3VnaCB0aGVtLiBUaGVtZSBkZWZhdWx0OiBgU2VhcmNoIGZvciBwb3dlciB0b29scy4uLnxGaW5kIHdlbGRpbmcgZXF1aXBtZW50Li4ufEJyb3dzZSBzYWZldHkgZ2Vhci4uLnxEaXNjb3ZlciBjb21wcmVzc29ycyAmIGFjY2Vzc29yaWVzLi4uYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodm9pY2Ugc2VhcmNoKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqRW5hYmxlIHZvaWNlIHNlYXJjaCoqIChjaGVja2JveCkuIERlZmF1bHQ6IG9uLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2VsY29tZSB0ZXh0KToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqV2VsY29tZSBUZXh0KiouIEZvcm1hdDogcGxhaW4gdGV4dCBzaG93biBpbiB0aGUgdG9wIGJhci4gRGVmYXVsdDogZW1wdHku-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY29sb3JzKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSIHRoZSB0b3AtYmFyL25hdiBjb2xvciBzd2F0Y2hlcyBsaXN0ZWQgYWJvdmUu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Typing phrases (pipe | separated)</span><span class="te-tx">Search for power tools</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Enable voice search</span><span class="te-desc">Enable voice search (eshopping-search-voice)</span></span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Welcome Text</span><span class="te-desc">Welcome Text (eshopping-welcome-text)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">setting</span><span class="te-desc">Theme Editor field (eShopping Theme)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

See [Header & top bar](header-and-topbar.md) for the full header reference.

### 6. Hero carousel

The hero is the BigCommerce **Home Page Carousel** styled by the theme.

![Hero on the storefront](../img/electronics-hero.png){ loading=lazy }

1. **Storefront → Home Page Carousel** → upload 3 slides (1920 × 700).
2. Theme Editor → **Homepage** → turn on **Show carousel** (`homepage_show_carousel`).
3. (Optional) mobile fixed height — BigCommerce carousel setting → `420`.

!!! warning "There is no separate “Show hero” toggle"
    Earlier builds had an `eshopping-show-hero` switch. It has been **removed**. The hero now renders whenever **Show carousel** (`homepage_show_carousel`) is on **and** the BigCommerce Home Page Carousel has at least one slide. If the hero is missing, check those two things — not a hidden hero toggle.

Slide ideas (*suggestions only*):

| Slide | Image | Heading | CTA |
| :---: | ----- | ------- | --- |
| 1 | Gaming laptop hero | Power. Anywhere. | Shop laptops → /laptops |
| 2 | Wireless headphones | Sound that disappears | Shop audio → /audio |
| 3 | 4K monitor stack | Studio-grade displays | Shop monitors → /monitors |

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2xpZGVzKToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipTdG9yZWZyb250IOKGkiBIb21lIFBhZ2UgQ2Fyb3VzZWwqKiDigJQgYWRkL2VkaXQgc2xpZGUgaW1hZ2UsIGhlYWRpbmcsIHRleHQsIGFuZCBidXR0b24gbGluay4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqSG9tZXBhZ2UqKiDihpIgKipTaG93IGNhcm91c2VsKiogKGBob21lcGFnZV9zaG93X2Nhcm91c2VsYCwgY2hlY2tib3gpLiBEZWZhdWx0OiBvbi4gUmVsYXRlZCBjYXJvdXNlbCBvcHRpb25zIChhcnJvd3MsIHBsYXkvcGF1c2UsIHN0cmV0Y2ggaW1hZ2VzKSBhbHNvIGxpdmUgdW5kZXIgKipIb21lcGFnZSoqLg==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub is-active">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Homepage</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show carousel</span><span class="te-cb is-on"></span></div></div>

### 7. Trust strip — variation default

**Show Trust Strip** (`eshopping-show-trust-strip`) is on. The variation fills in four items, each a **title + description pair**:

- **Authorized Dealer** — Genuine products with full manufacturer warranty
- **Free Shipping** — On all orders over $99
- **Easy Returns** — 30-day hassle-free returns
- **Tech Support** — Expert assistance 7 days a week

![Trust strip on the storefront](../img/electronics-trust.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqU2hvdyBUcnVzdCBTdHJpcCoqIChgZXNob3BwaW5nLXNob3ctdHJ1c3Qtc3RyaXBgLCBjaGVja2JveCkuIERlZmF1bHQ6IG9uLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY29udGVudCk6KiogVGhlbWUgRWRpdG9yIOKGkiAqKmVTaG9wcGluZyBUaGVtZSoqIOKGkiAqKlRydXN0IFN0cmlwIEl0ZW1zKiogKGBlc2hvcHBpbmctdHJ1c3QtdGV4dGApLiBGb3JtYXQ6IGEgc2luZ2xlIGB8YC1zZXBhcmF0ZWQgc3RyaW5nIG9mICoqOCBzZWdtZW50cyA9IDQgYFRpdGxlfERlc2NyaXB0aW9uYCBwYWlycyoqIGluIG9yZGVyIChpdGVtIDEgdGl0bGUsIGl0ZW0gMSBkZXNjLCBpdGVtIDIgdGl0bGUsIGl0ZW0gMiBkZXNjLCDigKYpLiBUaGUgZm91ciBpY29ucyAoc2hpZWxkLCB0cnVjaywgc3RhciwgcGhvbmUpIGFyZSBmaXhlZCBieSB0aGUgdGVtcGxhdGUuIFRoZW1lIGRlZmF1bHQ6IGBNYWRlIGluIFVTQXxGYXN0ICYgcmVsaWFibGUgc2hpcHBpbmcgb24gYWxsIG9yZGVyc3xGcmVlIFNoaXBwaW5nfFNob3Agd2l0aCBjb25maWRlbmNlLCBndWFyYW50ZWVkfDQuOCBTdGFyIFJhdGluZ3xFYXN5IHJldHVybnMgd2l0aGluIDMwIGRheXN8RXhwZXJ0IFN1cHBvcnR8QXZhaWxhYmxlIE1vbi1TYXQsIDlhbS02cG1gLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show Trust Strip</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Trust Strip Items</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">8 segments = 4 Title|Description pairs</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### 8. Featured Products

**Show Featured Products** (`eshopping-show-featured`) is on. The Featured Products slider renders on the live home page.

![Featured Products on the storefront](../img/electronics-featured.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqU2hvdyBGZWF0dXJlZCBQcm9kdWN0cyoqIChgZXNob3BwaW5nLXNob3ctZmVhdHVyZWRgLCBjaGVja2JveCkuIERlZmF1bHQ6IG9uLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggcHJvZHVjdHMpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKlByb2R1Y3RzIOKGkiBWaWV3Kiog4oaSIHNldCBwcm9kdWN0cyBhcyAqRmVhdHVyZWQqIChhIHBlci1wcm9kdWN0IHRvZ2dsZSkuIFRoZSBzbGlkZXIgcHVsbHMgdGhlIHN0b3JlJ3MgRmVhdHVyZWQgcHJvZHVjdHMuIChOb3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show Featured Products</span><span class="te-cb is-on"></span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">View</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 9. Bestselling

**Show Best Sellers** (`eshopping-show-bestselling`) is on, but the demo has **no bestseller sales data**, so the bestselling slider does **not** appear on the live home page. It will only show once products have recorded sales.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqU2hvdyBCZXN0IFNlbGxlcnMqKiAoYGVzaG9wcGluZy1zaG93LWJlc3RzZWxsaW5nYCwgY2hlY2tib3gpLiBEZWZhdWx0OiBvbi4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show Best Sellers</span><span class="te-cb is-on"></span></div></div>

### 10. New Arrivals

**Show New Arrivals** (`eshopping-show-new`) is on. The New Arrivals slider renders on the live home page.

![New Arrivals on the storefront](../img/electronics-new.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqU2hvdyBOZXcgQXJyaXZhbHMqKiAoYGVzaG9wcGluZy1zaG93LW5ld2AsIGNoZWNrYm94KS4gRGVmYXVsdDogb24u-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show New Arrivals</span><span class="te-cb is-on"></span></div></div>

### 11. Products by Category tabs

**Show Categories** (`eshopping-show-categories`) is on. Demo configuration:

| Setting | Theme Editor field (eShopping Theme) | Value |
| ------- | ----- | ----- |
| Category IDs | **Category IDs (comma separated, leave empty for auto-detect)** (`eshopping-pbcst-catIDs`) | *(empty)* — auto-uses all top-level categories |
| Grid columns | **Grid layout: categories,products,subcategories (e.g. 3,4,6)** (`eshopping-pbcst-grid`) | `3,4,6` |
| Active tab | **Default active tab** (`eshopping-pbcst-active`) | Featured |
| Show Bestselling tab | `eshopping-pbcst-show-bestselling` | ✅ |
| Show Featured tab | `eshopping-pbcst-show-featured` | ✅ |
| Show New tab | `eshopping-pbcst-show-new` | ✅ |
| Show Reviews (Top Rated) tab | `eshopping-pbcst-show-reviews` | ❌ (off) |

![Products by Category on the storefront](../img/electronics-pbc.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlIHNlY3Rpb24pOioqIFRoZW1lIEVkaXRvciDihpIgKiplU2hvcHBpbmcgVGhlbWUqKiDihpIgKipTaG93IENhdGVnb3JpZXMqKiAoYGVzaG9wcGluZy1zaG93LWNhdGVnb3JpZXNgLCBjaGVja2JveCkuIERlZmF1bHQ6IG9uLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggY2F0ZWdvcmllcyk6KiogVGhlbWUgRWRpdG9yIOKGkiAqKmVTaG9wcGluZyBUaGVtZSoqIOKGkiAqKkNhdGVnb3J5IElEcyAoY29tbWEgc2VwYXJhdGVkLCBsZWF2ZSBlbXB0eSBmb3IgYXV0by1kZXRlY3QpKiogKGBlc2hvcHBpbmctcGJjc3QtY2F0SURzYCkuIEZvcm1hdDogY29tbWEtc2VwYXJhdGVkIGNhdGVnb3J5IElEcyAoZS5nLiBgMjMsMjQsMjVgKTsgbGVhdmUgZW1wdHkgdG8gYXV0by1kZXRlY3QgYWxsIHRvcC1sZXZlbCBjYXRlZ29yaWVzLiBEZWZhdWx0OiBlbXB0eS4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoZ3JpZCk6KiogVGhlbWUgRWRpdG9yIOKGkiAqKmVTaG9wcGluZyBUaGVtZSoqIOKGkiAqKkdyaWQgbGF5b3V0OiBjYXRlZ29yaWVzLHByb2R1Y3RzLHN1YmNhdGVnb3JpZXMqKiAoYGVzaG9wcGluZy1wYmNzdC1ncmlkYCkuIEZvcm1hdDogdGhyZWUgY29tbWEtc2VwYXJhdGVkIG51bWJlcnMg4oCUICoqYGNhdGVnb3JpZXMscHJvZHVjdHMsc3ViY2F0ZWdvcmllc2AqKiAobnVtYmVyIDEgPSBob3cgbWFueSBjYXRlZ29yeSBibG9ja3MsIG51bWJlciAyID0gcHJvZHVjdHMgcGVyIGJsb2NrLCBudW1iZXIgMyA9IHN1YmNhdGVnb3J5IGxpbmtzIHNob3duKS4gRGVmYXVsdDogYDMsNCw2YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoZGVmYXVsdCB0YWIpOioqIFRoZW1lIEVkaXRvciDihpIgKiplU2hvcHBpbmcgVGhlbWUqKiDihpIgKipEZWZhdWx0IGFjdGl2ZSB0YWIqKiAoYGVzaG9wcGluZy1wYmNzdC1hY3RpdmVgKS4gT3B0aW9uczogKipGZWF0dXJlZCoqIC8gKipCZXN0c2VsbGluZyoqIC8gKipOZXdlc3QqKiAvICoqVG9wIFJhdGVkKiouIERlZmF1bHQ6IGBmZWF0dXJlZGAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggdGFicyBhcHBlYXIpOioqIFRoZW1lIEVkaXRvciDihpIgKiplU2hvcHBpbmcgVGhlbWUqKiDihpIgdGhlIGZvdXIgdGFiIGNoZWNrYm94ZXMg4oCUICoqU2hvdyBGZWF0dXJlZCB0YWIqKiAoYGVzaG9wcGluZy1wYmNzdC1zaG93LWZlYXR1cmVkYCksICoqU2hvdyBCZXN0c2VsbGluZyB0YWIqKiAoYGVzaG9wcGluZy1wYmNzdC1zaG93LWJlc3RzZWxsaW5nYCksICoqU2hvdyBOZXcgdGFiKiogKGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1uZXdgKSwgKipTaG93IFJldmlld3MgdGFiKiogKGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1yZXZpZXdzYCkuIERlZmF1bHRzIChjb25maWcuanNvbik6IEZlYXR1cmVkIOKchSwgQmVzdHNlbGxpbmcg4pyFLCBOZXcg4pyFLCBSZXZpZXdzIOKdjC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show Categories</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Category IDs (comma separated, leave empty for auto-detect)</span><span class="te-desc">Category IDs (comma separated, leave empty for auto-detect) (eshopping-pbcst-catIDs)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Grid layout: categories,products,subcategories</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">categories,products,subcategories</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Default active tab</span><span class="te-desc">Default active tab (eshopping-pbcst-active)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Featured</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Bestselling</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Newest</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Top Rated</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show Featured tab</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show Bestselling tab</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show New tab</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show Reviews tab</span><span class="te-cb"></span></div></div>

### 12. Brands carousel

12 brand logos shown on the home page. The demo uses fictional brand names (TechNova, PixelCraft, AudioWave, etc.) — replace them with your own brands.

![Brands carousel on the storefront](../img/electronics-brands.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZSAoaG93IG1hbnkpOioqIFRoZW1lIEVkaXRvciDihpIgKiplU2hvcHBpbmcgVGhlbWUqKiDihpIgKipIb21lcGFnZSBCcmFuZHMgTGltaXQqKiAoYGVzaG9wcGluZy1ob21lcGFnZS1icmFuZHMtbGltaXRgKS4gRm9ybWF0OiBhIG51bWJlciAobWF4IGJyYW5kcyB0byBzaG93KS4gRGVmYXVsdDogYDEyYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggYnJhbmRzIC8gbG9nb3MpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKlByb2R1Y3RzIOKGkiBCcmFuZHMqKiDigJQgYWRkIGJyYW5kcyBhbmQgdXBsb2FkIGVhY2ggYnJhbmQncyBpbWFnZS4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Homepage Brands Limit</span><span class="te-dd"><span class="te-dd__v">12</span><span class="te-dd__b">▾</span></span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub is-active">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 13. Blog

Home page blog posts: `3`. Add at least 3 posts with featured images.

![Blog posts on the storefront](../img/electronics-blog.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZSAocG9zdHMpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKlN0b3JlZnJvbnQg4oaSIEJsb2cqKiDigJQgYWRkIHBvc3RzIGFuZCBzZXQgYSBmZWF0dXJlZCBpbWFnZSBvbiBlYWNoIHNvIHRoZSBob21lIHBhZ2UgY2FyZHMgaGF2ZSB0aHVtYm5haWxzLiAoTm90IGEgdGhlbWUgc2V0dGluZy4p-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub is-active">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 14. Why Choose Us (AI HTML Generator | PapaThemes)

A Page Builder **AI HTML Generator | PapaThemes** widget placed in the region **`home_below_products_by_category` (sort 0)**, with the heading **Tech That Performs. Pricing That Powers Up.** It arrives with the demo widget import — it is not a theme setting, and requires the PapaThemes app to be installed.

![Why Choose Us block on the storefront](../img/electronics-why.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZC4gU2VlIFtEZW1vIG1hcmtldGluZyBibG9ja3Mg4oaSIFdoeSBDaG9vc2UgVXNdKHdpZGdldHMtcGFwYXRoZW1lcy5tZCN3aHktY2hvb3NlLXVzKSBmb3IgdGhlIGV4YWN0IEhUTUwu-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (Electronics) — Why Choose Us, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-j965bu9i {
        --papathemes-ai-widget-j965bu9i-white: #ffffff;
        --papathemes-ai-widget-j965bu9i-cream: #f8fafc;
        --papathemes-ai-widget-j965bu9i-bark-100: #f1f5f9;
        --papathemes-ai-widget-j965bu9i-bark-200: #e2e8f0;
        --papathemes-ai-widget-j965bu9i-bark-400: #94a3b8;
        --papathemes-ai-widget-j965bu9i-bark-500: #64748b;
        --papathemes-ai-widget-j965bu9i-bark-700: #334155;
        --papathemes-ai-widget-j965bu9i-bark-800: #1e293b;
        --papathemes-ai-widget-j965bu9i-bark-900: #0f172a;
        --papathemes-ai-widget-j965bu9i-terra: #3b82f6;
        --papathemes-ai-widget-j965bu9i-terra-light: #60a5fa;
        --papathemes-ai-widget-j965bu9i-terra-dark: #2563eb;
        --papathemes-ai-widget-j965bu9i-terra-pale: #eff6ff;
        --papathemes-ai-widget-j965bu9i-accent: #f59e0b;
        --papathemes-ai-widget-j965bu9i-accent-soft: #fef3c7;
        --papathemes-ai-widget-j965bu9i-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-j965bu9i-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-j965bu9i *,
    .papathemes-ai-widget-j965bu9i *::before,
    .papathemes-ai-widget-j965bu9i *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-j965bu9i-section {
        padding: 32px 20px 0;
    }
    
    .papathemes-ai-widget-j965bu9i-card {
        background: var(--papathemes-ai-widget-j965bu9i-white);
        border: 1px solid var(--papathemes-ai-widget-j965bu9i-bark-100);
        border-radius: 8px;
        overflow: hidden;
    }
    
    .papathemes-ai-widget-j965bu9i-inner {
        display: grid;
        grid-template-columns: 1fr 1fr;
        min-height: 360px;
    }
    
    .papathemes-ai-widget-j965bu9i-visual {
        position: relative;
        background:
            linear-gradient(135deg, var(--papathemes-ai-widget-j965bu9i-bark-900) 0%, var(--papathemes-ai-widget-j965bu9i-bark-800) 100%);
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.04) inset;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        min-height: 260px;
    }
    
    .papathemes-ai-widget-j965bu9i-visual::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse 70% 100% at 90% 50%, rgba(245, 158, 11, 0.14), transparent 70%),
            radial-gradient(ellipse 40% 60% at 0% 0%, rgba(255, 255, 255, 0.04), transparent 60%);
        pointer-events: none;
    }
    
    .papathemes-ai-widget-j965bu9i-visual::after {
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
    
    .papathemes-ai-widget-j965bu9i-stats {
        position: relative;
        z-index: 2;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        padding: 36px;
    }
    
    .papathemes-ai-widget-j965bu9i-stat {
        text-align: center;
        padding: 18px;
        background: rgba(255, 255, 255, .06);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, .08);
    }
    
    .papathemes-ai-widget-j965bu9i-stat-num {
        font-family: var(--papathemes-ai-widget-j965bu9i-font-heading);
        font-size: 28px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-j965bu9i-cream);
        line-height: 1;
        margin-bottom: 3px;
    }
    
    .papathemes-ai-widget-j965bu9i-stat-num span {
        color: var(--papathemes-ai-widget-j965bu9i-accent);
    }
    
    .papathemes-ai-widget-j965bu9i-stat-label {
        font-family: var(--papathemes-ai-widget-j965bu9i-font-body);
        font-size: 10px;
        color: var(--papathemes-ai-widget-j965bu9i-bark-400);
        text-transform: uppercase;
        letter-spacing: .08em;
        font-weight: 600;
    }
    
    .papathemes-ai-widget-j965bu9i-content {
        padding: 36px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .papathemes-ai-widget-j965bu9i-eyebrow {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: var(--papathemes-ai-widget-j965bu9i-font-body);
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: .14em;
        font-weight: 700;
        color: var(--papathemes-ai-widget-j965bu9i-bark-700);
        margin-bottom: 10px;
    }
    
    .papathemes-ai-widget-j965bu9i-eyebrow::before {
        content: "";
        width: 24px;
        height: 2px;
        background: var(--papathemes-ai-widget-j965bu9i-accent);
    }
    
    .papathemes-ai-widget-j965bu9i-heading {
        font-family: var(--papathemes-ai-widget-j965bu9i-font-heading);
        font-size: 20px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-j965bu9i-bark-900);
        margin-bottom: 14px;
        line-height: 1.25;
    }
    
    .papathemes-ai-widget-j965bu9i-heading em {
        font-style: italic;
        font-weight: 400;
        color: var(--papathemes-ai-widget-j965bu9i-bark-500);
    }
    
    .papathemes-ai-widget-j965bu9i-desc {
        font-family: var(--papathemes-ai-widget-j965bu9i-font-body);
        font-size: 12px;
        color: var(--papathemes-ai-widget-j965bu9i-bark-500);
        line-height: 1.7;
        margin-bottom: 24px;
    }
    
    .papathemes-ai-widget-j965bu9i-features {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    
    .papathemes-ai-widget-j965bu9i-feat {
        display: flex;
        gap: 12px;
        align-items: flex-start;
    }
    
    .papathemes-ai-widget-j965bu9i-feat-icon {
        width: 38px;
        height: 38px;
        border-radius: 6px;
        background: var(--papathemes-ai-widget-j965bu9i-accent-soft);
        border: 1px solid var(--papathemes-ai-widget-j965bu9i-bark-200);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--papathemes-ai-widget-j965bu9i-accent);
        flex-shrink: 0;
    }
    
    .papathemes-ai-widget-j965bu9i-feat-icon svg {
        width: 17px;
        height: 17px;
    }
    
    .papathemes-ai-widget-j965bu9i-feat-title {
        font-family: var(--papathemes-ai-widget-j965bu9i-font-body);
        font-size: 12px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-j965bu9i-bark-800);
        margin-bottom: 1px;
    }
    
    .papathemes-ai-widget-j965bu9i-feat-desc {
        font-family: var(--papathemes-ai-widget-j965bu9i-font-body);
        font-size: 11px;
        color: var(--papathemes-ai-widget-j965bu9i-bark-500);
        line-height: 1.45;
    }
    
    @media (max-width: 1023px) {
        .papathemes-ai-widget-j965bu9i-inner {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-j965bu9i-section {
            padding: 24px 10px 0;
        }
    
        .papathemes-ai-widget-j965bu9i-stats {
            padding: 24px;
            gap: 12px;
        }
    
        .papathemes-ai-widget-j965bu9i-content {
            padding: 24px;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-j965bu9i">
        <div class="papathemes-ai-widget-j965bu9i-section">
            <div class="papathemes-ai-widget-j965bu9i-card">
                <div class="papathemes-ai-widget-j965bu9i-inner">
                    <div class="papathemes-ai-widget-j965bu9i-visual">
                        <div class="papathemes-ai-widget-j965bu9i-stats">
                            <div class="papathemes-ai-widget-j965bu9i-stat">
                                <div class="papathemes-ai-widget-j965bu9i-stat-num">15<span>+</span></div>
                                <div class="papathemes-ai-widget-j965bu9i-stat-label">YEARS IN ELECTRONICS</div>
                            </div>
                            <div class="papathemes-ai-widget-j965bu9i-stat">
                                <div class="papathemes-ai-widget-j965bu9i-stat-num">3,500<span>+</span></div>
                                <div class="papathemes-ai-widget-j965bu9i-stat-label">ELECTRONICS SKUS</div>
                            </div>
                            <div class="papathemes-ai-widget-j965bu9i-stat">
                                <div class="papathemes-ai-widget-j965bu9i-stat-num">8M<span>+</span></div>
                                <div class="papathemes-ai-widget-j965bu9i-stat-label">Orders Shipped</div>
                            </div>
                            <div class="papathemes-ai-widget-j965bu9i-stat">
                                <div class="papathemes-ai-widget-j965bu9i-stat-num">99<span>%</span></div>
                                <div class="papathemes-ai-widget-j965bu9i-stat-label">Customer Satisfaction</div>
                            </div>
                        </div>
                    </div>
                    <div class="papathemes-ai-widget-j965bu9i-content">
                        <div class="papathemes-ai-widget-j965bu9i-eyebrow">Why Choose Us</div>
                        <h2 data-localized="1" data-localized="1" class="papathemes-ai-widget-j965bu9i-heading">Tech That Performs. <em>Pricing That Powers Up.</em></h2>
                        <p class="papathemes-ai-widget-j965bu9i-desc">From laptops and monitors to audio gear and smart home — every product is tested for quality and stocked for fast dispatch to your desk or door.</p>
                        <div class="papathemes-ai-widget-j965bu9i-features">
                            <div class="papathemes-ai-widget-j965bu9i-feat">
                                <div class="papathemes-ai-widget-j965bu9i-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16zM12 4.15 18.4 7.8 12 11.45 5.6 7.8 12 4.15zM5 9.5l6 3.43v6.94l-6-3.43V9.5zm8 10.37v-6.94l6-3.43v6.94l-6 3.43z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-j965bu9i-feat-title">Tested for Quality</div>
                                    <div class="papathemes-ai-widget-j965bu9i-feat-desc">Every product evaluated for performance, build quality, and value before stocking.</div>
                                </div>
                            </div>
                            <div class="papathemes-ai-widget-j965bu9i-feat">
                                <div class="papathemes-ai-widget-j965bu9i-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2a3 3 0 0 0 6 0h6a3 3 0 0 0 6 0h2v-5l-3-4zM6 18.5A1.5 1.5 0 1 1 7.5 17 1.5 1.5 0 0 1 6 18.5zm13.5-9 1.96 2.5H17V9.5h2.5zM18 18.5A1.5 1.5 0 1 1 19.5 17 1.5 1.5 0 0 1 18 18.5z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-j965bu9i-feat-title">Fast Direct Fulfillment</div>
                                    <div class="papathemes-ai-widget-j965bu9i-feat-desc">Same-day dispatch on stock items with reliable tracking and packaging built for fragile electronics.</div>
                                </div>
                            </div>
                            <div class="papathemes-ai-widget-j965bu9i-feat">
                                <div class="papathemes-ai-widget-j965bu9i-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66.95-2.3c.48.17.98.3 1.34.3C19 20 22 3 22 3c-1 2-8 2.25-13 3.25S2 11.5 2 13.5s1.75 3.75 1.75 3.75C7 8 17 8 17 8z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-j965bu9i-feat-title">Expert Tech Support</div>
                                    <div class="papathemes-ai-widget-j965bu9i-feat-desc">Real specialists who help with compatibility, setup, and troubleshooting — not just sales reps.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    ```
### 15. Customer Reviews (AI HTML Generator | PapaThemes)

A Page Builder **AI HTML Generator | PapaThemes** widget placed in the region **`home_below_products_by_category` (sort 1)**, with the heading **Customer Reviews** — a social-proof block. It comes from the demo widget import (not a theme setting) and requires the PapaThemes app.

![Customer Reviews block on the storefront](../img/electronics-reviews.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZC4gU2VlIFtEZW1vIG1hcmtldGluZyBibG9ja3Mg4oaSIEN1c3RvbWVyIFJldmlld3NdKHdpZGdldHMtcGFwYXRoZW1lcy5tZCNjdXN0b21lci1yZXZpZXdzKSBmb3IgdGhlIGV4YWN0IEhUTUwu-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (Electronics) — Customer Reviews, paste into the widget's HTML Content field"

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
                        <p class="papathemes-ai-widget-pkg1-r-text">Upgraded my whole home office here. The ultrawide monitor and mechanical keyboard transformed my workflow.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #334155, #1e293b)">DM</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Dana M.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Software Engineer</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 week ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">The wireless headphones and audio interface ship same day with thoughtful packaging. Premium experience.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">EK</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Erin K.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Content Creator</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">2 weeks ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Laptops and docking stations arrive configured and ready. Bulk pricing keeps our refresh budget predictable.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">RT</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Ray T.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">IT Manager</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">3 weeks ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Right-spec memory cards and external SSDs cut my workflow time noticeably. Reordering by model is effortless.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #334155, #1e293b)">SP</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Sofia P.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Photographer</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 month ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">New monitor and peripherals shipped before a tournament. Saved my season.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">JL</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Jordan L.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Gamer</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 month ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">USB-C hubs and cables arrive labeled and ready. No more lost time hunting the right port.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #1e293b, #0f172a)">MA</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Marcus A.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Home Office Pro</span>
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
                                <span class="papathemes-ai-widget-pkg1-r-role">Software Engineer</span>
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
### 16. Resources (AI HTML Generator | PapaThemes)

A Page Builder **AI HTML Generator | PapaThemes** widget placed in the region **`home_below_products_by_category` (sort 2)**, with the heading **Tech Resources & Guides** (guide cards). It comes from the demo widget import (not a theme setting) and requires the PapaThemes app.

![Resources block on the storefront](../img/electronics-resources.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZC4gU2VlIFtEZW1vIG1hcmtldGluZyBibG9ja3Mg4oaSIFJlc291cmNlc10od2lkZ2V0cy1wYXBhdGhlbWVzLm1kI3Jlc291cmNlcykgZm9yIHRoZSBleGFjdCBIVE1MLg==-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (Electronics) — Resources, paste into the widget's HTML Content field"

    ```html
    
    <style>
    .papathemes-ai-widget-onrl0jrg {
        --papathemes-ai-widget-onrl0jrg-white: #ffffff;
        --papathemes-ai-widget-onrl0jrg-bark-100: #f1f5f9;
        --papathemes-ai-widget-onrl0jrg-bark-500: #64748b;
        --papathemes-ai-widget-onrl0jrg-bark-800: #1e293b;
        --papathemes-ai-widget-onrl0jrg-bark-900: #0f172a;
        --papathemes-ai-widget-onrl0jrg-terra: #3b82f6;
        --papathemes-ai-widget-onrl0jrg-terra-dark: #2563eb;
        --papathemes-ai-widget-onrl0jrg-terra-pale: #eff6ff;
        --papathemes-ai-widget-onrl0jrg-forest-700: #15803d;
        --papathemes-ai-widget-onrl0jrg-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-onrl0jrg-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-onrl0jrg *,
    .papathemes-ai-widget-onrl0jrg *::before,
    .papathemes-ai-widget-onrl0jrg *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-onrl0jrg-section {
        padding: 32px 20px 0;
    }
    
    .papathemes-ai-widget-onrl0jrg-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    
    .papathemes-ai-widget-onrl0jrg-header-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .papathemes-ai-widget-onrl0jrg-sec-icon {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        background: var(--papathemes-ai-widget-onrl0jrg-terra-pale);
        color: var(--papathemes-ai-widget-onrl0jrg-terra);
    }
    
    .papathemes-ai-widget-onrl0jrg-sec-icon svg {
        width: 18px;
        height: 18px;
    }
    
    .papathemes-ai-widget-onrl0jrg-title {
        font-family: var(--papathemes-ai-widget-onrl0jrg-font-heading);
        font-size: 18px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-onrl0jrg-bark-900);
    }
    
    .papathemes-ai-widget-onrl0jrg-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 20px;
    }
    
    .papathemes-ai-widget-onrl0jrg-card-link {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    
    .papathemes-ai-widget-onrl0jrg-card {
        background: var(--papathemes-ai-widget-onrl0jrg-white);
        border: 1px solid var(--papathemes-ai-widget-onrl0jrg-bark-100);
        border-radius: 8px;
        overflow: hidden;
        transition: all .35s;
    }
    
    a.papathemes-ai-widget-onrl0jrg-card-link .papathemes-ai-widget-onrl0jrg-card {
        cursor: pointer;
    }
    
    a.papathemes-ai-widget-onrl0jrg-card-link .papathemes-ai-widget-onrl0jrg-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 20px rgba(15, 13, 10, .08);
        border-color: transparent;
    }
    
    .papathemes-ai-widget-onrl0jrg-thumb {
        aspect-ratio: 16/9;
        position: relative;
        display: block;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        background-color: #f8fafc;
    }
    
    .papathemes-ai-widget-onrl0jrg-thumb img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        padding: 0;
        opacity: 0;
        transition: opacity 0.3s ease-in-out;
    }
    
    .papathemes-ai-widget-onrl0jrg-thumb img.papathemes-ai-widget-onrl0jrg-loaded {
        opacity: 1;
    }
    
    .papathemes-ai-widget-onrl0jrg-type {
        position: absolute;
        top: 10px;
        left: 10px;
        padding: 3px 9px;
        background: rgba(0, 0, 0, .45);
        backdrop-filter: blur(6px);
        border-radius: 4px;
        font-family: var(--papathemes-ai-widget-onrl0jrg-font-body);
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
    
    .papathemes-ai-widget-onrl0jrg-type svg {
        width: 10px;
        height: 10px;
    }
    
    .papathemes-ai-widget-onrl0jrg-body {
        padding: 18px;
    }
    
    .papathemes-ai-widget-onrl0jrg-body h3 {
        font-family: var(--papathemes-ai-widget-onrl0jrg-font-body);
        font-size: 13px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-onrl0jrg-bark-800);
        margin-bottom: 4px;
        line-height: 1.3;
        transition: color .2s;
    }
    
    a.papathemes-ai-widget-onrl0jrg-card-link .papathemes-ai-widget-onrl0jrg-card:hover .papathemes-ai-widget-onrl0jrg-body h3 {
        color: var(--papathemes-ai-widget-onrl0jrg-terra-dark);
    }
    
    .papathemes-ai-widget-onrl0jrg-body p {
        font-family: var(--papathemes-ai-widget-onrl0jrg-font-body);
        font-size: 11px;
        color: var(--papathemes-ai-widget-onrl0jrg-bark-500);
        line-height: 1.5;
    }
    
    @media (max-width: 1023px) {
        .papathemes-ai-widget-onrl0jrg-grid {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-onrl0jrg-section {
            padding: 24px 10px 0;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-onrl0jrg">
        <div class="papathemes-ai-widget-onrl0jrg-section">
            <div class="papathemes-ai-widget-onrl0jrg-header">
                <div class="papathemes-ai-widget-onrl0jrg-header-left">
                    <div class="papathemes-ai-widget-onrl0jrg-sec-icon">
                        <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-5 2v6l-2.5-1.5L8 10V4h5zM6 20V4h.01L6 20h12V4l.01 16H6z"/></svg>
                    </div>
                    <h2 class="papathemes-ai-widget-onrl0jrg-title">Tech Resources &amp; Guides</h2>
                </div>
            </div>
            <div class="papathemes-ai-widget-onrl0jrg-grid">
                <a href="https://eshopping-electronics-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-onrl0jrg-card-link">
                    <div class="papathemes-ai-widget-onrl0jrg-card">
                        <div class="papathemes-ai-widget-onrl0jrg-thumb">
                            <img
                                class="papathemes-ai-widget-onrl0jrg-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-v0uhwv1yxm/product_images/uploaded_images/the-ultimate-guide-to-buying-the-right-laptop-in-2026.png"
                                width="640"
                                height="360"
                                alt="Laptops on a wooden desk"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-onrl0jrg-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-onrl0jrg-body">
                            <h3>The Ultimate Guide to Buying the Right Laptop</h3>
                            <p>What to look for in displays, CPUs, GPUs, memory, and battery life when choosing your next laptop.</p>
                        </div>
                    </div>
                </a>
                <a href="https://eshopping-electronics-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-onrl0jrg-card-link">
                    <div class="papathemes-ai-widget-onrl0jrg-card">
                        <div class="papathemes-ai-widget-onrl0jrg-thumb">
                            <img
                                class="papathemes-ai-widget-onrl0jrg-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-v0uhwv1yxm/product_images/uploaded_images/product-review-the-best-wireless-headphones-weve-tested-this-year.png"
                                width="640"
                                height="360"
                                alt="Premium wireless headphones"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-onrl0jrg-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-onrl0jrg-body">
                            <h3>Best Wireless Headphones We&rsquo;ve Tested This Year</h3>
                            <p>In-depth review of premium ANC headphones and true-wireless earbuds — sound, comfort, battery.</p>
                        </div>
                    </div>
                </a>
                <a href="https://eshopping-electronics-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-onrl0jrg-card-link">
                    <div class="papathemes-ai-widget-onrl0jrg-card">
                        <div class="papathemes-ai-widget-onrl0jrg-thumb">
                            <img
                                class="papathemes-ai-widget-onrl0jrg-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-v0uhwv1yxm/product_images/uploaded_images/10-must-have-tech-gadgets-to-upgrade-your-home-office-in-2026.png"
                                width="640"
                                height="360"
                                alt="Home office tech gadgets"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-onrl0jrg-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-onrl0jrg-body">
                            <h3>10 Must-Have Tech Gadgets to Upgrade Your Home Office</h3>
                            <p>Smart monitors, ergonomic keyboards, USB-C hubs, and more — boost productivity at your desk.</p>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
    
    <script>
    (function(){
        var id = 'onrl0jrg';
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
### 17. Newsletter — variation default

**Show Newsletter** (`eshopping-show-newsletter`) is on. The variation sets the heading **Stay Ahead in *Tech*** with the description "Product launches, exclusive deals, and expert reviews delivered weekly."

![Newsletter on the storefront](../img/electronics-newsletter.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqU2hvdyBOZXdzbGV0dGVyKiogKGBlc2hvcHBpbmctc2hvdy1uZXdzbGV0dGVyYCwgY2hlY2tib3gpLiBEZWZhdWx0OiBvbi4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoaGVhZGluZyArIGRlc2NyaXB0aW9uKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqTmV3c2xldHRlciBTaWdudXAgVGV4dCoqIChgZXNob3BwaW5nLW5ld3NsZXR0ZXItdGV4dGApLiBGb3JtYXQ6IGBUaXRsZXxEZXNjcmlwdGlvbmAsIHR3byBgfGAtc2VwYXJhdGVkIHNlZ21lbnRzIOKAlCB0aGUgKip0aXRsZSBzdXBwb3J0cyBpbmxpbmUgSFRNTCoqIChlLmcuIGA8ZW0+4oCmPC9lbT5gKS4gVGhlbWUgZGVmYXVsdDogYFN0YXkgVXBkYXRlZCB3aXRoIDxlbT5PdXIgTmV3c2xldHRlcjwvZW0+fFByb2R1Y3QgbGF1bmNoZXMsIGZpZWxkIHRpcHMsIGFuZCBleGNsdXNpdmUgb2ZmZXJzIGluIHlvdXIgaW5ib3guYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show Newsletter</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Newsletter Signup Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">title supports inline HTML</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### 18. About (AI HTML Generator | PapaThemes)

A Page Builder **AI HTML Generator | PapaThemes** widget placed in the region **`home_below_newsletter` (sort 0)**, with the heading **Your Complete Consumer Electronics Source.** Like the blocks above, it comes from the demo widget import — not a theme setting — and requires the PapaThemes app.

![About block on the storefront](../img/electronics-about.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZC4gU2VlIFtEZW1vIG1hcmtldGluZyBibG9ja3Mg4oaSIEFib3V0XSh3aWRnZXRzLXBhcGF0aGVtZXMubWQjYWJvdXQpIGZvciB0aGUgZXhhY3QgSFRNTC4=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (Electronics) — About, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-z8pznc2g {
        --papathemes-ai-widget-z8pznc2g-white: #ffffff;
        --papathemes-ai-widget-z8pznc2g-bark-100: #f1f5f9;
        --papathemes-ai-widget-z8pznc2g-bark-600: #475569;
        --papathemes-ai-widget-z8pznc2g-bark-900: #0f172a;
        --papathemes-ai-widget-z8pznc2g-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-z8pznc2g-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 32px 20px 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-z8pznc2g *,
    .papathemes-ai-widget-z8pznc2g *::before,
    .papathemes-ai-widget-z8pznc2g *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-z8pznc2g-section {
        background: var(--papathemes-ai-widget-z8pznc2g-white);
        border: 1px solid var(--papathemes-ai-widget-z8pznc2g-bark-100);
        border-radius: 8px;
        padding: 32px;
    }
    
    .papathemes-ai-widget-z8pznc2g-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .papathemes-ai-widget-z8pznc2g-title {
        font-family: var(--papathemes-ai-widget-z8pznc2g-font-heading);
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--papathemes-ai-widget-z8pznc2g-bark-900);
        text-align: center;
        margin-bottom: 16px;
        line-height: 1.3;
    }
    
    .papathemes-ai-widget-z8pznc2g-text {
        font-family: var(--papathemes-ai-widget-z8pznc2g-font-body);
        font-size: 0.86rem;
        color: var(--papathemes-ai-widget-z8pznc2g-bark-600);
        line-height: 1.8;
        max-width: 860px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 12px;
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-z8pznc2g {
            margin: 24px 10px 0;
        }
    
        .papathemes-ai-widget-z8pznc2g-section {
            padding: 24px 18px;
        }
    
        .papathemes-ai-widget-z8pznc2g-title {
            font-size: 1.15rem;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-z8pznc2g">
        <div class="papathemes-ai-widget-z8pznc2g-section">
            <div class="papathemes-ai-widget-z8pznc2g-container">
                <h2 class="papathemes-ai-widget-z8pznc2g-title">Your Complete Consumer Electronics Source</h2>
                <p class="papathemes-ai-widget-z8pznc2g-text">We supply the laptops, monitors, audio gear, smart home devices, and accessories that keep professionals, creators, and enthusiasts powered up. Our catalog spans computing, displays, audio, mobile, smart home, and cables — all tested and stocked for fast, predictable shipping.</p>
                <p class="papathemes-ai-widget-z8pznc2g-text">From everyday productivity to high-performance gear, every product is chosen for quality and value. Browse trusted brands and pro-grade tech used by thousands of professionals and enthusiasts every day.</p>
            </div>
        </div>
    </div>
    ```
### 19. Talk to an Expert (AI HTML Generator | PapaThemes)

A Page Builder **AI HTML Generator | PapaThemes** widget placed in the region **`home_below_newsletter` (sort 1)**, a contact-CTA block with the heading **Need help choosing tech? Talk to a Tech Specialist.** It comes from the demo widget import (not a theme setting) and requires the PapaThemes app.

![Talk to an Expert block on the storefront](../img/electronics-expert.png){ loading=lazy }

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZC4gU2VlIFtEZW1vIG1hcmtldGluZyBibG9ja3Mg4oaSIFRhbGsgdG8gYW4gRXhwZXJ0XSh3aWRnZXRzLXBhcGF0aGVtZXMubWQjdGFsay10by1hbi1leHBlcnQpIGZvciB0aGUgZXhhY3QgSFRNTC4=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (Electronics) — Talk to an Expert, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-i24corxj {
        --papathemes-ai-widget-i24corxj-white: #ffffff;
        --papathemes-ai-widget-i24corxj-cream: #f8fafc;
        --papathemes-ai-widget-i24corxj-bark-200: #cbd5e1;
        --papathemes-ai-widget-i24corxj-bark-300: #cbd5e1;
        --papathemes-ai-widget-i24corxj-bark-400: #94a3b8;
        --papathemes-ai-widget-i24corxj-bark-700: #334155;
        --papathemes-ai-widget-i24corxj-bark-800: #1e293b;
        --papathemes-ai-widget-i24corxj-bark-900: #0f172a;
        --papathemes-ai-widget-i24corxj-bark-950: #060912;
        --papathemes-ai-widget-i24corxj-terra: #3b82f6;
        --papathemes-ai-widget-i24corxj-terra-dark: #2563eb;
        --papathemes-ai-widget-i24corxj-terra-light: #60a5fa;
        --papathemes-ai-widget-i24corxj-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-i24corxj-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-i24corxj *,
    .papathemes-ai-widget-i24corxj *::before,
    .papathemes-ai-widget-i24corxj *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-i24corxj-bar {
        margin: 32px 20px 0;
        background:
            linear-gradient(135deg, var(--papathemes-ai-widget-i24corxj-bark-900) 0%, var(--papathemes-ai-widget-i24corxj-bark-800) 100%);
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
    
    .papathemes-ai-widget-i24corxj-bar::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse 60% 90% at 92% 50%, rgba(59, 130, 246, 0.18), transparent 70%),
            radial-gradient(ellipse 40% 60% at 0% 0%, rgba(255, 255, 255, 0.04), transparent 60%);
        pointer-events: none;
    }
    
    .papathemes-ai-widget-i24corxj-bar::after {
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
    
    .papathemes-ai-widget-i24corxj-left {
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-i24corxj-heading {
        font-family: var(--papathemes-ai-widget-i24corxj-font-heading);
        font-size: 17px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-i24corxj-white);
        margin-bottom: 6px;
        letter-spacing: -0.01em;
    }
    
    .papathemes-ai-widget-i24corxj-heading em {
        font-style: italic;
        font-weight: 400;
        // Hardcoded warm gold accent — universal premium signal, decoupled from
        // per-store terra-light (renders blue on Electronics #60a5fa).
        color: #fbbf24;
    }
    
    .papathemes-ai-widget-i24corxj-desc {
        font-family: var(--papathemes-ai-widget-i24corxj-font-body);
        font-size: 13px;
        line-height: 1.55;
        color: var(--papathemes-ai-widget-i24corxj-bark-300);
        max-width: 60ch;
    }
    
    .papathemes-ai-widget-i24corxj-btns {
        display: flex;
        gap: 10px;
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-i24corxj-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 12px 24px;
        border-radius: 8px;
        font-family: var(--papathemes-ai-widget-i24corxj-font-heading);
        font-size: 13px;
        font-weight: 600;
        text-decoration: none;
        transition: all .25s cubic-bezier(.16, 1, .3, 1);
        letter-spacing: 0.01em;
        border: none;
        cursor: pointer;
    }
    
    .papathemes-ai-widget-i24corxj-btn svg {
        width: 15px;
        height: 15px;
        transition: transform .3s;
    }
    
    .papathemes-ai-widget-i24corxj-btn--terra {
        background: var(--papathemes-ai-widget-i24corxj-terra);
        color: var(--papathemes-ai-widget-i24corxj-white);
    }
    
    .papathemes-ai-widget-i24corxj-btn--terra:hover {
        background: var(--papathemes-ai-widget-i24corxj-terra-dark);
        color: var(--papathemes-ai-widget-i24corxj-white);
        box-shadow: 0 6px 24px rgba(59, 130, 246, .35);
        transform: translateY(-1px);
        text-decoration: none;
    }
    
    .papathemes-ai-widget-i24corxj-btn--terra:hover svg {
        transform: translateX(3px);
    }
    
    .papathemes-ai-widget-i24corxj-btn--ghost {
        border: 1px solid rgba(255, 255, 255, 0.22);
        color: var(--papathemes-ai-widget-i24corxj-white);
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(8px);
    }
    
    .papathemes-ai-widget-i24corxj-btn--ghost:hover {
        border-color: rgba(255, 255, 255, 0.45);
        color: var(--papathemes-ai-widget-i24corxj-white);
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-1px);
        text-decoration: none;
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-i24corxj-bar {
            margin-left: 10px;
            margin-right: 10px;
            flex-direction: column;
            text-align: center;
            padding: 28px 24px;
        }
    
        .papathemes-ai-widget-i24corxj-btns {
            flex-direction: column;
            width: 100%;
        }
    
        .papathemes-ai-widget-i24corxj-btn {
            justify-content: center;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-i24corxj">
        <div class="papathemes-ai-widget-i24corxj-bar">
            <div class="papathemes-ai-widget-i24corxj-left">
                <h3 class="papathemes-ai-widget-i24corxj-heading">Need help choosing tech? <em>Talk to a Tech Specialist</em></h3>
                <p class="papathemes-ai-widget-i24corxj-desc">Our specialists help you spec the right laptop, monitor, or peripheral for your work or play. Call or chat anytime.</p>
            </div>
            <div class="papathemes-ai-widget-i24corxj-btns">
                <a href="/contact-us/" class="papathemes-ai-widget-i24corxj-btn papathemes-ai-widget-i24corxj-btn--terra">
                    Request a Quote
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
                </a>
                <a href="tel:18005550123" class="papathemes-ai-widget-i24corxj-btn papathemes-ai-widget-i24corxj-btn--ghost">
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                    (800) 555-0123
                </a>
            </div>
        </div>
    </div>
    ```
### 20. Footer tagline (AI HTML Generator | PapaThemes)

The footer's short tagline is a Page Builder **AI HTML Generator | PapaThemes** widget in the **global** region **`eshopping_footer_description--global`** (one widget, placed on every template). On the live demo it reads: *"eShopping Electronics Demo — Laptops, monitors, audio gear, and smart home tech — tested for quality and shipped fast."*

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIGNsaWNrIHRoZSBmb290ZXIgdGFnbGluZSBibG9jayDihpIgKipIVE1MIENvbnRlbnQqKiBmaWVsZC4gU2VlIFtEZW1vIG1hcmtldGluZyBibG9ja3Mg4oaSIEZvb3RlciB0YWdsaW5lXSh3aWRnZXRzLXBhcGF0aGVtZXMubWQjZm9vdGVyLXRhZ2xpbmUpIGZvciB0aGUgZXhhY3QgSFRNTCwgYW5kIFtGb290ZXJdKGZvb3Rlci5tZCkgZm9yIHRoZSBvdGhlciBmb290ZXIgc2V0dGluZ3MgKGNvbG9ycywgcGF5bWVudCBpY29ucywgYnJhbmRzLCBjb3B5cmlnaHQpLg==-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (Electronics) — Footer tagline, paste into the widget's HTML Content field"

    ```html
    <span class="eshopping-footer-desc-text">eShopping Electronics Demo — Laptops, monitors, audio gear, and smart home tech — tested for quality and shipped fast.</span>
    ```
### 21. Marketing features to turn on

| Setting | Theme Editor field / location | Value |
| ------- | ----- | ----- |
| Frequently Bought Together count | **FBT Products Count** (`eshopping-fbt-count`) | `2` |
| Frequently Bought Together discount | **Visual Bundle Discount %** (`eshopping-fbt-discount-percent`) | `0`% |
| Urgency: view count | `eshopping-urgency-view-count` | ✅ |
| Urgency: last order | `eshopping-urgency-last-order` | ✅ |
| Recent sales pages | `eshopping-recent-sales-pages` | All pages |
| Newsletter popup | `eshopping-popup-nl-text` | Heading "Get 10% Off Your First Order", description "Sign up for our newsletter and receive an exclusive discount code." |
| Promo popup | `eshopping-popup-promo-text` | Heading "Spring Sale", description "Get 15% off your entire order with the code below.", code `SPRING15`, button "Shop Now", link `/` |
| Exit popup | `eshopping-popup-exit-text` | Heading "Wait! Don't Go Empty-Handed", description "Here's a special 10% discount just for you.", code `STAY10`, button "Claim Discount", link `/` |
| Exit popup options | `eshopping-popup-exit-opts` | Type `discount`, after 45 seconds, show once per session |

<!--te-src:PiAqKkN1c3RvbWl6ZSAoRkJUKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqRkJUIFByb2R1Y3RzIENvdW50KiogKGBlc2hvcHBpbmctZmJ0LWNvdW50YCwgc2VsZWN0OiBEaXNhYmxlZC8xLzIvMywgZGVmYXVsdCBgMmApIGFuZCAqKlZpc3VhbCBCdW5kbGUgRGlzY291bnQgJSoqIChgZXNob3BwaW5nLWZidC1kaXNjb3VudC1wZXJjZW50YCwgYSBwZXJjZW50YWdlIG51bWJlciwgZGVmYXVsdCBgMGApLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodXJnZW5jeSwgcmVjZW50IHNhbGVzLCBwb3B1cHMpOioqIFRoZW1lIEVkaXRvciDihpIgKiplU2hvcHBpbmcgVGhlbWUqKiDihpIgdGhlIG1hdGNoaW5nIGZpZWxkcy4gUG9wdXAgdGV4dCBmaWVsZHMgYXJlIGB8YC1zZXBhcmF0ZWQgKHBvcHVwIGZvcm1hdCB2YXJpZXMg4oCUIHNlZSB0aGUgZGVkaWNhdGVkIHBhZ2VzKS4gU2VlIFtVcmdlbmN5ICsgcmVjZW50IHNhbGVzXSh1cmdlbmN5LWFuZC1yZWNlbnQtc2FsZXMubWQpLCBbUG9wdXBzXShwb3B1cHMubWQpLCBbRkJUXShwcm9kdWN0LWZidC5tZCku-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">FBT Products Count</span><span class="te-tx">2</span></div><div class="te-mock__row"><span class="te-lbl">Visual Bundle Discount %</span><span class="te-tx">0</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">setting</span><span class="te-desc">Theme Editor field (eShopping Theme)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### 22. Sidebar promo / cart goal / PDP shipping & warranty (variation defaults)

| Setting | Theme Editor field (eShopping Theme) | Value |
| ------- | ----- | ----- |
| Sidebar promo | **Sidebar Promo Text** (`eshopping-promo-text`) | Heading "Free Shipping $99+", text "Free shipping on all electronics orders over $99.", button "Shop Deals", link `/shipping/` |
| Cart goals | **Goal items (amount\|icon\|label, comma-separated)** (`eshopping-cart-goal-items`) | Free Shipping at $30, 5% Off at $75, Free Accessory at $150 |
| PDP shipping notes | **PDP Shipping Text** (`eshopping-pdp-shipping-text`) | "Free Shipping" — on orders over $99; "Manufacturer Warranty" — full coverage included; "30-Day Returns" — hassle-free policy |
| PDP warranty | **PDP Warranty Text** (`eshopping-pdp-warranty-text`) | "What's Covered", "What's Not Covered", "How to Claim", "Extended Protection" (four blocks, pre-filled) |

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2lkZWJhciBwcm9tbyk6KiogVGhlbWUgRWRpdG9yIOKGkiAqKmVTaG9wcGluZyBUaGVtZSoqIOKGkiAqKlNpZGViYXIgUHJvbW8gVGV4dCoqIChgZXNob3BwaW5nLXByb21vLXRleHRgKS4gRm9ybWF0OiBgSGVhZGluZ3xEZXNjcmlwdGlvbnxCdXR0b24gTGFiZWx8VVJMYCDigJQgZm91ciBgfGAtc2VwYXJhdGVkIHNlZ21lbnRzLiBUaGVtZSBkZWZhdWx0OiBgRnJlZSBTaGlwcGluZyAkNTAwK3xGcmVlIGdyb3VuZCBzaGlwcGluZyBvbiBxdWFsaWZ5aW5nIG9yZGVycy58U2hvcCBOb3d8L3NoaXBwaW5nL2Au-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY2FydCBnb2Fscyk6KiogVGhlbWUgRWRpdG9yIOKGkiAqKmVTaG9wcGluZyBUaGVtZSoqIOKGkiAqKkdvYWwgaXRlbXMgKGFtb3VudHxpY29ufGxhYmVsLCBjb21tYS1zZXBhcmF0ZWQpKiogKGBlc2hvcHBpbmctY2FydC1nb2FsLWl0ZW1zYCkuIEZvcm1hdDogY29tbWEtc2VwYXJhdGVkIGdvYWxzLCBlYWNoIGdvYWwgYGFtb3VudHxpY29ufGxhYmVsYC4gYGljb25gIGlzIG9wdGlvbmFsOyBzdXBwb3J0ZWQgaWNvbnM6IGBzaGlwcGluZ2AsIGBkaXNjb3VudGAsIGBnaWZ0YCwgYGNoZWNrYCwgYGJhZ2AsIGBzdGFyYC4gVGhlbWUgZGVmYXVsdDogYDUwfHNoaXBwaW5nfEZyZWUgU2hpcHBpbmcsMTAwfGRpc2NvdW50fDEwJSBPZmYsMTUwfGdpZnR8RnJlZSBHaWZ0YC4gRWxlY3Ryb25pY3MgdmFsdWU6IGAzMHxzaGlwcGluZ3xGcmVlIFNoaXBwaW5nLDc1fGRpc2NvdW50fDUlIE9mZiwxNTB8Z2lmdHxGcmVlIEFjY2Vzc29yeWAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoUERQIHNoaXBwaW5nIG5vdGVzKToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqUERQIFNoaXBwaW5nIFRleHQqKiAoYGVzaG9wcGluZy1wZHAtc2hpcHBpbmctdGV4dGApLiBGb3JtYXQ6IGB8YC1zZXBhcmF0ZWQsICoqNiBzZWdtZW50cyA9IDMgYFRpdGxlfERlc2NyaXB0aW9uYCBwYWlycyoqLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoUERQIHdhcnJhbnR5KToqKiBUaGVtZSBFZGl0b3Ig4oaSICoqZVNob3BwaW5nIFRoZW1lKiog4oaSICoqUERQIFdhcnJhbnR5IFRleHQqKiAoYGVzaG9wcGluZy1wZHAtd2FycmFudHktdGV4dGApLiBGb3JtYXQ6IGB8YC1zZXBhcmF0ZWQsICoqOCBzZWdtZW50cyA9IDQgYFRpdGxlfERlc2NyaXB0aW9uYCBwYWlycyoqLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Sidebar Promo Text</span><span class="te-desc">Sidebar Promo Text (eshopping-promo-text)</span></span><span class="te-tx">Free Shipping $500+|Free ground ship…</span></div><div class="te-mock__row"><span class="te-lbl">Goal items (amount|icon|label, comma-separated)</span><span class="te-tx">50|shipping|Free Shipping,100|discou…</span></div><div class="te-mock__row"><span class="te-lbl">PDP Shipping Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">6 segments = 3 Title|Description pairs</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">PDP Warranty Text</span><span class="te-desc">PDP Warranty Text (eshopping-pdp-warranty-text)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">8 segments = 4 Title|Description pairs</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

---

## Final check

Compare to <https://eshopping-electronics-demo.mybigcommerce.com>.

---

## Next

- [Product page](product.md)
- [Frequently Bought Together](product-fbt.md)
- [Demo marketing blocks](widgets-papathemes.md)
- [Packaging →](home-packaging.md)
