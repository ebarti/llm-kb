#!/usr/bin/env python3
"""Static site generator for the LLM knowledge base wiki.

Converts the wiki into a beautiful static HTML website with:
- Markdown to HTML conversion (headers, bold, italic, lists, code blocks, blockquotes, tables, HR)
- [[wikilink]] resolution
- YAML frontmatter metadata headers
- Responsive CSS with dark/light mode toggle
- Sidebar navigation with collapsible sections
- Full-text client-side search
- Breadcrumbs, backlinks, tag cloud, index page
- RSS feed

Usage: python3 tools/export/build-site.py
Output: output/site/
"""

import os
import re
import json
import html
import datetime
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI = ROOT / "wiki"
OUTPUT = ROOT / "output" / "site"

# ---------------------------------------------------------------------------
# YAML frontmatter parser (simple, stdlib-only)
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
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
            # Parse simple YAML values
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]
            elif val.startswith("["):
                # Parse array
                items = re.findall(r'"([^"]*)"', val)
                if not items:
                    items = re.findall(r"'([^']*)'", val)
                val = items
            meta[key] = val
    return meta, body


# ---------------------------------------------------------------------------
# Markdown -> HTML converter
# ---------------------------------------------------------------------------

def md_to_html(text, all_pages, current_slug=""):
    """Convert markdown text to HTML, resolving wikilinks."""
    # First resolve wikilinks
    text = resolve_wikilinks(text, all_pages, current_slug)

    lines = text.split("\n")
    out = []
    in_code_block = False
    code_lang = ""
    code_lines = []
    in_list = None  # 'ul' or 'ol'
    list_lines = []
    in_blockquote = False
    bq_lines = []
    in_table = False
    table_lines = []

    def flush_list():
        nonlocal in_list, list_lines
        if in_list and list_lines:
            tag = in_list
            out.append(f"<{tag}>")
            for li in list_lines:
                out.append(f"  <li>{inline_format(li)}</li>")
            out.append(f"</{tag}>")
        in_list = None
        list_lines = []

    def flush_blockquote():
        nonlocal in_blockquote, bq_lines
        if in_blockquote and bq_lines:
            content = "\n".join(bq_lines)
            out.append(f'<blockquote>{inline_format(content)}</blockquote>')
        in_blockquote = False
        bq_lines = []

    def flush_table():
        nonlocal in_table, table_lines
        if in_table and table_lines:
            out.append('<div class="table-wrap"><table>')
            for i, row in enumerate(table_lines):
                cells = [c.strip() for c in row.strip("|").split("|")]
                # Skip separator row
                if all(re.match(r'^[-:]+$', c.strip()) for c in cells):
                    continue
                tag = "th" if i == 0 else "td"
                out.append("  <tr>")
                for cell in cells:
                    out.append(f"    <{tag}>{inline_format(cell)}</{tag}>")
                out.append("  </tr>")
            out.append("</table></div>")
        in_table = False
        table_lines = []

    for line in lines:
        # Code blocks
        if re.match(r'^```', line):
            if in_code_block:
                escaped = html.escape("\n".join(code_lines))
                cls = f' class="language-{code_lang}"' if code_lang else ""
                out.append(f'<pre><code{cls}>{escaped}</code></pre>')
                in_code_block = False
                code_lines = []
                code_lang = ""
                continue
            else:
                flush_list()
                flush_blockquote()
                flush_table()
                in_code_block = True
                code_lang = line[3:].strip()
                continue
        if in_code_block:
            code_lines.append(line)
            continue

        # Table rows
        if re.match(r'^\|', line.strip()):
            flush_list()
            flush_blockquote()
            if not in_table:
                in_table = True
            table_lines.append(line)
            continue
        elif in_table:
            flush_table()

        # Blockquote
        if re.match(r'^>\s?', line):
            flush_list()
            if not in_blockquote:
                in_blockquote = True
            bq_lines.append(re.sub(r'^>\s?', '', line))
            continue
        elif in_blockquote:
            flush_blockquote()

        # Horizontal rule
        if re.match(r'^(---|\*\*\*|___)\s*$', line.strip()):
            flush_list()
            out.append("<hr>")
            continue

        # Headers
        hm = re.match(r'^(#{1,6})\s+(.*)', line)
        if hm:
            flush_list()
            level = len(hm.group(1))
            text_content = hm.group(2).strip()
            slug = re.sub(r'[^\w\s-]', '', text_content.lower())
            slug = re.sub(r'\s+', '-', slug).strip('-')
            out.append(f'<h{level} id="{slug}">{inline_format(text_content)}</h{level}>')
            continue

        # Unordered list
        lm = re.match(r'^(\s*)[-*+]\s+(.*)', line)
        if lm:
            flush_blockquote()
            if in_list != 'ul':
                flush_list()
                in_list = 'ul'
            list_lines.append(lm.group(2))
            continue

        # Ordered list
        lm = re.match(r'^(\s*)\d+\.\s+(.*)', line)
        if lm:
            flush_blockquote()
            if in_list != 'ol':
                flush_list()
                in_list = 'ol'
            list_lines.append(lm.group(2))
            continue

        # End list on non-list line
        if in_list:
            flush_list()

        # Empty line
        if not line.strip():
            out.append("")
            continue

        # Paragraph
        out.append(f"<p>{inline_format(line)}</p>")

    # Flush remaining
    flush_list()
    flush_blockquote()
    flush_table()
    if in_code_block:
        escaped = html.escape("\n".join(code_lines))
        out.append(f'<pre><code>{escaped}</code></pre>')

    return "\n".join(out)


