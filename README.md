# Md Tauhidul Islam: personal website

A small, quiet personal site in plain HTML and CSS. There is no framework, no JavaScript and no build step.

Live at <https://tauhidul.vercel.app/>.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The home page: text, links and page metadata |
| `404.html` | The page shown for addresses that don't exist |
| `fonts/` | Cormorant Garamond (regular, medium, semibold, bold) and its licence, `OFL.txt` |
| `style.css` | The design for every page. Colors and fonts are at the top, in the `:root` block |
| `photo.jpg` | The portrait shown at the top |
| `favicon.svg`, `favicon.ico` | The browser tab icon (the `.ico` is for older browsers) |
| `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `site.webmanifest` | The icon and name shown when the site is added to a phone's home screen |
| `og.png` | The picture shown when a link to the site is shared (1200 × 630) |
| `vercel.json` | Security headers and clean addresses (used by Vercel; other hosts ignore it) |
| `robots.txt`, `sitemap.xml` | Search engine instructions and the page list |
| `LICENSE` | Terms of use |
| `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` | What kind of help is welcome, and how to behave |
| `SECURITY.md` | How to report a problem |
| `CHANGELOG.md` | A short history of changes |
| `.github/` | Issue and pull request templates |
| `.editorconfig`, `.gitattributes`, `.gitignore` | Editor and git settings |

## How the layout works

The page is one composition scaled from the width of the screen. Text, photo, spacing and icons are all sized in `em`, and the `em` is 3.6% of the page width (`font-size: 3.6cqw` in `.frame`). A phone and a tablet show the page filling the screen, and a desktop shows it at the largest width (`--max`, 760px) in the middle. The proportions are identical everywhere, including a phone browser's "desktop site" view.

- To make everything bigger or smaller on all screens, change `3.6cqw` (and the matching `3.6vw` and `27.4px` fallback lines just above it).
- To let the page grow wider on big screens, raise `--max`.

## Header (switched off for now)

The site has no header at the moment: no name, no menu and no line at the top. Nothing is reserved for it, so the photo sits comfortably near the top on its own.

The name is kept as a hidden heading (`<h1 class="sr-only">`) on the home page, for search engines and screen readers.

**To bring the header back**, paste the block below at the very top of `.frame`, just above `<main>`, on every page. Nothing else needs to change: the page makes room for it by itself, and the photo and text move down by exactly the header's height. The styles for it (`.site-header`, `.brand`, `.menu`) are still in `style.css`. It looks the same on desktop, tablet, phone and a phone browser's desktop view: a thin line with a small bold name on the left and a plain row of links on the right, with a fine hairline underneath. There is never a hamburger button.

```html
<header class="site-header">
  <a class="brand" href="/">Md Tauhidul Islam</a>
  <nav class="menu" aria-label="Main">
    <ul>
      <li><a href="/" aria-current="page">Home</a></li>
      <li><a href="/writing">Writing</a></li>
    </ul>
  </nav>
</header>
```

Mark the current page's link with `aria-current="page"` and add one `<li>` per page. The hidden `<h1>` can stay when the header comes back; the header's name link is not a heading, so the page keeps exactly one.

## Adding a page

1. Copy `404.html` to a new file, for example `writing.html`. Change the `<title>`, and in `<main>` change `class="page center"` to `class="page"` (the `center` part is only for the 404 message).
2. Replace the content of `<main>`. For plain paragraphs use `<section class="text"><p>...</p></section>`. For a list of items use the `.list` pattern described at the bottom of `style.css`.
3. Keep the footer as it is: **every page except the home page has the home icon first**, then LinkedIn and email, with no "Contact" label. The home page has no home icon.
4. Link to the new page from the home page's text (see below), and add its address to `sitemap.xml`.
5. Bump `site-version` and add a line to `CHANGELOG.md`, then commit. On Vercel the page is available at `/writing` (without `.html`).

The footer is repeated in each page because there is no build step. If the site grows to many pages, a static-site generator can share it; until then, copy and edit keeps things simple.

### How to link to pages without crowding the site

- **One to three pages:** link them inside the home page's own words, as plain underlined links, for example "I also write a few notes." This feels like part of the writing, not a menu.
- **More than that:** make one quiet index page (for example `/more`) in the `.list` style, and link only that from the home page. The home page stays the same however many pages there are.
- **Icons are only for things everyone recognises:** home, LinkedIn, email and, at most, one more profile. Keep the row to four icons or fewer, and don't make icons for pages: nobody can guess what an icon for "Writing" means.

The home icon is the same blue box as the others, with the house drawn in the same thin line as the envelope and the letters. All three symbols are sized and centred to take the same share of the box, so keep that if you change one:

```html
<a class="icon" href="/" aria-label="Home">
  <svg viewBox="0 0 24 24" aria-hidden="true">
    <rect x="1" y="2" width="22" height="20" rx="1.6"/>
    <path class="cut" d="M5.61 12.38 L11.34 7.16Q12 6.55 12.66 7.16 L18.39 12.38 M7.86 10.88 L7.86 16.75Q7.86 17.65 8.76 17.65 L9.6 17.65Q10.5 17.65 10.5 16.75 L10.5 14.6Q10.5 13.7 11.4 13.7 L12.6 13.7Q13.5 13.7 13.5 14.6 L13.5 16.75Q13.5 17.65 14.4 17.65 L15.24 17.65Q16.14 17.65 16.14 16.75 L16.14 10.88"/>
  </svg>
