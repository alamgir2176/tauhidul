# Website audit: Md Tauhidul Islam

| | |
| --- | --- |
| **Site** | <https://tauhidul.vercel.app/> (source: this repository, `main`) |
| **Audit date** | 21 November 2026 |
| **Version audited** | `site-version` 2026-11-21-e, plus the check script added afterwards |
| **Prepared by** | [Claude](https://claude.com) (Sonnet 5.5), an AI assistant made by [Anthropic](https://www.anthropic.com) |
| **Approved by** | Md Tauhidul Islam, 21 November 2026 |

## 1. Summary

This is a very small, very safe site. It has no JavaScript, no forms, no login, no database, no cookies, no analytics and no third-party requests, so most of the usual ways a website gets attacked simply do not exist here. I found **no way to break into it through its own code**, and nothing that leaks private details in the files it publishes today.

What I did find is mostly about **comfort and polish**, not safety:

- Two lines of small print are **very small on a phone** (about 7 px and 9 px). This is the one finding I would fix first.
- The blue icons and the faint link underline are **below the usual contrast guidelines**.
- The photo file is **about twice as large as it needs to be**.
- **Old phone photos still sit in the git history**, with camera model and date (no location). They matter only while the repository is public.

Nothing here is urgent. Section 12 lists what I would do, in order, and which items need your decision because they touch the design.

### Scorecard

"Strong" means I found nothing worth changing. "Good" means small improvements are possible. "Attention" means there is something I would change.

| Area | Verdict | One line |
| --- | --- | --- |
| Security of the site itself | Strong | Nothing to attack; strict policy as a second wall |
| Privacy | Good | Published files are clean; old photos remain in git history |
| Accessibility | Attention | Good structure; small print and contrast need work |
| Performance | Good | About 250 KB for a first visit; photo could be half that |
| Search and link previews | Strong | Complete and correct |
| Responsive behaviour | Strong | Same view from 320 px to 1920 px, no overflow |
| Code quality and upkeep | Good | Clean and consistent; one stale line in the README |
| Repository hygiene | Strong | Licence, policies, changelog and a check script |
| Moving to a new host | Good | Documented; two things work only on Vercel |

## 2. Scope, method and honest limits

I read every file in the repository, ran the site locally (`python3 -m http.server`) and opened it in a real Chromium browser at 320, 390, 820, 1280 and 1920 px wide, with JavaScript off and on. I measured sizes, contrast ratios and text sizes with scripts instead of judging by eye, and looked at the git history for files that should not be there.

I am an AI assistant, not a professional auditor, and this is not a penetration test. Things I **could not** do:

- **Check the live server.** My workspace cannot reach the live site, so I read the security headers from `vercel.json` but could not confirm that Vercel sends them. The owner then checked at <https://securityheaders.com> on 21 November 2026: the Vercel site scores **A+**, and the old Netlify copy scores **D** (see S3). The Mozilla Observatory (<https://observatory.mozilla.org>) is a good second test.
- **Run Lighthouse or an HTML validator.** I measured the same things by hand (sizes, contrast, text size, overflow), but a tool report would be a good second opinion. Chrome's built-in Lighthouse (developer tools) is free.
- **Test on real phones, a screen reader, or older browsers.** I tested keyboard order and zoom, not VoiceOver or TalkBack.
- **Judge the account side** (GitHub, Vercel, domain, email). You told me these are secured, and I took that as given.

## 3. Security

### What I checked

The HTML, CSS and `vercel.json` for anything that runs code, takes input, loads from outside, or can be framed or misused; the Content-Security-Policy; links to other sites; and the repository for secrets.

### What is good

- **There is nothing to inject into.** No scripts, forms, inputs, iframes, `on…=` handlers or `javascript:` links anywhere. Cross-site scripting and similar attacks have no entry point.
- **A strict policy as a second wall.** `default-src 'none'`, `script-src 'none'`, `connect-src 'none'`, `form-action 'none'`, `base-uri 'none'`, and images, styles, fonts and the manifest only from the site itself. Even if someone managed to slip code into a page, the browser would refuse to run it. The same policy is set in `vercel.json` and in a `<meta>` tag in every page, so it still applies on a host that ignores `vercel.json`.
- **No outside dependencies.** The font is served from this site, there is no CDN, no package manager, no build step. That removes the commonest modern risk: a compromised third-party package.
- **Clickjacking and framing blocked** (`frame-ancestors 'none'`, `X-Frame-Options: DENY`).
- **Other headers present:** `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy` (camera, microphone, location, payment, USB off), `Strict-Transport-Security`, `Cross-Origin-Opener-Policy`.
- **Outgoing links** to LinkedIn, Wikipedia and the university use `rel="noopener noreferrer"`, so those sites cannot reach back to this page.
- **No secrets** in the files or history (searched for keys, tokens, passwords).
- **The JSON-LD block** (search-engine data) is plain data. With `script-src 'none'` it cannot run.

### Findings

| ID | Level | Finding | Advice |
| --- | --- | --- | --- |
| S1 | Low | The email address is written in plain `mailto:`, so spam robots can collect it. This cannot harm the site, only your inbox. | Accept it, or use a separate address for the site. Hiding it properly needs JavaScript, which would cost more than it saves. |
| S2 | Info | On Vercel, files such as `README.md`, `CHANGELOG.md` and `LICENSE` are also served as web pages. They hold nothing secret, but they describe how the site is built. `scripts/` and this audit are hidden by `.vercelignore`. | Optional: add the other documents to `.vercelignore`. |
| S3 | Info | The same site was also built on Netlify, with different headers. The owner's check shows it scores **D** on securityheaders.com, against **A+** for the Vercel site. | The owner plans to delete that site and its link. Once it is gone, nothing more is needed. |
| S4 | Info | `Strict-Transport-Security` includes `includeSubDomains`. On a custom domain this makes every subdomain require HTTPS. | Fine if all subdomains support HTTPS. Know it before adding one that does not. |
| S5 | Info | `frame-ancestors` cannot be set from a `<meta>` tag, only by a real header. On a host without headers, `X-Frame-Options` and `frame-ancestors` are lost. | Set them in `_headers` or the host's settings (section 11). |
| S6 | Info | When the old hosting project is deleted, a DNS record that still points to it lets a stranger claim the address ("subdomain takeover"). | Remove the DNS record when you remove the project. |

### Account side (outside the code)

Most real-world incidents for a site like this come from accounts, not code. Worth one look: two-step login on GitHub, Vercel, the domain registrar and the email account; registrar "domain lock" on; the domain set to auto-renew; and a recovery method that is not only the same email address.

## 4. Privacy

### What I checked

Hidden data in every image, the text of every page, the full git history, and what the browser contacts when the page loads.

### What is good

- `photo.jpg`, `og.png` and every icon have **no EXIF data** (no camera, no time, no GPS).
- The pages contain **no phone number, home address, grades or similar**. The only contact details are the LinkedIn profile and one email address.
- **Nothing is sent to third parties.** No Google Fonts, no analytics, no cookies, no tracking pixel. The browser made no request outside the site, and the policy forbids it.
- The text was written to stay at the level you were comfortable with: region, university, interests. The photo caption gives the place the photo was taken, not where you live.

### Findings

| ID | Level | Finding | Advice |
| --- | --- | --- | --- |
| P1 | Medium (while public) | The git history still holds three older images: two phone photos and a screenshot. I checked the two photos: both carry **device information and a timestamp** (camera or phone model, software, date). Neither has GPS. | Make the repository private soon, as you planned. Making it private does not erase copies someone already downloaded or forked. For a clean history I can rewrite it and force-push once (a one-time job; it changes every commit's identifier). |
| P2 | Low | The email address is public by design (see S1). | None needed. |
| P3 | Info | `Referrer-Policy: strict-origin-when-cross-origin` tells LinkedIn only that the visitor came from this site's address, not from which page. | Fine. |

## 5. Accessibility

### What I checked

Page structure, keyboard use, zoom, text sizes and colour contrast (measured against the WCAG 2.2 guidelines), touch-target size, and motion.

### What is good

- `<html lang="en">`, one `<h1>` (hidden but readable by screen readers and search engines), proper `<main>` and `<footer>`.
- Every icon link has a text label (`aria-label`); the portrait has a description (`role="img"` with a label).
- Keyboard use works: the first Tab stop is the first link, order follows the page, a visible outline shows focus.
- Zooming is allowed (the viewport does not block pinch-zoom) and the page does not overflow at 200 % zoom.
- The gentle entrance animation is switched off for people who ask for reduced motion.
- Main text contrast is excellent: 16.1 : 1. Grey small print is 5.1 : 1 and links 7.2 : 1, all above the 4.5 : 1 guideline.

### Findings

| ID | Level | Finding | Advice |
| --- | --- | --- | --- |
| A1 | **Medium** | The page scales with the screen width, so on a 390 px phone the **photo caption is 7.0 px** and the **copyright line 8.7 px** (on a 320 px phone, 5.8 px and 7.1 px). That is too small to read comfortably, and zooming is the only remedy. On a desktop they are 13.7 px and 17 px, which is fine. | Give both a floor, for example `font-size: max(0.5em, 11px)` for the caption and `max(0.62em, 12px)` for the copyright. Desktop does not change at all. This slightly bends "identical on every screen", so it is your call. |
| A2 | Low | Body text is 14 px on a 390 px phone. Cormorant Garamond has small letters for its size, so it reads like 12 px in most fonts. Pleasant but delicate, especially outdoors. | Optional: raise the scale slightly (for example `3.6cqw` to `3.9cqw`). Changes the whole composition, so only if you agree after seeing it. |
| A3 | Low | The blue icon box against the page is **2.83 : 1**, and the pale symbol inside the blue is also **2.83 : 1**. The guideline for graphics is 3 : 1. The icons are extra (each has a text label), but the symbols are the part people must make out. | A slightly deeper blue such as `#0088e0` reaches 3.5 : 1 and still looks like the same blue. Your colour choice, so I have not touched it. |
| A4 | Low | Links in the text are told apart from the rest mainly by a thin, pale underline (1.7 : 1), and the link colour is only 2.2 : 1 darker/lighter than the text. Someone with low vision may not notice them. | Optional: a slightly darker underline colour (for example `#a39d90`). |
| A5 | Info | The visible icon is about 18 px on a phone. A hidden 36 px area around it makes it easier to tap, which passes the WCAG 2.2 minimum (24 px) but is under the 44 px that phone guidelines recommend. The two hidden areas overlap a little. | Fine as is. |
| A6 | Info | Only a light theme exists (`color-scheme: light`). Someone using dark mode sees a pale page. | A deliberate choice for a calm page; no change suggested. |

## 6. Performance

### What I checked

File sizes (and gzip sizes for the text files), what loads first, and what would slow a first visit on a weak connection.

| File | Size |
| --- | --- |
| `index.html` | 5.8 KB (2.2 KB compressed) |
| `style.css` | 9.2 KB (2.7 KB compressed) |
| `photo.jpg` | 197 KB (1100 × 1283 px) |
| Two preloaded fonts (medium, semibold) | 44 KB together |
| `og.png` (not loaded by visitors, only link previews) | 47 KB |
| Whole repository as served | about 418 KB |

A first visit loads roughly **250 KB**, which is small. The photo is the main part; the page is usable as soon as the HTML, CSS and fonts arrive.

### What is good

- One stylesheet, no render-blocking scripts, no images in the HTML, nothing to download from other servers.
- The photo and the two main fonts are preloaded; `font-display: swap` shows text immediately in a similar serif until the font arrives.
- Fonts are subset to the needed letters (about 22 KB each instead of hundreds).
- No layout jumping: the photo has a fixed aspect ratio.

### Findings

| ID | Level | Finding | Advice |
| --- | --- | --- | --- |
| F1 | Low | The photo is displayed at most 357 px wide, but the file is 1100 px. At 800 px (enough even for a 2× screen) with the same look it would be about **100 KB instead of 197 KB** (about 83 KB at 700 px). I tested the sizes, not the look. | Re-export at around 800 px wide and compare it visually before replacing. |
| F2 | Low | Fonts are `.woff`; `.woff2` is about a quarter to a third smaller. | Make `.woff2` from the full fonts on a machine that has the tools, keep `.woff` as fallback. Saves about 30 KB. |
| F3 | Info | As far as I know, Vercel revalidates static files on each visit by default, so returning visitors still make a small check for the fonts and photo. I did not verify this on the live site. | Optional: add a long `Cache-Control` for `/fonts/*` and the icons in `vercel.json`. If you change those files, rename them. |
| F4 | Info | The text fades in for 0.8 s on load. It is gentle, but means the page is visually "arriving" for a moment. | A design choice, left as is. |

## 7. Search and link previews

### What I checked

The `<head>` of each page, `robots.txt`, `sitemap.xml`, the structured data, and the share image.

### What is good

- Title, description (112 characters, above LinkedIn's 100 minimum), canonical address, `lang`, and one main heading.
- Open Graph and Twitter tags with a 1200 × 630 share image that does not use the portrait.
- Structured data (`Person`) with name, university, topics and the LinkedIn profile; it deliberately has no photo, birth date or contact details.
- `robots.txt` allows everything and points to the sitemap; the 404 page is marked `noindex`.
- The photo is blocked from image search (`noimageindex`).
- LinkedIn's Post Inspector warning was fixed. The remaining "publish date" note does not apply to a personal page.

### Findings

| ID | Level | Finding | Advice |
| --- | --- | --- | --- |
| E1 | Info | The visible page shows your full name nowhere except the browser tab and the hidden heading ("I'm Tauhidul" is the first line). Search engines handle this normally. | None; it matches your wish for a page without a header. |
| E2 | Info | On a new domain the addresses in the page, `robots.txt` and `sitemap.xml` must all change, and Google Search Console should receive the new sitemap. | The check script now catches a forgotten address; see section 11. |

## 8. Responsive behaviour and design consistency

### What I checked

Widths of 320, 390, 820, 1280 and 1920 px, without JavaScript: horizontal overflow, failed requests, console messages, font loading, the 404 status, and the look at 1280 px.

### Results

- **No horizontal scrolling** at any width, and none at 200 % zoom.
- **No failed requests, no console errors**, with JavaScript on or off. The custom font loads at every size.
- The unknown address returns a real **404** status with the 404 page.
- Text is about 80 characters per line at 1280 px, long but still comfortable at this size; on a phone it is about 30 to 40 characters.
- The page keeps the same composition everywhere, as intended. It works without JavaScript, without the web font (a similar serif is used) and in browsers without container units (a viewport-based size is used).

### Findings

| ID | Level | Finding | Advice |
| --- | --- | --- | --- |
| R1 | Info | At 1280 px the text column is about 1050 px wide because `--max` is 1100 px. A narrower column (around 760 px) would read slightly more like a book page. | Your own choice of width; no change suggested. |

## 9. Code quality and upkeep

### What I checked

Structure, repetition, comments, consistency between pages, and the documentation against the code.

### What is good

- Plain, readable files with no build step; every value in `em`, colours and fonts at the top of `style.css`.
- The footer and the home icon are the same on every page, and a check script (`scripts/check-pages.py`) now enforces it, together with the version marker, security policy, links, sitemap and site address.
- The README covers how to add a page, restore the header, replace the photo, move hosts and deploy.
- No AI traces inside the site's pages or code; the credit is only in the README and the commit history.

### Findings

| ID | Level | Finding | Advice |
| --- | --- | --- | --- |
| C1 | Low | The README said the page's widest size is 760 px, but `--max` in the CSS is 1100 px. (Fixed together with this audit.) | Keep the README in step when you change CSS values by hand. |
| C2 | Info | Each page repeats the footer and the long policy line. Fine for two pages; with many pages a generator saves effort. | The README already says when to reconsider. |
| C3 | Info | Old CSS rules for the header (`.site-header`, `.brand`, `.menu`) remain while the header is off. | Intentional: they are what makes restoring the header work. |

## 10. Repository hygiene

- Licence (all rights reserved, fonts under OFL), security policy, contributing guide, code of conduct, changelog, issue and pull-request templates, `.editorconfig`, `.gitattributes` and a `.gitignore` that blocks raw phone photos and secrets are all present.
- **Advice:** when the repository becomes private, also switch on branch protection for `main` (no force-push, no deletion) and keep two-step login on the account. Do this *after* any history rewrite (see P1), since a rewrite needs one force-push.

## 11. Moving to another host and a custom domain

Everything is plain static files, so any static host will serve it. Two things work only on Vercel, and one needs care:

1. **`vercel.json`** sets the headers and clean addresses. On Netlify or Cloudflare Pages, put the same headers in a `_headers` file. The policy `<meta>` in each page keeps working meanwhile, but `frame-ancestors` and the other headers need the real header.
2. **Clean addresses** (`/writing` without `.html`) are a Vercel setting. Check them on the new host before adding pages.
3. **Addresses inside the files** (canonical, `og:url`, `og:image`, `twitter:image`, structured data, `robots.txt`, `sitemap.xml`) must all change together. `python3 scripts/check-pages.py` now reports any that still show a different address.

The full step-by-step list is in the README under "Moving to another host or a custom domain".

## 12. Recommendations, in order

| # | What | Why | Your decision needed? |
| --- | --- | --- | --- |
| 1 | Give the photo caption and copyright line a minimum size (A1) | The only real readability problem | Yes (slightly bends "same on all screens") |
| 2 | Make the repository private; I can first clean the history of the old phone photos (P1) | Removes device information from public view | Yes (history rewrite) |
| 3 | After going live on the new domain, check the live headers again on securityheaders.com (the Vercel site scored A+) and run `python3 scripts/check-pages.py` | Other hosts do not read `vercel.json` | No |
| 4 | Delete the old Netlify site (scored D; the owner plans to), and remove stale DNS records when moving (S6) | Avoid a weaker duplicate and takeover risk | No |
| 5 | Deepen the blue a little (A3) and darken the link underline (A4) | Contrast guidelines | Yes (colour choices) |
| 6 | Re-export the photo at about 800 px (F1) | Halves the biggest file | Yes (check the look) |
| 7 | Add `.woff2` fonts and long cache times (F2, F3) | Small speed gain | No |
| 8 | Check two-step login, domain lock and auto-renew on all accounts | Accounts are the real risk | No |

## 13. What I would add, and what I would not

**Worth adding, later and only if wanted**

- A `_headers` file next to `vercel.json`, so the headers survive a move to Netlify or Cloudflare Pages without anyone remembering.
- A `security.txt` file, which gives researchers a standard place to find how to report a problem. It would repeat the email address, so only if you are comfortable with that.
- A simple monthly reminder to run the check script and the online header tests.

**I would not add**

- Analytics, comment boxes, contact forms, a newsletter, a cookie banner, social buttons, a dark theme or animations. Each one would cost the calm and the safety that make this site what it is, and none is needed for what the page is for.

## 14. Credit and approval

Prepared by **Claude** (Sonnet 5.5), an AI assistant made by Anthropic, at the request of Md Tauhidul Islam, on 21 November 2026. The measurements in sections 5, 6 and 8 were taken by scripts on a local copy of the site; the rest comes from reading the files. The findings are my best judgement and are not a substitute for a professional security review.

Reviewed and approved by **Md Tauhidul Islam**, 21 November 2026.
