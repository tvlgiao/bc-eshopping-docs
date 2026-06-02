# Quick Search — Keyword Suggestions

The keyword-suggestions feature adds **Google-style autocomplete** to the header search box. Users see popular keywords as they type, can press → to accept, ↑↓ to navigate, and Enter to search.

![Keyword suggestions in action](../img/keyword-suggestions.jpg){ loading=lazy }

!!! note "On by default — supply your own CSVs"
    Keyword suggestions are **enabled by default** (`suggest_keywords` defaults to `On`) and the demo stores ship with generated CSVs. Suggestions appear once the configured CSV file(s) are present at the keyword-file paths — supply your own `keyword,rank` CSV(s) to drive what shows. See the steps below.

## Quick start

1. **Generate keywords** — produce a CSV in the two-column `keyword,rank` format (see [CSV format](#csv-format) below). You can build it by hand or export it from your analytics / search-volume data. Whatever tool you use, the file **must** be in the `keyword,rank` format the theme expects.
2. **Upload the CSVs** — to BigCommerce **WebDAV → `/content/`** (drag & drop in **Storefront → File Manager**). Alternatively host on your own CDN.

<!--te-src:ICAgID4gKipDdXN0b21pemU6KiogQmlnQ29tbWVyY2UgYWRtaW4g4oaSICoqU3RvcmVmcm9udCDihpIgRmlsZSBNYW5hZ2VyIOKGkiBgL2NvbnRlbnQvYCoqIOKAlCB1cGxvYWQgeW91ciBga2V5d29yZCxyYW5rYCBDU1YgZmlsZShzKS4gKE9yIGhvc3QgdGhlbSBvbiBhbnkgQ0ROIHdob3NlIENPUlMgYWxsb3dzIHlvdXIgc3RvcmVmcm9udC4p-->
<!--te-mock--><div class="te-mock te-nav"><div class="te-nav__brand">BigCommerce admin</div><div class="te-nav__top"><span>Home</span></div><div class="te-nav__top"><span>Orders</span></div><div class="te-nav__top"><span>Products</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Customers</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top is-open"><span>Storefront</span><span class="te-nav__chev">⌃</span></div><div class="te-nav__sub">Themes</div><div class="te-nav__sub">Logo</div><div class="te-nav__sub">Home page carousel</div><div class="te-nav__sub">Social media links</div><div class="te-nav__sub">Script manager</div><div class="te-nav__sub">Web pages</div><div class="te-nav__sub">Blog</div><div class="te-nav__sub">Image manager</div><div class="te-nav__sub is-active">File Manager</div><div class="te-nav__top"><span>Marketing</span><span class="te-nav__chev">⌄</span></div><div class="te-nav__top"><span>Analytics</span></div><div class="te-nav__top"><span>Settings</span><span class="te-nav__chev">⌄</span></div></div>

3. **Enable in Theme Editor**:
    - Theme Editor → **eShopping Theme** section → **Search** heading → check **Enable keyword suggestions** ✅.
    - Set the **Keywords file 1 path** / **Keywords file 2 path** / **Keywords file 3 path** fields (see below).
4. **Save & publish**. Try searching on your storefront.

<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNlYXJjaCog4oaSICoqRW5hYmxlIGtleXdvcmQgc3VnZ2VzdGlvbnMqKiAoaWQgYHN1Z2dlc3Rfa2V5d29yZHNgKS4gRm9ybWF0OiBvbi9vZmYuIERlZmF1bHQ6IGB0cnVlYC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNlYXJjaCog4oaSICoqS2V5d29yZHMgZmlsZSAxIHBhdGgqKiAoaWQgYGtleXdvcmRzX2ZpbGUxYCkuIEZvcm1hdDogdGV4dCAocmVsYXRpdmUgYC9jb250ZW50L2AgcGF0aCBvciBmdWxsIFVSTCkuIERlZmF1bHQ6IGAvY29udGVudC9zdWdnZXN0LWtleXdvcmRzLTEuY3N2YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNlYXJjaCog4oaSICoqS2V5d29yZHMgZmlsZSAyIHBhdGgqKiAoaWQgYGtleXdvcmRzX2ZpbGUyYCkuIEZvcm1hdDogdGV4dCAocmVsYXRpdmUgYC9jb250ZW50L2AgcGF0aCBvciBmdWxsIFVSTCkuIERlZmF1bHQ6IGAvY29udGVudC9zdWdnZXN0LWtleXdvcmRzLTIuY3N2YC4=-->
<!--te-src:PiAqKkN1c3RvbWl6ZToqKiBUaGVtZSBFZGl0b3Ig4oaSICplU2hvcHBpbmcgVGhlbWUg4oaSIFNlYXJjaCog4oaSICoqS2V5d29yZHMgZmlsZSAzIHBhdGgqKiAoaWQgYGtleXdvcmRzX2ZpbGUzYCkuIEZvcm1hdDogdGV4dCAocmVsYXRpdmUgYC9jb250ZW50L2AgcGF0aCBvciBmdWxsIFVSTCkuIERlZmF1bHQ6IGAvY29udGVudC9zdWdnZXN0LWtleXdvcmRzLTMuY3N2YC4=-->
<!--te-mock--><div class="te-mock"><div class="te-mock__hd"><span>eShopping Theme</span><span class="te-x">✕</span></div><div class="te-mock__grp">Search</div><div class="te-mock__row"><span class="te-lbl">Enable keyword suggestions</span><span class="te-cb is-on"></span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Keywords file 1 path</span><span class="te-desc">One slice of your keyword list (any keywords)</span></span><span class="te-tx">/content/suggest-keywords-1</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Keywords file 2 path</span><span class="te-desc">Another slice — optional</span></span><span class="te-tx">/content/suggest-keywords-2</span></div><div class="te-mock__row"><span class="te-fld"><span class="te-lbl">Keywords file 3 path</span><span class="te-desc">Another slice — optional</span></span><span class="te-tx">/content/suggest-keywords-3</span></div></div>

!!! warning "The path fields are pre-filled"
    The three path fields ship pre-filled with `/content/suggest-keywords-1.csv`, `/content/suggest-keywords-2.csv`, and `/content/suggest-keywords-3.csv`. If you enable the feature but **don't upload files to those exact paths**, the search box simply shows **no suggestions** — there's no on-screen error (only a console warning is logged). Either upload your CSVs to those exact paths, or change the paths to point at your files.

## How the 3 files work

You can supply up to 3 CSV files. There's no functional difference between them — the theme **concatenates all three and ranks every keyword together** by its rank column (see [CSV format](#csv-format)). The split into three files is purely for your own convenience (e.g. to keep large lists manageable), not to change behaviour.

<!--te-tbl:fCBGaWxlIHwgV2hhdCB8CnwgLS0tLSB8IC0tLS0gfAp8IEtleXdvcmRzIGZpbGUgMSBwYXRoIHwgT25lIHNsaWNlIG9mIHlvdXIga2V5d29yZCBsaXN0IChhbnkga2V5d29yZHMpIHwKfCBLZXl3b3JkcyBmaWxlIDIgcGF0aCB8IEFub3RoZXIgc2xpY2Ug4oCUIG9wdGlvbmFsIHwKfCBLZXl3b3JkcyBmaWxlIDMgcGF0aCB8IEFub3RoZXIgc2xpY2Ug4oCUIG9wdGlvbmFsIHw=-->

You don't have to use all three — leave a path empty to skip it.

## File path syntax

Either:

- **Relative**: `/content/suggest-keywords-1.csv` (resolves to your storefront's `/content/` folder, served from BigCommerce WebDAV)
- **Full URL**: `https://cdn.example.com/keywords/keywords-1.csv` (CORS must allow your storefront)

!!! note "Lazy load vs eager load"
    - If **any** of the 3 paths is **relative**, the theme **lazy-loads** the CSVs only when the user focuses the search box (except on the search-results page, where they load immediately). This avoids loading the CSVs for visitors who never use search.
    - If **all** paths are **full URLs**, the CSVs load **immediately** on page load (browser cache handles repeat visits).

## CSV format

Each line is `keyword,rank` (UTF-8), where **rank** is an integer — a **higher** number means the keyword ranks higher and is shown first. Lines without a numeric second value are silently ignored, so a single-column file (bare words, no rank) produces **no suggestions** at all.

```csv
laptop,1000
phone,950
mouse,800
keyboard,780
monitor,600
```

When the user first focuses the search box (before typing), the **top 10 keywords by rank** are shown. As they type, the list is filtered to keywords that start with what they've typed, still ordered by rank. To control which keywords appear first, set **higher rank numbers** — the order of lines in the file does not matter.

## Keyboard behaviour

| Key | Action |
| --- | ------ |
| `→` | Accept the inline suggestion (the dimmed text after your cursor) — only when the cursor is at the **end** of the typed text; otherwise Right arrow just moves the cursor as usual |
| `↑` `↓` | Navigate the dropdown |
| `Enter` | Submit the highlighted suggestion |
| `Esc` | Close the search dropdown and clear the search box |

## Updating the keyword list

Refresh your keyword CSVs whenever your catalog changes significantly. Keep them in the `keyword,rank` format, then re-upload to the same paths — the theme picks them up on the next page-load.

## Disabling

Either uncheck **Enable keyword suggestions** in the Theme Editor, or leave all 3 path fields empty.

---

## Next

- [Blog](blog.md)
- [Search](search.md)