def inline_format(text):
    """Apply inline formatting: bold, italic, code, links, images."""
    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Images
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Bold+italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Strikethrough
    text = re.sub(r'~~(.+?)~~', r'<del>\1</del>', text)
    return text


def resolve_wikilinks(text, all_pages, current_slug):
    """Convert [[wikilinks]] to HTML anchor tags."""
    def replace_link(m):
        target = m.group(1)
        display = m.group(2) if m.group(2) else target.split("/")[-1]
        # Normalize target
        target_clean = target.replace("\\", "/").strip()
        # Try to find matching page
        for slug in all_pages:
            if slug == target_clean or slug.endswith("/" + target_clean) or slug == target_clean.replace(" ", "-"):
                # Build relative path
                return f'<a href="/{slug}.html" class="wikilink">{display}</a>'
        # Broken link
        return f'<span class="broken-link" title="Page not found: {target_clean}">{display}</span>'

    # [[target|display]] or [[target]]
    return re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', replace_link, text)


# ---------------------------------------------------------------------------
# Page collection
# ---------------------------------------------------------------------------

def collect_pages():
    """Find all wiki markdown files, return list of dicts."""
    pages = []
    categories = ["sources", "concepts", "entities", "comparisons"]
    # Also include root-level files
    for md_file in sorted(WIKI.rglob("*.md")):
        rel = md_file.relative_to(WIKI)
        rel_str = str(rel)
        # Skip _meta and _index
        if rel_str.startswith("_meta"):
            continue
        slug = str(rel.with_suffix(""))
        parts = slug.split("/")
        if len(parts) > 1:
            category = parts[0]
        else:
            category = "root"
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        pages.append({
            "path": md_file,
            "slug": slug,
            "category": category,
            "meta": meta,
            "body": body,
            "title": meta.get("title", slug.split("/")[-1].replace("-", " ").title()),
        })
    return pages


def build_backlinks(pages):
    """Build a mapping of slug -> list of pages that link to it."""
    backlinks = {}
    for p in pages:
        backlinks[p["slug"]] = []
    for p in pages:
        full_text = p["body"]
        # Find all wikilinks in this page
        links = re.findall(r'\[\[([^\]|]+)', full_text)
        for link in links:
            link = link.strip()
            for target in pages:
                if target["slug"] == link or target["slug"].endswith("/" + link):
                    if p["slug"] != target["slug"]:
                        backlinks.setdefault(target["slug"], [])
                        if p not in backlinks[target["slug"]]:
                            backlinks[target["slug"]].append(p)
    return backlinks


