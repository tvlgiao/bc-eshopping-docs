# Search

eShopping's search has 3 layers:

1. **Quick-search popover** — appears as the user types in the header search box, showing matching products and (optionally) keyword suggestions
2. **Search-results page** — `/search.php?search_query=…` — full grid with filters
3. **Voice search** — optional mic button for browsers that support speech recognition

There is also a **category-scope dropdown** beside the search box — a folder/tree selector that lets a shopper limit a search to a specific category before submitting. Its depth is controlled by the **Category dropdown depth in search** setting (see below).

All theme search settings live in the Theme Editor; the underlying product/suggestion data comes from BigCommerce. Each setting below ends with a **Customize:** line that tells you exactly where to change it.

## Quick-search popover

Auto-enabled. As the user types, the popover shows:

- **The top matching products** returned by BigCommerce's quick-search (image, title, price). The theme does not set a fixed count — the number shown comes from BigCommerce.
- **Keyword suggestions** (if [Keyword Suggestions](keyword-suggestions.md) is set up).

<!--te-src:PiAqKkN1c3RvbWl6ZSAocHJvZHVjdCBkYXRhKToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipTZXR0aW5ncyDihpIgU2VhcmNoKiouIFRoZSBwcm9kdWN0cyB0aGF0IGFwcGVhciBpbiB0aGUgcG9wb3ZlciBhbmQgb24gdGhlIHJlc3VsdHMgcGFnZSBjb21lIGZyb20gQmlnQ29tbWVyY2UncyBzZWFyY2ggaW5kZXgsIG5vdCBhIHRoZW1lIHNldHRpbmcuIFR1bmUgcmVsZXZhbmNlLCB3ZWlnaHRpbmcgYW5kIHN5bm9ueW1zIHRoZXJlLg==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top is-open"><span>Settings</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Store profile</div><div class="te-nav__sub">Faceted search</div><div class="te-nav__sub">Currencies</div><div class="te-nav__sub">Shipping</div><div class="te-nav__sub">Payments</div><div class="te-nav__sub is-active">Search</div></div>

### Settings

<!--te-lead:KipUaGVtZSBFZGl0b3Ig4oaSIGVTaG9wcGluZyBUaGVtZSDihpIgU2VhcmNoKio6-->

<!--te-tbl:fCBTZXR0aW5nIHwgRWZmZWN0IHwKfCAtLS0tLS0tIHwgLS0tLS0tIHwKfCAqKkVuYWJsZSBrZXl3b3JkIHN1Z2dlc3Rpb25zKiogfCBUb2dnbGUgQ1NWLWRyaXZlbiBhdXRvY29tcGxldGUgKHNlZSBbS2V5d29yZCBTdWdnZXN0aW9uc10oa2V5d29yZC1zdWdnZXN0aW9ucy5tZCkpIHwKfCAqKktleXdvcmRzIGZpbGUgMSBwYXRoKiogLyAqKktleXdvcmRzIGZpbGUgMiBwYXRoKiogLyAqKktleXdvcmRzIGZpbGUgMyBwYXRoKiogfCBQYXRocyB0byB0aGUga2V5d29yZCBDU1YgZmlsZXMgfAp8ICoqQ2F0ZWdvcnkgZHJvcGRvd24gZGVwdGggaW4gc2VhcmNoKiogfCBgRGlzYWJsZWRgIMK3IGBUb3AtbGV2ZWwgb25seWAgwrcgYFR3byBsZXZlbHNgIMK3IGBUaHJlZSBsZXZlbHNgIMK3IGBGb3VyIGxldmVsc2Ag4oCUIHNldHMgaG93IGRlZXAgdGhlIGNhdGVnb3J5LXNjb3BlIGRyb3Bkb3duIChmb2xkZXIvdHJlZSBzZWxlY3RvcikgYmVzaWRlIHRoZSBzZWFyY2ggYm94IGdvZXMsIGxldHRpbmcgc2hvcHBlcnMgbGltaXQgYSBzZWFyY2ggdG8gYSBjaG9zZW4gY2F0ZWdvcnkuIEl0IGRvZXMgKipub3QqKiBjb250cm9sIGhvdyBtYW55IGNhdGVnb3JpZXMgYXBwZWFyIGluIHRoZSBwb3BvdmVyLiB8CnwgKipFbmFibGUgdm9pY2Ugc2VhcmNoKiogfCBTaG93IHRoZSBtaWMgaWNvbiAodXNlcyB0aGUgYnJvd3NlcidzIGJ1aWx0LWluIFdlYiBTcGVlY2ggQVBJOyB0aGUgbWljIGJ1dHRvbiBhdXRvbWF0aWNhbGx5IGhpZGVzIGluIGJyb3dzZXJzIHRoYXQgZG9uJ3Qgc3VwcG9ydCBpdCDigJQgZm9yIGV4YW1wbGUgRmlyZWZveCkgfAp8ICoqVHlwaW5nIHBocmFzZXMgKHBpcGUgXHwgc2VwYXJhdGVkKSoqIHwgUGlwZS1zZXBhcmF0ZWQgcGhyYXNlcyB0aGF0IHJvdGF0ZSBhcyB0aGUgaW5wdXQncyBwbGFjZWhvbGRlciwgZS5nLiBgU2VhcmNoIGZvciBwb3dlciB0b29scy4uLlx8RmluZCB3ZWxkaW5nIGVxdWlwbWVudC4uLlx8QnJvd3NlIHNhZmV0eSBnZWFyLi4uYCB8-->

