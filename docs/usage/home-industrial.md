# Home Page — Industrial Variant

Live demo: <https://eshopping-industrial-demo.mybigcommerce.com>

![Industrial home page composed view](../img/home-industrial-composed.png){ loading=lazy }

!!! note "Before you start"
    Theme installed, **Industrial** variation picked in Page Builder's *Theme styles* dropdown, **Industrial** product + widget data imported via BC Tools.

The Industrial variation ships with its own warm "rust + bark" palette and serif headings. **Five** marketing blocks on the page (plus the footer tagline) are **AI HTML Generator | PapaThemes** widgets placed with Page Builder — they arrive with the demo widget import, not with theme settings. They require the PapaThemes app to be installed. See [Marketing blocks](#14-marketing-blocks-ai-html-generator-papathemes-via-page-builder) below for the full list and the exact HTML for each.

What the live home page actually renders, top to bottom:

1. Hero (Home Page Carousel)
2. Trust strip
3. Featured Products slider
4. New Arrivals slider
5. Products by Category
6. AI HTML Generator widget — **Why Choose Us** value-prop callout ("Industrial Tools That Last. Pricing That…") — `home_below_products_by_category` sort 0
7. AI HTML Generator widget — **Customer Reviews** social proof — `home_below_products_by_category` sort 1
8. AI HTML Generator widget — **Resources** guide cards — `home_below_products_by_category` sort 2
9. Brands carousel
10. Blog posts
11. Newsletter
12. AI HTML Generator widget — **About** SEO intro ("Your Complete Industrial Supply Source") — `home_below_newsletter` sort 0
13. AI HTML Generator widget — **Talk to an Expert** contact CTA — `home_below_newsletter` sort 1

The footer **tagline** is a sixth AI HTML Generator widget in the global region `eshopping_footer_description--global` — it renders inside the footer on every page, not in the home-page flow above.

## Section-by-section recipe

### 1. Variation

Theme Editor → **Industrial** (top dropdown).

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSIHRvcCAqKnZhcmlhdGlvbiBkcm9wZG93bioqIChQYWdlIEJ1aWxkZXIgKlRoZW1lIHN0eWxlcyopLiBQaWNrICoqSW5kdXN0cmlhbCoqLCAqKkF1dG8gUGFydHMqKiwgKipFbGVjdHJvbmljcyoqLCBvciAqKlBhY2thZ2luZyoqLiBUaGUgdmFyaWF0aW9uIHN3YXBzIHRoZSB3aG9sZSBjb2xvci9mb250L2NvcHkgcHJlc2V0LiBEZWZhdWx0OiBgSW5kdXN0cmlhbGAgZm9yIHRoaXMgc3RvcmUu-->
<!--te-mock--><div class="te-mock te-mock--styles"><div class="te-mock__hd"><span>Styles</span><span class="te-x">✕</span></div><div class="te-mock__grp">Theme variation</div><div class="te-mock__row"><span class="te-lbl">Industrial</span><span class="te-check">✓</span></div><div class="te-mock__row"><span class="te-lbl">AutoParts</span></div><div class="te-mock__row"><span class="te-lbl">Electronics</span></div><div class="te-mock__row"><span class="te-lbl">Packaging</span></div></div>

### 2. Colors

The Industrial variation sets a warm rust-and-bark palette. These are the actual values:

<!--te-tbl:fCBDb2xvciB8IFZhbHVlIHwKfCAtLS0tLSB8IC0tLS0tIHwKfCBUZXJyYSB8IGAjYmY1YjMzYCB8CnwgVGVycmEgTGlnaHQgfCBgI2Q5ODQ1ZWAgfAp8IFRlcnJhIERhcmsgfCBgIzk5M2YxZmAgfAp8IFRlcnJhIFBhbGUgfCBgI2ZkZjBlOWAgfAp8IEJhcmsgOTUwIHwgYCMwZjBkMGFgIHwKfCBCYXJrIDkwMCB8IGAjMWExNzEzYCB8CnwgQmFyayA1MCB8IGAjZjVmM2VmYCB8CnwgQ3JlYW0gfCBgI2ZhZjhmNGAgfAp8IFdoaXRlIHwgYCNmZmZmZmZgIHw=-->

<!--te-lead:QmFkZ2UsIHJhdGluZywgYW5kIHByaWNlIGNvbG9yczo=-->

<!--te-tbl:fCBDb2xvciB8IFZhbHVlIHwKfCAtLS0tLSB8IC0tLS0tIHwKfCBTYWxlIGJhZGdlIGJhY2tncm91bmQgfCBgI2JmNWIzM2AgfAp8IFN0YWZmIHBpY2sgYmFkZ2UgYmFja2dyb3VuZCB8IGAjM2Y4MDYwYCB8CnwgQWN0aXZlIHJhdGluZyBzdGFyIHwgYCNmNTllMGJgIHwKfCBTYWxlIHByaWNlIHwgYCNkYzI2MjZgIHwKfCBPcmlnaW5hbCAoc3RydWNrLXRocm91Z2gpIHByaWNlIHwgYCM5NzhhNzRgIHw=-->

<!--te-lead:QmFubmVyLCB0b3AgYmFyLCBhbmQgbmF2IGNvbG9yczo=-->

<!--te-tbl:fCBDb2xvciB8IFZhbHVlIHwKfCAtLS0tLSB8IC0tLS0tIHwKfCBCYW5uZXIgYmFja2dyb3VuZCB8IGAjM2UzNjI5YCB8CnwgQmFubmVyIHRleHQgfCBgI2Q1Y2VjMmAgfAp8IEJhbm5lciBsaW5rIHwgYCNkOTg0NWVgIHwKfCBUb3AgYmFyIGJhY2tncm91bmQgfCBgIzFhMTcxM2AgfAp8IFRvcCBiYXIgdGV4dCB8IGAjOTc4YTc0YCB8CnwgTmF2IGJhY2tncm91bmQgfCBgI2ZmZmZmZmAgfAp8IE5hdiB0ZXh0IHwgYCM2YjVlNGZgIHwKfCBOYXYgc2VhcmNoIGJ1dHRvbiB8IGAjYzc1YTJhYCB8-->

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiB0aGUgcmVsZXZhbnQgY29sb3IgZ3JvdXAgKCpTYWxlICYgQmFkZ2VzKiwgKkJhbm5lciosICpIZWFkZXIqLCAqRm9vdGVyKikuIEV2ZXJ5IGNvbG9yIGFib3ZlIGlzIGl0cyBvd24gZmllbGQg4oCUIGUuZy4gKipCYW5uZXIgQmFja2dyb3VuZCoqIChpZCBgZXNob3BwaW5nLWJhbm5lci1iZ2AsIGRlZmF1bHQgYCMzZTM2MjlgKSwgKipCYW5uZXIgVGV4dCBDb2xvcioqIChpZCBgZXNob3BwaW5nLWJhbm5lci1jb2xvcmAsIGRlZmF1bHQgYCNkNWNlYzJgKSwgKipCYW5uZXIgTGluayBDb2xvcioqIChpZCBgZXNob3BwaW5nLWJhbm5lci1saW5rYCwgZGVmYXVsdCBgI2Q5ODQ1ZWApLCAqKlRvcCBCYXIgQmFja2dyb3VuZCoqIChpZCBgZXNob3BwaW5nLXRvcGJhci1iZ2AsIGRlZmF1bHQgYCMxYTE3MTNgKSwgKipOYXYgU2VhcmNoIEJ1dHRvbioqIChpZCBgZXNob3BwaW5nLW5hdi1zZWFyY2gtYnRuYCwgZGVmYXVsdCBgI2M3NWEyYWApLiBGb3JtYXQ6IGhleCBjb2xvci4gUGlja2luZyBhIGRpZmZlcmVudCAqKnZhcmlhdGlvbioqIHJlc2V0cyB0aGUgd2hvbGUgcGFsZXR0ZSBhdCBvbmNlLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Terra</span><span class="te-color"><span class="te-hex">#BF5B33</span><span class="te-sw" style="background:#bf5b33"></span></span></div><div class="te-mock__row"><span class="te-lbl">Terra Light</span><span class="te-color"><span class="te-hex">#D9845E</span><span class="te-sw" style="background:#d9845e"></span></span></div><div class="te-mock__row"><span class="te-lbl">Terra Dark</span><span class="te-color"><span class="te-hex">#993F1F</span><span class="te-sw" style="background:#993f1f"></span></span></div><div class="te-mock__row"><span class="te-lbl">Terra Pale</span><span class="te-color"><span class="te-hex">#FDF0E9</span><span class="te-sw" style="background:#fdf0e9"></span></span></div><div class="te-mock__row"><span class="te-lbl">Bark 950</span><span class="te-color"><span class="te-hex">#0F0D0A</span><span class="te-sw" style="background:#0f0d0a"></span></span></div><div class="te-mock__row"><span class="te-lbl">Bark 900</span><span class="te-color"><span class="te-hex">#1A1713</span><span class="te-sw" style="background:#1a1713"></span></span></div><div class="te-mock__row"><span class="te-lbl">Bark 50</span><span class="te-color"><span class="te-hex">#F5F3EF</span><span class="te-sw" style="background:#f5f3ef"></span></span></div><div class="te-mock__row"><span class="te-lbl">Cream</span><span class="te-color"><span class="te-hex">#FAF8F4</span><span class="te-sw" style="background:#faf8f4"></span></span></div><div class="te-mock__row"><span class="te-lbl">White</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__grp">Badge, rating, and price colors</div><div class="te-mock__row"><span class="te-lbl">Sale badge background</span><span class="te-color"><span class="te-hex">#BF5B33</span><span class="te-sw" style="background:#bf5b33"></span></span></div><div class="te-mock__row"><span class="te-lbl">Staff pick badge background</span><span class="te-color"><span class="te-hex">#3F8060</span><span class="te-sw" style="background:#3f8060"></span></span></div><div class="te-mock__row"><span class="te-lbl">Active rating star</span><span class="te-color"><span class="te-hex">#F59E0B</span><span class="te-sw" style="background:#f59e0b"></span></span></div><div class="te-mock__row"><span class="te-lbl">Sale price</span><span class="te-color"><span class="te-hex">#DC2626</span><span class="te-sw" style="background:#dc2626"></span></span></div><div class="te-mock__row"><span class="te-lbl">Original (struck-through) price</span><span class="te-color"><span class="te-hex">#978A74</span><span class="te-sw" style="background:#978a74"></span></span></div><div class="te-mock__grp">Banner, top bar, and nav colors</div><div class="te-mock__row"><span class="te-lbl">Banner background</span><span class="te-color"><span class="te-hex">#3E3629</span><span class="te-sw" style="background:#3e3629"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner text</span><span class="te-color"><span class="te-hex">#D5CEC2</span><span class="te-sw" style="background:#d5cec2"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner link</span><span class="te-color"><span class="te-hex">#D9845E</span><span class="te-sw" style="background:#d9845e"></span></span></div><div class="te-mock__row"><span class="te-lbl">Top bar background</span><span class="te-color"><span class="te-hex">#1A1713</span><span class="te-sw" style="background:#1a1713"></span></span></div><div class="te-mock__row"><span class="te-lbl">Top bar text</span><span class="te-color"><span class="te-hex">#978A74</span><span class="te-sw" style="background:#978a74"></span></span></div><div class="te-mock__row"><span class="te-lbl">Nav background</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Nav text</span><span class="te-color"><span class="te-hex">#6B5E4F</span><span class="te-sw" style="background:#6b5e4f"></span></span></div><div class="te-mock__row"><span class="te-lbl">Nav search button</span><span class="te-color"><span class="te-hex">#C75A2A</span><span class="te-sw" style="background:#c75a2a"></span></span></div></div>

### 3. Fonts

| Font | Value |
| ---- | ------- |
| Body font | Source Sans 3 (weights 400, 600, 700) |
| Headings font | Playfair Display (weights 600, 400, 700) |
| Mono font | IBM Plex Mono (weight 400) |
| Root font size | `14` |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpUeXBvZ3JhcGh5KiAodGhlIHN0YW5kYXJkIENvcm5lcnN0b25lIHBhbmVsKSDihpIgKipCb2R5IHRleHQgZm9udCBmYW1pbHkqKiwgKipIZWFkaW5nIGZvbnQgZmFtaWx5KiosIGFuZCAqKkJvZHkgdGV4dCBmb250IHNpemUqKiAoaWQgYGZvbnRTaXplLXJvb3RgLCBkZWZhdWx0IGAxNGApLiBUaGUgbW9ubyBmYWNlIGFuZCB3ZWlnaHRzIGFyZSBzZXQgYnkgdGhlIHZhcmlhdGlvbi4gRm9ybWF0OiBhIEdvb2dsZS1mb250IHBpY2tlciBmb3IgZmFtaWxpZXM7IGEgbnVtYmVyIGZvciByb290IHNpemUu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Typography</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Body text font family</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Heading font family</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Body text font size</span><span class="te-dd"><span class="te-dd__v">14</span><span class="te-dd__b">▾</span></span></div></div>

### 4. Header & search

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIZWFkZXI6-->

<!--te-tbl:fCBTZXR0aW5nIHwgVmFsdWUgfAp8IC0tLS0tLS0gfCAtLS0tLSB8CnwgV2VsY29tZSB0ZXh0IHwgKihlbXB0eSkqIHwKfCBFbmFibGUgdm9pY2Ugc2VhcmNoIHwgT24gfAp8IFR5cGluZyBwaHJhc2VzIChwaXBlIFx8IHNlcGFyYXRlZCkgfCBgU2VhcmNoIGZvciBwb3dlciB0b29scy4uLmAgwrcgYEZpbmQgd2VsZGluZyBlcXVpcG1lbnQuLi5gIMK3IGBCcm93c2Ugc2FmZXR5IGdlYXIuLi5gIMK3IGBEaXNjb3ZlciBjb21wcmVzc29ycyAmIGFjY2Vzc29yaWVzLi4uYCB8-->

The four typing phrases rotate in the search box placeholder.

<!--te-src:PiAqKkN1c3RvbWl6ZSAod2VsY29tZSB0ZXh0KToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKldlbGNvbWUgVGV4dCoqIChpZCBgZXNob3BwaW5nLXdlbGNvbWUtdGV4dGApLiBTaG93cyBhIGdyZWV0aW5nIGluIHRoZSB0b3AgYmFyLiBGb3JtYXQ6IHBsYWluIHRleHQuIERlZmF1bHQ6ICooZW1wdHkpKi4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodm9pY2Ugc2VhcmNoKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNlYXJjaCog4oaSICoqRW5hYmxlIHZvaWNlIHNlYXJjaCoqIChpZCBgZXNob3BwaW5nLXNlYXJjaC12b2ljZWApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYE9uYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodHlwaW5nIHBocmFzZXMpOioqIFRoZW1lIEVkaXRvciDihpIgKmVTaG9wcGluZyBUaGVtZSDihpIgU2VhcmNoKiDihpIgKipUeXBpbmcgcGhyYXNlcyAocGlwZSB8IHNlcGFyYXRlZCkqKiAoaWQgYGVzaG9wcGluZy1zZWFyY2gtdHlwaW5nLXBocmFzZXNgKS4gRWFjaCBwaHJhc2Ugcm90YXRlcyBpbiB0aGUgc2VhcmNoIHBsYWNlaG9sZGVyLiBGb3JtYXQ6IHBocmFzZXMgc2VwYXJhdGVkIGJ5IGB8YC4gRGVmYXVsdCAoSW5kdXN0cmlhbCk6IGBTZWFyY2ggZm9yIHBvd2VyIHRvb2xzLi4ufEZpbmQgd2VsZGluZyBlcXVpcG1lbnQuLi58QnJvd3NlIHNhZmV0eSBnZWFyLi4ufERpc2NvdmVyIGNvbXByZXNzb3JzICYgYWNjZXNzb3JpZXMuLi5gLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Welcome Text</span><span class="te-desc">(empty)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__grp">Search</div><div class="te-mock__row"><span class="te-lbl">Enable voice search</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Typing phrases (pipe | separated)</span><span class="te-tx">Search for power tools</span></div></div>

### 5. Hero

The hero is on. The slides themselves come from the store's **Storefront → Home Page Carousel** — upload your slide images there. The theme does not require a fixed slide size; use a wide landscape image (JPG or WebP) and keep all slides the same dimensions so they line up.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2xpZGVzKToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipTdG9yZWZyb250IOKGkiBIb21lIFBhZ2UgQ2Fyb3VzZWwqKi4gQWRkL2VkaXQvcmVvcmRlciBzbGlkZXMsIGltYWdlcywgaGVhZGluZ3MsIGFuZCBidXR0b24gbGlua3MgdGhlcmUuIChOb3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY2Fyb3VzZWwgYmVoYXZpb3VyKToqKiBUaGVtZSBFZGl0b3Ig4oaSICpIb21lIFBhZ2UqIChzdGFuZGFyZCBDb3JuZXJzdG9uZSBwYW5lbCkg4oaSICoqU2hvdyBDYXJvdXNlbCoqIChpZCBgaG9tZXBhZ2Vfc2hvd19jYXJvdXNlbGAsIGRlZmF1bHQgYE9uYCksICoqU2hvdyBDYXJvdXNlbCBBcnJvd3MqKiAoaWQgYGhvbWVwYWdlX3Nob3dfY2Fyb3VzZWxfYXJyb3dzYCwgZGVmYXVsdCBgT25gKSwgKipTaG93IENhcm91c2VsIFBsYXkvUGF1c2UgQnV0dG9uKiogKGlkIGBob21lcGFnZV9zaG93X2Nhcm91c2VsX3BsYXlfcGF1c2VfYnV0dG9uYCwgZGVmYXVsdCBgT25gKSwgcGx1cyB0aGUgY2Fyb3VzZWwgY29sb3IgZmllbGRzIChgY2Fyb3VzZWwtdGl0bGUtY29sb3JgLCBgY2Fyb3VzZWwtYXJyb3ctY29sb3JgLCBgY2Fyb3VzZWwtZG90LWNvbG9yYCwg4oCmKS4gRm9ybWF0OiBvbi9vZmYgdG9nZ2xlcyArIGhleCBjb2xvcnMu-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub is-active">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Homepage</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show Carousel</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show Carousel Arrows</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show Carousel Play/Pause Button</span><span class="te-cb is-on"></span></div></div>

!!! tip "Slide ideas (suggestions only)"
    The demo's actual slides come from the Home Page Carousel. If you're building your own, these themes work well for an industrial catalog:

    | Slide | Image content | Heading | CTA |
    | :---: | ------------- | ------- | --- |
    | 1 | Workshop floor with tools | **Built to last. Priced to move.** | `Shop the catalog` |
    | 2 | Safety gear hero | **Safety first, every shift.** | `Browse safety` |
    | 3 | Bulk warehouse shot | **Bulk pricing on 100+ orders** | `Get a quote` |

### 6. Trust strip

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IFRydXN0IFN0cmlwKiogaXMgb24uIEZvdXIgaXRlbXMsIGVhY2ggYSB0aXRsZSBhbmQgYSBkZXNjcmlwdGlvbjo=-->

| Title | Description |
| ----- | ----------- |
| Made in USA | Fast & reliable shipping on all orders |
| Free Shipping | Shop with confidence, guaranteed |
| 4.8 Star Rating | Easy returns within 30 days |
| Expert Support | Available Mon-Sat, 9am-6pm |

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IFRydXN0IFN0cmlwKiogKGlkIGBlc2hvcHBpbmctc2hvdy10cnVzdC1zdHJpcGApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYE9uYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoaXRlbXMpOioqIFRoZW1lIEVkaXRvciDihpIgKmVTaG9wcGluZyBUaGVtZSDihpIgVHJ1c3QgU3RyaXAqIOKGkiAqKlRydXN0IFN0cmlwIEl0ZW1zKiogKGlkIGBlc2hvcHBpbmctdHJ1c3QtdGV4dGApLiBUaGUgc3RyaXAgYWx3YXlzIHNob3dzIGV4YWN0bHkgKio0IGZpeGVkIGljb25zKio7IHRoZSB0ZXh0IGNvbWVzIGZyb20gdGhpcyBmaWVsZCBhcyAqKjQgdGl0bGUvZGVzY3JpcHRpb24gcGFpcnMqKiA9IDggcGlwZS1zZXBhcmF0ZWQgc2VnbWVudHMgaW4gb3JkZXIgYFRpdGxlMXxEZXNjMXxUaXRsZTJ8RGVzYzJ8VGl0bGUzfERlc2MzfFRpdGxlNHxEZXNjNGAuIERlZmF1bHQgKEluZHVzdHJpYWwpOiBgTWFkZSBpbiBVU0F8RmFzdCAmIHJlbGlhYmxlIHNoaXBwaW5nIG9uIGFsbCBvcmRlcnN8RnJlZSBTaGlwcGluZ3xTaG9wIHdpdGggY29uZmlkZW5jZSwgZ3VhcmFudGVlZHw0LjggU3RhciBSYXRpbmd8RWFzeSByZXR1cm5zIHdpdGhpbiAzMCBkYXlzfEV4cGVydCBTdXBwb3J0fEF2YWlsYWJsZSBNb24tU2F0LCA5YW0tNnBtYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Trust Strip</span><span class="te-cb is-on"></span></div><div class="te-mock__grp">Trust Strip</div><div class="te-mock__row"><span class="te-lbl">Trust Strip Items</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">4 fixed icons</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">4 title/description pairs</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### 7. Featured Products

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IEZlYXR1cmVkIFByb2R1Y3RzKiogaXMgb24u-->

In **Catalog → Products** mark products as **Featured** — they auto-render in the slider.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IEZlYXR1cmVkIFByb2R1Y3RzKiogKGlkIGBlc2hvcHBpbmctc2hvdy1mZWF0dXJlZGApLiBGb3JtYXQ6IG9uL29mZi4gRGVmYXVsdDogYE9uYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY291bnQpOioqIFRoZW1lIEVkaXRvciDihpIgKkhvbWUgUGFnZSogKHN0YW5kYXJkIENvcm5lcnN0b25lIHBhbmVsKSDihpIgKipOdW1iZXIgb2YgRmVhdHVyZWQgUHJvZHVjdHMqKiAoaWQgYGhvbWVwYWdlX2ZlYXR1cmVkX3Byb2R1Y3RzX2NvdW50YCkuIEZvcm1hdDogc2VsZWN0Lg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggcHJvZHVjdHMpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKkNhdGFsb2cg4oaSIFByb2R1Y3RzKiog4oaSIGVkaXQgYSBwcm9kdWN0IOKGkiBtYXJrIGl0ICoqRmVhdHVyZWQqKi4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Featured Products</span><span class="te-cb is-on"></span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Homepage</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Number of Featured Products</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 8. New Arrivals

eShopping Theme → Homepage Sections → **Show New Arrivals** is on. Recently added products render here automatically.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IE5ldyBBcnJpdmFscyoqIChpZCBgZXNob3BwaW5nLXNob3ctbmV3YCkuIEZvcm1hdDogb24vb2ZmLiBEZWZhdWx0OiBgT25gLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoY291bnQpOioqIFRoZW1lIEVkaXRvciDihpIgKkhvbWUgUGFnZSog4oaSICoqTnVtYmVyIG9mIE5ldyBQcm9kdWN0cyoqIChpZCBgaG9tZXBhZ2VfbmV3X3Byb2R1Y3RzX2NvdW50YCkuIEZvcm1hdDogc2VsZWN0Lg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show New Arrivals</span><span class="te-cb is-on"></span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Homepage</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Number of New Products</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>

### 9. Bestselling Products

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IEJlc3QgU2VsbGVycyoqIGlzIG9uLg==-->

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IEJlc3QgU2VsbGVycyoqIChpZCBgZXNob3BwaW5nLXNob3ctYmVzdHNlbGxpbmdgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGBPbmAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Best Sellers</span><span class="te-cb is-on"></span></div></div>

!!! warning "Won't appear until you have sales data"
    The toggle is enabled, but the demo store has no bestseller / sales data yet, so the Bestselling slider does **not** appear on the live home page. It will show once the store accumulates sales and bestseller data.

### 10. Products by Category

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IHByb2R1Y3RzIGJ5IGNhdGVnb3J5KiogaXMgb24u-->

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBQcm9kdWN0cyBieSBDYXRlZ29yeSBzZWN0aW9uOg==-->

<!--te-tbl:fCBTZXR0aW5nIHwgVmFsdWUgfAp8IC0tLS0tLS0gfCAtLS0tLSB8CnwgQ2F0ZWdvcnkgSURzIHwgKihlbXB0eSDigJQgYXV0bzogc2hvd3MgYWxsIHRvcC1sZXZlbCBjYXRlZ29yaWVzKSogfAp8IEdyaWQgbGF5b3V0IHwgYDMsNCw2YCAodXAgdG8gMyBjYXRlZ29yaWVzLCA0IHByb2R1Y3RzIHBlciBjYXRlZ29yeSwgNiBzdWJjYXRlZ29yaWVzIHNob3duKSB8CnwgRGVmYXVsdCBhY3RpdmUgdGFiIHwgRmVhdHVyZWQgfAp8IFNob3cgQmVzdHNlbGxpbmcgdGFiIHwgT24gfAp8IFNob3cgRmVhdHVyZWQgdGFiIHwgT24gfAp8IFNob3cgTmV3IEFycml2YWxzIHRhYiB8IE9uIHwKfCBTaG93IFJldmlld3MgdGFiICh0aGUgIlRvcCBSYXRlZCIgdGFiKSB8IE9mZiB8-->

!!! note "Category IDs left empty on purpose"
    With no IDs entered, the section automatically pulls all top-level categories — no need to look up or type any IDs.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IENhdGVnb3JpZXMqKiAoaWQgYGVzaG9wcGluZy1zaG93LWNhdGVnb3JpZXNgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGBPbmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggY2F0ZWdvcmllcyk6KiogVGhlbWUgRWRpdG9yIOKGkiAqZVNob3BwaW5nIFRoZW1lIOKGkiBQcm9kdWN0cyBieSBDYXRlZ29yeSog4oaSICoqQ2F0ZWdvcnkgSURzIChjb21tYSBzZXBhcmF0ZWQsIGxlYXZlIGVtcHR5IGZvciBhdXRvLWRldGVjdCkqKiAoaWQgYGVzaG9wcGluZy1wYmNzdC1jYXRJRHNgKS4gRm9ybWF0OiBjb21tYS1zZXBhcmF0ZWQgY2F0ZWdvcnkgSURzOyBlbXB0eSA9IGF1dG8tZGV0ZWN0IGFsbCB0b3AtbGV2ZWwgY2F0ZWdvcmllcy4gRGVmYXVsdDogKihlbXB0eSkqLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoZ3JpZCk6Kiogc2FtZSBzZWN0aW9uIOKGkiAqKkdyaWQgbGF5b3V0OiBjYXRlZ29yaWVzLHByb2R1Y3RzLHN1YmNhdGVnb3JpZXMgKGUuZy4gMyw0LDYpKiogKGlkIGBlc2hvcHBpbmctcGJjc3QtZ3JpZGApLiBGb3JtYXQ6IHRocmVlIGNvbW1hLXNlcGFyYXRlZCBudW1iZXJzIGBkLHQsc2AgPSBudW1iZXIgb2YgKipjYXRlZ29yaWVzICh0YWJzKSoqLCAqKnByb2R1Y3RzIHBlciBjYXRlZ29yeSoqLCBhbmQgKipzdWJjYXRlZ29yaWVzKiogc2hvd24uIERlZmF1bHQgKEluZHVzdHJpYWwpOiBgMyw0LDZgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoYWN0aXZlIHRhYik6Kiogc2FtZSBzZWN0aW9uIOKGkiAqKkRlZmF1bHQgYWN0aXZlIHRhYioqIChpZCBgZXNob3BwaW5nLXBiY3N0LWFjdGl2ZWApLiBGb3JtYXQ6IHNlbGVjdCDigJQgYGZlYXR1cmVkYCwgYGJlc3RzZWxsaW5nYCwgYG5ld2VzdGAsIG9yIGBhdmdjdXN0b21lcnJldmlld2AgKFRvcCBSYXRlZCkuIERlZmF1bHQ6IGBmZWF0dXJlZGAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodGFiIHRvZ2dsZXMpOioqIHNhbWUgc2VjdGlvbiDihpIgKipTaG93IEJlc3RzZWxsaW5nIHRhYioqIChpZCBgZXNob3BwaW5nLXBiY3N0LXNob3ctYmVzdHNlbGxpbmdgLCBkZWZhdWx0IGBPbmApLCAqKlNob3cgRmVhdHVyZWQgdGFiKiogKGlkIGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1mZWF0dXJlZGAsIGRlZmF1bHQgYE9uYCksICoqU2hvdyBOZXcgdGFiKiogKGlkIGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1uZXdgLCBkZWZhdWx0IGBPZmZgIGluIHRoZW1lIGRlZmF1bHRzIOKAlCBgT25gIGZvciB0aGUgSW5kdXN0cmlhbCBkZW1vKSwgKipTaG93IFJldmlld3MgdGFiKiogKGlkIGBlc2hvcHBpbmctcGJjc3Qtc2hvdy1yZXZpZXdzYCwgZGVmYXVsdCBgT2ZmYCkuIEZvcm1hdDogb24vb2ZmLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Categories</span><span class="te-cb is-on"></span></div><div class="te-mock__grp">Products by Category</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Category IDs (comma separated, leave empty for auto-detect)</span><span class="te-desc">(empty — auto: shows all top-level categories)</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Grid layout: categories,products,subcategories (e.g. 3,4,6)</span><span class="te-desc">3,4,6 (up to 3 categories, 4 products per category, 6 subcategories shown)</span></span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">categories (tabs)</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">products per category</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">subcategories</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Default active tab</span><span class="te-dd"><span class="te-dd__v">featured</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Show Bestselling tab</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show Featured tab</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show New tab</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Show Reviews tab</span><span class="te-cb"></span></div></div>

### 11. Brands carousel

eShopping Theme → Homepage Sections → **Homepage Brands Limit**: `12`. Upload brand logos in **Catalog → Brands** — transparent PNGs work best, and keeping all logos a consistent size helps them sit evenly in the carousel.

<!--te-src:PiAqKkN1c3RvbWl6ZSAobGltaXQpOioqIFRoZW1lIEVkaXRvciDihpIgKmVTaG9wcGluZyBUaGVtZSDihpIgSG9tZXBhZ2UgU2VjdGlvbnMqIOKGkiAqKkhvbWVwYWdlIEJyYW5kcyBMaW1pdCoqIChpZCBgZXNob3BwaW5nLWhvbWVwYWdlLWJyYW5kcy1saW1pdGApLiBGb3JtYXQ6IG51bWJlciAobWF4IGJyYW5kcyBzaG93bikuIERlZmF1bHQ6IGAxMmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAobG9nb3MpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKkNhdGFsb2cg4oaSIEJyYW5kcyoqLiBBZGQgYnJhbmRzIGFuZCB1cGxvYWQgZWFjaCBicmFuZCdzIGxvZ28gaW1hZ2UgdGhlcmUuIChOb3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Homepage Brands Limit</span><span class="te-dd"><span class="te-dd__v">12</span><span class="te-dd__b">▾</span></span></div></div>
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub is-active">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 12. Blog posts

Blog posts count: `3`. This count is set in the standard **Homepage** Theme-Editor panel (not the eShopping Theme panel). Posts come from **Storefront → Blog**.

<!--te-src:PiAqKkN1c3RvbWl6ZSAocG9zdHMpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKlN0b3JlZnJvbnQg4oaSIEJsb2cqKi4gV3JpdGUvcHVibGlzaCBwb3N0cyB0aGVyZS4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub is-active">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

### 13. Newsletter

<!--te-lead:ZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyDihpIgKipTaG93IE5ld3NsZXR0ZXIqKiBpcyBvbi4gVGhlIGhlYWRpbmcgYW5kIGRlc2NyaXB0aW9uICh0aGUgYDxlbT5gIHdyYXBzIHRoZSBpdGFsaWMgZW1waGFzaXMpOg==-->

- **Heading:** Stay Updated with *Our Newsletter*
- **Description:** Product launches, field tips, and exclusive offers in your inbox.

The signup writes to **Customers → Subscribers**.

<!--te-src:PiAqKkN1c3RvbWl6ZSAoc2hvdy9oaWRlKToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEhvbWVwYWdlIFNlY3Rpb25zKiDihpIgKipTaG93IE5ld3NsZXR0ZXIqKiAoaWQgYGVzaG9wcGluZy1zaG93LW5ld3NsZXR0ZXJgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGBPbmAuIChBbHNvIHJlcXVpcmVzIHRoZSBzdG9yZS1sZXZlbCAqU2hvdyBuZXdzbGV0dGVyKiBzZXR0aW5nIHRvIGJlIG9uLik=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAodGV4dCk6KiogVGhlbWUgRWRpdG9yIOKGkiAqZVNob3BwaW5nIFRoZW1lIOKGkiBIb21lcGFnZSBTZWN0aW9ucyog4oaSICoqTmV3c2xldHRlciBTaWdudXAgVGV4dCoqIChpZCBgZXNob3BwaW5nLW5ld3NsZXR0ZXItdGV4dGApLiBGb3JtYXQ6IGBIZWFkaW5nfERlc2NyaXB0aW9uYCwgc3BsaXQgb24gYSBzaW5nbGUgYHxgLiBUaGUgKipoZWFkaW5nIHN1cHBvcnRzIGlubGluZSBIVE1MKiogKGUuZy4gYDxlbT7igKY8L2VtPmAgZm9yIHRoZSBpdGFsaWMgZW1waGFzaXMpOyB0aGUgZGVzY3JpcHRpb24gaXMgcGxhaW4gdGV4dC4gRGVmYXVsdCAoSW5kdXN0cmlhbCk6IGBTdGF5IFVwZGF0ZWQgd2l0aCA8ZW0+T3VyIE5ld3NsZXR0ZXI8L2VtPnxQcm9kdWN0IGxhdW5jaGVzLCBmaWVsZCB0aXBzLCBhbmQgZXhjbHVzaXZlIG9mZmVycyBpbiB5b3VyIGluYm94LmA=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Homepage Sections</div><div class="te-mock__row"><span class="te-lbl">Show Newsletter</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Newsletter Signup Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">heading supports inline HTML</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### 14. Marketing blocks (AI HTML Generator | PapaThemes via Page Builder)

The Industrial demo home page has **five** content blocks built with the **AI HTML Generator | PapaThemes** widget, plus a sixth widget for the footer tagline. These are placed through Page Builder, not theme settings — they require the PapaThemes app installed and arrive with the demo widget import.

>
> | Block | Region · sort | Exact HTML |
> | ----- | ------------- | ---------- |
> | Why Choose Us (value-prop callout, "Industrial Tools That Last. Pricing That…") | `home_below_products_by_category` · 0 | [Why Choose Us](widgets-papathemes.md#why-choose-us) |
> | Customer Reviews (social proof) | `home_below_products_by_category` · 1 | [Customer Reviews](widgets-papathemes.md#customer-reviews) |
> | Resources (guide cards) | `home_below_products_by_category` · 2 | [Resources](widgets-papathemes.md#resources) |
> | About (SEO intro, "Your Complete Industrial Supply Source") | `home_below_newsletter` · 0 | [About](widgets-papathemes.md#about) |
> | Talk to an Expert (contact CTA) | `home_below_newsletter` · 1 | [Talk to an Expert](widgets-papathemes.md#talk-to-an-expert) |
> | Footer tagline | `eshopping_footer_description--global` | [Footer tagline](widgets-papathemes.md#footer-tagline) |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBTdG9yZWZyb250IOKGkiAqKk15IFRoZW1lcyDihpIgQ3VzdG9taXplKiogKFBhZ2UgQnVpbGRlcikg4oaSIGNsaWNrIHRoZSBibG9jayDihpIgZWRpdCB0aGUgKipIVE1MIENvbnRlbnQqKiBmaWVsZCAod2lkZ2V0IHNjaGVtYSBpZCBgY29udGVudGAsIHR5cGUgYGNvZGVgL2h0bWwpIOKGkiAqKlNhdmUqKi4gVGhlIGV4YWN0IEhUTUwgZm9yIGVhY2ggYmxvY2sgbGl2ZXMgaW4gdGhlIGNhbm9uaWNhbCByZWZlcmVuY2Ug4oCUIGNvcHkvcGFzdGUgZnJvbSB0aGVyZTo=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

??? example "Exact demo HTML (Industrial) — Why Choose Us, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-yofvc0ew {
        --papathemes-ai-widget-yofvc0ew-white: #ffffff;
        --papathemes-ai-widget-yofvc0ew-cream: #f8fafc;
        --papathemes-ai-widget-yofvc0ew-bark-100: #f1f5f9;
        --papathemes-ai-widget-yofvc0ew-bark-200: #e2e8f0;
        --papathemes-ai-widget-yofvc0ew-bark-400: #94a3b8;
        --papathemes-ai-widget-yofvc0ew-bark-500: #64748b;
        --papathemes-ai-widget-yofvc0ew-bark-700: #334155;
        --papathemes-ai-widget-yofvc0ew-bark-800: #1e293b;
        --papathemes-ai-widget-yofvc0ew-bark-900: #0f172a;
        --papathemes-ai-widget-yofvc0ew-terra: #bf5b33;
        --papathemes-ai-widget-yofvc0ew-terra-light: #d9845e;
        --papathemes-ai-widget-yofvc0ew-terra-dark: #993f1f;
        --papathemes-ai-widget-yofvc0ew-terra-pale: #fdf0e9;
        --papathemes-ai-widget-yofvc0ew-accent: #f59e0b;
        --papathemes-ai-widget-yofvc0ew-accent-soft: #fef3c7;
        --papathemes-ai-widget-yofvc0ew-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-yofvc0ew-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-yofvc0ew *,
    .papathemes-ai-widget-yofvc0ew *::before,
    .papathemes-ai-widget-yofvc0ew *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-yofvc0ew-section {
        padding: 32px 20px 0;
    }
    
    .papathemes-ai-widget-yofvc0ew-card {
        background: var(--papathemes-ai-widget-yofvc0ew-white);
        border: 1px solid var(--papathemes-ai-widget-yofvc0ew-bark-100);
        border-radius: 8px;
        overflow: hidden;
    }
    
    .papathemes-ai-widget-yofvc0ew-inner {
        display: grid;
        grid-template-columns: 1fr 1fr;
        min-height: 360px;
    }
    
    .papathemes-ai-widget-yofvc0ew-visual {
        position: relative;
        background:
            linear-gradient(135deg, var(--papathemes-ai-widget-yofvc0ew-bark-900) 0%, var(--papathemes-ai-widget-yofvc0ew-bark-800) 100%);
        box-shadow: 0 1px 0 rgba(255, 255, 255, 0.04) inset;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        min-height: 260px;
    }
    
    .papathemes-ai-widget-yofvc0ew-visual::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse 70% 100% at 90% 50%, rgba(245, 158, 11, 0.14), transparent 70%),
            radial-gradient(ellipse 40% 60% at 0% 0%, rgba(255, 255, 255, 0.04), transparent 60%);
        pointer-events: none;
    }
    
    .papathemes-ai-widget-yofvc0ew-visual::after {
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
    
    .papathemes-ai-widget-yofvc0ew-stats {
        position: relative;
        z-index: 2;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        padding: 36px;
    }
    
    .papathemes-ai-widget-yofvc0ew-stat {
        text-align: center;
        padding: 18px;
        background: rgba(255, 255, 255, .06);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, .08);
    }
    
    .papathemes-ai-widget-yofvc0ew-stat-num {
        font-family: var(--papathemes-ai-widget-yofvc0ew-font-heading);
        font-size: 28px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-yofvc0ew-cream);
        line-height: 1;
        margin-bottom: 3px;
    }
    
    .papathemes-ai-widget-yofvc0ew-stat-num span {
        color: var(--papathemes-ai-widget-yofvc0ew-accent);
    }
    
    .papathemes-ai-widget-yofvc0ew-stat-label {
        font-family: var(--papathemes-ai-widget-yofvc0ew-font-body);
        font-size: 10px;
        color: var(--papathemes-ai-widget-yofvc0ew-bark-400);
        text-transform: uppercase;
        letter-spacing: .08em;
        font-weight: 600;
    }
    
    .papathemes-ai-widget-yofvc0ew-content {
        padding: 36px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .papathemes-ai-widget-yofvc0ew-eyebrow {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: var(--papathemes-ai-widget-yofvc0ew-font-body);
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: .14em;
        font-weight: 700;
        color: var(--papathemes-ai-widget-yofvc0ew-bark-700);
        margin-bottom: 10px;
    }
    
    .papathemes-ai-widget-yofvc0ew-eyebrow::before {
        content: "";
        width: 24px;
        height: 2px;
        background: var(--papathemes-ai-widget-yofvc0ew-accent);
    }
    
    .papathemes-ai-widget-yofvc0ew-heading {
        font-family: var(--papathemes-ai-widget-yofvc0ew-font-heading);
        font-size: 20px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-yofvc0ew-bark-900);
        margin-bottom: 14px;
        line-height: 1.25;
    }
    
    .papathemes-ai-widget-yofvc0ew-heading em {
        font-style: italic;
        font-weight: 400;
        color: var(--papathemes-ai-widget-yofvc0ew-bark-500);
    }
    
    .papathemes-ai-widget-yofvc0ew-desc {
        font-family: var(--papathemes-ai-widget-yofvc0ew-font-body);
        font-size: 12px;
        color: var(--papathemes-ai-widget-yofvc0ew-bark-500);
        line-height: 1.7;
        margin-bottom: 24px;
    }
    
    .papathemes-ai-widget-yofvc0ew-features {
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    
    .papathemes-ai-widget-yofvc0ew-feat {
        display: flex;
        gap: 12px;
        align-items: flex-start;
    }
    
    .papathemes-ai-widget-yofvc0ew-feat-icon {
        width: 38px;
        height: 38px;
        border-radius: 6px;
        background: var(--papathemes-ai-widget-yofvc0ew-accent-soft);
        border: 1px solid var(--papathemes-ai-widget-yofvc0ew-bark-200);
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--papathemes-ai-widget-yofvc0ew-accent);
        flex-shrink: 0;
    }
    
    .papathemes-ai-widget-yofvc0ew-feat-icon svg {
        width: 17px;
        height: 17px;
    }
    
    .papathemes-ai-widget-yofvc0ew-feat-title {
        font-family: var(--papathemes-ai-widget-yofvc0ew-font-body);
        font-size: 12px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-yofvc0ew-bark-800);
        margin-bottom: 1px;
    }
    
    .papathemes-ai-widget-yofvc0ew-feat-desc {
        font-family: var(--papathemes-ai-widget-yofvc0ew-font-body);
        font-size: 11px;
        color: var(--papathemes-ai-widget-yofvc0ew-bark-500);
        line-height: 1.45;
    }
    
    @media (max-width: 1023px) {
        .papathemes-ai-widget-yofvc0ew-inner {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-yofvc0ew-section {
            padding: 24px 10px 0;
        }
    
        .papathemes-ai-widget-yofvc0ew-stats {
            padding: 24px;
            gap: 12px;
        }
    
        .papathemes-ai-widget-yofvc0ew-content {
            padding: 24px;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-yofvc0ew">
        <div class="papathemes-ai-widget-yofvc0ew-section">
            <div class="papathemes-ai-widget-yofvc0ew-card">
                <div class="papathemes-ai-widget-yofvc0ew-inner">
                    <div class="papathemes-ai-widget-yofvc0ew-visual">
                        <div class="papathemes-ai-widget-yofvc0ew-stats">
                            <div class="papathemes-ai-widget-yofvc0ew-stat">
                                <div class="papathemes-ai-widget-yofvc0ew-stat-num">15<span>+</span></div>
                                <div class="papathemes-ai-widget-yofvc0ew-stat-label">YEARS IN INDUSTRIAL</div>
                            </div>
                            <div class="papathemes-ai-widget-yofvc0ew-stat">
                                <div class="papathemes-ai-widget-yofvc0ew-stat-num">3,500<span>+</span></div>
                                <div class="papathemes-ai-widget-yofvc0ew-stat-label">INDUSTRIAL SKUS</div>
                            </div>
                            <div class="papathemes-ai-widget-yofvc0ew-stat">
                                <div class="papathemes-ai-widget-yofvc0ew-stat-num">8M<span>+</span></div>
                                <div class="papathemes-ai-widget-yofvc0ew-stat-label">Orders Shipped</div>
                            </div>
                            <div class="papathemes-ai-widget-yofvc0ew-stat">
                                <div class="papathemes-ai-widget-yofvc0ew-stat-num">99<span>%</span></div>
                                <div class="papathemes-ai-widget-yofvc0ew-stat-label">Customer Satisfaction</div>
                            </div>
                        </div>
                    </div>
                    <div class="papathemes-ai-widget-yofvc0ew-content">
                        <div class="papathemes-ai-widget-yofvc0ew-eyebrow">Why Choose Us</div>
                        <h2 data-localized="1" data-localized="1" class="papathemes-ai-widget-yofvc0ew-heading">Industrial Tools That Last. <em>Pricing That Works.</em></h2>
                        <p class="papathemes-ai-widget-yofvc0ew-desc">From welding gear to power tools and shop supplies — every product is stocked for fast dispatch and tested to keep your jobsite running.</p>
                        <div class="papathemes-ai-widget-yofvc0ew-features">
                            <div class="papathemes-ai-widget-yofvc0ew-feat">
                                <div class="papathemes-ai-widget-yofvc0ew-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16zM12 4.15 18.4 7.8 12 11.45 5.6 7.8 12 4.15zM5 9.5l6 3.43v6.94l-6-3.43V9.5zm8 10.37v-6.94l6-3.43v6.94l-6 3.43z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-yofvc0ew-feat-title">Heavy-Duty Built</div>
                                    <div class="papathemes-ai-widget-yofvc0ew-feat-desc">Tools rated for daily commercial use, with cushioned grips and steel construction that outlast cheap alternatives.</div>
                                </div>
                            </div>
                            <div class="papathemes-ai-widget-yofvc0ew-feat">
                                <div class="papathemes-ai-widget-yofvc0ew-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2a3 3 0 0 0 6 0h6a3 3 0 0 0 6 0h2v-5l-3-4zM6 18.5A1.5 1.5 0 1 1 7.5 17 1.5 1.5 0 0 1 6 18.5zm13.5-9 1.96 2.5H17V9.5h2.5zM18 18.5A1.5 1.5 0 1 1 19.5 17 1.5 1.5 0 0 1 18 18.5z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-yofvc0ew-feat-title">Fast Bulk Fulfillment</div>
                                    <div class="papathemes-ai-widget-yofvc0ew-feat-desc">Same-day dispatch on stock items and case pricing trusted by 9,000+ contractors and shops.</div>
                                </div>
                            </div>
                            <div class="papathemes-ai-widget-yofvc0ew-feat">
                                <div class="papathemes-ai-widget-yofvc0ew-feat-icon">
                                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M17 8C8 10 5.9 16.17 3.82 21.34l1.89.66.95-2.3c.48.17.98.3 1.34.3C19 20 22 3 22 3c-1 2-8 2.25-13 3.25S2 11.5 2 13.5s1.75 3.75 1.75 3.75C7 8 17 8 17 8z"/></svg>
                                </div>
                                <div>
                                    <div class="papathemes-ai-widget-yofvc0ew-feat-title">Pro-Grade Warranty</div>
                                    <div class="papathemes-ai-widget-yofvc0ew-feat-desc">Lifetime guarantees on hand tools, multi-year coverage on power tools — built to back our quality.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    ```

??? example "Exact demo HTML (Industrial) — Customer Reviews, paste into the widget's HTML Content field"

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
                        <p class="papathemes-ai-widget-pkg1-r-text">Switched our entire fab shop to their welding gear. Better arc stability and longer consumable life than the brand we used for years.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #334155, #1e293b)">DM</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Dana M.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Shop Foreman</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 week ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">The cordless drills hold a charge through a full day on the jobsite. Cases of fasteners ship next day every time.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">EK</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Erin K.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Contractor</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">2 weeks ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">PPE arrives on a pallet, on time, every time. Volume pricing keeps our safety budget predictable.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">RT</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Ray T.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Plant Manager</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">3 weeks ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Right-spec replacement parts cut our downtime by 30%. Reordering by the case is effortless.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #334155, #1e293b)">SP</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Sofia P.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Maintenance Lead</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 month ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Hoods and gloves shipped same day when I ran low before a big project. Saved my deadline.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #475569, #334155)">JL</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Jordan L.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Welder</span>
                            </div>
                        </footer>
                    </article>
    
                    <article class="papathemes-ai-widget-pkg1-review">
                        <span class="papathemes-ai-widget-pkg1-quote-bg" aria-hidden="true">&ldquo;</span>
                        <div class="papathemes-ai-widget-pkg1-r-meta">
                            <div class="papathemes-ai-widget-pkg1-r-stars"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg></div>
                            <span class="papathemes-ai-widget-pkg1-r-ago">1 month ago</span>
                        </div>
                        <p class="papathemes-ai-widget-pkg1-r-text">Power tools arrive calibrated and ready. No more lost time on jobsite re-spec.</p>
                        <footer class="papathemes-ai-widget-pkg1-r-author">
                            <div class="papathemes-ai-widget-pkg1-avatar" style="background:linear-gradient(135deg, #1e293b, #0f172a)">MA</div>
                            <div class="papathemes-ai-widget-pkg1-r-id">
                                <strong class="papathemes-ai-widget-pkg1-r-name">Marcus A.<span class="papathemes-ai-widget-pkg1-r-check" aria-label="Verified buyer" title="Verified buyer"><svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg></span></strong>
                                <span class="papathemes-ai-widget-pkg1-r-role">Site Supervisor</span>
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
                                <span class="papathemes-ai-widget-pkg1-r-role">Shop Foreman</span>
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

??? example "Exact demo HTML (Industrial) — Resources, paste into the widget's HTML Content field"

    ```html
    
    <style>
    .papathemes-ai-widget-i7iwdj7m {
        --papathemes-ai-widget-i7iwdj7m-white: #ffffff;
        --papathemes-ai-widget-i7iwdj7m-bark-100: #f1f5f9;
        --papathemes-ai-widget-i7iwdj7m-bark-500: #64748b;
        --papathemes-ai-widget-i7iwdj7m-bark-800: #1e293b;
        --papathemes-ai-widget-i7iwdj7m-bark-900: #0f172a;
        --papathemes-ai-widget-i7iwdj7m-terra: #bf5b33;
        --papathemes-ai-widget-i7iwdj7m-terra-dark: #993f1f;
        --papathemes-ai-widget-i7iwdj7m-terra-pale: #fdf0e9;
        --papathemes-ai-widget-i7iwdj7m-forest-700: #15803d;
        --papathemes-ai-widget-i7iwdj7m-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-i7iwdj7m-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-i7iwdj7m *,
    .papathemes-ai-widget-i7iwdj7m *::before,
    .papathemes-ai-widget-i7iwdj7m *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-i7iwdj7m-section {
        padding: 32px 20px 0;
    }
    
    .papathemes-ai-widget-i7iwdj7m-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
    }
    
    .papathemes-ai-widget-i7iwdj7m-header-left {
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .papathemes-ai-widget-i7iwdj7m-sec-icon {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        background: var(--papathemes-ai-widget-i7iwdj7m-terra-pale);
        color: var(--papathemes-ai-widget-i7iwdj7m-terra);
    }
    
    .papathemes-ai-widget-i7iwdj7m-sec-icon svg {
        width: 18px;
        height: 18px;
    }
    
    .papathemes-ai-widget-i7iwdj7m-title {
        font-family: var(--papathemes-ai-widget-i7iwdj7m-font-heading);
        font-size: 18px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-i7iwdj7m-bark-900);
    }
    
    .papathemes-ai-widget-i7iwdj7m-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-top: 20px;
    }
    
    .papathemes-ai-widget-i7iwdj7m-card-link {
        text-decoration: none;
        color: inherit;
        display: block;
    }
    
    .papathemes-ai-widget-i7iwdj7m-card {
        background: var(--papathemes-ai-widget-i7iwdj7m-white);
        border: 1px solid var(--papathemes-ai-widget-i7iwdj7m-bark-100);
        border-radius: 8px;
        overflow: hidden;
        transition: all .35s;
    }
    
    a.papathemes-ai-widget-i7iwdj7m-card-link .papathemes-ai-widget-i7iwdj7m-card {
        cursor: pointer;
    }
    
    a.papathemes-ai-widget-i7iwdj7m-card-link .papathemes-ai-widget-i7iwdj7m-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 20px rgba(15, 13, 10, .08);
        border-color: transparent;
    }
    
    .papathemes-ai-widget-i7iwdj7m-thumb {
        aspect-ratio: 16/9;
        position: relative;
        display: block;
        align-items: center;
        justify-content: center;
        overflow: hidden;
        background-color: #f8fafc;
    }
    
    .papathemes-ai-widget-i7iwdj7m-thumb img {
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
    
    .papathemes-ai-widget-i7iwdj7m-thumb img.papathemes-ai-widget-i7iwdj7m-loaded {
        opacity: 1;
    }
    
    .papathemes-ai-widget-i7iwdj7m-type {
        position: absolute;
        top: 10px;
        left: 10px;
        padding: 3px 9px;
        background: rgba(0, 0, 0, .45);
        backdrop-filter: blur(6px);
        border-radius: 4px;
        font-family: var(--papathemes-ai-widget-i7iwdj7m-font-body);
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
    
    .papathemes-ai-widget-i7iwdj7m-type svg {
        width: 10px;
        height: 10px;
    }
    
    .papathemes-ai-widget-i7iwdj7m-body {
        padding: 18px;
    }
    
    .papathemes-ai-widget-i7iwdj7m-body h3 {
        font-family: var(--papathemes-ai-widget-i7iwdj7m-font-body);
        font-size: 13px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-i7iwdj7m-bark-800);
        margin-bottom: 4px;
        line-height: 1.3;
        transition: color .2s;
    }
    
    a.papathemes-ai-widget-i7iwdj7m-card-link .papathemes-ai-widget-i7iwdj7m-card:hover .papathemes-ai-widget-i7iwdj7m-body h3 {
        color: var(--papathemes-ai-widget-i7iwdj7m-terra-dark);
    }
    
    .papathemes-ai-widget-i7iwdj7m-body p {
        font-family: var(--papathemes-ai-widget-i7iwdj7m-font-body);
        font-size: 11px;
        color: var(--papathemes-ai-widget-i7iwdj7m-bark-500);
        line-height: 1.5;
    }
    
    @media (max-width: 1023px) {
        .papathemes-ai-widget-i7iwdj7m-grid {
            grid-template-columns: 1fr;
        }
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-i7iwdj7m-section {
            padding: 24px 10px 0;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-i7iwdj7m">
        <div class="papathemes-ai-widget-i7iwdj7m-section">
            <div class="papathemes-ai-widget-i7iwdj7m-header">
                <div class="papathemes-ai-widget-i7iwdj7m-header-left">
                    <div class="papathemes-ai-widget-i7iwdj7m-sec-icon">
                        <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M18 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm-5 2v6l-2.5-1.5L8 10V4h5zM6 20V4h.01L6 20h12V4l.01 16H6z"/></svg>
                    </div>
                    <h2 class="papathemes-ai-widget-i7iwdj7m-title">Industrial Resources &amp; Guides</h2>
                </div>
            </div>
            <div class="papathemes-ai-widget-i7iwdj7m-grid">
                <a href="https://eshopping-industrial-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-i7iwdj7m-card-link">
                    <div class="papathemes-ai-widget-i7iwdj7m-card">
                        <div class="papathemes-ai-widget-i7iwdj7m-thumb">
                            <img
                                class="papathemes-ai-widget-i7iwdj7m-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-w0rowd2tbb/product_images/uploaded_images/industrial-power-tool-selection.jpg?v=1779872198"
                                width="640"
                                height="360"
                                alt="Power tools on workbench"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-i7iwdj7m-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-i7iwdj7m-body">
                            <h3>Power Tool Selection Guide</h3>
                            <p>Choose the right drills, saws, and grinders for your trade and jobsite needs.</p>
                        </div>
                    </div>
                </a>
                <a href="https://eshopping-industrial-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-i7iwdj7m-card-link">
                    <div class="papathemes-ai-widget-i7iwdj7m-card">
                        <div class="papathemes-ai-widget-i7iwdj7m-thumb">
                            <img
                                class="papathemes-ai-widget-i7iwdj7m-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-w0rowd2tbb/product_images/uploaded_images/industrial-ppe-standards.jpg?v=1779872207"
                                width="640"
                                height="360"
                                alt="Industrial PPE gear"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-i7iwdj7m-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-i7iwdj7m-body">
                            <h3>PPE Standards &amp; Best Practices</h3>
                            <p>ANSI ratings, fit guides, and worker safety essentials for every job site.</p>
                        </div>
                    </div>
                </a>
                <a href="https://eshopping-industrial-demo.mybigcommerce.com/blog/" class="papathemes-ai-widget-i7iwdj7m-card-link">
                    <div class="papathemes-ai-widget-i7iwdj7m-card">
                        <div class="papathemes-ai-widget-i7iwdj7m-thumb">
                            <img
                                class="papathemes-ai-widget-i7iwdj7m-thumb-img"
                                data-src="https://cdn11.bigcommerce.com/s-w0rowd2tbb/product_images/uploaded_images/industrial-welding-equipment-setup.jpg?v=1779872221"
                                width="640"
                                height="360"
                                alt="Welding equipment"
                                loading="lazy"
                            />
                            <span class="papathemes-ai-widget-i7iwdj7m-type">
                                <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                                Guide
                            </span>
                        </div>
                        <div class="papathemes-ai-widget-i7iwdj7m-body">
                            <h3>Welding Equipment Setup</h3>
                            <p>Choose the right MIG, TIG, or stick welder for your shop and material.</p>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
    
    <script>
    (function(){
        var id = 'i7iwdj7m';
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

??? example "Exact demo HTML (Industrial) — About, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-i79zbp57 {
        --papathemes-ai-widget-i79zbp57-white: #ffffff;
        --papathemes-ai-widget-i79zbp57-bark-100: #f1f5f9;
        --papathemes-ai-widget-i79zbp57-bark-600: #475569;
        --papathemes-ai-widget-i79zbp57-bark-900: #0f172a;
        --papathemes-ai-widget-i79zbp57-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-i79zbp57-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 32px 20px 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-i79zbp57 *,
    .papathemes-ai-widget-i79zbp57 *::before,
    .papathemes-ai-widget-i79zbp57 *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-i79zbp57-section {
        background: var(--papathemes-ai-widget-i79zbp57-white);
        border: 1px solid var(--papathemes-ai-widget-i79zbp57-bark-100);
        border-radius: 8px;
        padding: 32px;
    }
    
    .papathemes-ai-widget-i79zbp57-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .papathemes-ai-widget-i79zbp57-title {
        font-family: var(--papathemes-ai-widget-i79zbp57-font-heading);
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--papathemes-ai-widget-i79zbp57-bark-900);
        text-align: center;
        margin-bottom: 16px;
        line-height: 1.3;
    }
    
    .papathemes-ai-widget-i79zbp57-text {
        font-family: var(--papathemes-ai-widget-i79zbp57-font-body);
        font-size: 0.86rem;
        color: var(--papathemes-ai-widget-i79zbp57-bark-600);
        line-height: 1.8;
        max-width: 860px;
        margin-left: auto;
        margin-right: auto;
        margin-bottom: 12px;
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-i79zbp57 {
            margin: 24px 10px 0;
        }
    
        .papathemes-ai-widget-i79zbp57-section {
            padding: 24px 18px;
        }
    
        .papathemes-ai-widget-i79zbp57-title {
            font-size: 1.15rem;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-i79zbp57">
        <div class="papathemes-ai-widget-i79zbp57-section">
            <div class="papathemes-ai-widget-i79zbp57-container">
                <h2 class="papathemes-ai-widget-i79zbp57-title">Your Complete Industrial Supply Source</h2>
                <p class="papathemes-ai-widget-i79zbp57-text">We supply the tools, welding gear, PPE, and shop supplies that keep contractors, fabricators, and maintenance teams moving. Our catalog spans hand tools, power tools, welding equipment, safety gear, and shop consumables — all stocked in cases and on pallets for fast, predictable reordering.</p>
                <p class="papathemes-ai-widget-i79zbp57-text">From hand tools to heavy welding equipment, every product is chosen to outlast the alternatives and keep your jobsite or shop running. Browse trusted brands and pro-grade gear used by thousands of trades professionals every day.</p>
            </div>
        </div>
    </div>
    ```

??? example "Exact demo HTML (Industrial) — Talk to an Expert, paste into the widget's HTML Content field"

    ```html
    <style>
    .papathemes-ai-widget-yqoflirz {
        --papathemes-ai-widget-yqoflirz-white: #ffffff;
        --papathemes-ai-widget-yqoflirz-cream: #f8fafc;
        --papathemes-ai-widget-yqoflirz-bark-200: #cbd5e1;
        --papathemes-ai-widget-yqoflirz-bark-300: #cbd5e1;
        --papathemes-ai-widget-yqoflirz-bark-400: #94a3b8;
        --papathemes-ai-widget-yqoflirz-bark-700: #334155;
        --papathemes-ai-widget-yqoflirz-bark-800: #1e293b;
        --papathemes-ai-widget-yqoflirz-bark-900: #0f172a;
        --papathemes-ai-widget-yqoflirz-bark-950: #060912;
        --papathemes-ai-widget-yqoflirz-terra: #bf5b33;
        --papathemes-ai-widget-yqoflirz-terra-dark: #993f1f;
        --papathemes-ai-widget-yqoflirz-terra-light: #d9845e;
        --papathemes-ai-widget-yqoflirz-font-heading: 'Inter', sans-serif;
        --papathemes-ai-widget-yqoflirz-font-body: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        width: 100%;
    }
    
    .papathemes-ai-widget-yqoflirz *,
    .papathemes-ai-widget-yqoflirz *::before,
    .papathemes-ai-widget-yqoflirz *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }
    
    .papathemes-ai-widget-yqoflirz-bar {
        margin: 32px 20px 0;
        background:
            linear-gradient(135deg, var(--papathemes-ai-widget-yqoflirz-bark-900) 0%, var(--papathemes-ai-widget-yqoflirz-bark-800) 100%);
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
    
    .papathemes-ai-widget-yqoflirz-bar::before {
        content: "";
        position: absolute;
        inset: 0;
        background:
            radial-gradient(ellipse 60% 90% at 92% 50%, rgba(191, 91, 51, 0.18), transparent 70%),
            radial-gradient(ellipse 40% 60% at 0% 0%, rgba(255, 255, 255, 0.04), transparent 60%);
        pointer-events: none;
    }
    
    .papathemes-ai-widget-yqoflirz-bar::after {
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
    
    .papathemes-ai-widget-yqoflirz-left {
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-yqoflirz-heading {
        font-family: var(--papathemes-ai-widget-yqoflirz-font-heading);
        font-size: 17px;
        font-weight: 600;
        color: var(--papathemes-ai-widget-yqoflirz-white);
        margin-bottom: 6px;
        letter-spacing: -0.01em;
    }
    
    .papathemes-ai-widget-yqoflirz-heading em {
        font-style: italic;
        font-weight: 400;
        // Hardcoded warm gold accent — universal premium signal, decoupled from
        // per-store terra-light (renders blue on Electronics #60a5fa).
        color: #fbbf24;
    }
    
    .papathemes-ai-widget-yqoflirz-desc {
        font-family: var(--papathemes-ai-widget-yqoflirz-font-body);
        font-size: 13px;
        line-height: 1.55;
        color: var(--papathemes-ai-widget-yqoflirz-bark-300);
        max-width: 60ch;
    }
    
    .papathemes-ai-widget-yqoflirz-btns {
        display: flex;
        gap: 10px;
        position: relative;
        z-index: 1;
    }
    
    .papathemes-ai-widget-yqoflirz-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 12px 24px;
        border-radius: 8px;
        font-family: var(--papathemes-ai-widget-yqoflirz-font-heading);
        font-size: 13px;
        font-weight: 600;
        text-decoration: none;
        transition: all .25s cubic-bezier(.16, 1, .3, 1);
        letter-spacing: 0.01em;
        border: none;
        cursor: pointer;
    }
    
    .papathemes-ai-widget-yqoflirz-btn svg {
        width: 15px;
        height: 15px;
        transition: transform .3s;
    }
    
    .papathemes-ai-widget-yqoflirz-btn--terra {
        background: var(--papathemes-ai-widget-yqoflirz-terra);
        color: var(--papathemes-ai-widget-yqoflirz-white);
    }
    
    .papathemes-ai-widget-yqoflirz-btn--terra:hover {
        background: var(--papathemes-ai-widget-yqoflirz-terra-dark);
        color: var(--papathemes-ai-widget-yqoflirz-white);
        box-shadow: 0 6px 24px rgba(191, 91, 51, .35);
        transform: translateY(-1px);
        text-decoration: none;
    }
    
    .papathemes-ai-widget-yqoflirz-btn--terra:hover svg {
        transform: translateX(3px);
    }
    
    .papathemes-ai-widget-yqoflirz-btn--ghost {
        border: 1px solid rgba(255, 255, 255, 0.22);
        color: var(--papathemes-ai-widget-yqoflirz-white);
        background: rgba(255, 255, 255, 0.04);
        backdrop-filter: blur(8px);
    }
    
    .papathemes-ai-widget-yqoflirz-btn--ghost:hover {
        border-color: rgba(255, 255, 255, 0.45);
        color: var(--papathemes-ai-widget-yqoflirz-white);
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-1px);
        text-decoration: none;
    }
    
    @media (max-width: 767px) {
        .papathemes-ai-widget-yqoflirz-bar {
            margin-left: 10px;
            margin-right: 10px;
            flex-direction: column;
            text-align: center;
            padding: 28px 24px;
        }
    
        .papathemes-ai-widget-yqoflirz-btns {
            flex-direction: column;
            width: 100%;
        }
    
        .papathemes-ai-widget-yqoflirz-btn {
            justify-content: center;
        }
    }
    </style>
    
    <div class="papathemes-ai-widget-yqoflirz">
        <div class="papathemes-ai-widget-yqoflirz-bar">
            <div class="papathemes-ai-widget-yqoflirz-left">
                <h3 class="papathemes-ai-widget-yqoflirz-heading">Need help spec’ing tools? <em>Talk to an Industrial Specialist</em></h3>
                <p class="papathemes-ai-widget-yqoflirz-desc">Our specialists help you spec the right welder, drill, or PPE for your jobsite. Call or chat anytime.</p>
            </div>
            <div class="papathemes-ai-widget-yqoflirz-btns">
                <a href="/contact-us/" class="papathemes-ai-widget-yqoflirz-btn papathemes-ai-widget-yqoflirz-btn--terra">
                    Request a Quote
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M12 4l-1.41 1.41L16.17 11H4v2h12.17l-5.58 5.59L12 20l8-8z"/></svg>
                </a>
                <a href="tel:18005550123" class="papathemes-ai-widget-yqoflirz-btn papathemes-ai-widget-yqoflirz-btn--ghost">
                    <svg aria-hidden="true" focusable="false" fill="currentColor" viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                    (800) 555-0123
                </a>
            </div>
        </div>
    </div>
    ```

??? example "Exact demo HTML (Industrial) — Footer tagline, paste into the widget's HTML Content field"

    ```html
    <span class="eshopping-footer-desc-text">eShopping Industrial Demo — Industrial tools, welding, safety, and shop supplies built to last.</span>
    ```
See the [PapaThemes marketing blocks reference](widgets-papathemes.md) for a clean copy-paste template per block and a per-store `<details>` with the verbatim demo HTML.

## Beyond the home page

These Industrial settings drive other pages and on-site widgets. They're set by the variation — listed here so you know what to expect.

### Top banner

eShopping Theme → Banner. Banner colors are listed in the Colors table above (dark `#3e3629` background, `#d5cec2` text, `#d9845e` link).

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEJhbm5lciog4oaSICoqQmFubmVyIEJhY2tncm91bmQqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItYmdgLCBkZWZhdWx0IGAjM2UzNjI5YCksICoqQmFubmVyIFRleHQgQ29sb3IqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItY29sb3JgLCBkZWZhdWx0IGAjZDVjZWMyYCksICoqQmFubmVyIExpbmsgQ29sb3IqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItbGlua2AsIGRlZmF1bHQgYCNkOTg0NWVgKS4gRm9ybWF0OiBoZXggY29sb3JzLiBUaGUgYmFubmVyICpjb250ZW50KiAodGhlIHByb21vdGlvbmFsIG1lc3NhZ2UpIGNvbWVzIGZyb20gdGhlIEJpZ0NvbW1lcmNlICoqcHJvbW8vYW5ub3VuY2VtZW50KiogcmVnaW9uLCBub3QgdGhlc2UgZmllbGRzLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Banner</div><div class="te-mock__row"><span class="te-lbl">Banner Background</span><span class="te-color"><span class="te-hex">#3E3629</span><span class="te-sw" style="background:#3e3629"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner Text Color</span><span class="te-color"><span class="te-hex">#D5CEC2</span><span class="te-sw" style="background:#d5cec2"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner Link Color</span><span class="te-color"><span class="te-hex">#D9845E</span><span class="te-sw" style="background:#d9845e"></span></span></div></div>

### Promo bar

- **Text:** Free Shipping $500+ — Free ground shipping on qualifying orders.
- **Button:** Shop Now → `/shipping/`

This is the sidebar promo card, not the top banner.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNpZGViYXIgUHJvbW8gQ2FyZCog4oaSICoqU2lkZWJhciBQcm9tbyBUZXh0KiogKGlkIGBlc2hvcHBpbmctcHJvbW8tdGV4dGApLiBGb3JtYXQ6IGBIZWFkaW5nfFN1YnRleHR8QnV0dG9uIGxhYmVsfEJ1dHRvbiBVUkxgLCBzcGxpdCBvbiBgfGAgKDQgc2VnbWVudHMpLiBEZWZhdWx0IChJbmR1c3RyaWFsKTogYEZyZWUgU2hpcHBpbmcgJDUwMCt8RnJlZSBncm91bmQgc2hpcHBpbmcgb24gcXVhbGlmeWluZyBvcmRlcnMufFNob3AgTm93fC9zaGlwcGluZy9gLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Sidebar Promo Card</div><div class="te-mock__row"><span class="te-lbl">Sidebar Promo Text</span><span class="te-tx">Free Shipping $500+|Free ground ship…</span></div></div>

### Cart free-shipping / reward goals

Progress goals shown in the cart drawer:

| Threshold | Reward |
| --------- | ------ |
| $50 | Free Shipping |
| $100 | 10% Off |
| $150 | Free Gift |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENhcnQgR29hbCBCYXIqIOKGkiAqKkdvYWwgaXRlbXMgKGFtb3VudHxpY29ufGxhYmVsLCBjb21tYS1zZXBhcmF0ZWQpKiogKGlkIGBlc2hvcHBpbmctY2FydC1nb2FsLWl0ZW1zYCkuIEZvcm1hdDogYSAqKmNvbW1hLXNlcGFyYXRlZCoqIGxpc3Qgb2YgZ29hbHM7IGVhY2ggZ29hbCBpcyBgYW1vdW50fGljb258bGFiZWxgICh0aGUgaWNvbiBpcyBvbmUgb2YgYHNoaXBwaW5nYCwgYGRpc2NvdW50YCwgYGdpZnRgKS4gRGVmYXVsdCAoSW5kdXN0cmlhbCk6IGA1MHxzaGlwcGluZ3xGcmVlIFNoaXBwaW5nLDEwMHxkaXNjb3VudHwxMCUgT2ZmLDE1MHxnaWZ0fEZyZWUgR2lmdGAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Cart Goal Bar</div><div class="te-mock__row"><span class="te-lbl">Goal items (amount|icon|label, comma-separated)</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">comma-separated</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### Cart cross-sell ("You May Also Like")

A "You May Also Like" cross-sell block appears in the shopping cart: up to **6** items on the full cart page and up to **4** items in the slide-out cart drawer.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENyb3NzLXNlbGwqIOKGkiAqKkNyb3NzLXNlbGwgcHJvZHVjdHMgKHBhZ2UsZHJhd2VyIOKAlCAwID0gb2ZmKSoqIChpZCBgZXNob3BwaW5nLWNyb3Nzc2VsbC1jb3VudGApLiBGb3JtYXQ6IHR3byBjb21tYS1zZXBhcmF0ZWQgbnVtYmVycyBgcGFnZSxkcmF3ZXJgIChzZXQgZWl0aGVyIHRvIGAwYCB0byBoaWRlIHRoYXQgcGxhY2VtZW50KS4gRGVmYXVsdCAoSW5kdXN0cmlhbCk6IGA2LDRgLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Cross-sell</div><div class="te-mock__row"><span class="te-lbl">Cross-sell products (page,drawer — 0 = off)</span><span class="te-tx">6,4</span></div></div>

### Product page (PDP)

Shipping / warranty strip:

| Title | Detail |
| ----- | ------ |
| Free Shipping | on orders over $500 |
| 1-Year Warranty | included with purchase |
| 30-Day Returns | hassle-free policy |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb2R1Y3QgUGFnZSAoUERQKSog4oaSICoqUERQIFNoaXBwaW5nIFRleHQqKiAoaWQgYGVzaG9wcGluZy1wZHAtc2hpcHBpbmctdGV4dGApLiBGb3JtYXQ6IGBUaXRsZXxEZXRhaWxgIHBhaXJzIHNwbGl0IG9uIGB8YCDigJQgMyBwYWlycyA9IDYgc2VnbWVudHMgaW4gb3JkZXIgYFRpdGxlMXxEZXRhaWwxfFRpdGxlMnxEZXRhaWwyfFRpdGxlM3xEZXRhaWwzYC4gRGVmYXVsdCAoSW5kdXN0cmlhbCk6IGBGcmVlIFNoaXBwaW5nfG9uIG9yZGVycyBvdmVyICQ1MDB8MS1ZZWFyIFdhcnJhbnR5fGluY2x1ZGVkIHdpdGggcHVyY2hhc2V8MzAtRGF5IFJldHVybnN8aGFzc2xlLWZyZWUgcG9saWN5YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Product Page (PDP)</div><div class="te-mock__row"><span class="te-lbl">PDP Shipping Text</span><span class="te-tx">Free Shipping|on orders over $500|1-…</span></div></div>

Warranty accordion:

| Section | Content |
| ------- | ------- |
| What's Covered | Manufacturing defects, material failures, broken welds, and faulty components under normal field use conditions. |
| What's Not Covered | Damage from misuse, improper maintenance, normal wear and tear, or unauthorized modifications. |
| How to Claim | Contact us with your order number and description of the issue. |
| Extended Warranty | Extend your coverage for additional protection. Contact us for details. |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb2R1Y3QgUGFnZSAoUERQKSog4oaSICoqUERQIFdhcnJhbnR5IFRleHQqKiAoaWQgYGVzaG9wcGluZy1wZHAtd2FycmFudHktdGV4dGApLiBGb3JtYXQ6IGBTZWN0aW9ufENvbnRlbnRgIHBhaXJzIHNwbGl0IG9uIGB8YCDigJQgdGhlIGRlbW8gdXNlcyA0IHBhaXJzID0gOCBzZWdtZW50cy4gRGVmYXVsdCAoSW5kdXN0cmlhbCk6IGBXaGF0J3MgQ292ZXJlZHzigKZ8V2hhdCdzIE5vdCBDb3ZlcmVkfOKApnxIb3cgdG8gQ2xhaW184oCmfEV4dGVuZGVkIFdhcnJhbnR5fOKApmAuIChBbHNvOiAqKlNob3cgRkFRIFRhYioqLCBpZCBgZXNob3BwaW5nLXBkcC1zaG93LWZhcS10YWJgLCBhbmQgKipTaG93IE1vYmlsZSBTdGlja3kgQWRkIHRvIENhcnQqKiwgaWQgYGVzaG9wcGluZy1wZHAtc2hvdy1tb2JpbGUtYXRjYCwgYm90aCBvbi9vZmYuKQ==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Product Page (PDP)</div><div class="te-mock__row"><span class="te-lbl">PDP Warranty Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show FAQ Tab</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show Mobile Sticky Add to Cart</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

**Frequently Bought Together:** shows `2` products, discount `0%`.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEZyZXF1ZW50bHkgQm91Z2h0IFRvZ2V0aGVyKiDihpIgKipGQlQgUHJvZHVjdHMgQ291bnQqKiAoaWQgYGVzaG9wcGluZy1mYnQtY291bnRgLCBzZWxlY3QgYDBgL2AxYC9gMmAvYDNgOyBgMGAgPSBvZmY7IGRlZmF1bHQgSW5kdXN0cmlhbCBgMmApIGFuZCAqKlZpc3VhbCBCdW5kbGUgRGlzY291bnQgJSoqIChpZCBgZXNob3BwaW5nLWZidC1kaXNjb3VudC1wZXJjZW50YCwgYSBudW1iZXIgdXNlZCBmb3IgYSAqZGlzcGxheS1vbmx5KiBidW5kbGUgZGlzY291bnQ7IGRlZmF1bHQgYDBgKS4gRm9ybWF0OiBzZWxlY3QgKyBudW1iZXIu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Frequently Bought Toget…</div><div class="te-mock__row"><span class="te-lbl">FBT Products Count</span><span class="te-dd"><span class="te-dd__v">2</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Visual Bundle Discount %</span><span class="te-dd"><span class="te-dd__v">0</span><span class="te-dd__b">▾</span></span></div></div>

### Urgency & social proof

- **Live view count** and **last order time** are both on.
- **Recent sales pop-ups** show on **all pages**, cycling through demo sales from California, Texas, Florida, New York, and Oregon.

<!--te-src:PiAqKkN1c3RvbWl6ZSAodXJnZW5jeSk6KiogVGhlbWUgRWRpdG9yIOKGkiAqZVNob3BwaW5nIFRoZW1lIOKGkiBVcmdlbmN5IFNpZ25hbHMgKFNvY2lhbCBQcm9vZikqIOKGkiAqKlNob3cgbGl2ZSB2aWV3IGNvdW50KiogKGlkIGBlc2hvcHBpbmctdXJnZW5jeS12aWV3LWNvdW50YCwgZGVmYXVsdCBgT25gKSBhbmQgKipTaG93IGxhc3Qgb3JkZXIgdGltZSoqIChpZCBgZXNob3BwaW5nLXVyZ2VuY3ktbGFzdC1vcmRlcmAsIGRlZmF1bHQgYE9uYCkuIFRoZSByYW5nZXMgYXJlICoqRmFrZSB2aWV3IGNvdW50IHJhbmdlOiBtaW4sbWF4KiogKGlkIGBlc2hvcHBpbmctdXJnZW5jeS12aWV3LXJhbmdlYCwgZGVmYXVsdCBgMywyNWApIGFuZCAqKkxhc3Qgb3JkZXIgdGltZSByYW5nZTogbWluLG1heCBob3VycyBhZ28qKiAoaWQgYGVzaG9wcGluZy11cmdlbmN5LW9yZGVyLXJhbmdlYCwgZGVmYXVsdCBgMSw0OGApLiBGb3JtYXQ6IG9uL29mZiArIGBtaW4sbWF4YCBudW1iZXIgcGFpcnMu-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAocmVjZW50IHNhbGVzIHBvcC11cHMpOioqIHNhbWUgcGFuZWwg4oaSICpSZWNlbnQgU2FsZXMgUG9wdXAqIOKGkiAqKlNob3cgb24gcGFnZXMqKiAoaWQgYGVzaG9wcGluZy1yZWNlbnQtc2FsZXMtcGFnZXNgLCBzZWxlY3QgYG5vbmVgL2BhbGxgL2Bob21lYC9gcHJvZHVjdGAvYGNhdGVnb3J5YDsgZGVmYXVsdCBJbmR1c3RyaWFsIGBhbGxgKSwgKipQb3B1cCB0aW1pbmc6IGRlbGF5LCBzaG93IGR1cmF0aW9uLCBwYXVzZSBiZXR3ZWVuLCBtYXggcG9wdXBzKiogKGlkIGBlc2hvcHBpbmctcmVjZW50LXNhbGVzLXRpbWluZ2AsIGRlZmF1bHQgYDUsNSwxNSw1YCksIGFuZCAqKlByb2R1Y3RzIChJRCBvciBTS1V8bG9jYXRpb258dGltZUFnbywgY29tbWEtc2VwYXJhdGVkKSoqIChpZCBgZXNob3BwaW5nLXJlY2VudC1zYWxlcy1pdGVtc2ApLiBGb3JtYXQ6IGVhY2ggc2FsZSBpcyBgcHJvZHVjdElEfGxvY2F0aW9ufHRpbWVBZ29gLCBzYWxlcyBjb21tYS1zZXBhcmF0ZWQuIERlZmF1bHQgKEluZHVzdHJpYWwpOiBgNzd8Q2FsaWZvcm5pYXwyIGhvdXJzIGFnbyw3OHxUZXhhc3wzNSBtaW4gYWdvLDc5fEZsb3JpZGF8NCBob3VycyBhZ28sODB8TmV3IFlvcmt8MSBob3VyIGFnbyw4MXxPcmVnb258NiBob3VycyBhZ29gLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Urgency Signals (Social…</div><div class="te-mock__row"><span class="te-lbl">Show live view count</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Show last order time</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Fake view count range: min,max</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Last order time range: min,max hours ago</span><span class="te-cb"></span></div><div class="te-mock__row"><span class="te-lbl">Show on pages</span><span class="te-tx">all</span></div><div class="te-mock__row"><span class="te-lbl">Popup timing: delay, show duration, pause between, max popups</span><span class="te-tx">5,5,15,5</span></div><div class="te-mock__row"><span class="te-lbl">Products (ID or SKU|location|timeAgo, comma-separated)</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

### Pop-ups

**Newsletter pop-up:**

- **Text:** Get 10% Off Your First Order — Sign up for our newsletter and receive an exclusive discount code.
- **Options:** shows after 20 seconds; reappears after 14 days.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIE5ld3NsZXR0ZXIgUG9wdXAqIOKGkiAqKk5ld3NsZXR0ZXIgQ29udGVudCDigJQgVGl0bGV8RGVzY3JpcHRpb24qKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1ubC10ZXh0YDsgbGVhdmUgZW1wdHkgdG8gZGlzYWJsZTsgZm9ybWF0IGBUaXRsZXxEZXNjcmlwdGlvbmApIGFuZCAqKlNob3cgYWZ0ZXIgKHNlY29uZHMpIHwgUmVwZWF0IGV2ZXJ5IChkYXlzKSoqIChpZCBgZXNob3BwaW5nLXBvcHVwLW5sLW9wdHNgOyBmb3JtYXQgYHNlY29uZHN8ZGF5c2ApLiBEZWZhdWx0IChJbmR1c3RyaWFsKTogYEdldCAxMCUgT2ZmIFlvdXIgRmlyc3QgT3JkZXJ8U2lnbiB1cCBmb3Igb3VyIG5ld3NsZXR0ZXIgYW5kIHJlY2VpdmUgYW4gZXhjbHVzaXZlIGRpc2NvdW50IGNvZGUuYCBhbmQgYDIwfDE0YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Newsletter Popup</div><div class="te-mock__row"><span class="te-lbl">Newsletter Content — Title|Description</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show after (seconds) | Repeat every (days)</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

**Promo pop-up:**

- **Heading:** Spring Sale
- **Body:** Get 15% off your entire order with the code below.
- **Code:** `SPRING15`
- **Button:** Shop Now → `/`
- **Options:** shows after 5 seconds; reappears after 3 days.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFByb21vdGlvbiBQb3B1cCog4oaSICoqUHJvbW8gQ29udGVudCDigJQgVGl0bGV8RGVzY3JpcHRpb258Q291cG9uIENvZGV8QnV0dG9uIFRleHR8QnV0dG9uIFVSTCoqIChpZCBgZXNob3BwaW5nLXBvcHVwLXByb21vLXRleHRgOyBsZWF2ZSBlbXB0eSB0byBkaXNhYmxlKSBhbmQgKipTaG93IGFmdGVyIChzZWNvbmRzKSB8IFJlcGVhdCBldmVyeSAoZGF5cykgfCBTdGFydCBkYXRlIHwgRW5kIGRhdGUqKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1wcm9tby1vcHRzYCkuIERlZmF1bHQgKEluZHVzdHJpYWwpOiBgU3ByaW5nIFNhbGV8R2V0IDE1JSBvZmYgeW91ciBlbnRpcmUgb3JkZXIgd2l0aCB0aGUgY29kZSBiZWxvdy58U1BSSU5HMTV8U2hvcCBOb3d8L2AgYW5kIGA1fDN8fGAgKG5vIGRhdGUgbGltaXRzKS4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Promotion Popup</div><div class="te-mock__row"><span class="te-lbl">Promo Content — Title|Description|Coupon Code|Button Text|Button URL</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Show after (seconds) | Repeat every (days) | Start date | End date</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

**Exit-intent pop-up:**

- **Heading:** Wait! Don't Go Empty-Handed
- **Body:** Here's a special 10% discount just for you.
- **Code:** `STAY10`
- **Button:** Claim Discount → `/`
- **Options:** discount type. On desktop it triggers when the mouse leaves the top of the viewport (after at least 5 seconds on the page); on mobile it triggers after 45 seconds of inactivity. It reappears at most once per day.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEV4aXQgSW50ZW50IFBvcHVwKiDihpIgKipFeGl0IENvbnRlbnQg4oCUIFRpdGxlfERlc2NyaXB0aW9ufENvdXBvbiBDb2RlfEJ1dHRvbiBUZXh0fEJ1dHRvbiBVUkwqKiAoaWQgYGVzaG9wcGluZy1wb3B1cC1leGl0LXRleHRgOyBsZWF2ZSBlbXB0eSB0byBkaXNhYmxlKSBhbmQgKipUeXBlIChkaXNjb3VudC9uZXdzbGV0dGVyL2N1c3RvbSkgfCBNb2JpbGUgdGltZW91dCAoc2Vjb25kcykgfCBSZXBlYXQgZXZlcnkgKGRheXMpKiogKGlkIGBlc2hvcHBpbmctcG9wdXAtZXhpdC1vcHRzYCkuIERlZmF1bHQgKEluZHVzdHJpYWwpOiBgV2FpdCEgRG9uJ3QgR28gRW1wdHktSGFuZGVkfEhlcmUncyBhIHNwZWNpYWwgMTAlIGRpc2NvdW50IGp1c3QgZm9yIHlvdS58U1RBWTEwfENsYWltIERpc2NvdW50fC9gIGFuZCBgZGlzY291bnR8NDV8MWAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Exit Intent Popup</div><div class="te-mock__row"><span class="te-lbl">Exit Content — Title|Description|Coupon Code|Button Text|Button URL</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Type (discount/newsletter/custom) | Mobile timeout (seconds) | Repeat every (days)</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

---

## Final check

Click **Save → Publish**. Open the storefront in a private browser window. Compare to <https://eshopping-industrial-demo.mybigcommerce.com>.

---

## Next

- [Product page](product.md)
- [Category page](category.md)
- [Other variant home pages →](home-overview.md)
