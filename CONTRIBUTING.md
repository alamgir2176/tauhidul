# Contributing

This is a personal website, so the words, the photo and the design are not open for changes. Thank you for looking, and for caring enough to read this.

## What is welcome

- **A broken link, a typo or a display problem.** Please open an issue and tell me what you saw, on which page, and on which device and browser. A screenshot helps.
- **A security concern.** Please follow [SECURITY.md](SECURITY.md) and don't post details publicly.

## What is not accepted

- Pull requests that change the text, the photo, the colors or the layout.
- New features, scripts, trackers or third-party embeds. The site is meant to stay small and quiet.

If you want to build something similar for yourself, you're welcome to be inspired by it, but the files themselves are covered by the [LICENSE](LICENSE).

## For the owner: before you publish a change

1. Open the site locally (see the README) and check it on a narrow and a wide window.
2. Check any new image for hidden information such as camera model, time or place.
3. If you add a page, link it from the home page's text (see the README, "Adding a page"), keep the footer with the home icon, and add it to `sitemap.xml`.
4. Change `site-version` in the `<head>` of every page so you can tell which version is live.
5. Add a line to [CHANGELOG.md](CHANGELOG.md).
6. Run `python3 scripts/check-pages.py`; it should say "All good".
