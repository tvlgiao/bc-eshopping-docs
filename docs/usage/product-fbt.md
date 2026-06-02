# Frequently Bought Together (FBT)

FBT shows a small bundle of related products on the product page that a shopper can review and add together. It's a simple way to surface obvious add-ons (accessories, consumables, companion items) right where the shopper is deciding.

![FBT bundle example](../img/fbt-bundle.jpg){ loading=lazy }

## How it works

FBT shows **only when the product has Related Products set in BigCommerce** (Catalog → edit product → **Related Products** tab). If a product has no Related Products linked, the FBT block does not render at all — there is no category fallback.

The block renders in the product info area of the product page (the right column on desktop). It lists the main product plus up to your configured number of related products. Each entry is a card:

- The **main product** is flagged with a **This item** badge and is always included.
- Each **related product** has a checkbox so the shopper can include or exclude it.
- If a related product has variants, it shows a **Select Options** button instead of a plain checkbox — the shopper picks options (via the quick-view step) before that item can be added.
- A **Bundle Price** summary shows the running total for the selected items.
- A **Bundle & Save** badge always appears in the header whenever the FBT block renders.
- A **You save** line appears under the total **only when a Visual Bundle Discount % is set** (see below).
- A single **Add** button adds all selected items to the cart at once.

## Setup

### 1. Turn FBT on

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIGVTaG9wcGluZyBUaGVtZSoqLCBpbiB0aGUgRnJlcXVlbnRseSBCb3VnaHQgVG9nZXRoZXIgZ3JvdXA6-->

<!--te-tbl:fCBTZXR0aW5nIHwgT3B0aW9ucyB8IE5vdGVzIHwKfCAtLS0tLS0tIHwgLS0tLS0tLSB8IC0tLS0tIHwKfCAqKkZCVCBQcm9kdWN0cyBDb3VudCoqIHwgT2ZmIOKAlCBkb24ndCBzaG93IMK3IDEgwrcgMiDCtyAzIHwgSG93IG1hbnkgcmVsYXRlZCBwcm9kdWN0cyB0byBzaG93IGFsb25nc2lkZSB0aGUgbWFpbiBwcm9kdWN0IHwKfCAqKlZpc3VhbCBCdW5kbGUgRGlzY291bnQgJSoqIHwgZS5nLiBgMTBgIGZvciAxMCUgb2ZmIHwgKipEaXNwbGF5IG9ubHkqKiDigJQgc2VlIHRoZSBub3RlIGJlbG93IHw=-->

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEZyZXF1ZW50bHkgQm91Z2h0IFRvZ2V0aGVyKiDihpIgKipGQlQgUHJvZHVjdHMgQ291bnQqKiAoaWQgYGVzaG9wcGluZy1mYnQtY291bnRgKS4gRm9ybWF0OiBzZWxlY3QgKGBPZmYg4oCUIGRvbid0IHNob3dgIC8gYDFgIC8gYDJgIC8gYDNgKS4gRGVmYXVsdDogYDJgLg==-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIEZyZXF1ZW50bHkgQm91Z2h0IFRvZ2V0aGVyKiDihpIgKipWaXN1YWwgQnVuZGxlIERpc2NvdW50ICUqKiAoaWQgYGVzaG9wcGluZy1mYnQtZGlzY291bnQtcGVyY2VudGApLiBGb3JtYXQ6IG51bWJlciAod2hvbGUtbnVtYmVyIHBlcmNlbnQ7IGAwYCBzaG93cyBubyBzYXZpbmcpLiBEZWZhdWx0OiBgMGAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Frequently Bought Toget…</div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">FBT Products Count</span><span class="te-desc">Off — don't show · 1 · 2 · 3</span></span><span class="te-dd"><span class="te-dd__v">2</span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Visual Bundle Discount %</span><span class="te-desc">e.g. 10 for 10% off</span></span><span class="te-dd"><span class="te-dd__v">0</span><span class="te-dd__b">▾</span></span></div></div>

### 2. About the "Visual Bundle Discount %"

!!! warning "The discount is visual only"
    The **Visual Bundle Discount %** changes only what the shopper *sees*: it lowers the displayed **Bundle Price** and shows a **You save** line. It does **not** discount the actual cart — items are added at their normal price.

    If you want that saving to be real at checkout, you must **create a matching BigCommerce promotion yourself** (Marketing → Promotions). The theme will not create or enforce any promotion. Leave the field at `0` if you only want the convenience of one-click bundle add without any displayed saving.

