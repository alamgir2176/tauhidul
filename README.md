# Md Tauhidul Islam: personal website

A small, quiet personal site in plain HTML and CSS. There is no framework, no JavaScript and no build step.

Live at <https://tauhidul.vercel.app/>.

## Files

| File | What it is |
| --- | --- |
| `index.html` | The home page: text, links and page metadata |
| `404.html` | The page shown for addresses that don't exist |
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

The page is one composition scaled from the width of the screen. Header, text, photo, spacing and icons are all sized in `em`, and the `em` is 3.6% of the page width (`font-size: 3.6cqw` in `.frame`). A phone and a tablet show the page filling the screen, and a desktop shows it at the largest width (`--max`, 760px) in the middle. The proportions, and the menu, are identical everywhere. The menu is always a plain row of links, with no hamburger button.

- To make everything bigger or smaller on all screens, change `3.6cqw` (and the matching `3.6vw` and `27.4px` fallback lines just above it).
- To let the page grow wider on big screens, raise `--max`.

## Adding a page

1. Copy `404.html` to a new file, for example `writing.html`, and change the `<title>`.
2. Replace the `<main>` block with your content. For plain paragraphs use `<section class="text"><p>...</p></section>`. For a list of items use the `.list` pattern described at the bottom of `style.css`.
3. Add one line to the menu in **every** page's header: `<li><a href="/writing">Writing</a></li>`. Mark the current page's link with `aria-current="page"`.
4. Add the new address to `sitemap.xml`.
5. Commit. On Vercel the page is available at `/writing` (without `.html`).

The header and footer are repeated in each page because there is no build step. If the site grows to many pages, a static-site generator can share them; until then, copy and edit keeps things simple.

## Photo

- The portrait is a CSS background (`.portrait` in `style.css`), not an `<img>`, so it can't be saved by pressing and holding on a phone or by dragging it out. This stops casual saving only: anyone can still take a screenshot or find the file through the browser's developer tools.
- Use a **6:7 portrait** image (for example 1100 × 1283 px), saved as a real JPEG with location and camera information removed. The current file has none. Check any new photo before adding it, because phone photos usually carry the camera model, the time and sometimes the place.
- Link previews use `og.png` (a plain card with the name), not the photo, so the portrait isn't passed around when the link is shared.

## Security and fallbacks

- `vercel.json` sets a strict Content-Security-Policy and related headers. The same policy is also in a `<meta>` tag in each page, so it applies on hosts that ignore `vercel.json`.
- The site loads nothing from third parties except the Google Fonts stylesheet and font files. It sets no cookies and uses no analytics.
- The page works without JavaScript (it uses none), without the web font (a similar local serif is used), and in browsers without container units (a viewport-based size is used instead).
- The Content-Security-Policy also lets the page read its own `site.webmanifest` (`manifest-src 'self'`).
- If you add anything new (a script, an embed, another font host), the Content-Security-Policy in `vercel.json` and in every `.html` file has to allow it, otherwise the browser will block it.

## Privacy

- The only contact details on the site are the LinkedIn profile and the email address in the footer. No phone number, home address or similar details are published.
- Before adding a file, check it for hidden information (photo metadata, document properties). Files in this repository are public while the repository is public.

## Icons and the share picture

The "T" icon is a Crimson Text capital (SIL Open Font License) drawn as a path, so it looks the same on every device. The share picture `og.png` uses the same typeface. To change the wording on the share picture, edit and re-export it at 1200 × 630, then raise `site-version`. Social apps keep old previews for a while; the Facebook Sharing Debugger and LinkedIn Post Inspector can refresh them.

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