The settings appear in this order in the Theme Editor, matching the table above. The exact field label (left column), setting **id**, value **format** and shipped **default** for each:

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKkVuYWJsZSBrZXl3b3JkIHN1Z2dlc3Rpb25zKiog4oCUIHR1cm5zIENTVi1kcml2ZW4ga2V5d29yZCBhdXRvY29tcGxldGUgb24vb2ZmIChzZWUgW0tleXdvcmQgU3VnZ2VzdGlvbnNdKGtleXdvcmQtc3VnZ2VzdGlvbnMubWQpKS4gRm9ybWF0OiBjaGVja2JveCAob24vb2ZmKS4gU2V0dGluZyBpZDogYHN1Z2dlc3Rfa2V5d29yZHNgLiBEZWZhdWx0OiBgb25gIChjaGVja2VkKS4gKlRoaXMgc2V0dGluZyBpcyBsaXZlIOKAlCBpdCBpcyByZWFkIGJ5IGBlU2hvcHBpbmdTdWdnZXN0S2V5d29yZHMuanNgLio=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKktleXdvcmRzIGZpbGUgMSBwYXRoKiogLyAqKktleXdvcmRzIGZpbGUgMiBwYXRoKiogLyAqKktleXdvcmRzIGZpbGUgMyBwYXRoKiog4oCUIHBhdGhzIHRvIHVwIHRvIHRocmVlIGtleXdvcmQgQ1NWIGZpbGVzIHRoYXQgZmVlZCB0aGUgYXV0b2NvbXBsZXRlIGNoaXBzLiBGb3JtYXQ6IGEgVVJMIHBhdGggKGUuZy4gYSBXZWJEQVYgYC9jb250ZW50L+KApmAgcGF0aCkgb3IgZW1wdHkgdG8gc2tpcCB0aGF0IHNsb3QuIFNldHRpbmcgaWRzOiBga2V5d29yZHNfZmlsZTFgLCBga2V5d29yZHNfZmlsZTJgLCBga2V5d29yZHNfZmlsZTNgLiBEZWZhdWx0czogYC9jb250ZW50L3N1Z2dlc3Qta2V5d29yZHMtMS5jc3ZgLCBgL2NvbnRlbnQvc3VnZ2VzdC1rZXl3b3Jkcy0yLmNzdmAsIGAvY29udGVudC9zdWdnZXN0LWtleXdvcmRzLTMuY3N2YC4gKlRoZXNlIGFyZSBsaXZlIOKAlCB0aGUgQ1NWIGZpbGVzIGFyZSBmZXRjaGVkIGF0IHJ1bnRpbWUgYnkgYGVTaG9wcGluZ1N1Z2dlc3RLZXl3b3Jkcy5qc2AuKiBTZWUgW0tleXdvcmQgU3VnZ2VzdGlvbnNdKGtleXdvcmQtc3VnZ2VzdGlvbnMubWQpIGZvciB0aGUgQ1NWIGZvcm1hdCBhbmQgaG93IHRvIHVwbG9hZCB0aGUgZmlsZXMu-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKkNhdGVnb3J5IGRyb3Bkb3duIGRlcHRoIGluIHNlYXJjaCoqIOKAlCBzZXRzIGhvdyBtYW55IGNhdGVnb3J5IGxldmVscyB0aGUgY2F0ZWdvcnktc2NvcGUgZHJvcGRvd24gKGZvbGRlci90cmVlIHNlbGVjdG9yKSBiZXNpZGUgdGhlIHNlYXJjaCBib3ggc2hvd3MuIEZvcm1hdDogc2VsZWN0IOKAlCBgRGlzYWJsZWRgIChgMGApLCBgVG9wLWxldmVsIG9ubHlgIChgMWApLCBgVHdvIGxldmVsc2AgKGAyYCksIGBUaHJlZSBsZXZlbHNgIChgM2ApLCBgRm91ciBsZXZlbHNgIChgNGApLiBTZXR0aW5nIGlkOiBgZXNob3BwaW5nLXNlYXJjaC1jYXRlZ29yeS1kZXB0aGAuIERlZmF1bHQ6IGBGb3VyIGxldmVsc2AgKGA0YCkuIENob29zaW5nIGBEaXNhYmxlZGAgcmVtb3ZlcyB0aGUgY2F0ZWdvcnkgZHJvcGRvd24gZW50aXJlbHkuIFRoZSBjYXRlZ29yeSBsaXN0IGl0c2VsZiBjb21lcyBmcm9tIEJpZ0NvbW1lcmNlOyB0aGlzIG9ubHkgbGltaXRzIGhvdyBkZWVwIHRoZSBwaWNrZXIgZHJpbGxzIGluLiBJdCBkb2VzICoqbm90KiogY29udHJvbCBob3cgbWFueSBjYXRlZ29yaWVzIGFwcGVhciBpbiB0aGUgcG9wb3Zlci4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKkVuYWJsZSB2b2ljZSBzZWFyY2gqKiDigJQgc2hvd3MgdGhlIG1pYyBpY29uIGluIHRoZSBzZWFyY2ggYm94ICh1c2VzIHRoZSBicm93c2VyJ3MgV2ViIFNwZWVjaCBBUEkpLiBGb3JtYXQ6IGNoZWNrYm94IChvbi9vZmYpLiBTZXR0aW5nIGlkOiBgZXNob3BwaW5nLXNlYXJjaC12b2ljZWAuIERlZmF1bHQ6IGBvbmAgKGNoZWNrZWQpLiBUaGUgbWljIGJ1dHRvbiBhdXRvLWhpZGVzIGluIGJyb3dzZXJzIHdpdGhvdXQgc3BlZWNoIHJlY29nbml0aW9uIChmb3IgZXhhbXBsZSBGaXJlZm94KS4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKlR5cGluZyBwaHJhc2VzIChwaXBlIHwgc2VwYXJhdGVkKSoqIOKAlCBwaHJhc2VzIHRoYXQgcm90YXRlIGFzIHRoZSBzZWFyY2ggaW5wdXQncyBwbGFjZWhvbGRlci4gRm9ybWF0OiBwaHJhc2VzIHNlcGFyYXRlZCBieSB0aGUgcGlwZSBjaGFyYWN0ZXIgYHxgIChzdXJyb3VuZGluZyBzcGFjZXMgYXJlIHRyaW1tZWQpOyBsZWF2ZSBlbXB0eSB0byBkaXNhYmxlIHRoZSByb3RhdGluZyBwbGFjZWhvbGRlci4gU2V0dGluZyBpZDogYGVzaG9wcGluZy1zZWFyY2gtdHlwaW5nLXBocmFzZXNgLiBEZWZhdWx0OiBgU2VhcmNoIGZvciBwb3dlciB0b29scy4uLnxGaW5kIHdlbGRpbmcgZXF1aXBtZW50Li4ufEJyb3dzZSBzYWZldHkgZ2Vhci4uLnxEaXNjb3ZlciBjb21wcmVzc29ycyAmIGFjY2Vzc29yaWVzLi4uYCAoZWFjaCBkZW1vIHN0b3JlIHNoaXBzIGl0cyBvd24gcGhyYXNlIHNldCku-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Enable keyword suggestions</span><span class="te-desc">Toggle CSV-driven autocomplete (see Keyword Suggestions)</span></span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Keywords file 1 path</span><span class="te-desc">Paths to the keyword CSV files</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Keywords file 2 path</span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Keywords file 3 path</span><span class="te-desc">Paths to the keyword CSV files</span></span><span class="te-tx te-tx--ph">Enter text…</span></div><div class="te-mock__row"><span class="te-lbl">Category dropdown depth in search</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">not</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Enable voice search</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-lbl">Typing phrases (pipe | separated)</span><span class="te-tx">Search for power tools</span></div></div>

