#!/usr/bin/env python3
"""
Reading list plugin — generates a prioritized reading list from raw sources.

Hook: post_compile
Scans raw/ for source documents, extracts metadata, and generates
wiki/Reading-List.md grouped by topic with quality indicators.
"""

import os
import re
from collections import defaultdict
from datetime import datetime


def register():
    return {"post_compile": run_post_compile}


def extract_frontmatter(content):
    """Extract frontmatter fields as a dict."""
    fm = {}
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).split("\n"):
        m = re.match(r"(\w+):\s*(.+)", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return fm


def extract_topics(content, frontmatter):
    """Determine topics for a source document."""
    topics = set()

    # From tags
    tags_str = frontmatter.get("tags", "")
    if tags_str:
        for tag in re.findall(r'"([^"]+)"', tags_str):
            topics.add(tag)

    # From related/sources fields - extract concept names
    for field in ("related", "sources"):
        val = frontmatter.get(field, "")
        for link in re.findall(r"\[\[concepts/([^\]]+)\]\]", val):
            topics.add(link.replace("-", " ").title())

    # From title keywords as fallback
    title = frontmatter.get("title", "")
    if not topics and title:
        # Use significant words from title
        words = re.findall(r"[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*", title)
        for w in words[:2]:
            topics.add(w)

    return topics if topics else {"Uncategorized"}


def compute_quality_score(content, frontmatter):
    """Compute a simple quality score based on content indicators."""
    score = 0
    indicators = []

    # Length bonus
    word_count = len(content.split())
    if word_count > 2000:
        score += 3
        indicators.append("detailed")
    elif word_count > 500:
        score += 2
        indicators.append("substantial")
    else:
        score += 1

    # Has code examples
    if re.search(r"```", content):
        score += 1
        indicators.append("has code")

    # Has links/references
    link_count = len(re.findall(r"https?://", content))
    if link_count > 3:
        score += 2
        indicators.append("well-referenced")
    elif link_count > 0:
        score += 1
        indicators.append("has references")

    # Has structured sections
    heading_count = len(re.findall(r"^##", content, re.MULTILINE))
    if heading_count > 3:
        score += 1
        indicators.append("well-structured")

    # Has summary
    if frontmatter.get("summary"):
        score += 1

    return min(score, 10), indicators


def run_post_compile(root, *args):
    """Generate the reading list from raw sources."""
    raw_dir = os.path.join(root, "raw")
    wiki_dir = os.path.join(root, "wiki")
    sources_dir = os.path.join(wiki_dir, "sources")

    if not os.path.isdir(raw_dir):
        print("  [reading_list] No raw/ directory found, skipping.")
        return

    # Collect all source info
    sources = []
    for fname in sorted(os.listdir(raw_dir)):
        if not fname.endswith(".md"):
            continue
        fpath = os.path.join(raw_dir, fname)
        try:
            with open(fpath, "r", errors="replace") as f:
                content = f.read()
        except OSError:
            continue

        fm = extract_frontmatter(content)
        topics = extract_topics(content, fm)
        quality, indicators = compute_quality_score(content, fm)

        # Check if it has been compiled into wiki
        source_name = fname.replace(".md", "")
        compiled = os.path.exists(os.path.join(sources_dir, fname))

        sources.append({
            "file": fname,
            "title": fm.get("title", source_name.replace("-", " ").title()),
            "url": fm.get("url", fm.get("source", "")),
            "author": fm.get("author", fm.get("by", "Unknown")),
            "date": fm.get("date", fm.get("published", "")),
            "summary": fm.get("summary", ""),
            "topics": topics,
            "quality": quality,
            "indicators": indicators,
            "compiled": compiled,
            "word_count": len(content.split()),
        })

    if not sources:
        print("  [reading_list] No source documents found.")
        return

    # Group by topic
    by_topic = defaultdict(list)
    for src in sources:
        for topic in src["topics"]:
            by_topic[topic].append(src)

    # Sort each topic group by quality (descending)
    for topic in by_topic:
        by_topic[topic].sort(key=lambda x: -x["quality"])

    # Generate Reading-List.md
    now = datetime.now().strftime("%Y-%m-%d")
    lines = [
        "---",
        'title: "Reading List"',
        "type: meta",
        f"last_updated: {now}",
        f"total_sources: {len(sources)}",
        "---",
        "",
        "# Reading List",
        "",
        f"Prioritized reading list of {len(sources)} raw sources, grouped by topic.",
        f"Quality scores range from 1 (basic) to 10 (comprehensive).",
        "",
    ]

    # Sort topics by total quality of their sources
    topic_order = sorted(by_topic.keys(),
                         key=lambda t: -sum(s["quality"] for s in by_topic[t]))

    for topic in topic_order:
        topic_sources = by_topic[topic]
        lines.append(f"## {topic}")
        lines.append("")

        for src in topic_sources:
            stars = "★" * src["quality"] + "☆" * (5 - min(src["quality"], 5))
            status = "✅" if src["compiled"] else "📋"

            title_link = src["title"]
            if src["url"]:
                title_link = f"[{src['title']}]({src['url']})"

            lines.append(f"- {status} {stars} **{title_link}**")
            if src["author"] != "Unknown":
                lines.append(f"  - By: {src['author']}")
            if src["summary"]:
                lines.append(f"  - {src['summary'][:150]}")
            if src["indicators"]:
                lines.append(f"  - _{', '.join(src['indicators'])}_")
            if src["compiled"]:
                source_link = src["file"].replace(".md", "")
                lines.append(f"  - Wiki: [[sources/{source_link}]]")
            lines.append("")

    reading_list_path = os.path.join(wiki_dir, "Reading-List.md")
    with open(reading_list_path, "w") as f:
        f.write("\n".join(lines))

    print(f"  [reading_list] Generated reading list with {len(sources)} sources "
          f"across {len(by_topic)} topics")
    print(f"  [reading_list] Written to wiki/Reading-List.md")