def collect_tags(pages):
    """Collect all tags from pages."""
    tags = {}
    for p in pages:
        page_tags = p["meta"].get("tags", [])
        ptype = p["meta"].get("type", "")
        if isinstance(page_tags, str):
            page_tags = [t.strip() for t in page_tags.split(",")]
        if ptype:
            page_tags.append(ptype)
        for t in page_tags:
            t = t.strip()
            if t:
                tags.setdefault(t, [])
                tags[t].append(p)
    return tags


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

CSS = r"""
:root {
  --bg: #1e1e2e;
  --bg-secondary: #181825;
  --bg-tertiary: #11111b;
  --text: #cdd6f4;
  --text-muted: #a6adc8;
  --text-faint: #6c7086;
  --accent: #89b4fa;
  --accent-hover: #74c7ec;
  --border: #313244;
  --code-bg: #181825;
  --link: #89b4fa;
  --link-hover: #74c7ec;
  --tag-bg: #313244;
  --tag-text: #cba6f7;
  --blockquote-border: #cba6f7;
  --sidebar-bg: #181825;
  --sidebar-width: 280px;
  --header-height: 56px;
  --success: #a6e3a1;
  --warning: #f9e2af;
  --error: #f38ba8;
  --shadow: 0 2px 8px rgba(0,0,0,0.3);
}

[data-theme="light"] {
  --bg: #eff1f5;
  --bg-secondary: #e6e9ef;
  --bg-tertiary: #dce0e8;
  --text: #4c4f69;
  --text-muted: #6c6f85;
  --text-faint: #9ca0b0;
  --accent: #1e66f5;
  --accent-hover: #2a6ef5;
  --border: #ccd0da;
  --code-bg: #e6e9ef;
  --link: #1e66f5;
  --link-hover: #2a6ef5;
  --tag-bg: #dce0e8;
  --tag-text: #8839ef;
  --blockquote-border: #8839ef;
  --sidebar-bg: #e6e9ef;
  --shadow: 0 2px 8px rgba(0,0,0,0.1);
}

* { margin: 0; padding: 0; box-sizing: border-box; }

html { font-size: 16px; scroll-behavior: smooth; }

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  display: flex;
  min-height: 100vh;
}

a { color: var(--link); text-decoration: none; transition: color 0.2s; }
a:hover { color: var(--link-hover); text-decoration: underline; }

/* Header / Topbar */
.topbar {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  height: var(--header-height);
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border);
  display: flex; align-items: center;
  padding: 0 1.5rem;
  gap: 1rem;
  box-shadow: var(--shadow);
}
.topbar .logo {
  font-weight: 700; font-size: 1.1rem;
  color: var(--accent); white-space: nowrap;
}
.topbar .search-box {
  flex: 1; max-width: 480px; position: relative;
}
.topbar .search-box input {
  width: 100%; padding: 0.45rem 0.9rem;
  border: 1px solid var(--border); border-radius: 6px;
  background: var(--bg); color: var(--text);
  font-size: 0.9rem; outline: none;
}
.topbar .search-box input:focus { border-color: var(--accent); }
.search-results {
  display: none; position: absolute; top: 100%; left: 0; right: 0;
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: 6px; max-height: 400px; overflow-y: auto;
  box-shadow: var(--shadow); z-index: 200; margin-top: 4px;
}
.search-results.active { display: block; }
.search-results a {
  display: block; padding: 0.6rem 1rem;
  border-bottom: 1px solid var(--border); color: var(--text);
}
.search-results a:hover { background: var(--bg); text-decoration: none; }
.search-results a small { color: var(--text-muted); }

.theme-toggle {
  background: none; border: 1px solid var(--border);
  border-radius: 6px; padding: 0.4rem 0.7rem;
  color: var(--text); cursor: pointer; font-size: 1rem;
  transition: background 0.2s;
}
.theme-toggle:hover { background: var(--bg); }

.sidebar-toggle {
  display: none; background: none; border: none;
  color: var(--text); font-size: 1.4rem; cursor: pointer;
}

/* Sidebar */
.sidebar {
  position: fixed; top: var(--header-height); left: 0; bottom: 0;
  width: var(--sidebar-width);
  background: var(--sidebar-bg);
  border-right: 1px solid var(--border);
  overflow-y: auto; padding: 1rem 0;
  z-index: 50;
  transition: transform 0.3s;
}
.sidebar h3 {
  font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--text-faint); padding: 0.6rem 1.2rem 0.3rem;
  cursor: pointer; user-select: none;
  display: flex; align-items: center; gap: 0.4rem;
}
.sidebar h3::before {
  content: "\25BE"; font-size: 0.7rem; transition: transform 0.2s;
}
.sidebar h3.collapsed::before { transform: rotate(-90deg); }
.sidebar ul {
  list-style: none; padding: 0 0 0.5rem;
}
.sidebar h3.collapsed + ul { display: none; }
.sidebar li a {
  display: block; padding: 0.3rem 1.2rem 0.3rem 1.6rem;
  color: var(--text-muted); font-size: 0.88rem;
  border-left: 2px solid transparent; transition: all 0.15s;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.sidebar li a:hover, .sidebar li a.active {
  color: var(--accent); border-left-color: var(--accent);
  background: var(--bg); text-decoration: none;
}

/* Main content */
.main {
  margin-left: var(--sidebar-width);
  margin-top: var(--header-height);
  flex: 1; padding: 2rem 3rem 4rem;
  max-width: 900px;
  min-height: calc(100vh - var(--header-height));
}

/* Breadcrumbs */
.breadcrumbs {
  font-size: 0.85rem; color: var(--text-faint);
  margin-bottom: 1.5rem;
}
.breadcrumbs a { color: var(--text-muted); }
.breadcrumbs span { margin: 0 0.4rem; }

/* Metadata header */
.meta-header {
  background: var(--bg-secondary); border: 1px solid var(--border);
  border-radius: 8px; padding: 1rem 1.4rem; margin-bottom: 2rem;
  font-size: 0.88rem;
}
.meta-header .meta-title { font-size: 0.75rem; color: var(--text-faint); text-transform: uppercase; letter-spacing: 0.05em; }
.meta-header .meta-value { color: var(--text); margin-bottom: 0.3rem; }
.meta-header .tag {
  display: inline-block; background: var(--tag-bg); color: var(--tag-text);
  padding: 0.15rem 0.55rem; border-radius: 4px; font-size: 0.8rem; margin: 0.1rem 0.2rem;
}

/* Article content */
.content h1 { font-size: 2rem; margin: 0 0 1rem; font-weight: 700; color: var(--text); }
.content h2 { font-size: 1.5rem; margin: 2rem 0 0.8rem; padding-bottom: 0.3rem; border-bottom: 1px solid var(--border); color: var(--text); }
.content h3 { font-size: 1.2rem; margin: 1.5rem 0 0.6rem; color: var(--text); }
.content h4, .content h5, .content h6 { font-size: 1rem; margin: 1.2rem 0 0.5rem; color: var(--text-muted); }
.content p { margin: 0.6rem 0; }
.content ul, .content ol { padding-left: 1.5rem; margin: 0.6rem 0; }
.content li { margin: 0.25rem 0; }

.content pre {
  background: var(--code-bg); border: 1px solid var(--border);
  border-radius: 6px; padding: 1rem 1.2rem;
  overflow-x: auto; margin: 1rem 0;
  font-size: 0.88rem; line-height: 1.5;
}
.content code {
  font-family: "SF Mono", "Fira Code", "Cascadia Code", "Consolas", monospace;
  background: var(--code-bg); padding: 0.15rem 0.4rem; border-radius: 3px;
  font-size: 0.88em;
}
.content pre code { background: none; padding: 0; }

.content blockquote {
  border-left: 3px solid var(--blockquote-border);
  padding: 0.5rem 1rem; margin: 1rem 0;
  color: var(--text-muted); background: var(--bg-secondary);
  border-radius: 0 6px 6px 0;
}

.content table {
  width: 100%; border-collapse: collapse; margin: 1rem 0;
}
.content th, .content td {
  padding: 0.6rem 0.8rem; border: 1px solid var(--border); text-align: left;
}
.content th { background: var(--bg-secondary); font-weight: 600; }

.content hr { border: none; border-top: 1px solid var(--border); margin: 2rem 0; }

.content img { max-width: 100%; border-radius: 6px; margin: 1rem 0; }

.table-wrap { overflow-x: auto; }

.wikilink { color: var(--accent); border-bottom: 1px dashed var(--accent); }
.wikilink:hover { border-bottom-style: solid; }
.broken-link { color: var(--error); border-bottom: 1px dashed var(--error); cursor: help; }

/* Backlinks */
.backlinks {
  margin-top: 3rem; padding-top: 1.5rem;
  border-top: 1px solid var(--border);
}
.backlinks h3 { font-size: 0.9rem; color: var(--text-faint); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; border: none; }
.backlinks ul { list-style: none; padding: 0; }
.backlinks li { margin: 0.3rem 0; }
.backlinks li a { color: var(--accent); font-size: 0.9rem; }

/* Tag cloud */
.tag-cloud { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0; }
.tag-cloud a {
  display: inline-block; background: var(--tag-bg); color: var(--tag-text);
  padding: 0.3rem 0.8rem; border-radius: 6px; font-size: 0.9rem;
  transition: background 0.2s;
}
.tag-cloud a:hover { background: var(--border); text-decoration: none; }

/* Index page */
.page-list { list-style: none; padding: 0; }
.page-list li { margin: 0.3rem 0; padding: 0.4rem 0; border-bottom: 1px solid var(--border); }
.page-list li:last-child { border-bottom: none; }
.page-list .summary { color: var(--text-muted); font-size: 0.88rem; margin-left: 0.5rem; }

/* Responsive */
@media (max-width: 768px) {
  .sidebar { transform: translateX(-100%); }
  .sidebar.open { transform: translateX(0); }
  .sidebar-toggle { display: block; }
  .main { margin-left: 0; padding: 1.2rem 1rem 3rem; }
  .topbar .logo { font-size: 0.95rem; }
}
"""