### Voice search

Uses the browser's built-in Web Speech API and feature-detects support at load time: the mic button is hidden automatically in browsers that don't implement speech recognition (for example Firefox). Browser support changes over time, so treat any specific browser list as approximate. When supported, the user's browser still needs to grant microphone permission.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUqIOKGkiAqKkVuYWJsZSB2b2ljZSBzZWFyY2gqKiAoaWQgYGVzaG9wcGluZy1zZWFyY2gtdm9pY2VgKS4gRm9ybWF0OiBjaGVja2JveC4gRGVmYXVsdDogYG9uYC4gVW5jaGVjayB0byByZW1vdmUgdGhlIG1pYyBidXR0b24gZm9yIGFsbCBicm93c2Vycy4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Enable voice search</span><span class="te-cb is-on"></span></div></div>

## Search-results page

Settings same as Category page:

- **Products per page** — controls the grid size on the results page.

<!--te-src:ICAgID4gKipDdXN0b21pemU6KiogVGhlbWUgRWRpdG9yIOKGkiAqUHJvZHVjdHMqIOKGkiAodW5kZXIgdGhlICoqTnVtYmVyIG9mIHByb2R1Y3RzIGRpc3BsYXllZCoqIGhlYWRpbmcpIOKGkiAqKlNlYXJjaCByZXN1bHQgcGFnZSoqIOKAlCBudW1iZXIgb2YgcHJvZHVjdHMgc2hvd24gcGVyIHBhZ2Ugb24gc2VhcmNoIHJlc3VsdHMuIEZvcm1hdDogc2VsZWN0IOKAlCBgNmAsIGA4YCwgYDlgLCBgMTJgLCBgMTVgLCBgMTZgLCBgMThgLCBgMjBgLiBTZXR0aW5nIGlkOiBgc2VhcmNocGFnZV9wcm9kdWN0c19wZXJfcGFnZWAuIERlZmF1bHQ6IGAxMmAu-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>Products</span><span class="te-x">✕</span></div><div class="te-mock__row"><span class="te-lbl">Number of products displayed</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div><div class="te-mock__row"><span class="te-lbl">Search result page</span><span class="te-dd"><span class="te-dd__v"></span><span class="te-dd__b">▾</span></span></div></div>

