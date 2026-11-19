# Md Tauhidul Islam: personal website

A one-page personal site in plain HTML and CSS. There is no menu, no framework and no build step.

## Files

- `index.html`: all the text, links and page metadata
- `style.css`: the design; colors and fonts are at the top, in the `:root` block
- `photo.jpg`: the portrait shown at the top (also used for link previews)
- `404.html`: the page shown for addresses that don't exist
- `favicon.svg`: the browser tab icon

## How the layout works

Every size on the page (text, spacing, photo, icons) is relative to the width of the text column. The column fills a phone screen and stops growing at `--col` (30rem), so a tablet or desktop shows the same view as a phone, scaled and centered. To make everything larger or smaller on all screens, change `--col`; to change only the text size, change the `5.6cqw` value in `.page`.

## Editing

- Change the text directly in `index.html`.
- To change the photo, replace `photo.jpg` with another image (a portrait-shaped photo about 800 px wide looks best).
- The font (Cormorant Garamond) loads from Google Fonts. If it can't load, the page falls back to Garamond or Georgia.
- The domain in the `canonical`, `og:url`, `og:image` and structured-data lines of `index.html` is `https://tauhidul.vercel.app/`. Update those lines if the site moves to a different address.

## Running locally

Open `index.html` in a browser, or run `python3 -m http.server` in this folder.

## Deploying

Any static host works. On Vercel, import the repository and leave the framework preset as "Other"; no build command or output directory is needed.
