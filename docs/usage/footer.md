# Footer

The eShopping footer is built into the theme and has these areas:

1. **Brand block** — your logo, a tagline widget, and (optionally) social icons (left column).
2. **Navigate column** — your Storefront Web Pages, plus an automatic *Sitemap* link.
3. **Categories column** — your store's top-level categories.
4. **Brands column** — your shop-by-brand list (can be turned off; see ③).
5. **Bottom bar** — copyright line, payment-method icons, and the Powered-by / Designed-by credit.

The three link columns (Navigate, Categories, Brands) are generated automatically from your store — they are **not** hand-built link menus and there is no "Footer menu" to configure.

![Footer example — Industrial](../img/footer-industrial.png){ loading=lazy }
![Footer example — Auto Parts](../img/footer-autoparts.png){ loading=lazy }
![Footer example — Packaging](../img/footer-packaging.png){ loading=lazy }

---

## ① The brand block

The brand block shows your store logo, a tagline area, and (optionally) your social icons.

The tagline area is a global widget region (`eshopping_footer_description--global`). By default it's empty. See the [Widget regions reference](widget-regions.md) for the full list of regions.

1. Open Page Builder (**Storefront → My Theme → Customize**). Scroll down to the footer — the first column shows a dashed widget-region outline.
2. Click the **+** button inside that outline and drag in an **AI HTML Generator | PapaThemes** widget (this drops it into the **`eshopping_footer_description--global`** region). This widget is provided by the PapaThemes app, which must be installed.
3. Paste your tagline + contact details, e.g.:

   ```html
   <p>
     Acme Industrial Supply has been the trusted source for MRO, safety,
     and tooling since 1972. We stock over 50,000 SKUs and ship same-day
     from 3 US warehouses.
   </p>
   <p>
     <strong>Mon–Fri 8am–6pm CT</strong><br>
     <a href="tel:+18001234567">+1 (800) 123-4567</a><br>
     <a href="mailto:support@acme.com">support@acme.com</a>
   </p>
   ```

4. Save HTML.

### Social icons

Social icons render in the brand block **only when** the **Footer Placement** toggle is enabled under **Theme Editor → Header and footer → Social media icons**. The icons themselves come from the accounts you fill in at **Storefront → Social media accounts**.

Supported networks: Facebook, Instagram, X (Twitter), LinkedIn, YouTube, Pinterest, Tumblr, Google+, and RSS.

---

## ② The Navigate and Categories columns

These two columns are filled in automatically — there is nothing to wire up in a menu:

- **Navigate** — lists your **Storefront → Web Pages** (e.g. *About Us*, *Privacy Policy*, *Returns*, *Shipping*), and always ends with an automatic **Sitemap** link.
- **Categories** — lists your store's top-level categories.

To change what appears in the **Navigate** column, add, remove, or reorder your Storefront Web Pages. To change the **Categories** column, edit your category tree.

---

## ③ The Brands column { #brand-strip }

The third link column is titled **Brands**. It lists your shop-by-brand brands and ends with a **View All** link. Configure it in **Theme Editor → Header and footer**:

| Setting | Default | Effect |
| ------- | ------- | ------ |
| Show brands in footer | On | Show / hide the Brands column |
| Max brands in footer | 10 | Dropdown (5 / 8 / 10 / 15 / 20) — caps how many brands list before the *View All* link |

!!! note
    The Brands column hides automatically if **Show brands in footer** is off **or** your store has no brands.

---

## ④ The bottom bar

The bottom bar holds the copyright line, the payment-method icons, and the Powered-by / Designed-by credit. Each part has its own on/off control.

| Setting | Effect | Where |
| ------- | ------ | ----- |
| Store name | Appears in the copyright line | **Settings → Store profile → Store name** |
| Show Copyright Footer | Shows / hides the copyright line | Theme Editor → Header and footer |
| Show Powered By | Shows / hides the Powered-by / Designed-by line | Theme Editor → Header and footer |
| Payment-method icons | One toggle per provider | Theme Editor → Header and footer |

**Copyright line.** When **Show Copyright Footer** is on, the line reads:

> © {year} {Store name}. All rights reserved.

**Powered-by / Designed-by line.** When **Show Powered By** is on, the line reads:

> Powered by BigCommerce · Designed by PapaThemes.com

This whole line is controlled by the single **Show Powered By** toggle — turning it off hides **both** the BigCommerce and the PapaThemes credits together.

**Payment-method icons.** Supported providers: Amex, Discover, Mastercard, PayPal, Visa, Amazon Pay, Google Pay, Klarna. Each has its own toggle.

- On by default: Amex, Discover, Mastercard, PayPal, Visa
- Off by default: Amazon Pay, Google Pay, Klarna

---

## Footer colors

Set footer colors in **Theme Editor → eShopping Theme → Footer**. The **real defaults vary per variation**:

| Setting | Industrial (default) | AutoParts | Electronics | Packaging |
| ------- | -------------------- | --------- | ----------- | --------- |
| Footer Background | `#1a1713` | `#0f172a` | `#18181b` | `#1c1917` |
| Footer Text | `#a89b86` | `#94a3b8` | `#a1a1aa` | `#a8a29e` |
| Footer Heading | `#b8ad9b` | `#cbd5e1` | `#d4d4d8` | `#d6d3d1` |
| Footer Link | `#a89b86` | `#94a3b8` | `#a1a1aa` | `#a8a29e` |
| Footer Link Hover | `#faf8f4` | `#f8fafc` | `#fafafa` | `#fafaf9` |
| Footer Border | `#2e2a25` | `#1e293b` | `#27272a` | `#292524` |

You can override any of these after picking your variation.

---

## Next

- [Sidebar](sidebar.md)
- [Home page recipes](home-overview.md)
