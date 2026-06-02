# Sidebar

The 280 px-wide left sidebar appears on **category, brand, and search** pages. It shows:

1. **Categories tree** — collapsible navigation
2. **Faceted filters** (when filters are enabled on the category)
3. **Promo card** (optional, text-only — driven by the Sidebar promo card setting)
4. **Custom widgets** (optional, via Page Builder regions)

![Sidebar layout](../img/sidebar-layout.jpg){ loading=lazy }

---

## ① Categories tree { #categories-tree }

The tree is built from your store's **product category structure** (BigCommerce admin: **Products → Categories**). It displays **up to four levels** of categories — any subcategories deeper than the fourth level are not shown in the sidebar tree.

The categories section **auto-collapses whenever a filter is currently applied** (to give the active filters more room), and otherwise shows the tree with the active category branch expanded. You can still expand/collapse it manually by clicking the **Categories** header (see [Sidebar toggle behavior](#sidebar-toggle)).

Each top-level category shows the same fixed grid icon. There is no per-category icon feature.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipQcm9kdWN0cyDihpIgQ2F0ZWdvcmllcyoqLiBUaGUgdHJlZSBtaXJyb3JzIHlvdXIgY2F0ZWdvcnkgc3RydWN0dXJlICh1cCB0byBmb3VyIGxldmVscyBkZWVwKS4gKE5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub is-active">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

---

## ② Faceted filters

When a category has product filters enabled, eShopping shows them here as collapsible filter groups.

1. Turn filtering on store-wide in **Settings → Product Filtering**.
2. Choose which attributes act as filters in **Catalog → Product Filtering**.

Each filter group renders as a **collapsible accordion**: **Price** shows as a range form, and every other filter (Brand, Rating, and any product attribute such as Color or Size) shows as a **checkbox list**. Picking a value narrows the grid instantly and adds a removable chip at the top of the products (see [Filter chips](category.md#filter-chips-active-filters)).

The **Price** range form is gated by the BigCommerce "Shop by Price" feature. When a category has no faceted filters enabled, eShopping still shows the price range form alone if the theme setting `shop_by_price_visibility` is on (default: `true`).

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipTZXR0aW5ncyDihpIgRmFjZXRlZCBTZWFyY2gqKiAodHVybiBmaWx0ZXJpbmcgb24pLCB0aGVuICoqQ2hhbm5lbCBNYW5hZ2VyIC8gQ2F0YWxvZyDihpIgUHJvZHVjdCBGaWx0ZXJpbmcqKiB0byBwaWNrIHdoaWNoIGF0dHJpYnV0ZXMgKEJyYW5kLCBSYXRpbmcsIENvbG9yLCBTaXplLCBldGMuKSBhY3QgYXMgZmlsdGVycy4gKE5vdCBhIHRoZW1lIHNldHRpbmcg4oCUIHRoZSBzaWRlYmFyIHNpbXBseSByZW5kZXJzIHdoYXRldmVyIEJpZ0NvbW1lcmNlIHJldHVybnMuKQ==-->
<!--te-src:PiAqKkN1c3RvbWl6ZSAocHJpY2UgZm9ybSk6KiogVGhlbWUgRWRpdG9yIOKGkiAqUHJvZHVjdHMqIOKGkiAqKlNob3cgIlNob3AgYnkgUHJpY2UiIGluIGZpbHRlcnMqKiDigJQgdG9nZ2xlcyB0aGUgc3RhbmRhbG9uZSBwcmljZSByYW5nZSBmb3JtIG9uIGNhdGVnb3JpZXMgdGhhdCBoYXZlIG5vIG90aGVyIGZpbHRlcnMuIEZvcm1hdDogb24vb2ZmIChpZCBgc2hvcF9ieV9wcmljZV92aXNpYmlsaXR5YCkuIERlZmF1bHQ6IGB0cnVlYC4=-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top is-open"><span>Settings</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Store profile</div><div class="te-nav__sub is-active">Faceted search</div><div class="te-nav__sub">Currencies</div><div class="te-nav__sub">Shipping</div><div class="te-nav__sub">Payments</div></div>
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Show &quot;Shop by Price&quot; in filters</span><span class="te-cb is-on"></span></div></div>

---

## ③ Promo card { #promo-card }

A single text-only card (heading + body + a button). This is a **built-in theme section**, not a Page Builder widget — it is configured entirely from one Theme Editor field. In **Theme Editor → eShopping** — under the **Sidebar** heading, then the **Sidebar Promo Card** heading — there is **one** field labeled **Sidebar Promo Text** (id `eshopping-promo-text`).

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcqIOKGkiAqKlNpZGViYXIqKiDihpIgKipTaWRlYmFyIFByb21vIENhcmQqKiDihpIgKipTaWRlYmFyIFByb21vIFRleHQqKiDigJQgdGhlIHdob2xlIGNhcmQgb24gb25lIGxpbmUuIEZvcm1hdDogYEhlYWRpbmd8RGVzY3JpcHRpb258QnV0dG9uIExhYmVsfFVSTGAgKGZvdXIgYHxgLXNlcGFyYXRlZCBwYXJ0czsgc3Vycm91bmRpbmcgc3BhY2VzIGFyZSB0cmltbWVkLCBzbyBgQSB8IEJgIGFuZCBgQXxCYCBiZWhhdmUgdGhlIHNhbWUpLiBMZWF2ZSAqKmVtcHR5KiogdG8gaGlkZSB0aGUgY2FyZC4gaWQgYGVzaG9wcGluZy1wcm9tby10ZXh0YC4gRGVmYXVsdCAoYmFzZSk6IGBGcmVlIFNoaXBwaW5nICQ1MDArfEZyZWUgZ3JvdW5kIHNoaXBwaW5nIG9uIHF1YWxpZnlpbmcgb3JkZXJzLnxTaG9wIE5vd3wvc2hpcHBpbmcvYCAocGVyLXZhcmlhdGlvbiBkZWZhdWx0cyBiZWxvdyku-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Sidebar</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Sidebar Promo Card</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Sidebar Promo Text</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">empty</span><span class="te-tx te-tx--ph">Enter text…</span></div></div>

You enter the whole card as a **single line**, using `|` (the pipe character) to separate four parts:

```
Heading | Description | Button Label | URL
```

Example:

```
Free Shipping $250+ | Free ground shipping on qualifying parts orders. | Shop Parts | /shipping/
```

The four per-variation defaults:

| Variation | Default promo card |
| --------- | ------------------ |
| Industrial | *Free Shipping $500+* / *Free ground shipping on qualifying orders.* / button *Shop Now* → `/shipping/` |
| AutoParts | *Free Shipping $250+* / *Free ground shipping on qualifying parts orders.* / button *Shop Parts* → `/shipping/` |
| Electronics | *Free Shipping $99+* / *Free shipping on all electronics orders over $99.* / button *Shop Deals* → `/shipping/` |
| Packaging | *Free Shipping $300+* / *Free ground shipping on qualifying packaging orders.* / button *Shop Supplies* → `/shipping/` |

Leave the **Sidebar Promo Text** field empty to hide the built-in card.

For more design control (image, custom colors), drop an **AI HTML Generator | PapaThemes** widget (or any PapaThemes widget) into the **`sidebar_below--global`** region. In the template this region renders **immediately above** the built-in text promo card, so the widget appears first and the text card (if filled) appears under it. If you want the widget to **replace** the built-in card entirely, clear the **Sidebar Promo Text** field. The demo stores use the **AI HTML Generator | PapaThemes** widget here, which requires the PapaThemes app to be installed.

<!--te-src:PiAqKkN1c3RvbWl6ZSAocmljaGVyIHByb21vKToqKiBQYWdlIEJ1aWxkZXIg4oaSIENhdGVnb3J5IHBhZ2Ug4oaSIGRyYWcgYSB3aWRnZXQgaW50byB0aGUgKipgc2lkZWJhcl9iZWxvdy0tZ2xvYmFsYCoqIHJlZ2lvbiAoZGFzaGVkIGJsdWUgb3V0bGluZSkuIEZvciBhbiBBSSBIVE1MIEdlbmVyYXRvciB3aWRnZXQsIGVkaXQgaXRzICoqSFRNTCBDb250ZW50KiogZmllbGQg4oCUIHNlZSBbSG93IHRvIHVzZSB0aGUgQUkgSFRNTCBHZW5lcmF0b3Igd2lkZ2V0XSh3aWRnZXRzLWh0bWwubWQpLiBCZWNhdXNlIHRoZSByZWdpb24gaXMgKipnbG9iYWwqKiwgdGhlIHdpZGdldCBzaG93cyBvbiAqKmV2ZXJ5KiogY2F0ZWdvcnksIGJyYW5kLCBhbmQgc2VhcmNoIHBhZ2Uu-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

---

## ④ Custom sidebar widgets

The sidebar has 2 Page Builder regions:

| Region (id) | Scope | Renders | Use it for |
| ----------- | ----- | ------- | ---------- |
| `sidebar_below--global` | Every category, brand, search page | **Above** the built-in promo card | Newsletter signup, brand logos, "Need help?" card |
| `sidebar_below` | The page you're editing | **Below** the built-in promo card | Page-specific promo (e.g. "Free fitment service" on the Tires category) |

To use:

1. Page Builder → switch to the page (Category > pick any).
2. Drag any widget into the appropriate region (visible as a dashed blue outline).
3. Save.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBQYWdlIEJ1aWxkZXIg4oaSIENhdGVnb3J5IHBhZ2Ug4oaSIGRyYWcgYSB3aWRnZXQgaW50byAqKmBzaWRlYmFyX2JlbG93LS1nbG9iYWxgKiogKHNob3dzIHNpdGUtd2lkZSBvbiBhbGwgbGlzdGluZyBwYWdlcykgb3IgKipgc2lkZWJhcl9iZWxvd2AqKiAodGhpcyBwYWdlIG9ubHkpLiAoTm90IGEgdGhlbWUgc2V0dGluZyDigJQgdGhlc2UgYXJlIFBhZ2UgQnVpbGRlciByZWdpb25zLik=-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

---

## Sidebar toggle behavior { #sidebar-toggle }

Both the **Categories** section and each **filter group** are collapsible:

- Click (or focus + press **Enter** / **Space**) the **Categories** header to expand/collapse the tree. Within the tree, the L1/L2/L3 caret toggles open each branch.
- The **Categories** section auto-collapses when any faceted filter is selected and re-expands when filters are cleared. The initial state is rendered server-side (to prevent layout shift), then kept in sync after AJAX filter updates.

---

## Mobile behavior

Below 1024 px the desktop sidebar is hidden. Tap the **Filter** button at the top of the page and a **bottom-sheet drawer** (titled **Filters**) slides up from the bottom. This sheet contains **only the faceted filters** — the categories tree and the promo card are not shown on mobile.

Preview by resizing Page Builder preview to mobile (3rd device icon at the top).

---

## Per-variation promo recommendations

!!! note
    These are editable suggestions — not theme defaults. The actual defaults are listed in the [Promo card](#promo-card) table above. Replace them with whatever fits your store.

=== "Industrial"
    - Default: `Free Shipping $500+ | Free ground shipping on qualifying orders. | Shop Now | /shipping/`
=== "AutoParts"
    - Default: `Free Shipping $250+ | Free ground shipping on qualifying parts orders. | Shop Parts | /shipping/` — or swap in a custom fitment-lookup promo
=== "Electronics"
    - Default: `Free Shipping $99+ | Free shipping on all electronics orders over $99. | Shop Deals | /shipping/`
=== "Packaging"
    - Default: `Free Shipping $300+ | Free ground shipping on qualifying packaging orders. | Shop Supplies | /shipping/`

---

## Next

- [Category page](category.md)
- [Footer](footer.md)
