# Md Tauhidul Islam: personal website

A one-page personal site in plain HTML and CSS. There is no menu, no framework, no JavaScript and no build step.

## Files

- `index.html`: all the text, links and page metadata
- `style.css`: the design; colors and fonts are at the top, in the `:root` block
- `photo.jpg`: the portrait shown at the top
- `404.html`: the page shown for addresses that don't exist
- `favicon.svg`: the browser tab icon
- `vercel.json`: security headers (used by Vercel; other hosts ignore it)

## How the layout works

The page is one composition scaled from the width of the screen. Text, photo, spacing and icons are all sized in `em`, and the `em` is 3.6% of the page width (`font-size: 3.6cqw` in `.page`). So a phone and a tablet show the page filling the screen, and a desktop shows it at the largest width (`--max`, 760px) in the middle. The proportions are identical everywhere.

- To make everything bigger or smaller on all screens, change `3.6cqw` (and the matching `3.6vw` and `27.4px` fallback lines just above it).
- To let the page grow wider on big screens, raise `--max`.

## Photo

- The portrait is a CSS background (`.portrait` in `style.css`), not an `<img>`, so it can't be saved by pressing and holding on a phone or by dragging it out. This stops casual saving only: anyone can still take a screenshot or find the file through the browser's developer tools.
- Use a **6:7 portrait** image (for example 1100 × 1283 px), save it as a real JPEG, and strip location/camera metadata before uploading. The current file has none.
- `index.html` also lists `photo.jpg` for link previews (`og:image`). Remove that line if you don't want the photo to appear when the site is shared.

## Security and fallbacks

- `vercel.json` sets a strict Content-Security-Policy and related headers. The same policy is also in a `<meta>` tag in each page, so it applies on hosts that ignore `vercel.json`.
- The page works without JavaScript (it uses none), without the web font (a similar local serif is used), and in browsers without container units (a viewport-based size is used instead).
- If you add anything new (a script, an embed, another font host), the Content-Security-Policy in `vercel.json` and in both `.html` files has to allow it, otherwise the browser will block it.

## Editing

- Change the text directly in `index.html`.
- The domain in the `canonical`, `og:url`, `og:image` and structured-data lines of `index.html` is `https://tauhidul.vercel.app/`. Update those lines if the site moves.

## Running locally

Run `python3 -m http.server` in this folder and open the address it prints. Opening `index.html` directly from disk may not show the photo, because of the security policy.

## Deploying

Any static host works. On Vercel, import the repository and leave the framework preset as "Other"; no build command or output directory is needed.
