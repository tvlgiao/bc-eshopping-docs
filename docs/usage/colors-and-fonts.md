# Colors & Fonts

This page covers every color and typography control in eShopping. Open Page Builder, open the single **eShopping Theme** panel, and scroll to the relevant heading (Colors, Fonts, Banner, …) as you follow along.

!!! tip "Pick a variation first"
    The four variations (Industrial / AutoParts / Electronics / Packaging) ship with completely different color palettes and fonts. Pick one first ([Step 2](choose-variant.md)) — then use this page to fine-tune.

## The color system

eShopping uses three colour families plus accents. Each family has multiple shades so the design stays consistent across buttons, badges, hovers, borders, etc.

<!--te-tbl:fCBGYW1pbHkgfCBXaGF0IGl0J3MgZm9yIHwgKipEZWZhdWx0KiogKEluZHVzdHJpYWwpIHwKfCAtLS0tLS0gfCAtLS0tLS0tLS0tLS0tIHwgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIHwKfCAqKlRlcnJhKiogfCBQcmltYXJ5IGFjY2VudCDigJQgYnV5IGJ1dHRvbnMsIGxpbmtzLCBvbi1zYWxlIHByaWNlcywgaGVyby10ZXh0IGhpZ2hsaWdodHMgfCBgI2JmNWIzM2AgfAp8ICoqRm9yZXN0KiogfCBTZWNvbmRhcnkgYWNjZW50IOKAlCAiTmV3IiAvICJCZXN0c2VsbGluZyIgLyAiUG9wdWxhciIgYmFkZ2UgdGV4dCwgc2VjdGlvbiBsaW5rcywgaW4tcGFnZSBhY2NlbnRzIGFjcm9zcyBjYXRlZ29yeSwgcHJvZHVjdCwgY2FydCwgYW5kIGJsb2cgcGFnZXMgfCBgIzJkNWE0MmAgKDcwMCkgfAp8ICoqQmFyayoqIHwgTmV1dHJhbHMg4oCUIHRleHQsIGJvcmRlcnMsIGRpdmlkZXJzLCBzdXJmYWNlcy4gMTEgc2hhZGVzIGZyb20gQmFyayA1MCAoYWxtb3N0IHdoaXRlKSB0byBCYXJrIDk1MCAoYWxtb3N0IGJsYWNrKSB8IGAjMGYwZDBhYCAoOTUwKSB8CnwgKipDcmVhbSoqIHwgVGhlIHdhcm0gb2ZmLXdoaXRlIHBhZ2UgYmFja2dyb3VuZCB8IGAjZmFmOGY0YCB8CnwgKipXaGl0ZSoqIHwgQ2FyZHMsIHBvcG92ZXJzIHwgYCNmZmZmZmZgIHwKfCAqKkJhZGdlIFNhbGUqKiB8IFNhbGUtcGVyY2VudGFnZSBiYWRnZSB8IGAjYmY1YjMzYCAvIGAjZmZmZmZmYCB8CnwgKipCYWRnZSBTdGFmZioqIHwgIlN0YWZmIHBpY2siIHBpbGwgfCBgIzNmODA2MGAgLyBgI2ZmZmZmZmAgfAp8ICoqUmF0aW5nIHN0YXIqKiB8IFJldmlldyBzdGFycyB8IGAjZjU5ZTBiYCAvIGAjZDVjZWMyYCB8CnwgKipQcmljZSoqIHwgT24tc2FsZSBwcmljZSArIHN0cnVjay10aHJvdWdoIG9yaWdpbmFsIHwgYCNkYzI2MjZgIC8gYCM5NzhhNzRgIHw=-->

Find them under the **Colors** heading in the **eShopping Theme** panel of the Theme Editor:

![eShopping color panel](../img/eshopping-color-panel.jpg){ loading=lazy }

Click any swatch to open the colour-picker.

!!! note "The full set of swatches"
    Each family is more than one swatch. **Terra** has Dark / Light / Pale variants, **Bark** exposes all 11 individually editable shades (50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950), and **Forest** exposes 50 / 100 / 300 / 500 / 700 / 900 — so you can fine-tune any intermediate tone if you need to. The defaults are tuned to harmonize, so most merchants only ever touch the base of each family.

