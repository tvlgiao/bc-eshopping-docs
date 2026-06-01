# FAQs

## Setup & install

??? question "Do I need a developer to install this theme?"
    No. Everything in this guide is point-and-click in the BigCommerce admin. The only "code" you ever paste is into an **HTML Widget** — and we provide ready-to-copy snippets.

??? question "Can I switch between variants (Industrial, AutoParts, Packaging, Electronics)?"
    Yes. The theme ships with four variants — **Industrial**, **AutoParts**, **Packaging**, and **Electronics**. Switching a variant only changes colors, fonts, and a few text snippets (such as the trust strip and newsletter text). Your products, orders, customers, and settings are unaffected. Widget placements are **not** part of a variant — you rebuild those manually in Page Builder (see step 2 below). You can:

    1. Make a backup copy of your current theme (My Themes → ⋯ → Make a copy).
    2. Apply the variant in the Theme Editor, then rebuild that variant's home-page widgets in Page Builder (the demo stores use BigCommerce's built-in HTML widgets for their marketing blocks).
    3. Update the colors / fonts to match the new variant.

    Allow ~30 minutes for a full variant swap.

??? question "Does it work with multi-storefront?"
    Yes. Install the theme on each channel separately. Each channel keeps its own widget content, colors, fonts, and settings.

??? question "Do I need the PapaThemes Widgets app?"
    Not for the core layout. The demo stores build their home-page marketing blocks and footer description with BigCommerce's **built-in HTML widgets** in Page Builder — no third-party app required. If you do choose to add the PapaThemes Widgets app for extra building blocks, check its listing in the BigCommerce App Marketplace for current pricing and capabilities.

??? question "Page Builder widgets don't show up after editing."
    Refresh the Page Builder tab once and re-open the page you're editing. If a widget you added still doesn't appear, drag it onto the page again from the widget panel and save.

## Customization

??? question "How do I change the primary color across the whole site?"
    Theme Editor → **eShopping Theme → Colors → Terra**. That single setting updates the primary accent across buttons, links, accent borders, and hover states.

    Two things it does **not** touch — they have their own settings in the same **Colors** panel:

    - **Sale Price** — the color of the discounted price (red by default).
    - **Sale Badge Background** — the background of the "on sale" badge.

    Change those two separately if you want them to match (or contrast with) your Terra color.

??? question "How do I add a sticky 'order' bar at the bottom of the PDP on mobile?"
    Theme Editor → **eShopping Theme → Product Page (PDP) → Show Mobile Sticky Add to Cart** ✅. It's automatic — appears once the user scrolls past the in-page ATC.

??? question "How do I show a different image on mobile vs desktop?"
    The hero is the built-in BigCommerce **Carousel** — edit its slides in the BC admin under **Storefront → Carousel** (one image per slide). For full control over mobile vs desktop imagery on any other section, use a `<picture>` element with `srcset` inside an HTML widget:

    ```html
    <picture>
      <source media="(max-width:600px)" srcset="/content/mobile.jpg">
      <img src="/content/desktop.jpg" alt="…">
    </picture>
    ```

??? question "How do I hide the breadcrumbs?"
    Theme Editor → **Global → Pages → Hide breadcrumbs** ✅. This is a single global toggle that hides breadcrumbs site-wide. (Separately, the same panel has **Hide page heading**, **Hide category page heading**, **Hide blog page heading**, and **Hide contact us page heading** toggles — but those hide the page *title*, not the breadcrumbs.)

??? question "Can I change the order of the sections on the home page?"
    The built-in toggles only show/hide sections — they do not reorder them. To change the order, disable the built-in sections you want to move and recreate them as Page Builder widgets in your preferred order. Check the PapaThemes Widgets app listing in the BigCommerce App Marketplace for available product-display widgets.

## Bugs & quirks

