#!/usr/bin/env python3
"""Print-ready HTML export for the LLM knowledge base wiki.

Generates a beautifully formatted single HTML file designed for printing
(with @media print CSS, page breaks, headers, footers, table of contents).

Usage:
  python3 tools/export/build-pdf.py                           -> output/wiki-export.html (entire wiki)
  python3 tools/export/build-pdf.py wiki/concepts/llm-knowledge-base.md  -> single article

Output: output/wiki-export.html
"""

import os
import re
import sys
import html
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI = ROOT / "wiki"
OUTPUT = ROOT / "output"

PRINT_CSS = r"""
@page {
  size: A4;
  margin: 2cm 2.5cm;
  @top-center { content: "LLM Knowledge Base"; font-size: 9pt; color: #666; }
  @bottom-center { content: counter(page); font-size: 9pt; color: #666; }
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: "Georgia", "Times New Roman", serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #1a1a1a;
  background: #fff;
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

@media print {
  body { padding: 0; max-width: none; }
}

/* Cover page */
.cover {
  text-align: center;
  padding: 6rem 2rem;
  page-break-after: always;
}
.cover h1 { font-size: 2.5rem; margin-bottom: 0.5rem; color: #1a1a1a; }
.cover .subtitle { font-size: 1.2rem; color: #555; margin-bottom: 2rem; }
.cover .date { font-size: 0.95rem; color: #888; }

/* TOC */
.toc { page-break-after: always; }
.toc h2 { font-size: 1.5rem; margin-bottom: 1rem; padding-bottom: 0.3rem; border-bottom: 2px solid #333; }
.toc ul { list-style: none; padding: 0; }
.toc li { padding: 0.25rem 0; border-bottom: 1px dotted #ccc; }
.toc li a { color: #1a1a1a; text-decoration: none; }
.toc li a:hover { color: #0066cc; }
.toc .toc-section { font-weight: bold; margin-top: 1rem; padding-top: 0.5rem; border-bottom: none; font-size: 1.05rem; }
.toc .toc-page { float: right; color: #888; font-size: 0.9rem; }

/* Articles */
.article {
  page-break-before: always;
  padding-top: 1rem;
}
.article:first-of-type { page-break-before: auto; }

.article-meta {
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 0.6rem 1rem;
  font-size: 0.85rem;
  color: #555;
  margin-bottom: 1rem;
}
.article-meta strong { color: #333; }

h1 { font-size: 1.8rem; margin: 0 0 0.8rem; color: #1a1a1a; }
h2 { font-size: 1.35rem; margin: 1.5rem 0 0.6rem; padding-bottom: 0.2rem; border-bottom: 1px solid #ddd; }
h3 { font-size: 1.1rem; margin: 1.2rem 0 0.5rem; }
h4, h5, h6 { font-size: 1rem; margin: 1rem 0 0.4rem; color: #444; }

p { margin: 0.5rem 0; text-align: justify; }
ul, ol { padding-left: 1.5rem; margin: 0.5rem 0; }
li { margin: 0.2rem 0; }

pre {
  background: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 0.8rem 1rem;
  overflow-x: auto;
  font-size: 0.85rem;
  line-height: 1.4;
  margin: 0.8rem 0;
}
code {
  font-family: "SF Mono", "Consolas", "Courier New", monospace;
  background: #f0f0f0;
  padding: 0.1rem 0.3rem;
  border-radius: 2px;
  font-size: 0.9em;
}
pre code { background: none; padding: 0; }

blockquote {
  border-left: 3px solid #999;
  padding: 0.4rem 1rem;
  margin: 0.8rem 0;
  color: #555;
  font-style: italic;
}

table { width: 100%; border-collapse: collapse; margin: 0.8rem 0; }
th, td { padding: 0.4rem 0.6rem; border: 1px solid #ccc; text-align: left; font-size: 0.9rem; }
th { background: #f0f0f0; font-weight: 600; }

hr { border: none; border-top: 1px solid #ddd; margin: 1.5rem 0; }
img { max-width: 100%; }

a { color: #0066cc; text-decoration: none; }
@media print {
  a { color: #1a1a1a; text-decoration: underline; }
  .no-print { display: none; }
}

.tag { display: inline-block; background: #eee; padding: 0.1rem 0.4rem; border-radius: 3px; font-size: 0.8rem; margin: 0.1rem; }
"""


def parse_frontmatter_local(text):
    """Return (metadata_dict, body_text)."""
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