!!! tip "Stay inside one family"
    Changing the **Terra** base updates every primary button, link, sale badge, and price across the entire theme. The Terra Light / Dark / Pale shades are also picker-controlled, but the defaults are designed to harmonize with the base — you rarely need to touch them.

Every swatch is an individual color field under the **Colors** heading. The base config.json defaults (Industrial palette) are:

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqVGVycmEqKiAoaWQgYGVzaG9wcGluZy1jb2xvci10ZXJyYWApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNiZjViMzNgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqVGVycmEgRGFyayoqIChpZCBgZXNob3BwaW5nLWNvbG9yLXRlcnJhLWRhcmtgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjOTkzZjFmYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqVGVycmEgTGlnaHQqKiAoaWQgYGVzaG9wcGluZy1jb2xvci10ZXJyYS1saWdodGApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNkOTg0NWVgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqVGVycmEgUGFsZSoqIChpZCBgZXNob3BwaW5nLWNvbG9yLXRlcnJhLXBhbGVgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjZmRmMGU5YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqRm9yZXN0IDcwMCAvIDUwMCAvIDkwMCAvIDMwMCAvIDEwMCAvIDUwKiogKGlkcyBgZXNob3BwaW5nLWNvbG9yLWZvcmVzdC03MDBgLCBgZXNob3BwaW5nLWNvbG9yLWZvcmVzdC01MDBgLCBgZXNob3BwaW5nLWNvbG9yLWZvcmVzdC05MDBgLCBgZXNob3BwaW5nLWNvbG9yLWZvcmVzdC0zMDBgLCBgZXNob3BwaW5nLWNvbG9yLWZvcmVzdC0xMDBgLCBgZXNob3BwaW5nLWNvbG9yLWZvcmVzdC01MGApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdCAoNzAwKTogYCMyZDVhNDJgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqQmFyayA1MOKAkzk1MCoqIChpZHMgYGVzaG9wcGluZy1jb2xvci1iYXJrLTUwYCDigKYgYGVzaG9wcGluZy1jb2xvci1iYXJrLTk1MGAsIGFsbCAxMSBzaGFkZXMgaW5kaXZpZHVhbGx5IGVkaXRhYmxlKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHRzOiBCYXJrIDk1MCBgIzBmMGQwYWAsIEJhcmsgOTAwIGAjMWExNzEzYCwgQmFyayA1MCBgI2Y1ZjNlZmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqQ3JlYW0qKiAoaWQgYGVzaG9wcGluZy1jb2xvci1jcmVhbWApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNmYWY4ZjRgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqV2hpdGUqKiAoaWQgYGVzaG9wcGluZy1jb2xvci13aGl0ZWApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNmZmZmZmZgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqU2FsZSBCYWRnZSBCYWNrZ3JvdW5kKiogKGlkIGBlc2hvcHBpbmctYmFkZ2Utc2FsZS1iZ2ApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNiZjViMzNgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqU2FsZSBCYWRnZSBUZXh0KiogKGlkIGBlc2hvcHBpbmctYmFkZ2Utc2FsZS10ZXh0YCkuIEZvcm1hdDogaGV4IGNvbG9yLiBEZWZhdWx0OiBgI2ZmZmZmZmAu-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqU3RhZmYgUGljayBCYWRnZSBCYWNrZ3JvdW5kKiogKGlkIGBlc2hvcHBpbmctYmFkZ2Utc3RhZmYtYmdgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjZDk3NzA2YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqU3RhZmYgUGljayBCYWRnZSBUZXh0KiogKGlkIGBlc2hvcHBpbmctYmFkZ2Utc3RhZmYtdGV4dGApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNmZmZmZmZgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqUmF0aW5nIFN0YXIgKEFjdGl2ZSkqKiAoaWQgYGVzaG9wcGluZy1yYXRpbmctc3Rhci1hY3RpdmVgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjZjU5ZTBiYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqUmF0aW5nIFN0YXIgKEluYWN0aXZlKSoqIChpZCBgZXNob3BwaW5nLXJhdGluZy1zdGFyLWluYWN0aXZlYCkuIEZvcm1hdDogaGV4IGNvbG9yLiBEZWZhdWx0OiBgI2U0ZTRlN2Au-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqU2FsZSBQcmljZSoqIChpZCBgZXNob3BwaW5nLXByaWNlLXNhbGVgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjZGMyNjI2YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIENvbG9ycyog4oaSICoqT3JpZ2luYWwgLyBTdHJpa2V0aHJvdWdoIFByaWNlKiogKGlkIGBlc2hvcHBpbmctcHJpY2Utb3JpZ2luYWxgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjOTRhM2I4YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Colors</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Terra</span><span class="te-desc">Primary accent — buy buttons, links, on-sale prices, hero-text highlights</span></span><span class="te-color"><span class="te-hex">#BF5B33</span><span class="te-sw" style="background:#bf5b33"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Terra Dark</span><span class="te-desc">Primary accent — buy buttons, links, on-sale prices, hero-text highlights</span></span><span class="te-color"><span class="te-hex">#993F1F</span><span class="te-sw" style="background:#993f1f"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Terra Light</span><span class="te-desc">Primary accent — buy buttons, links, on-sale prices, hero-text highlights</span></span><span class="te-color"><span class="te-hex">#D9845E</span><span class="te-sw" style="background:#d9845e"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Terra Pale</span><span class="te-desc">Primary accent — buy buttons, links, on-sale prices, hero-text highlights</span></span><span class="te-color"><span class="te-hex">#FDF0E9</span><span class="te-sw" style="background:#fdf0e9"></span></span></div><div class="te-mock__row"><span class="te-lbl">Forest 700 / 500 / 900 / 300 / 100 / 50</span><span class="te-color"><span class="te-hex">#2D5A42</span><span class="te-sw" style="background:#2d5a42"></span></span></div><div class="te-mock__row"><span class="te-lbl">Bark 50–950</span><span class="te-color"><span class="te-hex">#0F0D0A</span><span class="te-sw" style="background:#0f0d0a"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Cream</span><span class="te-desc">The warm off-white page background</span></span><span class="te-color"><span class="te-hex">#FAF8F4</span><span class="te-sw" style="background:#faf8f4"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">White</span><span class="te-desc">Cards, popovers</span></span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Sale Badge Background</span><span class="te-color"><span class="te-hex">#BF5B33</span><span class="te-sw" style="background:#bf5b33"></span></span></div><div class="te-mock__row"><span class="te-lbl">Sale Badge Text</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Staff Pick Badge Background</span><span class="te-color"><span class="te-hex">#D97706</span><span class="te-sw" style="background:#d97706"></span></span></div><div class="te-mock__row"><span class="te-lbl">Staff Pick Badge Text</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Rating Star (Active)</span><span class="te-desc">Review stars</span></span><span class="te-color"><span class="te-hex">#F59E0B</span><span class="te-sw" style="background:#f59e0b"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Rating Star (Inactive)</span><span class="te-desc">Review stars</span></span><span class="te-color"><span class="te-hex">#E4E4E7</span><span class="te-sw" style="background:#e4e4e7"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Sale Price</span><span class="te-desc">On-sale price + struck-through original</span></span><span class="te-color"><span class="te-hex">#DC2626</span><span class="te-sw" style="background:#dc2626"></span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Original / Strikethrough Price</span><span class="te-desc">On-sale price + struck-through original</span></span><span class="te-color"><span class="te-hex">#94A3B8</span><span class="te-sw" style="background:#94a3b8"></span></span></div></div>