# ---------------------------------------------------------------------------
# JavaScript (search + theme toggle + sidebar)
# ---------------------------------------------------------------------------

JS_TEMPLATE = """
var searchData = SEARCH_DATA_PLACEHOLDER;

(function() {
  // Theme toggle
  var theme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', theme);
  var btn = document.getElementById('theme-toggle');
  btn.textContent = theme === 'dark' ? '\\u2600' : '\\u263E';
  btn.addEventListener('click', function() {
    theme = theme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    btn.textContent = theme === 'dark' ? '\\u2600' : '\\u263E';
  });

  // Sidebar toggle (mobile)
  var sidebarBtn = document.getElementById('sidebar-toggle');
  var sidebar = document.getElementById('sidebar');
  if (sidebarBtn) {
    sidebarBtn.addEventListener('click', function() {
      sidebar.classList.toggle('open');
    });
  }

  // Collapsible sidebar sections
  document.querySelectorAll('.sidebar h3').forEach(function(h3) {
    h3.addEventListener('click', function() {
      this.classList.toggle('collapsed');
    });
  });

  // Search
  var searchInput = document.getElementById('search-input');
  var searchResults = document.getElementById('search-results');
  searchInput.addEventListener('input', function() {
    var q = this.value.toLowerCase().trim();
    if (q.length < 2) {
      searchResults.classList.remove('active');
      searchResults.innerHTML = '';
      return;
    }
    var matches = [];
    for (var i = 0; i < searchData.length; i++) {
      var page = searchData[i];
      var score = 0;
      if (page.title.toLowerCase().indexOf(q) !== -1) score += 10;
      if (page.body.toLowerCase().indexOf(q) !== -1) score += 1;
      if (score > 0) matches.push({page: page, score: score});
    }
    matches.sort(function(a, b) { return b.score - a.score; });
    matches = matches.slice(0, 15);
    if (matches.length === 0) {
      searchResults.innerHTML = '<div style="padding:0.8rem 1rem;color:var(--text-faint)">No results</div>';
    } else {
      searchResults.innerHTML = matches.map(function(m) {
        return '<a href="/' + m.page.slug + '.html"><strong>' + m.page.title + '</strong><br><small>' + m.page.category + '</small></a>';
      }).join('');
    }
    searchResults.classList.add('active');
  });
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.search-box')) searchResults.classList.remove('active');
  });
})();
"""


