# Md Tauhidul Islam: personal website

A one-page personal site in plain HTML and CSS. There is no menu, no framework and no build step.

## Files

- `index.html`: all the text and links
- `style.css`: the design; colors and fonts are at the top, in the `:root` block
- `photo.jpg`: the portrait shown at the top
- `favicon.svg`: the browser tab icon

## Editing

- Change the text directly in `index.html`.
- To change the photo, replace `photo.jpg` with another image of any size (a portrait-shaped photo of about 800 px wide looks best).
- The font (Cormorant Garamond) is loaded from Google Fonts. If it cannot load, the page falls back to Garamond or Georgia.

## Running locally

Open `index.html` in a browser, or run `python3 -m http.server` in this folder.

## Deploying

Any static host works. On Vercel, import the repository and leave the framework preset as "Other"; no build command or output directory is needed.
