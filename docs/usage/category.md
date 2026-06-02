# Category Page

The category page is what shoppers land on when they click a category in the nav. eShopping's category page has 3 zones:

1. **Header** — name, description, optional banner
2. **Sidebar** — categories tree + filters (see [Sidebar](sidebar.md))
3. **Product grid** — the products with the sort + toolbar above

![Category page example](../img/category-page.jpg){ loading=lazy }

![Packaging category page](../img/packaging-category-page.png){ loading=lazy }

---

## Header

Edit the category title, description, and banner in **Catalog → Categories → (edit a category)**:

| Field | Effect |
| ----- | ------ |
| Name | The H1 |
| Page description | Rich-text block shown under the H1 — use it for SEO |
| Header image | Wide banner shown above the description (wide landscape crop; BigCommerce scales it to the container width) |

<!--te-src:PiAqKkN1c3RvbWl6ZSAoY29udGVudCk6KiogQmlnQ29tbWVyY2UgYWRtaW4g4oaSICoqQ2F0YWxvZyDihpIgQ2F0ZWdvcmllcyDihpIgKGVkaXQgYSBjYXRlZ29yeSkqKiDigJQgc2V0IE5hbWUsIFBhZ2UgZGVzY3JpcHRpb24sIGFuZCBIZWFkZXIgaW1hZ2UgdGhlcmUuIChOb3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub is-active">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

To hide the page heading globally:

**Theme Editor → Global → Pages → Hide category page heading** ✅.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwqIOKGkiAqKkhpZGUgY2F0ZWdvcnkgcGFnZSBoZWFkaW5nKiog4oCUIGhpZGVzIHRoZSBjYXRlZ29yeSBIMSAoYW5kLCB3aXRoIGl0LCB0aGUgYGNhdGVnb3J5X2JlbG93X2hlYWRlcmAgd2lkZ2V0IHJlZ2lvbikgb24gZXZlcnkgY2F0ZWdvcnkgcGFnZS4gRm9ybWF0OiBjaGVja2JveCAob24vb2ZmKS4gRGVmYXVsdDogYGZhbHNlYCAoaGVhZGluZyBzaG93bikuIFNjaGVtYSBpZDogYGhpZGVfY2F0ZWdvcnlfcGFnZV9oZWFkaW5nYC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Global</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Hide category page heading</span><span class="te-cb"></span></div></div>

!!! note
    This is the **category-specific** toggle. The generic **Hide page heading** (`hide_page_heading`) under the same *Global → Pages* group affects other page types, not the category H1.

---

## Number of products per page

**Theme Editor → Products → Number of products displayed → Category page** — default `12`. Set whatever value suits your catalog.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpQcm9kdWN0cyog4oaSIChoZWFkaW5nICpOdW1iZXIgb2YgcHJvZHVjdHMgZGlzcGxheWVkKikg4oaSICoqQ2F0ZWdvcnkgcGFnZSoqIOKAlCBob3cgbWFueSBwcm9kdWN0cyBzaG93IHBlciBwYWdlIGJlZm9yZSBwYWdpbmF0aW9uLiBGb3JtYXQ6IHNlbGVjdCwgb25lIG9mIGA2IMK3IDggwrcgOSDCtyAxMiDCtyAxNSDCtyAxNiDCtyAxOCDCtyAyMGAuIERlZmF1bHQ6IGAxMmAuIFNjaGVtYSBpZDogYGNhdGVnb3J5cGFnZV9wcm9kdWN0c19wZXJfcGFnZWAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Category page</span><span class="te-dd"><span class="te-dd__v">12</span><span class="te-dd__b">▾</span></span></div></div>

---

## Sort & toolbar

Above the grid is a toolbar with:

| Control | Options |
| ------- | ------- |
| **Sort by** | Featured Items · Newest Items · Best Selling · A to Z · Z to A · By Review · Price: Ascending · Price: Descending |
| **Grid / Bulk-order toggle** | Switches the listing between the standard product grid and the bulk-order table |

!!! note
    **Relevance** is added to the **Sort by** list only on search / result pages — it does not appear on a standard category page.

