#!/usr/bin/env python3
"""EPUB export for the LLM knowledge base wiki.

Generates an EPUB ebook from the wiki using only Python stdlib (zipfile, xml.etree).
Organized as chapters by type: Sources, Concepts, Entities, Comparisons.

Usage: python3 tools/export/build-epub.py
Output: output/wiki.epub
"""

import os
import re
import sys
import html
import uuid
import datetime
import zipfile
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI = ROOT / "wiki"
OUTPUT = ROOT / "output"

BOOK_TITLE = "LLM Knowledge Base"
BOOK_AUTHOR = "LLM Knowledge Base Wiki"
BOOK_ID = str(uuid.uuid4())

# ---------------------------------------------------------------------------
# Frontmatter parser
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[4:end]
    body = text[end + 4:].lstrip("\n")
    meta = {}
    for line in yaml_block.split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r'^(\w[\w_-]*)\s*:\s*(.*)$', line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            elif val.startswith("["):
                items = re.findall(r'"([^"]*)"', val)
                if not items:
                    items = re.findall(r"'([^']*)'", val)
                val = items
            meta[key] = val
    return meta, body


# ---------------------------------------------------------------------------
# Markdown -> XHTML converter (epub-safe)
# ---------------------------------------------------------------------------

def md_to_xhtml(text, all_slugs):
    """Convert markdown to XHTML suitable for epub, with internal links."""
    # Resolve wikilinks to internal epub links
    def replace_wikilink(m):
        target = m.group(1).strip()
        display = m.group(2) if m.group(2) else target.split("/")[-1].replace("-", " ").title()
        target_id = target.replace("/", "-").replace(" ", "-").lower()
        for slug in all_slugs:
            slug_id = slug.replace("/", "-")
            if slug == target or slug.endswith("/" + target):
                return f'<a href="{slug_id}.xhtml">{html.escape(display)}</a>'
        return html.escape(display)

    text = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', replace_wikilink, text)

    lines = text.split("\n")
    out = []
    in_code = False
    code_lines = []
    in_list = None
    list_items = []
    in_bq = False
    bq_lines = []

    def flush_list():
        nonlocal in_list, list_items
        if in_list and list_items:
            tag = in_list
            out.append(f"<{tag}>")
            for li in list_items:
                out.append(f"  <li>{_inline(li)}</li>")
            out.append(f"</{tag}>")
        in_list = None
        list_items = []

    def flush_bq():
        nonlocal in_bq, bq_lines
        if in_bq and bq_lines:
            out.append(f'<blockquote><p>{_inline(" ".join(bq_lines))}</p></blockquote>')
        in_bq = False
        bq_lines = []

    for line in lines:
        if re.match(r'^```', line):
            if in_code:
                out.append(f'<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>')
                in_code = False
                code_lines = []
                continue
            else:
                flush_list(); flush_bq()
                in_code = True
                continue
        if in_code:
            code_lines.append(line)
            continue

        if re.match(r'^>\s?', line):
            flush_list()
            in_bq = True
            bq_lines.append(re.sub(r'^>\s?', '', line))
            continue
        elif in_bq:
            flush_bq()

        if re.match(r'^(---|\*\*\*|___)\s*$', line.strip()):
            flush_list()
            out.append("<hr/>")
            continue

        hm = re.match(r'^(#{1,6})\s+(.*)', line)
        if hm:
            flush_list()
            lv = len(hm.group(1))
            out.append(f'<h{lv}>{_inline(hm.group(2))}</h{lv}>')
            continue

        lm = re.match(r'^\s*[-*+]\s+(.*)', line)
        if lm:
            flush_bq()
            if in_list != 'ul':
                flush_list(); in_list = 'ul'
            list_items.append(lm.group(1))
            continue

        lm = re.match(r'^\s*\d+\.\s+(.*)', line)
        if lm:
            flush_bq()
            if in_list != 'ol':
                flush_list(); in_list = 'ol'
            list_items.append(lm.group(1))
            continue

        if in_list:
            flush_list()

        if not line.strip():
            continue

        out.append(f"<p>{_inline(line)}</p>")

    flush_list(); flush_bq()
    if in_code:
        out.append(f'<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>')

    return "\n".join(out)


def _inline(text):
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