!!! note "Variation defaults differ from the base"
    The per-variation tables on this page list the *variation-override* values (e.g. Industrial sets Staff Badge bg to `#3f8060`, Rating Star inactive to `#d5cec2`, Original Price to `#978a74`). The **Default** in each Customize block above is the base value shipped in `config.json` `settings`. Selecting a variation applies its overrides on top.

### Real per-variation defaults

| Color | Industrial | AutoParts | Electronics | Packaging |
| ----- | ---------- | --------- | ----------- | --------- |
| Terra | `#bf5b33` | `#d97706` | `#3b82f6` | `#059669` |
| Terra light | `#d9845e` | `#f59e0b` | `#60a5fa` | `#34d399` |
| Terra dark | `#993f1f` | `#b45309` | `#2563eb` | `#047857` |
| Terra pale | `#fdf0e9` | `#fffbeb` | `#eff6ff` | `#ecfdf5` |
| Bark 950 | `#0f0d0a` | `#020617` | `#09090b` | `#0c0a09` |
| Bark 900 | `#1a1713` | `#0f172a` | `#18181b` | `#1c1917` |
| Bark 50 | `#f5f3ef` | `#f8fafc` | `#fafafa` | `#fafaf9` |
| Cream | `#faf8f4` | `#f8fafc` | `#fafafa` | `#fafaf9` |
| Forest 700 | `#2d5a42` | `#15803d` | `#1d4ed8` | `#15803d` |
| Sale badge bg | `#bf5b33` | `#dc2626` | `#dc2626` | `#dc2626` |

