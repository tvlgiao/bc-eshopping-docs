# bc-eshopping-docs

Documentation site for the **eShopping** BigCommerce theme by [PapaThemes](https://papathemes.com).

Production URL: <https://bc-eshopping-docs.papathemes.com>

## Local development

Install MkDocs Material once:

```bash
pip install mkdocs-material
```

Run the local dev server:

```bash
mkdocs serve
```

Open <http://127.0.0.1:8000>.

## Build the static site

```bash
mkdocs build
```

Output is written to `site/`.

## Deploy

If the docs are published via GitHub Pages:

```bash
mkdocs gh-deploy --clean --force
```

Otherwise upload the contents of `site/` to your hosting bucket (e.g. AWS S3 + CloudFront).