# ---------------------------------------------------------------------------
# Collect articles
# ---------------------------------------------------------------------------

def collect_articles():
    articles = []
    categories = [("sources", "Sources"), ("concepts", "Concepts"), ("entities", "Entities"), ("comparisons", "Comparisons")]
    for cat_key, cat_label in categories:
        cat_dir = WIKI / cat_key
        if not cat_dir.exists():
            continue
        for md_file in sorted(cat_dir.glob("*.md")):
            text = md_file.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)
            slug = str(md_file.relative_to(WIKI).with_suffix(""))
            title = meta.get("title", slug.split("/")[-1].replace("-", " ").title())
            articles.append({
                "slug": slug,
                "file_id": slug.replace("/", "-"),
                "title": title,
                "meta": meta,
                "body": body,
                "category": cat_key,
                "category_label": cat_label,
            })
    return articles


# ---------------------------------------------------------------------------
# EPUB building
# ---------------------------------------------------------------------------

EPUB_CSS = """
body { font-family: Georgia, serif; line-height: 1.6; color: #1a1a1a; margin: 1em; }
h1 { font-size: 1.6em; margin: 0 0 0.5em; }
h2 { font-size: 1.3em; margin: 1.2em 0 0.4em; border-bottom: 1px solid #ccc; padding-bottom: 0.2em; }
h3 { font-size: 1.1em; margin: 1em 0 0.3em; }
p { margin: 0.4em 0; text-align: justify; }
ul, ol { padding-left: 1.5em; margin: 0.4em 0; }
pre { background: #f5f5f5; padding: 0.6em; font-size: 0.85em; overflow-x: auto; border: 1px solid #ddd; border-radius: 3px; }
code { font-family: monospace; background: #f0f0f0; padding: 0.1em 0.3em; font-size: 0.9em; }
pre code { background: none; padding: 0; }
blockquote { border-left: 3px solid #999; padding: 0.3em 0.8em; margin: 0.6em 0; color: #555; font-style: italic; }
hr { border: none; border-top: 1px solid #ddd; margin: 1em 0; }
a { color: #0066cc; }
.meta { background: #f9f9f9; border: 1px solid #ddd; padding: 0.5em 0.8em; font-size: 0.85em; margin-bottom: 1em; border-radius: 3px; }
.meta strong { color: #333; }
.chapter-heading { text-align: center; padding: 3em 0; }
.chapter-heading h1 { font-size: 2em; }
"""


def make_xhtml_doc(title, body_content):
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
<meta charset="UTF-8"/>
<title>{html.escape(title)}</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
{body_content}
</body>
</html>"""


def make_container_xml():
    return """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""


def make_content_opf(articles, chapter_ids):
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    manifest_items = ['    <item id="style" href="style.css" media-type="text/css"/>']
    manifest_items.append('    <item id="toc" href="toc.xhtml" media-type="application/xhtml+xml"/>')
    manifest_items.append('    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>')

    spine_items = ['    <itemref idref="toc"/>']

    for cid in chapter_ids:
        manifest_items.append(f'    <item id="{cid}" href="{cid}.xhtml" media-type="application/xhtml+xml"/>')
        spine_items.append(f'    <itemref idref="{cid}"/>')

    for a in articles:
        fid = a["file_id"]
        manifest_items.append(f'    <item id="{fid}" href="{fid}.xhtml" media-type="application/xhtml+xml"/>')
        spine_items.append(f'    <itemref idref="{fid}"/>')

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookID" version="3.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>{html.escape(BOOK_TITLE)}</dc:title>
    <dc:creator>{html.escape(BOOK_AUTHOR)}</dc:creator>
    <dc:language>en</dc:language>
    <dc:identifier id="BookID">urn:uuid:{BOOK_ID}</dc:identifier>
    <meta property="dcterms:modified">{now}</meta>
  </metadata>
  <manifest>
{chr(10).join(manifest_items)}
  </manifest>
  <spine toc="ncx">
{chr(10).join(spine_items)}
  </spine>
