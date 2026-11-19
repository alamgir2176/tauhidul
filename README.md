# Md Tauhidul Islam: personal website

A small personal site in plain HTML and CSS. There is no framework, no JavaScript and no build step.

## Files

- `index.html`: the home page (text, links and page metadata)
- `style.css`: the design for every page; colors and fonts are at the top, in the `:root` block
- `photo.jpg`: the portrait shown at the top
- `404.html`: the page shown for addresses that don't exist
- `favicon.svg`: the browser tab icon
- `vercel.json`: security headers and clean addresses (used by Vercel; other hosts ignore it)

## How the layout works

The page is one composition scaled from the width of the screen. Header, text, photo, spacing and icons are all sized in `em`, and the `em` is 3.6% of the page width (`font-size: 3.6cqw` in `.frame`). So a phone and a tablet show the page filling the screen, and a desktop shows it at the largest width (`--max`, 760px) in the middle. The proportions, and the menu, are identical everywhere. The menu is always a plain row of links, with no hamburger button.

- To make everything bigger or smaller on all screens, change `3.6cqw` (and the matching `3.6vw` and `27.4px` fallback lines just above it).
- To let the page grow wider on big screens, raise `--max`.

## Adding a page

1. Copy `404.html` to a new file, for example `writing.html`, and change the `<title>`.
2. Replace the `<main>` block with your content. For a list of items (like a "clips" page) use the `.list` pattern shown in `style.css`:

   ```html
   <main class="page">
     <section class="list">
       <h2>Section heading</h2>
       <div class="item">
         <a class="title" href="https://example.com/">Title of the piece</a>
         <p>One short line about it.</p>
       </div>
     </section>
   </main>
   ```

   For plain paragraphs use `<section class="text"><p>...</p></section>`.
3. Add one line to the menu, in **every** page's header: `<li><a href="/writing">Writing</a></li>`. Mark the current page's link with `aria-current="page"`.
4. Commit. On Vercel the page is available at `/writing` (without `.html`).

The header and footer are repeated in each page because there is no build step. If you later have many pages, a static-site generator can share them; until then, the copy-and-edit approach keeps the site simple.

## Photo

- The portrait is a CSS background (`.portrait` in `style.css`), not an `<img>`, so it can't be saved by pressing and holding on a phone or by dragging it out. This stops casual saving only: anyone can still take a screenshot or find the file through the browser's developer tools.
- Use a **6:7 portrait** image (for example 1100 × 1283 px), saved as a real JPEG with location and camera metadata removed. The current file has none.
- `index.html` also lists `photo.jpg` for link previews (`og:image`). Remove that line if you don't want the photo to appear when the site is shared.

## Security and fallbacks

- `vercel.json` sets a strict Content-Security-Policy and related headers. The same policy is also in a `<meta>` tag in each page, so it applies on hosts that ignore `vercel.json`.
- The page works without JavaScript (it uses none), without the web font (a similar local serif is used), and in browsers without container units (a viewport-based size is used instead).
- If you add anything new (a script, an embed, another font host), the Content-Security-Policy in `vercel.json` and in every `.html` file has to allow it, otherwise the browser will block it.

## Checking which version is live

Every page has `<meta name="site-version" content="...">` in its `<head>`. To see which version a browser is really showing, open the page's source (on a phone, type `view-source:` in front of the address) and look for that line. If it doesn't match the latest one in this repository, you are looking at an older deployment or a cached copy.

## Editing

- Change the text directly in `index.html`.
- The domain in the `canonical`, `og:url`, `og:image` and structured-data lines of `index.html` is `https://tauhidul.vercel.app/`. Update those lines if the site is served from a different address.

## Running locally

Run `python3 -m http.server` in this folder and open the address it prints. Opening `index.html` directly from disk will not show the photo or styles, because pages use root-relative addresses and a security policy.

## Deploying

Any static host works. On Vercel, import the repository and leave the framework preset as "Other"; no build command or output directory is needed.
