# Product FAQs Tab

The **FAQs** tab on a product page renders a built-in **ask-a-question form** — name + email + question + captcha + submit. It is *not* a pre-filled accordion. Shoppers can submit questions about the product directly from the PDP.

![PDP FAQs tab — ask-a-question form](../img/pdp-faq.jpg){ loading=lazy }

---

## Turn the FAQs tab on

**Theme Editor → eShopping → Product Page (PDP) → Show FAQ Tab** ✅.

A new **FAQs** tab (the default tab label) appears alongside the other product tabs that are active for that product — for example *Description*, *Videos*, *Specifications*, *Warranty*, *Reviews*.

!!! note "Tabs vs. stacked sections"
    The FAQs section appears as a **tab** only when **Show Product Description Tabs** is enabled (the default). If that setting is turned **off**, the FAQs section — along with *Description*, *Videos*, *Specifications*, *Warranty*, and *Reviews* — renders as a **stacked section** down the page (each with its own heading) instead of as a tab.

Those neighbor tabs are conditional, so the exact lineup varies per product:

- **Specifications** only appears when **Product custom fields in tabs** is on *and* the product has custom fields.
- **Warranty** only appears when the product has warranty text entered.
- **Videos** only appears when the product has product videos.

---

## How submissions are handled

When a shopper submits the form:

- The question is sent through your store's built-in BigCommerce **Contact Us** system — it uses your store's Contact page behind the scenes. The question is delivered to whatever address your Contact Us form is set to email.
- The theme automatically **prepends the product name and URL** to the submitted question (e.g. `[Product: Acme Wireless Drill - https://yourstore.com/acme-wireless-drill/]`) on its own line above the shopper's text, so you can immediately see which product each question is about in the Contact Us email.
- A success message renders inline.
- A **reCAPTCHA** box appears on the form when reCAPTCHA is enabled for your storefront in the store settings.

To change where these questions are delivered, edit your **Contact Us** page form recipient in the BigCommerce control panel (**Storefront → Web Pages →** your Contact page), where the contact form's destination email address is set.

---

## Where to put pre-written FAQ answers instead

If you want to display **answers** (not just collect questions), use one of these alternatives:

1. **Product description** — paste a Q&A section into the product's description (Catalog → Products → edit → Description).
2. **Custom fields tab** — turn on **Product custom fields in tabs**, then add custom fields named like `Q: Does this fit my vehicle?` with the answer as the value. They render in the **Specifications** tab as a 2-column table (label / value).
3. **Warranty tab widget area** — drop an accordion or collapsible-content widget into the Warranty tab widget area (region `product_below_warranty--global`). It renders **inside the Warranty tab**, after the warranty description text and *before* the warranty card grid, on every PDP that has warranty text.

    !!! warning "Requires the tabbed layout"
        This widget area only exists when **Show Product Description Tabs** is enabled. If that setting is off and the product sections render stacked, the `product_below_warranty--global` region is not included in the page, and any widgets placed there will not appear.
4. **Below-tabs widget area** — drop the accordion into the below-tabs widget area (region `product_below_content--global`, with the non-global twin `product_below_content`). It renders directly under the tabbed (or stacked) product content, visible on every PDP.

The 4th option is the closest to a "site-wide FAQ accordion that shows on every product page".

---

## SEO — `FAQPage` schema.org rich snippet

The built-in form doesn't emit FAQ schema markup (because there are no answers in it). If you provide FAQ content via an accordion in the below-tabs widget area, add this in **Storefront → Script Manager** (Location: Footer, Pages: Store pages) to expose JSON-LD:

```html
<script>
(function() {
  var items = document.querySelectorAll('[data-faq-item]');
  if (!items.length) return;
  var data = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: Array.from(items).map(function(li) {
      return {
        "@type": "Question",
        name: (li.querySelector('[data-faq-q]')?.textContent || '').trim(),
        acceptedAnswer: {
          "@type": "Answer",
          text: (li.querySelector('[data-faq-a]')?.textContent || '').trim()
        }
      };
    })
  };
  var s = document.createElement('script');
  s.type = 'application/ld+json';
  s.textContent = JSON.stringify(data);
  document.head.appendChild(s);
})();
</script>
```

Adapt the selectors (`[data-faq-item]`, `[data-faq-q]`, `[data-faq-a]`) to match the markup actually emitted by your Accordion widget.

---

## Next

- [Frequently Bought Together](product-fbt.md)
- [Product page overview](product.md)
- [Category page](category.md)
