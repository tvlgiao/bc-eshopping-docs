# Demo Marketing Blocks

Every marketing block you see on the demos is either a **built-in theme section** (controlled in the Theme Editor) or an **AI HTML Generator | PapaThemes** widget dropped into a widget region in Page Builder. The configurable theme sections ship with the theme and need no app; the marketing-block widgets use the **AI HTML Generator | PapaThemes** widget, which requires the **PapaThemes app** installed on your store.

If you imported a demo and are wondering where a banner, callout, or about block "comes from", this page tells you which is which — and where to edit it.

!!! info "Marketing blocks need the PapaThemes app"
    The theme's own configurable sections need nothing extra to install. The demo marketing blocks, however, use the **AI HTML Generator | PapaThemes** widget, which is provided by the **PapaThemes app** and works fully only on a store where that app is installed.

## Built-in theme sections (Theme Editor)

These appear automatically on the home page and are turned on/off and styled from **Storefront → My Themes → Customize**. They are not widgets and do not live in Page Builder.

- **Hero** — the home page hero banner
- **Trust strip** — the icon + label row beneath the hero
- **Featured Products**, **Best Sellers**, and **New Arrivals** sliders
- **Products by Category** sections
- **Brands carousel**
- **Blog posts** row
- **Newsletter** signup block
- **Sidebar Promo Card** — the promotional callout shown in the sidebar on category, brand, and search pages

All four demo home pages share the same section order: Hero → Trust strip → Featured → Best Sellers → New Arrivals → Products by Category → value-prop / social-proof blocks → Brands → Blog → Newsletter → about / contact blocks.

The "value-prop / social-proof" position and the "about / contact" position are not single blocks — each one holds a stack of several **AI HTML Generator | PapaThemes** widgets on the demos (see [Marketing widgets](#built-in-html-widgets-page-builder) below).

!!! note "Best Sellers only shows with sales data"
    The Best Sellers slider is turned on in every demo, but it only appears once your store has top-seller data. On a freshly imported store with no sales history yet, it stays hidden until BigCommerce has recorded enough orders to rank best sellers.

## Marketing widgets (Page Builder) { #built-in-html-widgets-page-builder }

Several marketing blocks on the demo home page are **AI HTML Generator | PapaThemes** widgets, added during the demo content import — they are not theme settings, and they require the **PapaThemes app**. They are grouped into two widget regions, and each region holds **a stack of multiple widgets**, not a single block. In Page Builder you'll see them stacked one above the other, and each is edited independently:

| Widget region | AI HTML Generator widgets stacked here (top to bottom) |
| ------------- | ----------------------------------------- |
| `home_below_products_by_category` (below Products by Category) | up to three blocks — a value-prop callout ("why shop with us"), a customer-reviews / social-proof block, and a resources block |
| `home_below_newsletter` (below the Newsletter) | up to two blocks — an about block and a "talk to an expert" / contact block |

!!! note "The exact set can vary per store"
    The blocks above are what the standard demo import creates. An individual imported store may have fewer or differently-named blocks in these regions. Treat each one as its own AI HTML Generator widget you can edit or delete.

The sidebar promo card on listing pages is a built-in theme section — configure it under the **Sidebar Promo Card** section in the Theme Editor. The `sidebar_below--global` region is also available if you want to add extra Page Builder widgets below the promo card. The footer brand description is an AI HTML Generator widget in `eshopping_footer_description--global`.

To edit any of these, open Page Builder, click the block, and edit its HTML. See the [AI HTML Generator guide](widgets-html.md) for the full editing flow.

!!! note "The PDP FAQ tab is built-in, not a widget"
    The FAQ accordion on product pages is a built-in theme feature, not a Page Builder widget. You cannot drop an accordion widget into it.

## Editing the marketing widgets

1. Open Page Builder: **Storefront → My Themes → Customize**.
2. Click the marketing block you want to change.
3. Edit the block's HTML in the inline editor.

The **AI HTML Generator | PapaThemes** widget exposes a single HTML code field — there are no separate padding, colour, or animation controls. Styling lives inside the HTML/CSS you write in that field. See [AI HTML Generator](widgets-html.md) for examples and the CSS classes the demos use.

## Next

- [AI HTML Generator](widgets-html.md)
- [Widget regions reference](widget-regions.md)