</package>"""


def make_toc_ncx(articles, chapter_ids, chapter_labels):
    points = []
    order = 1
    for cid, clabel in zip(chapter_ids, chapter_labels):
        points.append(f"""    <navPoint id="nav-{cid}" playOrder="{order}">
      <navLabel><text>{html.escape(clabel)}</text></navLabel>
      <content src="{cid}.xhtml"/>
    </navPoint>""")
        order += 1
        for a in articles:
            if a["category"] == cid.replace("chapter-", ""):
                points.append(f"""      <navPoint id="nav-{a['file_id']}" playOrder="{order}">
        <navLabel><text>{html.escape(a['title'])}</text></navLabel>
        <content src="{a['file_id']}.xhtml"/>
      </navPoint>""")
                order += 1

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="urn:uuid:{BOOK_ID}"/>
  </head>
  <docTitle><text>{html.escape(BOOK_TITLE)}</text></docTitle>
  <navMap>
    <navPoint id="nav-toc" playOrder="0">
      <navLabel><text>Table of Contents</text></navLabel>
      <content src="toc.xhtml"/>
    </navPoint>
{chr(10).join(points)}
  </navMap>
</ncx>"""


def make_toc_xhtml(articles, chapter_ids, chapter_labels):
    items = []
    for cid, clabel in zip(chapter_ids, chapter_labels):
        items.append(f'<h2><a href="{cid}.xhtml">{html.escape(clabel)}</a></h2>')
        items.append("<ul>")
        for a in articles:
            if a["category"] == cid.replace("chapter-", ""):
                items.append(f'<li><a href="{a["file_id"]}.xhtml">{html.escape(a["title"])}</a></li>')
        items.append("</ul>")

    body = f"<h1>Table of Contents</h1>\n" + "\n".join(items)
    return make_xhtml_doc("Table of Contents", body)


def main():
    print("Collecting articles...")
    articles = collect_articles()
    if not articles:
        print("No articles found.")
        return

    all_slugs = [a["slug"] for a in articles]

    # Determine chapters
    categories_present = []
    cat_map = {"sources": "Sources", "concepts": "Concepts", "entities": "Entities", "comparisons": "Comparisons"}
    for cat_key, cat_label in cat_map.items():
        if any(a["category"] == cat_key for a in articles):
            categories_present.append((cat_key, cat_label))

    chapter_ids = [f"chapter-{c[0]}" for c in categories_present]
    chapter_labels = [c[1] for c in categories_present]

    OUTPUT.mkdir(parents=True, exist_ok=True)
    epub_path = OUTPUT / "wiki.epub"

    print(f"Building EPUB with {len(articles)} articles...")

    with zipfile.ZipFile(epub_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # mimetype must be first and uncompressed
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)

        # META-INF
        zf.writestr("META-INF/container.xml", make_container_xml())

        # OEBPS
        zf.writestr("OEBPS/style.css", EPUB_CSS)
        zf.writestr("OEBPS/content.opf", make_content_opf(articles, chapter_ids))
        zf.writestr("OEBPS/toc.ncx", make_toc_ncx(articles, chapter_ids, chapter_labels))
        zf.writestr("OEBPS/toc.xhtml", make_toc_xhtml(articles, chapter_ids, chapter_labels))

        # Chapter divider pages
        for cid, clabel in zip(chapter_ids, chapter_labels):
            body = f'<div class="chapter-heading"><h1>{html.escape(clabel)}</h1></div>'
            zf.writestr(f"OEBPS/{cid}.xhtml", make_xhtml_doc(clabel, body))

        # Article pages
        for a in articles:
            content = md_to_xhtml(a["body"], all_slugs)

            # Meta block
            meta_parts = []
            for k, v in a["meta"].items():
                if k == "title":
                    continue
                if isinstance(v, list):
                    v = ", ".join(v)
                v = re.sub(r'\[\[([^\]|]+)\]\]', lambda m: m.group(1).split("/")[-1].replace("-", " ").title(), str(v))
                meta_parts.append(f"<strong>{html.escape(k)}:</strong> {html.escape(v)}")
            meta_html = f'<div class="meta">{" | ".join(meta_parts)}</div>' if meta_parts else ""

            body = f"<h1>{html.escape(a['title'])}</h1>\n{meta_html}\n{content}"
            xhtml = make_xhtml_doc(a["title"], body)
            zf.writestr(f"OEBPS/{a['file_id']}.xhtml", xhtml)

    size_kb = epub_path.stat().st_size / 1024
    print(f"Done! {epub_path} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