If you switch the variation in Page Builder, the picker resets to these values. Any value you change after that overrides the variation default.

---

## Fonts

Only one font control lives under the **Fonts** heading in the **eShopping Theme** panel — the **Monospace Font**. The body and heading font families, plus every font size, are set in the **Global** panel (under **Body text and links** and **Headings**):

| Setting | Where to set it | Default | Notes |
| ------- | --------------- | ------- | ----- |
| **Body Text Font Family** | Global → Body text and links | Source Sans 3 | The font used for paragraphs, buttons, product cards. |
| **Heading Font Family** | Global → Headings | Playfair Display | H1-H6, hero headlines. |
| **Monospace Font** | eShopping Theme → Fonts | IBM Plex Mono | SKUs, prices, codes. |
| **Body Text Font Size** | Global → Body text and links | `14` | The root font-size in px. Other sizes scale relative to it. |
| **H1-H6 Font Size** | Global → Headings | `24 / 22 / 20 / 18 / 16 / 13` px | Override individually. |

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwg4oaSIEJvZHkgdGV4dCBhbmQgbGlua3MqIOKGkiAqKkJvZHkgdGV4dCBmb250IGZhbWlseSoqIChpZCBgYm9keS1mb250YCkuIEZvcm1hdDogZHJvcGRvd24gKEdvb2dsZSBmb250ICsgd2VpZ2h0cykuIERlZmF1bHQ6IGBHb29nbGVfU291cmNlK1NhbnMrM180MDAsNjAwLDcwMGAgKFNvdXJjZSBTYW5zIDMpLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwg4oaSIEhlYWRpbmdzKiDihpIgKipIZWFkaW5nIGZvbnQgZmFtaWx5KiogKGlkIGBoZWFkaW5ncy1mb250YCkuIEZvcm1hdDogZHJvcGRvd24gKEdvb2dsZSBmb250ICsgd2VpZ2h0cykuIERlZmF1bHQ6IGBHb29nbGVfUGxheWZhaXIrRGlzcGxheV82MDAsNDAwLDcwMGAgKFBsYXlmYWlyIERpc3BsYXkpLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEZvbnRzKiDihpIgKipNb25vc3BhY2UgRm9udCoqIChpZCBgZXNob3BwaW5nLW1vbm8tZm9udGApLiBGb3JtYXQ6IGRyb3Bkb3duIOKAlCAqSUJNIFBsZXggTW9ubyogLyAqSUJNIFBsZXggTW9ubyBNZWRpdW0qIC8gKkpldEJyYWlucyBNb25vKi4gRGVmYXVsdDogYEdvb2dsZV9JQk0rUGxleCtNb25vXzQwMGAgKElCTSBQbGV4IE1vbm8pLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwg4oaSIEJvZHkgdGV4dCBhbmQgbGlua3MqIOKGkiAqKkJvZHkgdGV4dCBmb250IHNpemUqKiAoaWQgYGZvbnRTaXplLXJvb3RgKS4gRm9ybWF0OiBzZWxlY3Qg4oCUIGAxMmAgLyBgMTNgIC8gYDE0YCAvIGAxNmAgLyBgMThgIHB4IChyb290IHNpemU7IG90aGVyIHNpemVzIHNjYWxlIHJlbGF0aXZlIHRvIGl0KS4gRGVmYXVsdDogYDE0YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwg4oaSIEhlYWRpbmdzKiDihpIgKipIZWFkaW5nIDEqKuKAkyoqSGVhZGluZyA2KiogZm9udCBzaXplIChpZHMgYGZvbnRTaXplLWgxYCDigKYgYGZvbnRTaXplLWg2YCkuIEZvcm1hdDogc2VsZWN0IChweCkuIERlZmF1bHRzOiBgMjQgLyAyMiAvIDIwIC8gMTggLyAxNiAvIDEzYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Global</span><span class="te-x">✕</span></div><div class="te-mock__grp">Body text and links</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Body text font family</span><span class="te-desc">Global → Body text and links</span></span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__grp">Headings</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Heading font family</span><span class="te-desc">Global → Headings</span></span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Fonts</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Monospace Font</span><span class="te-desc">eShopping Theme → Fonts</span></span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Global</span><span class="te-x">✕</span></div><div class="te-mock__grp">Body text and links</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Body text font size</span><span class="te-desc">Global → Body text and links</span></span><span class="te-dd"><span class="te-dd__v">14</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__grp">Headings</div><div class="te-mock__row"><span class="te-lbl">Heading 1</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Heading 6</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>

