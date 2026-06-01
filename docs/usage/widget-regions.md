# Widget Regions Reference

Every page in the eShopping theme exposes **widget regions** — empty slots where you can drop Page Builder widgets without editing theme files. This page is the complete, template-verified map.

Naming convention:

- `name` — page-local region (only this specific page sees content dropped here)
- `name--global` — global region (every page of that type sees the same content)

Many product page regions support **both** `--global` and local; some don't.

---

## Home page (`templates/pages/home.html`)

| Region | Renders |
| ------ | ------- |
| `home_below_menu` | Just under the header — above the hero |
| `home_below_carousel` | Below the hero |
| `home_content` | Top of the main content column (above all auto-sections) |
| `home_below_featured_products` | Between Featured slider and Bestsellers |
| `home_below_top_products` | Between Bestsellers and New |
| `home_below_new_products` | Between New and Products-by-Category |
| `home_below_products_by_category` | Between Products-by-Category and Brands |
| `home_below_brands` | Between Brands and Blog |
| `home_below_blog_posts` | Between Blog and Newsletter |
| `home_below_newsletter` | Below the Newsletter section. |

---

## Product page (`templates/pages/product.html` + `product-view.html` + `eshopping-description-tabs.html`)

### Page-level (outside the product card)

| Region | Renders |
| ------ | ------- |
| `product_above_content` / `--global` | Below the breadcrumbs and shipping messages, above the product gallery+info card |
| `product_below_content` / `--global` | Below the entire product card — below the gallery, options, FBT, and tabs. Use `product_above_description` / `product_below_description` (inside the product card) if you need to target positions around the tabs |
| `product_above_related` / `--global` | Just above the Related/Cross-sell sliders |
| `product_below_related` / `--global` | Below the Related sliders, above the footer |

### Inside the product-view component

| Region | Renders |
| ------ | ------- |
| `product_below_price` / `--global` | Right column — directly below the price |
| `product_below_actions` / `--global` | Right column — below the Add-to-Cart button and the wishlist/compare/share action row, above the shipping info |
| `product_above_description` / `--global` | Above the tabs strip (between info card and tabs) |
| `product_below_description` / `--global` | Below the tabs strip |

### Inside the description-tabs component

| Region | Renders |
| ------ | ------- |
| `product_below_warranty` / `--global` | Inside the **Warranty** tab, below `product.warranty` content |

!!! note "The FAQ tab is NOT a widget region"
    The **FAQ** tab renders a built-in **ask-a-question form** (name + email + question, submits via captcha). It is not a widget region — you cannot drop accordion widgets into the FAQ tab.

### Inside the product card (sliders, category grids)

| Region | Renders |
| ------ | ------- |
| `product_item_below_price` / `--global` | Below the price on every product card (grid view) |
| `product_item_below_price` | Below the price on every list-item (list view) — **local only**, no `--global` variant |

---

## Category page (`templates/pages/category.html` and the bulk-order variant)

| Region | Renders |
| ------ | ------- |
| `category_below_header` | Below the category title, above the description and product grid. Note: hidden when the "Hide category page heading" setting is enabled |
| `category_below_content` | Below the grid, above the footer |

---

## Brand page (`templates/pages/brand.html` and the bulk-order variant)

| Region | Renders |
| ------ | ------- |
| `brand_below_header` | Below title, above the grid |
| `brand_below_content` | Below the grid |

The same two regions also render in the brand bulk-order page variant (`templates/pages/custom/brand/bulk-order.html`).

---

## All-brands index (`templates/pages/brands.html`)

| Region | Renders |
| ------ | ------- |
| `brands_below_header` | Below the page heading |
| `brands_below_content` | Below the brand list |

---

## Cart page (`templates/pages/cart.html`)

| Region | Renders |
| ------ | ------- |
| `cart_below_totals` | Below the order summary and the cart cross-sell section, near the bottom of the cart page |

---

## Search results (`templates/pages/search.html`)

| Region | Renders |
| ------ | ------- |
| `search_below_content` | Below the search results grid |

---

## Static web pages (`templates/pages/page.html`)

| Region | Renders |
| ------ | ------- |
| `page_builder_content` | Main content area of every WYSIWYG web page |

---

## Sidebar (renders on category, brand, search pages)

| Region | Renders |
| ------ | ------- |
| `sidebar_below--global` | Bottom of the sidebar, every page that has a sidebar |
| `sidebar_below` | Bottom of the sidebar, this page only |

!!! note
    If the sidebar promo text setting is filled in the Theme Editor, the theme's built-in promo card renders **between** the global and local sidebar regions.

---

## Footer (global)

| Region | Renders |
| ------ | ------- |
| `eshopping_footer_description--global` | Description column (first column) of the footer |

---

## NOT widget regions

- The **promo/announcement bar above the header** is a BigCommerce native banner — managed in **Marketing → Banners**, not Page Builder.
- The **header's main nav** is built from your Web Pages (**Storefront → Web Pages**) — each page's "Show in navigation menu" toggle controls whether it appears, and pages with child pages become dropdowns. It is not a widget region.
- The footer **Navigate**, **Categories**, and **Brands** columns are populated from the store's web pages, categories, and brands lists respectively (managed in **Storefront → Web Pages**, **Products → Categories**, and **Products → Brands**) — the Brands column is conditional on the **Show brands in footer** setting. None are widget regions.

---

## Tips

- **Use `--global` for stuff that should appear on every page of that type** (every PDP, every category page). Otherwise you'll have to repeat the widget on each page.
- **Use the local region (no `--global`)** for one-off content — e.g. a sale banner just on Black Friday, or a category-specific FAQ.
- **Widgets in `--global` render first**, then page-local widgets render second. So if both have content, layout stacks vertically: global on top, local underneath.
- **Empty regions don't take space** — they collapse to zero height. Add a widget to see it.

---

## How to add a widget to a region

1. **Storefront → My Themes → Customize** (opens Page Builder).
2. **Top dropdown** — pick the page that contains the region.
3. **Scroll to the region** in the live preview — you'll see a dashed blue outline with the region name on hover.
4. **Drag a widget** from the left panel into the outlined area.
5. **Click the widget** to edit its content.
6. **Save → Publish**.

For deeper widget tutorials, see [HTML widget](widgets-html.md) — the main way to fill these regions — and [Demo Marketing Blocks](widgets-papathemes.md) for how the demo storefronts use them.