??? question "Stop the product image gallery from sticking as I scroll the PDP"
    On desktop, the product image gallery stays pinned (sticky) while you scroll the product details. To turn that off, add a script in **Storefront → Script Manager** (Location: Footer, Pages: Store pages):

    ```html
    <script>
      (function(){
        var s = document.createElement('style');
        s.textContent = '.productView .productView-images { position: static !important }';
        document.head.appendChild(s);
      })();
    </script>
    ```

??? question "Video doesn't play in Safari"
    If your MP4 video was encoded with an unsupported codec (e.g. H.265/HEVC on older devices, or VP9), Safari may refuse to play it. The safest format for cross-browser compatibility is **H.264 MP4**. To re-encode to H.264 with ffmpeg:

    ```bash
    ffmpeg -i input.mp4 -vcodec libx264 -c:a aac output.mp4
    ```

??? question "Where is the 'You May Also Like' section on the cart?"
    It appears in two places: on the **cart page** below your cart items, and inside the **slide-out cart drawer**. The setting takes two numbers: the first controls how many products appear on the cart page, the second controls how many appear in the cart drawer. In both places it shows as a horizontal product slider, and only when the cart has products and your store is set to display prices to the current shopper.

    If it's missing, open Theme Editor → **eShopping Theme → Cart Cross-sell → Cross-sell products (page,drawer — 0 = off)**. This field takes **two numbers separated by a comma** — the first is how many cross-sell products show on the **cart page**, the second is how many show in the **cart drawer**. Set the first number above `0` (the default is `6,4`) to show the section on the cart page.

??? question "Lighthouse score is lower than I expected"
    Three quick wins:

    1. **Optimize images** — make sure every product image is JPEG/WebP under 200 KB.
    2. **Lazy-load Products-by-Category** — Theme Editor → eShopping Theme → Products by Category → **Lazy load sections on scroll** ✅.
    3. **Narrow the Recent Sales popup scope** — Theme Editor → eShopping Theme → Recent Sales Popup → **Show on pages**. Choose a narrower option such as **Homepage only** (or **Off — don't show**) instead of **All pages**.

??? question "How do I add Google Analytics / Meta Pixel / Klaviyo?"
    Use **Settings → Tracking & Analytics** for the standard integrations, or **Storefront → Script Manager** for any custom snippet. Don't edit theme files — your customization survives updates this way.

??? question "Page Builder shows a 'Save failed' error after I edited a widget"
    Refresh the Page Builder tab and try the save again — a stale editing session is the usual culprit. If it persists, re-open the page from Storefront → Web Pages (or the page's Page Builder entry), make your edit again, and save.

## Performance

??? question "What's the recommended image size?"
    These are general suggestions — the theme doesn't enforce fixed dimensions, and BigCommerce automatically resizes images for each placement. As a starting point:

    - **Product images**: large square images (e.g. ~1500 × 1500) in JPG/PNG, compressed to keep file size small.
    - **Hero / carousel images**: wide landscape images; upload at the largest size you'll display and compress well.
    - **Brand logos**: small transparent PNGs.
    - **Category banners**: wide landscape images in JPG/WebP.

    The most important thing for performance is keeping each file's weight low after compression.

??? question "How fast does the theme load?"
    Real-world scores depend mostly on your image weight, the apps and 3rd-party scripts you add, and your store's content. The theme is built to meet these Core Web Vitals targets: **LCP under 2.5 s, CLS under 0.1, INP under 200 ms**. For your own numbers, run Lighthouse on your live store after adding your content.

## Support

??? question "Can you set up the theme for me?"
    We offer paid setup services. Email <contact@papathemes.com> with your store URL + which demo you want to clone — we'll send a quote.

??? question "Can you customize the theme for me?"
    Yes — we offer custom development on top of our themes. Email us with a description of what you want and we'll quote.

??? question "What we don't support"
    See [Support → What we don't support](support.md#we-do-not-support).

---

## Still stuck?

Email <contact@papathemes.com> — Mon–Fri, 8 AM – 5 PM (GMT+8).