### 3. (Optional) Choose which products appear

The bundle is built from the main product's **Related Products** list, in order:

1. Catalog → Products → edit the **main** product → **Related Products** tab.
2. Add the partner products in the order you want them to appear.
3. Save.

The FBT block reads up to your **FBT Products Count** from the Related Products list, in order.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipDYXRhbG9nIOKGkiBQcm9kdWN0cyDihpIgZWRpdCB0aGUgbWFpbiBwcm9kdWN0IOKGkiBSZWxhdGVkIFByb2R1Y3RzIHRhYioqLiAoTm90IGEgdGhlbWUgc2V0dGluZyDigJQgdGhpcyBpcyB0aGUgc291cmNlIGxpc3QgZm9yIHRoZSBidW5kbGUuKQ==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

---

## How to hide FBT for one specific product

There's no per-product toggle in Theme Editor. The FBT block hides itself automatically when the product has no Related Products linked. So the simplest way to hide FBT on one product is to remove all of its Related Products (Catalog → edit product → Related Products tab → remove).

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipDYXRhbG9nIOKGkiBQcm9kdWN0cyDihpIgZWRpdCB0aGUgcHJvZHVjdCDihpIgUmVsYXRlZCBQcm9kdWN0cyB0YWIg4oaSIHJlbW92ZSBhbGwqKi4gKE5vdCBhIHRoZW1lIHNldHRpbmcg4oCUIGVtcHRpZXMgdGhlIEZCVCBzb3VyY2Ugc28gdGhlIGJsb2NrIHNlbGYtaGlkZXMuKQ==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top is-open"><span>Products</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">All products</div><div class="te-nav__sub">Add</div><div class="te-nav__sub">Categories</div><div class="te-nav__sub">Options</div><div class="te-nav__sub">Filtering</div><div class="te-nav__sub">Reviews</div><div class="te-nav__sub">Brands</div><div class="te-nav__sub">Import</div><div class="te-nav__sub">Export</div><div class="te-nav__sub is-active">Products</div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

If you need a hard hide on a specific product while keeping its Related Products, add a CSS-only override via **Storefront → Script Manager** that targets the product ID:

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipTdG9yZWZyb250IOKGkiBTY3JpcHQgTWFuYWdlciDihpIgQ3JlYXRlIGEgU2NyaXB0KiogKExvY2F0aW9uOiBGb290ZXIsIFBhZ2VzOiBBbGwgcGFnZXMpLCB0aGVuIHBhc3RlIHRoZSBzbmlwcGV0IGJlbG93LiAoTm90IGEgdGhlbWUgc2V0dGluZy4p-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub is-active">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

```html
<script>
  (function(){
    var HIDE_FBT_ON = [123, 456]; // product IDs
    var id = parseInt(document.querySelector('.productView[data-entity-id]')?.dataset.entityId, 10);
    if (HIDE_FBT_ON.indexOf(id) !== -1) {
      var s = document.createElement('style');
      s.textContent = '[data-eshopping-fbt]{display:none}';
      document.head.appendChild(s);
    }
  })();
</script>
```

---

## Settings in the demo stores

All four demo stores ship FBT with the same settings:

| Variant | FBT Products Count | Visual Bundle Discount % |
| ------- | :----------------: | :----------------------: |
| Industrial | 2 | 0 |
| Auto Parts | 2 | 0 |
| Electronics | 2 | 0 |
| Packaging | 2 | 0 |

In other words, every demo shows two related products with no displayed saving. Whether the block actually appears on a given product still depends on that product having Related Products linked.

---

## Cross-sell vs FBT

These are two different features. FBT lives on the **product page**; Cross-sell is a **cart** feature.

| | FBT | Cart Cross-sell |
| - | --- | --------------- |
| Where it appears | Product page, in the product info area (right column on desktop) | Cart page and cart drawer |
| Add to cart | One **Add** button for the selected items | Per-product |
| Saving | Optional **visual** bundle % (not a real discount) | Per-product price |
| Source | Product's Related Products | Related Products of the items in your cart (aggregated by frequency) |

You can run both at the same time.

---

## Next

- [Product FAQ tab](product-faq.md)
- [Urgency + recent sales](urgency-and-recent-sales.md)
- [Category page](category.md)