# ---------------------------------------------------------------------------
# HTML templates
# ---------------------------------------------------------------------------

def page_template(title, content_html, breadcrumbs_html, meta_html, backlinks_html, sidebar_html, search_data_json):
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)} - LLM Knowledge Base</title>
<style>{CSS}</style>
</head>
<body>
<div class="topbar">
  <button class="sidebar-toggle" id="sidebar-toggle">&#9776;</button>
  <a href="/index.html" class="logo">LLM Knowledge Base</a>
  <div class="search-box">
    <input type="text" id="search-input" placeholder="Search articles..." autocomplete="off">
    <div class="search-results" id="search-results"></div>
  </div>
  <button class="theme-toggle" id="theme-toggle">&#9790;</button>
</div>
{sidebar_html}
<div class="main">
  {breadcrumbs_html}
  {meta_html}
  <div class="content">
    {content_html}
  </div>
  {backlinks_html}
</div>
<script>{search_data_json}</script>
</body>
</html>"""


def build_sidebar(pages):
    categories = {
        "sources": "Sources",
        "concepts": "Concepts",
        "entities": "Entities",
        "comparisons": "Comparisons",
        "root": "Other",
    }
    sidebar = '<nav class="sidebar" id="sidebar">\n'
    for cat_key, cat_label in categories.items():
        cat_pages = [p for p in pages if p["category"] == cat_key]
        if not cat_pages:
            continue
        sidebar += f'  <h3>{html.escape(cat_label)}</h3>\n  <ul>\n'
        for p in sorted(cat_pages, key=lambda x: x["title"]):
            sidebar += f'    <li><a href="/{p["slug"]}.html">{html.escape(p["title"])}</a></li>\n'
        sidebar += '  </ul>\n'
    sidebar += '</nav>'
    return sidebar


def build_breadcrumbs(page):
    parts = page["slug"].split("/")
    crumbs = ['<a href="/index.html">Home</a>']
    if len(parts) > 1:
        crumbs.append(f'<a href="/index.html">{parts[0].title()}</a>')
    crumbs.append(f'<span>{html.escape(page["title"])}</span>')
    return '<div class="breadcrumbs">' + ' <span>/</span> '.join(crumbs) + '</div>'


def build_meta_header(meta):
    if not meta:
        return ""
    rows = []
    skip = {"title"}
    for key, val in meta.items():
        if key in skip:
            continue
        if isinstance(val, list):
            # Render as tags
            rendered = " ".join(f'<span class="tag">{html.escape(str(v))}</span>' for v in val)
        else:
            rendered = html.escape(str(val))
        rows.append(f'<div><span class="meta-title">{html.escape(key)}</span><div class="meta-value">{rendered}</div></div>')
    if not rows:
        return ""
    return '<div class="meta-header">' + "\n".join(rows) + '</div>'


def build_backlinks_section(backlinks_for_page):
    if not backlinks_for_page:
        return ""
    items = []
    for p in backlinks_for_page:
        items.append(f'<li><a href="/{p["slug"]}.html">{html.escape(p["title"])}</a></li>')
    return f'<div class="backlinks"><h3>Backlinks</h3><ul>{"".join(items)}</ul></div>'


# ---------------------------------------------------------------------------
# Special pages
# ---------------------------------------------------------------------------

def build_index_page(pages):
    cats = {"sources": "Sources", "concepts": "Concepts", "entities": "Entities", "comparisons": "Comparisons", "root": "Other"}
    h = "<h1>All Articles</h1>\n"
    for cat_key, cat_label in cats.items():
        cat_pages = [p for p in pages if p["category"] == cat_key]
        if not cat_pages:
            continue
        h += f"<h2>{cat_label}</h2>\n<ul class='page-list'>\n"
        for p in sorted(cat_pages, key=lambda x: x["title"]):
            summary = p["meta"].get("summary", "")
            summary_html = f'<span class="summary">-- {html.escape(summary)}</span>' if summary else ""
            h += f'<li><a href="/{p["slug"]}.html">{html.escape(p["title"])}</a>{summary_html}</li>\n'
        h += "</ul>\n"
    return h


def build_tags_page(tags):
    h = "<h1>Tag Cloud</h1>\n<div class='tag-cloud'>\n"
    for tag in sorted(tags.keys()):
        count = len(tags[tag])
        h += f'<a href="#tag-{html.escape(tag)}">{html.escape(tag)} ({count})</a>\n'
    h += "</div>\n<hr>\n"
    for tag in sorted(tags.keys()):
        h += f'<h2 id="tag-{html.escape(tag)}">{html.escape(tag)}</h2>\n<ul class="page-list">\n'
        for p in tags[tag]:
            h += f'<li><a href="/{p["slug"]}.html">{html.escape(p["title"])}</a></li>\n'
        h += "</ul>\n"
    return h


def build_rss(pages):
    items = []
    for p in sorted(pages, key=lambda x: x["meta"].get("last_compiled", ""), reverse=True)[:20]:
        title = html.escape(p["title"])
        link = f'/{p["slug"]}.html'
        desc = html.escape(p["meta"].get("summary", ""))
        date = p["meta"].get("last_compiled", "")
        items.append(f"""  <item>
    <title>{title}</title>
    <link>{link}</link>
    <description>{desc}</description>
    <pubDate>{date}</pubDate>
  </item>""")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>LLM Knowledge Base</title>
  <description>Wiki export</description>
  <link>/index.html</link>
  <lastBuildDate>{datetime.datetime.now().isoformat()}</lastBuildDate>
{"".join(items)}
</channel>
</rss>"""


