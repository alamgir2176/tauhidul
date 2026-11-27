#!/usr/bin/env python3
"""Check that every page of the site is consistent.

Run it from the project folder before you publish:

    python3 scripts/check-pages.py

It reads every .html file next to it (nothing is changed) and reports
anything that doesn't match: the footer, the home icon, the version marker,
the security policy, the header, links and files that don't exist, and the
sitemap, and security.txt. It needs only Python 3, no installs. It exits with an error code if
it finds a problem, so it can also be run automatically later.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
HOME_PAGE = "index.html"
NO_SITEMAP = {"404.html"}  # pages that are not listed in sitemap.xml

problems = []


def problem(page, text):
    problems.append(f"  {page}: {text}")


def squash(text):
    return re.sub(r"\s+", " ", text).strip()


pages = sorted(p for p in ROOT.glob("*.html"))
if not pages:
    sys.exit(f"No .html files found in {ROOT}")
if not (ROOT / HOME_PAGE).exists():
    sys.exit(f"{HOME_PAGE} is missing in {ROOT}")

data = {}
for p in pages:
    html = p.read_text(encoding="utf-8")
    footer = re.search(r"<footer.*?</footer>", html, re.S)
    data[p.name] = {
        "html": html,
        "footer": footer.group(0) if footer else None,
        "version": (re.search(r'name="site-version" content="([^"]*)"', html) or [None, None])[1],
        "csp": (re.search(r'http-equiv="Content-Security-Policy" content="([^"]*)"', html) or [None, None])[1],
        "has_header": bool(re.search(r'<header class="site-header">', html)),
    }

# 1. Footer and home icon
HOME_ICON = re.compile(r'<a class="icon" href="/"[^>]*aria-label="Home"[^>]*>.*?</a>\s*', re.S)
reference = None
for name, d in data.items():
    if d["footer"] is None:
        problem(name, "has no <footer>")
        continue
    has_home = bool(HOME_ICON.search(d["footer"]))
    if name == HOME_PAGE and has_home:
        problem(name, "the home page must not have the home icon")
    if name != HOME_PAGE:
        if not has_home:
            problem(name, "the footer has no home icon")
        else:
            first_icon = re.search(r'<a class="icon" href="([^"]*)"', d["footer"]).group(1)
            if first_icon != "/":
                problem(name, "the home icon must come first in the footer")
    if re.search(r'class="label"', d["footer"]):
        problem(name, 'the footer still has a "Contact" label')
    body = squash(HOME_ICON.sub("", d["footer"]))
    if reference is None:
        reference = (name, body)
    elif body != reference[1]:
        problem(name, f"the footer (apart from the home icon) differs from {reference[0]}")

home_svgs = {n: squash(HOME_ICON.search(d["footer"]).group(0)) for n, d in data.items()
             if d["footer"] and HOME_ICON.search(d["footer"])}
if len(set(home_svgs.values())) > 1:
    problem("(all pages)", "the home icon is not identical on every page that has it")

# 2. Version marker
versions = {n: d["version"] for n, d in data.items()}
if None in versions.values():
    for n, v in versions.items():
        if v is None:
            problem(n, 'has no <meta name="site-version">')
if len({v for v in versions.values() if v}) > 1:
    problem("(all pages)", "site-version differs: " + ", ".join(f"{n}={v}" for n, v in versions.items()))

# 3. Security policy: same on every page, and the same as vercel.json (which only adds frame-ancestors)
csps = {n: d["csp"] for n, d in data.items()}
if None in csps.values():
    for n, v in csps.items():
        if v is None:
            problem(n, "has no Content-Security-Policy <meta>")
if len({v for v in csps.values() if v}) > 1:
    problem("(all pages)", "the Content-Security-Policy <meta> differs between pages")
vj = ROOT / "vercel.json"
if vj.exists():
    try:
        cfg = json.loads(vj.read_text(encoding="utf-8"))
        header_csp = next(h["value"] for rule in cfg.get("headers", []) for h in rule["headers"]
                          if h["key"] == "Content-Security-Policy")
        norm = lambda s: sorted(x.strip() for x in s.split(";") if x.strip() and not x.strip().startswith("frame-ancestors"))
        for n, v in csps.items():
            if v and norm(v) != norm(header_csp):
                problem(n, "the Content-Security-Policy <meta> doesn't match vercel.json")
    except (StopIteration, KeyError, ValueError):
        problem("vercel.json", "could not read the Content-Security-Policy")

# 4. Header: either every page has it, or none does
with_header = [n for n, d in data.items() if d["has_header"]]
if with_header and len(with_header) != len(data):
    missing = [n for n in data if n not in with_header]
    problem("(all pages)", "the header is on " + ", ".join(with_header) + " but missing from " + ", ".join(missing))
if with_header:
    menus = {}
    for n in with_header:
        links = re.findall(r'<li><a href="([^"]*)"', re.search(r'<nav.*?</nav>', data[n]["html"], re.S).group(0))
        menus[n] = links
    if len({tuple(v) for v in menus.values()}) > 1:
        problem("(all pages)", "the header menus list different links")

# 5. Basics every page needs
for n, d in data.items():
    h = d["html"]
    if '<html lang="' not in h:
        problem(n, "<html> has no lang")
    if "<title>" not in h:
        problem(n, "has no <title>")
    if 'name="viewport"' not in h:
        problem(n, "has no viewport <meta>")
    if n != HOME_PAGE and not re.search(r'<main class="page', h):
        problem(n, 'has no <main class="page">')

# 6. Links and files must exist (addresses starting with "/")
def target_exists(href):
    path = href.split("#")[0].split("?")[0]
    if path in ("", "/"):
        return (ROOT / HOME_PAGE).exists()
    rel = path.lstrip("/")
    return any((ROOT / c).exists() for c in (rel, rel + ".html", rel.rstrip("/") + "/index.html"))

for n, d in data.items():
    for attr, href in re.findall(r'(href|src)="(/[^"]*)"', d["html"]):
        if not target_exists(href):
            problem(n, f'{attr}="{href}" points to a file that doesn\'t exist')
css = ROOT / "style.css"
if css.exists():
    for href in re.findall(r'url\("?(/[^")]+)"?\)', css.read_text(encoding="utf-8")):
        if not target_exists(href):
            problem("style.css", f"url({href}) points to a file that doesn't exist")
manifest = ROOT / "site.webmanifest"
if manifest.exists():
    for icon in json.loads(manifest.read_text(encoding="utf-8")).get("icons", []):
        if not target_exists(icon["src"]):
            problem("site.webmanifest", f'icon {icon["src"]} doesn\'t exist')

# 7. Sitemap lists every page
sm = ROOT / "sitemap.xml"
if sm.exists():
    listed = re.findall(r"<loc>https?://[^/]+(/[^<]*)</loc>", sm.read_text(encoding="utf-8"))
    listed = {u.rstrip("/") or "/" for u in listed}
    for n in data:
        if n in NO_SITEMAP:
            continue
        addr = "/" if n == HOME_PAGE else "/" + n[:-5]
        if addr not in listed:
            problem(n, f"is not in sitemap.xml (expected {addr})")
    for u in listed:
        if u != "/" and not (ROOT / (u.lstrip("/") + ".html")).exists():
            problem("sitemap.xml", f"lists {u}, but there is no such page")
else:
    problem("sitemap.xml", "is missing")

# 8. One address for the site everywhere (canonical, share picture, structured data,
#    robots.txt, sitemap.xml). Useful when the site moves to a custom domain.
own = {}
for n, d in data.items():
    h = d["html"]
    for pat in (r'rel="canonical" href="https?://([^/"]+)',
                r'property="og:url" content="https?://([^/"]+)',
                r'property="og:image" content="https?://([^/"]+)',
                r'name="twitter:image" content="https?://([^/"]+)',
                r'"url":\s*"https?://([^/"]+)'):
        for host in re.findall(pat, h):
            own.setdefault(host, []).append(n)
for fname in ("robots.txt", "sitemap.xml"):
    f = ROOT / fname
    if f.exists():
        for host in re.findall(r"(?:Sitemap:\s*|<loc>)https?://([^/<\s]+)", f.read_text(encoding="utf-8")):
            own.setdefault(host, []).append(fname)
if len(own) > 1:
    problem("(site address)", "more than one address is used: " +
            "; ".join(f"{h} in {', '.join(sorted(set(v)))}" for h, v in own.items()))

# 9. security.txt: present, has Contact and Expires, not expired (renew it once a year),
#    and its contact is an address that is on the home page.
sec = ROOT / ".well-known" / "security.txt"
if not sec.exists():
    problem(".well-known/security.txt", "is missing")
else:
    txt = sec.read_text(encoding="utf-8")
    contact = re.search(r"^Contact:\s*(\S+)", txt, re.M)
    expires = re.search(r"^Expires:\s*(\S+)", txt, re.M)
    if not contact:
        problem(".well-known/security.txt", "has no Contact line")
    elif contact.group(1).startswith("mailto:") and contact.group(1) not in data[HOME_PAGE]["html"]:
        problem(".well-known/security.txt", f"contact {contact.group(1)} is not on the home page")
    if not expires:
        problem(".well-known/security.txt", "has no Expires line")
    else:
        from datetime import datetime, timezone, timedelta
        try:
            when = datetime.fromisoformat(expires.group(1).replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            if when < now:
                problem(".well-known/security.txt", f"expired on {expires.group(1)}: set a new date, up to a year ahead")
            elif when < now + timedelta(days=45):
                problem(".well-known/security.txt", f"expires soon ({expires.group(1)}): set a new date, up to a year ahead")
        except ValueError:
            problem(".well-known/security.txt", f"Expires is not a valid date: {expires.group(1)}")

# Report
print(f"Checked {len(data)} page(s): {', '.join(data)}")
if problems:
    print(f"\n{len(problems)} problem(s) found:")
    print("\n".join(problems))
    sys.exit(1)
print("All good: footers, home icon, version, security policy, header, links, sitemap, security.txt and site address match.")