- Faceted filters: same as Category page (works on search results too).
- Sort options: **Featured Items**, **Newest Items**, **Best Selling**, **A to Z**, **Z to A**, **By Review**, **Price: Ascending**, **Price: Descending**, and **Relevance**. Relevance only appears on a query-based result set; the default sort order is set by BigCommerce, not the theme.

<!--te-src:ICAgID4gKipDdXN0b21pemUgKHNvcnQgKyByZWxldmFuY2UpOioqIEJpZ0NvbW1lcmNlIGFkbWluIOKGkiAqKlNldHRpbmdzIOKGkiBTZWFyY2gqKi4gVGhlIGF2YWlsYWJsZSBzb3J0IG9wdGlvbnMgYW5kIHNlYXJjaCByZWxldmFuY2UgYXJlIGRyaXZlbiBieSBCaWdDb21tZXJjZSdzIHNlYXJjaCBjb25maWd1cmF0aW9uLCBub3QgYSB0aGVtZSBzZXR0aW5nLg==-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top is-open"><span>Settings</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Store profile</div><div class="te-nav__sub">Faceted search</div><div class="te-nav__sub">Currencies</div><div class="te-nav__sub">Shipping</div><div class="te-nav__sub">Payments</div><div class="te-nav__sub is-active">Search</div></div>