def md_to_html_print(text):
    """Simplified markdown to HTML for print. Strips wikilinks to plain text."""
    # Remove wikilinks, keep display text
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)
    text = re.sub(r'\[\[([^\]|]+)\]\]', lambda m: m.group(1).split("/")[-1].replace("-", " ").title(), text)

    lines = text.split("\n")
    out = []
    in_code = False
    code_lines = []
    code_lang = ""
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
            out.append(f'<blockquote>{_inline(chr(10).join(bq_lines))}</blockquote>')
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
                flush_list()
                flush_bq()
                in_code = True
                code_lang = line[3:].strip()
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
            out.append("<hr>")
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
                flush_list()
                in_list = 'ul'
            list_items.append(lm.group(1))
            continue

        lm = re.match(r'^\s*\d+\.\s+(.*)', line)
        if lm:
            flush_bq()
            if in_list != 'ol':
                flush_list()
                in_list = 'ol'
            list_items.append(lm.group(1))
            continue

        if in_list:
            flush_list()

        if not line.strip():
            out.append("")
            continue

        out.append(f"<p>{_inline(line)}</p>")

    flush_list()
    flush_bq()
    if in_code:
        out.append(f'<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>')

    return "\n".join(out)


def _inline(text):
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text


def collect_articles(single_file=None):
    """Collect articles, optionally just one."""
    if single_file:
        p = Path(single_file)
        if not p.is_absolute():
            p = ROOT / p
        text = p.read_text(encoding="utf-8")
        meta, body = parse_frontmatter_local(text)
        slug = str(p.relative_to(WIKI).with_suffix("")) if str(p).startswith(str(WIKI)) else p.stem
        title = meta.get("title", slug.replace("-", " ").title())
        return [{"path": p, "slug": slug, "meta": meta, "body": body, "title": title, "category": "single"}]

    articles = []
    categories = ["sources", "concepts", "entities", "comparisons"]
    for cat in categories:
        cat_dir = WIKI / cat
        if not cat_dir.exists():
            continue
        for md_file in sorted(cat_dir.glob("*.md")):
            text = md_file.read_text(encoding="utf-8")
            meta, body = parse_frontmatter_local(text)
            slug = str(md_file.relative_to(WIKI).with_suffix(""))
            title = meta.get("title", slug.split("/")[-1].replace("-", " ").title())
            articles.append({"path": md_file, "slug": slug, "meta": meta, "body": body, "title": title, "category": cat})
    # Root-level files
    for md_file in sorted(WIKI.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter_local(text)
        slug = md_file.stem
        title = meta.get("title", slug.replace("-", " ").title())
        articles.append({"path": md_file, "slug": slug, "meta": meta, "body": body, "title": title, "category": "root"})
    return articles


def build_html(articles, single=False):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LLM Knowledge Base Export</title>
<style>{PRINT_CSS}</style>
</head>
<body>""")

    # Cover page
    if not single:
        parts.append(f"""<div class="cover">
  <h1>LLM Knowledge Base</h1>
  <div class="subtitle">Complete Wiki Export</div>
  <div class="date">Generated {now} &middot; {len(articles)} articles</div>
</div>""")

        # TOC
        parts.append('<div class="toc"><h2>Table of Contents</h2><ul>')
        cats = {"sources": "Sources", "concepts": "Concepts", "entities": "Entities", "comparisons": "Comparisons", "root": "Other"}
        for cat_key, cat_label in cats.items():
            cat_articles = [a for a in articles if a["category"] == cat_key]
            if not cat_articles:
                continue
            parts.append(f'<li class="toc-section">{cat_label}</li>')
            for a in cat_articles:
                anchor = re.sub(r'[^\w-]', '', a["slug"].replace("/", "-"))
                parts.append(f'<li><a href="#{anchor}">{html.escape(a["title"])}</a></li>')
        parts.append("</ul></div>")

    # Articles
    for a in articles:
        anchor = re.sub(r'[^\w-]', '', a["slug"].replace("/", "-"))
        content_html = md_to_html_print(a["body"])

        # Meta block
        meta_parts = []
        for k, v in a["meta"].items():
            if k == "title":
                continue
            if isinstance(v, list):
                v_str = ", ".join(v)
            else:
                v_str = str(v)
            # Strip wikilink syntax from meta values
            v_str = re.sub(r'\[\[([^\]|]+)\]\]', lambda m: m.group(1).split("/")[-1].replace("-", " ").title(), v_str)
            meta_parts.append(f"<strong>{html.escape(k)}:</strong> {html.escape(v_str)}")
        meta_html = f'<div class="article-meta">{" &middot; ".join(meta_parts)}</div>' if meta_parts else ""

        parts.append(f"""<div class="article" id="{anchor}">
<h1>{html.escape(a["title"])}</h1>
{meta_html}
{content_html}
</div>""")

    parts.append("</body></html>")
    return "\n".join(parts)


def main():
    single_file = sys.argv[1] if len(sys.argv) > 1 else None
    articles = collect_articles(single_file)

    if not articles:
        print("No articles found.")
        return

    print(f"Building print-ready HTML for {len(articles)} article(s)...")
    html_content = build_html(articles, single=bool(single_file))

    OUTPUT.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT / "wiki-export.html"
    out_path.write_text(html_content, encoding="utf-8")

    size_kb = out_path.stat().st_size / 1024
    print(f"Done! {out_path} ({size_kb:.1f} KB)")
    print("Open in browser and use Print -> Save as PDF for a PDF version.")


if __name__ == "__main__":
    main()
