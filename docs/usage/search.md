# Search

eShopping's search has 3 layers:

1. **Quick-search popover** — appears as the user types in the header search box, showing matching products and (optionally) keyword suggestions
2. **Search-results page** — `/search.php?search_query=…` — full grid with filters
3. **Voice search** — optional mic button for browsers that support speech recognition

There is also a **category-scope dropdown** beside the search box — a folder/tree selector that lets a shopper limit a search to a specific category before submitting. Its depth is controlled by the **Category dropdown depth in search** setting (see below).

## Quick-search popover

Auto-enabled. As the user types, the popover shows:

- **The top matching products** returned by BigCommerce's quick-search (image, title, price). The theme does not set a fixed count — the number shown comes from BigCommerce.
- **Keyword suggestions** (if [Keyword Suggestions](keyword-suggestions.md) is set up).

### Settings

**Theme Editor → eShopping Theme → Search**:

| Setting | Effect |
| ------- | ------ |
| **Enable keyword suggestions** | Toggle CSV-driven autocomplete (see [Keyword Suggestions](keyword-suggestions.md)) |
| **Keywords file 1 path** / **Keywords file 2 path** / **Keywords file 3 path** | Paths to the keyword CSV files |
| **Category dropdown depth in search** | `Disabled` · `Top-level only` · `Two levels` · `Three levels` · `Four levels` — sets how deep the category-scope dropdown (folder/tree selector) beside the search box goes, letting shoppers limit a search to a chosen category. It does **not** control how many categories appear in the popover. |
| **Enable voice search** | Show the mic icon (uses the browser's built-in Web Speech API; the mic button automatically hides in browsers that don't support it — for example Firefox) |
| **Typing phrases (pipe \| separated)** | Pipe-separated phrases that rotate as the input's placeholder, e.g. `Search for power tools...\|Find welding equipment...\|Browse safety gear...` |

The settings appear in this order in the Theme Editor, matching the table above.

### Voice search

Uses the browser's built-in Web Speech API and feature-detects support at load time: the mic button is hidden automatically in browsers that don't implement speech recognition (for example Firefox). Browser support changes over time, so treat any specific browser list as approximate. When supported, the user's browser still needs to grant microphone permission.

## Search-results page

Settings same as Category page:

- **Theme Editor → Products → Number of products displayed → Search result page** — default `12`.
- Faceted filters: same as Category page (works on search results too).
- Sort options: **Featured Items**, **Newest Items**, **Best Selling**, **A to Z**, **Z to A**, **By Review**, **Price: Ascending**, **Price: Descending**, and **Relevance**. Relevance only appears on a query-based result set; the default sort order is set by BigCommerce, not the theme.

## Empty-results page

When a search returns no products **and** BigCommerce has spelling or term suggestions for that query, the page shows a **suggestions panel**. If BigCommerce has no suggestions to offer for the query, this panel does not appear at all — a zero-result search on its own does not guarantee any message.

When the panel does appear, it can include:

- A **Did you mean: X** correction link, shown when BigCommerce has a spelling/term correction for the query.
- A **"Your search for "X" did not match any products or information"** notice, shown alongside that correction.
- Matching **category** and **brand** links. These come from BigCommerce's own search suggestions and are independent of the Category dropdown depth setting.
- A short list of generic **search tips** (check spelling, try different keywords, try more general keywords).

Because every part of this panel is driven by BigCommerce's suggestions for the specific query, none of it shows on a zero-result search where BigCommerce has nothing to suggest.

To add your own content below the no-results message, place an HTML widget in the search page's `search_below_content` region (see the [widget regions reference](widget-regions.md)). You can also override the message text by editing the theme's language file (advanced, requires theme file access).

## Hiding zero-result products

To prevent out-of-stock products from showing in search:

**Settings → Display → Catalog settings → Don't display out-of-stock products** ✅.

## Search analytics

BigCommerce records every search in **Analytics → Marketing → Search terms**. Use it to discover what people search for that you don't carry — then add the products or create a redirect.

---

## Next

- [Keyword suggestions](keyword-suggestions.md)
- [Blog](blog.md)