### Real per-variation font defaults

| Variation | Body font | Heading font |
| --------- | --------- | ------------ |
| Industrial | Source Sans 3 (default) | Playfair Display (default) |
| AutoParts | Inter | Inter |
| Electronics | Inter | Space Grotesk |
| Packaging | DM Sans | DM Sans |

The font field is a **dropdown** — you pick from the fonts it lists; you can't type a custom one in. The per-variation fonts above (Inter, Space Grotesk, DM Sans) are preset by each variation and are **not** in the standard dropdown, so if you open it and choose a different font, that preset is replaced. Adding a Google Font that isn't already in the list is not possible from the visual editor.

---

## Top banner color

eShopping shows an optional thin promo bar above the header. Configure its colors under the **Banner** heading in the **eShopping Theme** panel:

<!--te-tbl:fCBTZXR0aW5nIHwgRGVmYXVsdCAoSW5kdXN0cmlhbCkgfAp8IC0tLS0tLS0gfCAtLS0tLS0tLS0tLS0tLS0tLS0tLSB8CnwgQmFubmVyIEJhY2tncm91bmQgfCBgIzNlMzYyOWAgfAp8IEJhbm5lciBUZXh0IENvbG9yIHwgYCNkNWNlYzJgIHwKfCBCYW5uZXIgTGluayBDb2xvciB8IGAjZDk4NDVlYCB8-->

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEJhbm5lciog4oaSICoqQmFubmVyIEJhY2tncm91bmQqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItYmdgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjM2UzNjI5YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEJhbm5lciog4oaSICoqQmFubmVyIFRleHQgQ29sb3IqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItY29sb3JgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjZDVjZWMyYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEJhbm5lciog4oaSICoqQmFubmVyIExpbmsgQ29sb3IqKiAoaWQgYGVzaG9wcGluZy1iYW5uZXItbGlua2ApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNkOTg0NWVgLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Banner</div><div class="te-mock__row"><span class="te-lbl">Banner Background</span><span class="te-color"><span class="te-hex">#3E3629</span><span class="te-sw" style="background:#3e3629"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner Text Color</span><span class="te-color"><span class="te-hex">#D5CEC2</span><span class="te-sw" style="background:#d5cec2"></span></span></div><div class="te-mock__row"><span class="te-lbl">Banner Link Color</span><span class="te-color"><span class="te-hex">#D9845E</span><span class="te-sw" style="background:#d9845e"></span></span></div></div>

The **content** of the bar comes from a Page Builder widget — see [Header & top bar](header-and-topbar.md).

---

## Buttons

Buttons are controlled by:

- **Primary button** — the main buy button. Each variation sets this to match Terra.
- **Default button** — outline / ghost buttons.
- **Disabled button** — disabled state.

