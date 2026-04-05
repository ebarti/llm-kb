#!/usr/bin/env python3
"""Markdown bundle export for the LLM knowledge base wiki.

Creates a single merged markdown file with all wiki content.
Table of contents at top, each article as a section, wikilinks converted
to markdown anchor links.

Usage:
  python3 tools/export/bundle.py                        -> output/wiki-bundle.md
  python3 tools/export/bundle.py --max-tokens 100000    -> truncated for LLM context

Output: output/wiki-bundle.md
"""

import os
import re
import sys
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WIKI = ROOT / "wiki"
OUTPUT = ROOT / "output"


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
                "title": title,
                "meta": meta,
                "body": body,
                "category": cat_key,
                "category_label": cat_label,
            })
    # Root-level files (excluding _index, _meta)
    for md_file in sorted(WIKI.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        slug = md_file.stem
        title = meta.get("title", slug.replace("-", " ").title())
        articles.append({
            "slug": slug,
            "title": title,
            "meta": meta,
            "body": body,
            "category": "root",
            "category_label": "Other",
        })
    return articles


def slug_to_anchor(slug):
    """Convert a wiki slug to a markdown anchor link."""
    anchor = slug.replace("/", "-").replace(" ", "-").lower()
    anchor = re.sub(r'[^\w-]', '', anchor)
    return anchor


def resolve_wikilinks(text, all_slugs):
    """Convert [[wikilinks]] to markdown anchor links."""
    def replace_link(m):
        target = m.group(1).strip()
        display = m.group(2) if m.group(2) else target.split("/")[-1].replace("-", " ").title()
        # Find matching slug
        for slug in all_slugs:
            if slug == target or slug.endswith("/" + target):
                anchor = slug_to_anchor(slug)
                return f"[{display}](#{anchor})"
        return display

    return re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]', replace_link, text)


def estimate_tokens(text):
    """Rough estimate: ~4 chars per token for English text."""
    return len(text) // 4


def main():
    parser = argparse.ArgumentParser(description="Bundle wiki into single markdown file")
    parser.add_argument("--max-tokens", type=int, default=0, help="Max tokens (approximate); 0 = no limit")
    args = parser.parse_args()

    articles = collect_articles()
    if not articles:
        print("No articles found.")
        return

    all_slugs = [a["slug"] for a in articles]

    # Build output
    parts = []
    parts.append("# LLM Knowledge Base - Complete Bundle\n")
    parts.append(f"*{len(articles)} articles*\n")

    # Table of contents
    parts.append("## Table of Contents\n")
    current_cat = None
    for a in articles:
        if a["category_label"] != current_cat:
            current_cat = a["category_label"]
            parts.append(f"\n### {current_cat}\n")
        anchor = slug_to_anchor(a["slug"])
        parts.append(f"- [{a['title']}](#{anchor})")
    parts.append("\n---\n")

    # Articles
    for a in articles:
        anchor = slug_to_anchor(a["slug"])
        section = []
        section.append(f'## {a["title"]} {{#{anchor}}}\n')

        # Metadata line
        meta_parts = []
        for k, v in a["meta"].items():
            if k == "title":
                continue
            if isinstance(v, list):
                v = ", ".join(v)
            # Strip wikilink syntax from meta values
            v = re.sub(r'\[\[([^\]|]+)\]\]', lambda m: m.group(1).split("/")[-1].replace("-", " ").title(), str(v))
            meta_parts.append(f"**{k}:** {v}")
        if meta_parts:
            section.append("*" + " | ".join(meta_parts) + "*\n")

        # Body with resolved wikilinks
        body = resolve_wikilinks(a["body"], all_slugs)
        section.append(body)
        section.append("\n---\n")
        parts.append("\n".join(section))

    full_text = "\n".join(parts)

    # Token truncation
    if args.max_tokens > 0:
        current_tokens = estimate_tokens(full_text)
        if current_tokens > args.max_tokens:
            # Truncate to approximate token limit
            char_limit = args.max_tokens * 4
            full_text = full_text[:char_limit]
            # Find last clean break
            last_hr = full_text.rfind("\n---\n")
            if last_hr > char_limit * 0.8:
                full_text = full_text[:last_hr + 5]
            full_text += f"\n\n*[Truncated to ~{args.max_tokens} tokens. Full bundle has {current_tokens} tokens.]*\n"
            print(f"Truncated from ~{current_tokens} to ~{args.max_tokens} tokens")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT / "wiki-bundle.md"
    out_path.write_text(full_text, encoding="utf-8")

    size_kb = out_path.stat().st_size / 1024
    tokens = estimate_tokens(full_text)
    print(f"Done! {out_path}")
    print(f"Size: {size_kb:.1f} KB, ~{tokens:,} tokens")


if __name__ == "__main__":
    main()