</a>
```

## Photo

- The portrait is a CSS background (`.portrait` in `style.css`), not an `<img>`, so it can't be saved by pressing and holding on a phone or by dragging it out. This stops casual saving only: anyone can still take a screenshot or find the file through the browser's developer tools.
- Use a **6:7 portrait** image (for example 1100 × 1283 px), saved as a real JPEG with location and camera information removed. The current file has none. Check any new photo before adding it, because phone photos usually carry the camera model, the time and sometimes the place.
- Link previews use `og.png` (a plain card with the name), not the photo, so the portrait isn't passed around when the link is shared.

## Security and fallbacks

- `vercel.json` sets a strict Content-Security-Policy and related headers. The same policy is also in a `<meta>` tag in each page, so it applies on hosts that ignore `vercel.json`.
- The site loads nothing from third parties: the font is served from this repository too, so no visitor's address is sent to Google. It sets no cookies and uses no analytics.
- The page works without JavaScript (it uses none), without the web font (a similar serif already on the device is used), and in browsers without container units (a viewport-based size is used instead).
- The Content-Security-Policy also lets the page read its own `site.webmanifest` (`manifest-src 'self'`).
- If you add anything new (a script, an embed, a font from another host), the Content-Security-Policy in `vercel.json` and in every `.html` file has to allow it, otherwise the browser will block it.

## Privacy

- The only contact details on the site are the LinkedIn profile and the email address in the footer. No phone number, home address or similar details are published.
- Before adding a file, check it for hidden information (photo metadata, document properties). Files in this repository are public while the repository is public.

## Fonts

Cormorant Garamond is served from `fonts/` as small `.woff` files that hold only the Latin letters, numbers and common punctuation. If a page ever needs other characters (for example accented capitals beyond Latin-1, or another script), the files need to be re-made from the full fonts at <https://fonts.google.com/specimen/Cormorant+Garamond>, or those characters will show in the fallback serif. When you change fonts, keep `OFL.txt` next to them.

## Icons and the share picture

The "T" icon is a Cormorant Garamond capital (bold, the same family as the site; the thin text weight turned faint and blurry at icon sizes) drawn as a path, so it looks the same on every device. It is dark (`#1d1c1a`) on the site's off-white (`#faf8f4`), with a fine hairline (`#c8c2b6`) round the browser-tab version so the pale square doesn't disappear into a light tab. The share picture `og.png` uses the same typeface as the site. To change the wording on the share picture, edit and re-export it at 1200 × 630, then raise `site-version`. Social apps keep old previews for a while; the Facebook Sharing Debugger and LinkedIn Post Inspector can refresh them.

## Checking which version is live

Every page has `<meta name="site-version" content="...">` in its `<head>`. To see which version a browser is really showing, open the page's source (on a phone, type `view-source:` in front of the address) and look for that line. If it doesn't match the one in this repository, you are looking at an older deployment or a cached copy. Change that value whenever you publish a visible change.

## Running locally

Run `python3 -m http.server` in this folder and open the address it prints. Opening `index.html` directly from disk will not show the photo or styles, because pages use root-relative addresses and a security policy.

## Deploying

Any static host works. On Vercel, import the repository and leave the framework preset as "Other"; no build command or output directory is needed. If the site moves to another address, update the `canonical`, `og:url`, `og:image` and structured-data lines in `index.html`, and `robots.txt` and `sitemap.xml`.

## License

All rights reserved. See [LICENSE](LICENSE).

## Credits

Built with the help of [Claude](https://claude.com), an AI assistant made by [Anthropic](https://www.anthropic.com). Claude helped write the code and the text; the photo, the design decisions and the final say are Tauhidul's.