You rarely need to override these — they're computed from the Terra + Bark scales. If you do override, do it in **Theme Editor → Buttons and Icons**.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpCdXR0b25zIGFuZCBpY29ucyDihpIgUHJpbWFyeSBhY3Rpb24gYnV0dG9uKiDihpIgKipCdXR0b24gYmFja2dyb3VuZCoqIChpZCBgYnV0dG9uLS1wcmltYXJ5LWJhY2tncm91bmRDb2xvcmApLiBGb3JtYXQ6IGhleCBjb2xvci4gRGVmYXVsdDogYCNiZjViMzNgLiBDb21wYW5pb24gZmllbGRzOiAqKkJ1dHRvbiB0ZXh0IGNvbG9yKiogKGlkIGBidXR0b24tLXByaW1hcnktY29sb3JgLCBkZWZhdWx0IGAjZmZmZmZmYCksICoqQnV0dG9uIHRleHQgaG92ZXIgY29sb3IqKiAoaWQgYGJ1dHRvbi0tcHJpbWFyeS1jb2xvckhvdmVyYCwgZGVmYXVsdCBgI2ZmZmZmZmApLCAqKkJ1dHRvbiBiYWNrZ3JvdW5kIGhvdmVyKiogKGlkIGBidXR0b24tLXByaW1hcnktYmFja2dyb3VuZENvbG9ySG92ZXJgLCBkZWZhdWx0IGAjOTkzZjFmYCku-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpCdXR0b25zIGFuZCBpY29ucyDihpIgU2Vjb25kYXJ5IGFjdGlvbiBidXR0b24qIOKGkiAqKkJ1dHRvbiBiYWNrZ3JvdW5kKiogKGlkIGBidXR0b24tLWRlZmF1bHQtYmFja2dyb3VuZENvbG9yYCkuIEZvcm1hdDogaGV4IGNvbG9yLiBEZWZhdWx0OiBgIzNlMzYyOWAuIENvbXBhbmlvbiBmaWVsZDogKipCdXR0b24gdGV4dCBjb2xvcioqIChpZCBgYnV0dG9uLS1kZWZhdWx0LWNvbG9yYCwgZGVmYXVsdCBgI2ZhZjhmNGApLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpCdXR0b25zIGFuZCBpY29ucyDihpIgRGlzYWJsZWQgYnV0dG9uKiDihpIgKipCdXR0b24gYmFja2dyb3VuZCoqIChpZCBgYnV0dG9uLS1kaXNhYmxlZC1iYWNrZ3JvdW5kQ29sb3JgKS4gRm9ybWF0OiBoZXggY29sb3IuIERlZmF1bHQ6IGAjZDVjZWMyYC4gQ29tcGFuaW9uIGZpZWxkOiAqKkJ1dHRvbiB0ZXh0IGNvbG9yKiogKGlkIGBidXR0b24tLWRpc2FibGVkLWNvbG9yYCwgZGVmYXVsdCBgI2ZmZmZmZmApLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Buttons and icons</span><span class="te-x">✕</span></div><div class="te-mock__grp">Primary action button</div><div class="te-mock__row"><span class="te-lbl">Button background</span><span class="te-color"><span class="te-hex">#BF5B33</span><span class="te-sw" style="background:#bf5b33"></span></span></div><div class="te-mock__row"><span class="te-lbl">Button text color</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Button text hover color</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div><div class="te-mock__row"><span class="te-lbl">Button background hover</span><span class="te-color"><span class="te-hex">#993F1F</span><span class="te-sw" style="background:#993f1f"></span></span></div><div class="te-mock__grp">Secondary action button</div><div class="te-mock__row"><span class="te-lbl">Button background</span><span class="te-color"><span class="te-hex">#3E3629</span><span class="te-sw" style="background:#3e3629"></span></span></div><div class="te-mock__row"><span class="te-lbl">Button text color</span><span class="te-color"><span class="te-hex">#FAF8F4</span><span class="te-sw" style="background:#faf8f4"></span></span></div><div class="te-mock__grp">Disabled button</div><div class="te-mock__row"><span class="te-lbl">Button background</span><span class="te-color"><span class="te-hex">#D5CEC2</span><span class="te-sw" style="background:#d5cec2"></span></span></div><div class="te-mock__row"><span class="te-lbl">Button text color</span><span class="te-color"><span class="te-hex">#FFFFFF</span><span class="te-sw" style="background:#ffffff"></span></span></div></div>

---

## Saving & previewing

Click **Save → Publish** to push colour & font changes live. The preview pane updates instantly; the public storefront updates after **Publish**.

---

## Next

- [Header & top bar](header-and-topbar.md)
- [Footer](footer.md)
- [Home page recipes](home-overview.md)