The **Grid / Bulk-order toggle** (two icon buttons) appears only when bulk-order mode is enabled. It is *not* a generic grid/list view switch — the second option is the B2B bulk-order table, not a "list" layout. See [Bulk-order mode](#bulk-order-mode-b2b) below.

To set the default listing layout, go to **Theme Editor → Global → Products → Display style** and choose **Show products in a grid** or **Show products in bulk order**.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwqIOKGkiAoaGVhZGluZyAqUHJvZHVjdHMqKSDihpIgKipEaXNwbGF5IHN0eWxlKiog4oCUIHRoZSBsYXlvdXQgdGhlIGxpc3Rpbmcgb3BlbnMgaW4uIEZvcm1hdDogc2VsZWN0IOKAlCBgU2hvdyBwcm9kdWN0cyBpbiBhIGdyaWRgICh2YWx1ZSBgZ3JpZGApIG9yIGBTaG93IHByb2R1Y3RzIGluIGJ1bGsgb3JkZXJgICh2YWx1ZSBgbGlzdGApLiBEZWZhdWx0OiBgZ3JpZGAuIFNjaGVtYSBpZDogYHByb2R1Y3RfbGlzdF9kaXNwbGF5X21vZGVgLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Global</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Display style</span><span class="te-dd"><span class="te-dd__v">grid</span><span class="te-dd__b">▾</span></span></div></div>

---

## Faceted filters (Price, Brand, Rating, Custom)

Powered by BigCommerce — enable in **Settings → Product Filtering**, then per-attribute toggles in **Catalog → Product Filtering**.

The sidebar renders each enabled filter as a **collapsible group**:

| Filter type | Render |
| ----------- | ------ |
| **Price** | Range form (min / max) |
| **Brand, Rating, and any product attribute** (Color, Size, custom fields…) | Checkbox list |

Picking a value updates the grid via AJAX and adds a removable chip at the top of the products.

<!--te-src:PiAqKkN1c3RvbWl6ZSAod2hpY2ggZmlsdGVycyBhcHBlYXIpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKlNldHRpbmdzIOKGkiBQcm9kdWN0IEZpbHRlcmluZyoqICh0dXJuIHRoZSBmZWF0dXJlIG9uKSwgdGhlbiAqKkNhdGFsb2cg4oaSIFByb2R1Y3QgRmlsdGVyaW5nKiogdG8gY2hvb3NlIHdoaWNoIGF0dHJpYnV0ZXMgYmVjb21lIGZpbHRlcnMgYW5kIHRoZWlyIG9yZGVyLiAoTm90IGEgdGhlbWUgc2V0dGluZyDigJQgdGhlIHRoZW1lIHJlbmRlcnMgd2hhdGV2ZXIgQmlnQ29tbWVyY2UgcmV0dXJucy4p-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAoU2hvcCBieSBQcmljZSBibG9jayk6KiogVGhlbWUgRWRpdG9yIOKGkiAqUHJvZHVjdHMqIOKGkiAqKlNob3cgIlNob3AgYnkgUHJpY2UiIGluIGZpbHRlcnMqKiDigJQgc2hvd3MgdGhlIHByaWNlLXJhbmdlICJTaG9wIGJ5IFByaWNlIiBibG9jayBpbiB0aGUgc2lkZWJhciBldmVuIHdoZW4gbm8gZmFjZXRlZCBmaWx0ZXJzIGFyZSBlbmFibGVkLiBGb3JtYXQ6IGNoZWNrYm94IChvbi9vZmYpLiBEZWZhdWx0OiBgdHJ1ZWAuIFNjaGVtYSBpZDogYHNob3BfYnlfcHJpY2VfdmlzaWJpbGl0eWAuICooVGhpcyBhbHNvIGNvbnRyb2xzIHdoZXRoZXIgdGhlIG1vYmlsZSBGaWx0ZXIgYnV0dG9uIGFwcGVhcnMgb24gYSBjYXRlZ29yeSB3aXRoIG5vIG90aGVyIGZpbHRlcnMg4oCUIHNlZSBbTW9iaWxlIGZpbHRlciBkcmF3ZXJdKCNtb2JpbGUtZmlsdGVyLWRyYXdlcikuKSo=-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top is-open"><span>Settings</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Store profile</div><div class="te-nav__sub">Faceted search</div><div class="te-nav__sub">Currencies</div><div class="te-nav__sub">Shipping</div><div class="te-nav__sub">Payments</div><div class="te-nav__sub is-active">Product Filtering</div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show &quot;Shop by Price&quot; in filters</span><span class="te-cb is-on"></span></div></div>

---

## Filter chips (active filters)

When the user picks a filter, eShopping renders an **active-filter chip** at the top of the grid. Clicking the × on a chip removes that filter. This is automatic — no setup needed.

---

## Mobile filter drawer

Below 1024 px the sidebar collapses into a bottom-sheet that opens with a **Filter** button at the top. Categories, filters, and promo cards are all preserved.

The **Filter** button only appears when the category actually has faceted filters enabled (or when shop-by-price is on). If a category has no enabled filters and shop-by-price is off, there is no filter drawer to open, so no Filter button is shown — on any screen size.

---

## Sub-category chips

Whenever a category has sub-categories, eShopping shows them as a scrollable row of **chips** at the top of the grid (e.g. "Indoor", "Outdoor", "Heavy duty"), each linking to the sub-category. Clicking a chip drills into that sub-category.

This is independent of faceted filters — sub-category chips and sidebar filters can appear at the same time. The chips show whenever sub-categories exist; the sidebar filters show whenever filters are enabled. Neither one disables the other.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipDYXRhbG9nIOKGkiBDYXRlZ29yaWVzKiog4oCUIGNyZWF0ZSBjaGlsZCBjYXRlZ29yaWVzIHVuZGVyIHRoZSBwYXJlbnQgdG8gbWFrZSB0aGUgY2hpcHMgYXBwZWFyOyByZW5hbWUgb3IgcmVvcmRlciBjaGlsZHJlbiB0aGVyZSB0byBjaGFuZ2UgdGhlIGNoaXAgbGFiZWxzIGFuZCBvcmRlci4gKE5vdCBhIHRoZW1lIHNldHRpbmcg4oCUIHRoZSBjaGlwcyBhcmUgZ2VuZXJhdGVkIGF1dG9tYXRpY2FsbHkgZnJvbSB0aGUgY2F0ZWdvcnkncyBzdWItY2F0ZWdvcmllcy4p-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub is-active">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

---

## Sidebar promo card

The sidebar can show a small **promo card** (heading, one line of copy, and a button) below the filters. It is also carried into the mobile filter drawer.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAoaGVhZGluZyAqU2lkZWJhciDihpIgU2lkZWJhciBQcm9tbyBDYXJkKikg4oaSICoqU2lkZWJhciBQcm9tbyBUZXh0Kiog4oCUIGZpbGxzIHRoZSBwcm9tbyBjYXJkLiBMZWF2ZSBpdCAqKmJsYW5rKiogdG8gaGlkZSB0aGUgY2FyZC4gRm9ybWF0OiBhIHNpbmdsZSBwaXBlLWRlbGltaXRlZCBzdHJpbmcgYEhlYWRpbmd8RGVzY3JpcHRpb258QnV0dG9uIExhYmVsfFVSTGAgKDQgc2VnbWVudHMpLiBEZWZhdWx0OiBgRnJlZSBTaGlwcGluZyAkNTAwK3xGcmVlIGdyb3VuZCBzaGlwcGluZyBvbiBxdWFsaWZ5aW5nIG9yZGVycy58U2hvcCBOb3d8L3NoaXBwaW5nL2AuIFNjaGVtYSBpZDogYGVzaG9wcGluZy1wcm9tby10ZXh0YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAod2lkZ2V0IGFsdGVybmF0aXZlKToqKiBQYWdlIEJ1aWxkZXIg4oaSICoqU2lkZWJhcioqIGdsb2JhbCByZWdpb24gKGBzaWRlYmFyX2JlbG93LS1nbG9iYWxgKSDigJQgZHJvcCBhbiAqKkFJIEhUTUwgR2VuZXJhdG9yIHwgUGFwYVRoZW1lcyoqIG9yICoqQmFubmVyKiogd2lkZ2V0IGhlcmUgZm9yIGEgcmljaGVyIHByb21vIGFib3ZlIHRoZSBzdGF0aWMgY2FyZC4gQSBwYWdlLWxvY2FsIGBzaWRlYmFyX2JlbG93YCByZWdpb24gYWxzbyByZW5kZXJzIGJlbG93IGl0LiBTZWUgW1NpZGViYXJdKHNpZGViYXIubWQpIGZvciB0aGUgZnVsbCBicmVha2Rvd24u-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Sidebar Promo Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">blank</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

!!! note
    All four demo stores ship a per-store value for **Sidebar Promo Text** (e.g. the autoparts store uses `Free Shipping $250+|…|Shop Parts|/shipping/`). Edit it per store in the Theme Editor.

---

## Category page widgets

Each category page exposes these widget regions you can drop content into:

<!--te-tbl:fCBSZWdpb24gfCBSZW5kZXJzIHwgVXNlIGl0IGZvciB8CnwgLS0tLS0tIHwgLS0tLS0tLSB8IC0tLS0tLS0tLS0gfAp8IGBjYXRlZ29yeV9iZWxvd19oZWFkZXJgIHwgQmVsb3cgdGhlIHBhZ2UgaGVhZGluZyAoSDEpLCBhYm92ZSB0aGUgZGVzY3JpcHRpb24gYW5kIGdyaWQgfCBGZWF0dXJlZC1jYXRlZ29yeSBiYW5uZXIgfAp8IGBjYXRlZ29yeV9iZWxvd19jb250ZW50YCB8IEJlbG93IHRoZSBncmlkIHwgRkFRcywgU0VPIGNvcHksIHJlbGF0ZWQgY2F0ZWdvcmllcyB8-->

!!! note
    The `category_below_header` region is only rendered when **Hide category page heading** is off (see [Header](#header)).

Page Builder → Category page → drop in an **AI HTML Generator | PapaThemes** widget, or use the **Banner** or **Accordion** widgets from the PapaThemes Widgets app (check the app for the exact widget names available in your store).

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIgKFN0b3JlZnJvbnQg4oaSIE15IFRoZW1lcyDihpIgQ3VzdG9taXplKSDihpIgb3BlbiBhICoqQ2F0ZWdvcnkgcGFnZSoqIOKGkiBkcmFnIGEgd2lkZ2V0IGludG8gdGhlICoqYGNhdGVnb3J5X2JlbG93X2hlYWRlcmAqKiBvciAqKmBjYXRlZ29yeV9iZWxvd19jb250ZW50YCoqIHJlZ2lvbiDihpIgZWRpdCBpdHMgZmllbGRzIOKGkiAqKlNhdmUqKi4gRm9yIHRoZSBBSSBIVE1MIEdlbmVyYXRvciB3aWRnZXQsIHBhc3RlIG1hcmt1cCBpbnRvIHRoZSAqKkhUTUwgQ29udGVudCoqIGZpZWxkIOKAlCBzZWUgW0FJIEhUTUwgR2VuZXJhdG9yIHdpZGdldF0od2lkZ2V0cy1odG1sLm1kKSBhbmQgdGhlIFtEZW1vIG1hcmtldGluZyBibG9ja3NdKHdpZGdldHMtcGFwYXRoZW1lcy5tZCkgZm9yIHJlYWR5LW1hZGUgSFRNTC4gKFJlZ2lvbiBjb250ZW50IGlzIHBlci1wYWdlLCBub3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

---

## Bulk-order mode (B2B)

eShopping can switch the category page into **bulk-order mode** — a table view with quantity inputs on every row and a single "Add to cart" at the bottom. See [Bulk Order](bulk-order.md).

Toggle: **Theme Editor → eShopping Theme → Bulk Order → Show bulk order mode** ✅.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAoaGVhZGluZyAqQnVsayBPcmRlciopIOKGkiAqKlNob3cgYnVsayBvcmRlciBtb2RlKiog4oCUIGVuYWJsZXMgdGhlIEdyaWQvQnVsay1vcmRlciB0b2dnbGUgb24gbGlzdGluZ3MgKGFuZCB0aGUgYnVsay1vcmRlciB0YWJsZSkuIEZvcm1hdDogY2hlY2tib3ggKG9uL29mZikuIERlZmF1bHQ6IGB0cnVlYCAob24pLiBTY2hlbWEgaWQ6IGBlc2hvcHBpbmctc2hvdy1idWxrLW9yZGVyLW1vZGVgLg==-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show bulk order mode</span><span class="te-cb is-on"></span></div></div>

---

## Hiding the breadcrumbs

**Theme Editor → Global → Pages → Hide breadcrumbs** ✅.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICpHbG9iYWwqIOKGkiAoaGVhZGluZyAqUGFnZXMqKSDihpIgKipIaWRlIGJyZWFkY3J1bWJzKiog4oCUIGhpZGVzIHRoZSBicmVhZGNydW1iIHRyYWlsIGFib3ZlIHRoZSBoZWFkZXIgb24gY2F0ZWdvcnkgKGFuZCBvdGhlcikgcGFnZXMuIEZvcm1hdDogY2hlY2tib3ggKG9uL29mZikuIERlZmF1bHQ6IGBmYWxzZWAgKGJyZWFkY3J1bWJzIHNob3duKS4gU2NoZW1hIGlkOiBgaGlkZV9icmVhZGNydW1ic2Au-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Global</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Hide breadcrumbs</span><span class="te-cb"></span></div></div>

---

## Defaults

None of the four demo stores override the category-page **layout** settings, so they all inherit the theme defaults below. (The **Sidebar Promo Text** is the exception — each store ships its own value; see [Sidebar promo card](#sidebar-promo-card).)

| Setting | Schema id | Value |
| ------- | --------- | ----- |
| Products per page | `categorypage_products_per_page` | 12 |
| Display style | `product_list_display_mode` | Show products in a grid (`grid`) |
| Bulk-order mode | `eshopping-show-bulk-order-mode` | Available (toggle on) |
| Hide category page heading | `hide_category_page_heading` | Off (heading shown) |
| Hide breadcrumbs | `hide_breadcrumbs` | Off (breadcrumbs shown) |
| Show "Shop by Price" in filters | `shop_by_price_visibility` | On |

Change any of them per store in the Theme Editor as described in the sections above.

---

## Next

- [Brand pages](brand.md)
- [Bulk order](bulk-order.md)
- [Search & keyword suggestions](search.md)