# ---------------------------------------------------------------------------
# Main build
# ---------------------------------------------------------------------------

def main():
    print("Collecting pages...")
    pages = collect_pages()
    all_slugs = {p["slug"] for p in pages}

    print(f"Found {len(pages)} pages")
    backlinks = build_backlinks(pages)
    tags = collect_tags(pages)
    sidebar_html = build_sidebar(pages)

    # Search index (lightweight: title, slug, category, first 500 chars of body)
    search_data = []
    for p in pages:
        search_data.append({
            "title": p["title"],
            "slug": p["slug"],
            "category": p["category"],
            "body": p["body"][:500].replace("\n", " "),
        })
    search_js = JS_TEMPLATE.replace("SEARCH_DATA_PLACEHOLDER", json.dumps(search_data))

    # Build output directory
    OUTPUT.mkdir(parents=True, exist_ok=True)

    # Build each page
    for p in pages:
        print(f"  Building {p['slug']}...")
        content_html = md_to_html(p["body"], all_slugs, p["slug"])
        title_html = f'<h1>{html.escape(p["title"])}</h1>\n' + content_html
        breadcrumbs = build_breadcrumbs(p)
        meta_header = build_meta_header(p["meta"])
        bl = build_backlinks_section(backlinks.get(p["slug"], []))

        page_html = page_template(p["title"], title_html, breadcrumbs, meta_header, bl, sidebar_html, search_js)

        out_path = OUTPUT / (p["slug"] + ".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(page_html, encoding="utf-8")

    # Index page
    print("  Building index.html...")
    index_content = build_index_page(pages)
    index_bc = '<div class="breadcrumbs"><span>Home</span></div>'
    index_html = page_template("All Articles", index_content, index_bc, "", "", sidebar_html, search_js)
    (OUTPUT / "index.html").write_text(index_html, encoding="utf-8")

    # Tags page
    print("  Building tags.html...")
    tags_content = build_tags_page(tags)
    tags_bc = '<div class="breadcrumbs"><a href="/index.html">Home</a> <span>/</span> <span>Tags</span></div>'
    tags_html = page_template("Tags", tags_content, tags_bc, "", "", sidebar_html, search_js)
    (OUTPUT / "tags.html").write_text(tags_html, encoding="utf-8")

    # RSS feed
    print("  Building feed.xml...")
    rss = build_rss(pages)
    (OUTPUT / "feed.xml").write_text(rss, encoding="utf-8")

    total_size = sum(f.stat().st_size for f in OUTPUT.rglob("*") if f.is_file())
    print(f"\nDone! {len(pages)} pages + index + tags + RSS")
    print(f"Output: {OUTPUT}")
    print(f"Total size: {total_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
