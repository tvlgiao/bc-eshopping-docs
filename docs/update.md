# Updating eShopping

## Standard update

BigCommerce will show an **Update available** badge on your theme card in **Storefront → My Themes** when a new version is released.

Click **Update available**. BigCommerce backs up your current configuration, installs the new version, and migrates your settings.

If you have a **customized** (edited theme files) copy, you cannot directly update — see below.

## Updating a customized theme

If you (or a developer) edited the theme files via Stencil CLI, the **Update available** badge won't appear on your custom copy. Instead:

1. Click **Update** on the **original** (un-customized) eShopping theme card to get the new version.
2. Make a **copy** of the new version (don't touch the original).
3. Re-apply your customizations to that new copy. If your edits are isolated in your own SCSS or template overrides, you can usually just re-paste them.
4. Re-confirm your chosen variation (**Industrial**, **AutoParts**, **Packaging**, or **Electronics**) and check that its colors, fonts, and copy are applied as expected — the active variation is part of your theme configuration.
5. Preview the new copy carefully — test home, PDP, category, cart.
6. Apply the new copy as the live theme.

## Reverting to an earlier version

If something breaks after an update:

1. **Storefront → My Themes → eShopping → ⋯ → Revisions**.
2. Pick the revision from before the update.
3. Click **Restore**.

The previous configuration comes back instantly. You can repeat this any time.

For more on theme revisions, see BigCommerce's help article on [Stencil themes](https://support.bigcommerce.com/s/article/Stencil-Themes).

## What changes between versions

We follow **semantic versioning** (`major.minor.patch`):

- **Patch** — bug fixes, no setting changes. Always safe to update.
- **Minor** — new features, new settings (with sensible defaults). Safe to update; review the new settings.
- **Major** — breaking changes or design overhauls. Read the [Release Notes](changelog.md) before updating. If you have a staging or preview storefront available, it's a good idea to test there first.

## Don't lose your custom widget content

Widget content created in **BigCommerce Page Builder** lives outside the theme files, so it survives every update untouched. If you use widgets from a **third-party widget app**, confirm with that app's vendor that they remain compatible after a major theme update. Any known issues will be noted in the [Release Notes](changelog.md).

---

## Next

- [Release notes](changelog.md)
- [FAQs](faqs.md)
- [Support](support.md)
