#!/usr/bin/env python3
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "about.html", "contact.html", "jobs.html"]
BANNED = ["layoutmaster", "finally done", "555) 123", "123 web street"]
errors = []


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.imgs, self.html, self.title, self.meta = [], [], {}, "", set()
        self._t = False

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "html":
            self.html = a
        if tag == "meta" and a.get("name"):
            self.meta.add(a["name"])
        if tag == "title":
            self._t = True
        for k in ("href", "src"):
            if k in a:
                self.refs.append(a[k])
        if tag == "img":
            self.imgs.append(a)

    def handle_endtag(self, tag):
        if tag == "title":
            self._t = False

    def handle_data(self, d):
        if self._t:
            self.title += d


for name in PAGES:
    f = ROOT / name
    if not f.exists():
        errors.append(f"missing {name}")
        continue
    text = f.read_text()
    p = P()
    p.feed(text)
    if not p.title.strip():
        errors.append(f"{name}: no title")
    if "viewport" not in p.meta:
        errors.append(f"{name}: no viewport")
    if "description" not in p.meta:
        errors.append(f"{name}: no description")
    if p.html.get("lang") != "en":
        errors.append(f'{name}: missing lang="en"')
    for i in p.imgs:
        if "alt" not in i:
            errors.append(f"{name}: img without alt: {i.get('src')}")
    for r in p.refs:
        if re.match(r"^(https?:|mailto:|tel:|#|data:)", r):
            continue
        if not (ROOT / r.split("#")[0].split("?")[0]).exists():
            errors.append(f"{name}: broken ref {r}")
    low = text.lower()
    for b in BANNED:
        if b in low:
            errors.append(f"{name}: banned text {b!r}")
    if re.search(r"\b(add|use this space|make this page useful)\b", re.sub(r"<[^>]+>", " ", low)):
        errors.append(f"{name}: possible editing-instruction wording")

css = (ROOT / "style.css").read_text()
for m in re.finditer(r"padding:\s*(\d{3,})px", css):
    errors.append(f"style.css: large fixed padding {m.group(0)}")

for img in (ROOT / "images").rglob("*"):
    if img.is_file() and img.stat().st_size > 1_000_000:
        errors.append(f"oversized asset {img.relative_to(ROOT)}")

print("\n".join(errors) if errors else f"OK: {len(PAGES)} pages checked")
sys.exit(1 if errors else 0)
