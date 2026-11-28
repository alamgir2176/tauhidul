# Changelog

Notable changes to the site, newest first. The version on each page is in `<meta name="site-version">`.

## 2026-11-28

- LICENSE: the first paragraph no longer says the text and the photograph are Tauhidul's own work (the photo was taken by someone else, and the text was written with help). It now says they are about him and asks people to ask before copying. To go back, use commit `e4704e6`.

## 2026-11-27

- Tried a thin hairline frame around the portrait and took it out again the same day. The site is back exactly as in commit `ac28646` (site version `2026-11-22-d`). The tried version is in commit `22d0931`.
- Removed `.well-known/security.txt` again, together with its check and README section: it needed a new date every year, and the site is meant to need no upkeep. The footer email stays as the contact. To bring it back, use commit `9604a6f`.
- Added `.well-known/security.txt` (contact: the email already on the home page; expires 2026-11-26 next year, so renew it once a year). The check script now looks at it. The pages themselves are unchanged. To go back, delete the file and the "security.txt" check, or use commit `da772f2`.

## 2026-11-24

- LICENSE: rewritten shorter and softer. It now covers the text and the photograph, asks for written permission before reuse, and keeps the fonts under their own licence. To go back, use commit `4be3904`.
- LICENSE: "the design" is no longer listed among the things Tauhidul owns (layout, colours and type are common ideas, as the README says); the icons are named instead. To go back, use commit `fe2d314`.
- README: added a short "About this site" paragraph. The site itself is unchanged (still version `2026-11-22-d`).

## 2026-11-22

- Home page text: "…helping where I could, and I like to wander…" is now two sentences ("…helping where I could. I like to wander…"), so fewer "and"s run on. To go back, use commit `66d5f6f` (site version `2026-11-22-c`).
- Home page text: "the philosophy of Bengal" is now "Bengali philosophy", and the last sentence is split so "And… and" no longer echoes: "And I always come back to Bengali novels. I keep a small collection of them." To go back, use commit `6f96ee6` (site version `2026-11-22-b`).
- Home page text, small edits for an English reader's ear: "it's still the place", "stayed on for my master's too", "live well alongside them", "and I keep a small collection of them". To go back, use commit `b15f192` (site version `2026-11-22-a`).
- Home page text: "I read Western and Indian thought…" is now "During those years I read Western and Indian thought…", which ties the reading to the university years.

## 2026-11-21

- Footer icons are back to the thin-line set (plain house with roof, "in" with a round arch, envelope), with the envelope made a little narrower (13.0 wide instead of 14.1, the same width as the "in") so it no longer stands out. The filled icons tried just before are in commit `dd7670b` (site version `2026-11-21-m`).
- Footer icons are now small filled blue shapes (house, envelope with fold lines, and an "in" in the style of the LinkedIn mark) instead of thin lines. Same blue (`#0099ff`), no box, same height and same top and bottom line. **To go back** to the thin-line icons, use commit `d4802af` (site version `2026-11-21-l`).
- The "n" in the LinkedIn icon is redrawn like the real logo's: a smooth round arch rising from the stem, with its top level with the top of the "i". Same thin line as the other icons. **To go back**, use commit `a1b444c` (site version `2026-11-21-k`).
- Footer icons redrawn to belong together: the house is now the plain house shape (no door), the "i" has a round dot, and the "n" has a flat top like the real LinkedIn "in". All three keep the same thin line, the same height and the same top and bottom line. **To go back** to the previous drawing, use commit `9d4aed8` (site version `2026-11-21-j`).
- The footer icons are blue again (`#0099ff`, as before) instead of slate blue, still as thin lines without boxes. **To go back** to the slate blue (`#4f6f8c`), use commit `4e490b4` (site version `2026-11-21-i`), or change `--icon` in `style.css`.
- The three footer icons now share the same height and the same top and bottom line (the house is a little lower and wider-set, the envelope and the letters nudged by a fraction of a pixel). **To go back** to the previous drawing, use commit `44e3a77` (site version `2026-11-21-h`).
- The three footer icons have square corners (house, envelope and the dot of the "i") instead of rounded ones, and sit closer together as one small group. **To go back** to the rounded, wider-spaced icons, use commit `ec8382b` (site version `2026-11-21-g`): `git checkout ec8382b -- index.html 404.html style.css README.md`, then raise `site-version`.
- Footer icons are now thin lines in a quiet slate blue (`#4f6f8c`) with no box behind them, a little larger, so they sit more calmly on the page and meet the contrast guideline. **To go back** to the bright blue boxes, use commit `20548f8` (site version `2026-11-21-f`): `git checkout 20548f8 -- index.html 404.html style.css README.md`, then raise `site-version`.
- Home page text: the reading (Western and Indian thought, the philosophy of Bengal, logic) now sits in the paragraph about studying philosophy, so the questions that follow it lead naturally into the paragraph about technology; a few phrases made plainer.
- Added `AUDIT.md`, a full audit of the site with findings and advice (live headers confirmed: A+ on securityheaders.com and A+, 135/100, on the MDN HTTP Observatory). README now gives the correct widest size (1100px, as in the CSS).
- `scripts/check-pages.py` also checks that the site's own address is the same in every page, `robots.txt` and `sitemap.xml`; the README has a checklist for moving to another host or a custom domain.
- Added `scripts/check-pages.py`, a small check that every page has the same footer and home icon, the same version and security policy, working links and a sitemap entry. Run it before publishing.
- The house icon's corners (roof peak, door, wall bottoms) are softly rounded, to match the rounded letters and the envelope.
- Icon letter made bolder and larger (still Cormorant Garamond) so it stays sharp and clear on a phone's home screen and in browser tabs; each icon size is drawn at its own size instead of shrunk from a large one.
- Tab icon and home-screen icons are now a dark "T" on the site's off-white instead of off-white on dark, still in Cormorant Garamond.
- The house icon now has an open doorway (no line under the door), like the familiar home icon; lighter and clearer at small size.
- Email icon now sits inside the blue box like the others, as a small envelope drawn in the same thin line. The three footer symbols are sized and centred to take the same share of their boxes.

## 2026-11-20

- Header and menu switched off for now, with no empty space left in their place. The README explains how to bring the header back.
- Pages other than the home page get a home icon first in the footer; the "Contact" label is gone.
- The 404 page's email icon now has the same size as on the home page.
- Longer link-preview description (LinkedIn asks for at least 100 characters).
- Tab icon, home-screen icons and the share picture now use the site's own typeface, Cormorant Garamond.
- The font (Cormorant Garamond) now comes from this site instead of Google, so nothing is loaded from third parties.
- New tab icon, phone home-screen icons and a manifest, so the site installs with a proper icon.
- A plain share picture (`og.png`) for link previews; the name is now the page's main heading.
- Rewrote the text about me in a calmer voice, with links to the Barishal region and Jahangirnagar University.
- LinkedIn icon now sits in a blue box like the email icon, with thinner letters.
- Shortened the footer line to "© 2026 Md Tauhidul Islam".
- Added the license, contributing notes, security note, robots.txt and sitemap.
- Removed an unused photo file from the repository.

## 2026-11-19

- First version of the site: portrait, short text, header with menu, footer with contact icons.
- Same view on phone, tablet and desktop.
- Security headers, a custom 404 page and a favicon.
- Menu changed from "Contact" to "Connect"; added a location line under the portrait.