## Empty-results page

When a search returns no products **and** BigCommerce has spelling or term suggestions for that query, the page shows a **suggestions panel**. If BigCommerce has no suggestions to offer for the query, this panel does not appear at all — a zero-result search on its own does not guarantee any message.

When the panel does appear, it can include:

- A **Did you mean: X** correction link, shown when BigCommerce has a spelling/term correction for the query.
- A **"Your search for "X" did not match any products or information"** notice, shown alongside that correction.
- Matching **category** and **brand** links. These come from BigCommerce's own search suggestions and are independent of the Category dropdown depth setting.
- A short list of generic **search tips** (check spelling, try different keywords, try more general keywords).

Because every part of this panel is driven by BigCommerce's suggestions for the specific query, none of it shows on a zero-result search where BigCommerce has nothing to suggest.

To add your own content below the no-results message, place an **AI HTML Generator | PapaThemes** widget in the search page's `search_below_content` region (see the [widget regions reference](widget-regions.md)). You can also override the message text by editing the theme's language file (advanced, requires theme file access).

<!--te-src:PiAqKkN1c3RvbWl6ZSAocGFuZWwgY29udGVudCk6KiogUGFnZSBCdWlsZGVyIOKGkiBzZWFyY2ggcGFnZSDihpIgYWRkIGFuICoqQUkgSFRNTCBHZW5lcmF0b3IgfCBQYXBhVGhlbWVzKiogd2lkZ2V0IHRvIHRoZSBgc2VhcmNoX2JlbG93X2NvbnRlbnRgIHJlZ2lvbjsgZWRpdCBpdHMgKipIVE1MIENvbnRlbnQqKiBmaWVsZC4gKFRoZSBzdWdnZXN0aW9uIHRleHQgaXRzZWxmIGNvbWVzIGZyb20gQmlnQ29tbWVyY2Ug4oCUIGl0IGlzIG5vdCBhIHRoZW1lIHNldHRpbmcuKQ==-->
<!--te-mock--><div class="te-mock te-mock--pb"><div class="te-mock__hd"><span>‹ AI HTML Generator | PapaThemes</span><span class="te-x">⋯</span></div><div class="te-mock__grp">▾ Content</div><div class="te-pbbox"><span class="k">&lt;style&gt;</span><br><span class="s">.papathemes-ai-widget-…</span> { … }<br>…your HTML…<br><span class="k">&lt;/style&gt;</span></div><div class="te-pbbtns"><span class="te-btn-ghost">Expand HTML Editor</span><span class="te-save te-save--full">Save HTML</span></div><div class="te-mock__row"><span class="te-cb"></span><span class="te-lbl">Show in container div</span></div></div>

## Hiding zero-result products

To prevent out-of-stock products from showing in search:

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBCaWdDb21tZXJjZSBhZG1pbiDihpIgKipTZXR0aW5ncyDihpIgRGlzcGxheSDihpIgQ2F0YWxvZyBzZXR0aW5ncyDihpIgRG9uJ3QgZGlzcGxheSBvdXQtb2Ytc3RvY2sgcHJvZHVjdHMqKiDinIUuIChOb3QgYSB0aGVtZSBzZXR0aW5nLik=-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Storefront</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top is-open"><span>Settings</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Store profile</div><div class="te-nav__sub">Faceted search</div><div class="te-nav__sub">Currencies</div><div class="te-nav__sub">Shipping</div><div class="te-nav__sub">Payments</div><div class="te-nav__sub is-active">Display</div></div>

## Search analytics

BigCommerce records every search in **Analytics → Marketing → Search terms**. Use it to discover what people search for that you don't carry — then add the products or create a redirect.

---

## Next

- [Keyword suggestions](keyword-suggestions.md)
- [Blog](blog.md)
