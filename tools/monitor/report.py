#!/usr/bin/env python3
"""
Discovery Report Generator — analyzes the wiki and suggests research directions.

Examines the current wiki for:
  - Topics that are thinly covered (few sources)
  - Concepts mentioned but not well-developed
  - Time gaps (no new sources in X days)
  - Trending related topics (based on cross-references)

Generates a discovery-suggestions report.

Usage:
    python3 tools/monitor/report.py
    python3 tools/monitor/report.py --output /path/to/report.md
"""

import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
KB_DIR = SCRIPT_DIR.parent.parent
WIKI_DIR = KB_DIR / "wiki"
CONCEPTS_DIR = WIKI_DIR / "concepts"
SOURCES_DIR = WIKI_DIR / "sources"
META_DIR = WIKI_DIR / "_meta"
OUTPUT_DIR = KB_DIR / "output" / "reports"

# ---------------------------------------------------------------------------
# Analysis helpers
# ---------------------------------------------------------------------------

def parse_frontmatter(text):
    """Extract YAML-ish frontmatter as a dict (basic parser, no pyyaml needed)."""
    fm = {}
    match = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return fm
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            fm[key] = val
    return fm


def extract_wikilinks(text):
    """Extract all [[...]] wikilinks from text."""
    return re.findall(r'\[\[([^\]]+)\]\]', text)


def read_md_files(directory):
    """Read all .md files in a directory, return list of (path, text, frontmatter)."""
    results = []
    if not directory.exists():
        return results
    for f in sorted(directory.iterdir()):
        if f.suffix == ".md":
            text = f.read_text(errors="replace")
            fm = parse_frontmatter(text)
            results.append((f, text, fm))
    return results


# ---------------------------------------------------------------------------
# Analyses
# ---------------------------------------------------------------------------

def analyze_thin_concepts(concepts):
    """Find concepts with few sources or short content."""
    thin = []
    for path, text, fm in concepts:
        # Count sources listed in frontmatter
        sources_raw = fm.get("sources", "")
        source_count = len(re.findall(r'\[\[', sources_raw))
        # Count content lines (excluding frontmatter)
        body = re.sub(r'^---.*?---', '', text, flags=re.DOTALL).strip()
        line_count = len([l for l in body.split("\n") if l.strip()])

        if source_count <= 1 or line_count < 15:
            thin.append({
                "concept": path.stem,
                "title": fm.get("title", path.stem),
                "source_count": source_count,
                "line_count": line_count,
            })

    thin.sort(key=lambda x: x["source_count"])
    return thin


def analyze_mentioned_but_missing(concepts, sources):
    """Find wikilinks that point to concepts that don't exist."""
    existing = set()
    for path, _, _ in concepts:
        existing.add(f"concepts/{path.stem}")
    for path, _, _ in sources:
        existing.add(f"sources/{path.stem}")

    all_links = Counter()
    for _, text, _ in concepts + sources:
        for link in extract_wikilinks(text):
            normalized = link.strip().lower()
            all_links[normalized] += 1

    missing = []
    for link, count in all_links.most_common():
        # Normalize for comparison
        if link not in existing and not link.startswith("raw/"):
            missing.append({"link": link, "references": count})

    return missing


def analyze_time_gaps(sources):
    """Find how long since last compilation for each source."""
    gaps = []
    now = datetime.now()
    for path, text, fm in sources:
        date_str = fm.get("last_compiled", "")
        try:
            compiled = datetime.strptime(date_str, "%Y-%m-%d")
            age_days = (now - compiled).days
            gaps.append({
                "source": path.stem,
                "title": fm.get("title", path.stem),
                "last_compiled": date_str,
                "age_days": age_days,
            })
        except ValueError:
            gaps.append({
                "source": path.stem,
                "title": fm.get("title", path.stem),
                "last_compiled": "unknown",
                "age_days": 999,
            })
    gaps.sort(key=lambda x: -x["age_days"])
    return gaps


def analyze_cross_references(concepts):
    """Find which concepts are most cross-referenced (trending internally)."""
    ref_count = Counter()
    for _, text, _ in concepts:
        for link in extract_wikilinks(text):
            if link.startswith("concepts/"):
                ref_count[link] += 1

    return ref_count.most_common(20)


def suggest_queries(thin_concepts, missing_links, trending):
    """Generate suggested search queries based on analysis."""
    suggestions = []

    for item in thin_concepts[:5]:
        concept = item["title"].replace("-", " ")
        suggestions.append({
            "reason": f"Thin coverage: {item['title']} ({item['source_count']} source(s))",
            "query": f"{concept} guide tutorial overview",
        })

    for item in missing_links[:5]:
        link_name = item["link"].replace("concepts/", "").replace("-", " ")
        suggestions.append({
            "reason": f"Referenced but missing: {item['link']} ({item['references']} ref(s))",
            "query": f"{link_name} LLM AI",
        })

    for link, count in trending[:3]:
        name = link.replace("concepts/", "").replace("-", " ")
        suggestions.append({
            "reason": f"Trending concept: {name} ({count} cross-refs)",
            "query": f"{name} latest developments 2024 2025",
        })

    return suggestions


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(output_path):
    """Run all analyses and write the report."""
    concepts = read_md_files(CONCEPTS_DIR)
    sources = read_md_files(SOURCES_DIR)

    thin = analyze_thin_concepts(concepts)
    missing = analyze_mentioned_but_missing(concepts, sources)
    time_gaps = analyze_time_gaps(sources)
    trending = analyze_cross_references(concepts)
    suggestions = suggest_queries(thin, missing, trending)

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = []
    lines.append("---")
    lines.append(f'title: "Discovery Suggestions"')
    lines.append("type: report")
    lines.append(f"generated: {now}")
    lines.append("---")
    lines.append("")
    lines.append("# Discovery Suggestions")
    lines.append("")
    lines.append(f"Generated: {now}")
    lines.append(f"Wiki stats: {len(concepts)} concepts, {len(sources)} sources")
    lines.append("")

    # --- Thin concepts ---
    lines.append("## Thinly Covered Topics")
    lines.append("")
    if thin:
        lines.append("These concepts have few sources or little content and could benefit from more research:")
        lines.append("")
        lines.append("| Concept | Sources | Lines |")
        lines.append("|---------|---------|-------|")
        for item in thin:
            lines.append(f"| {item['title']} | {item['source_count']} | {item['line_count']} |")
    else:
        lines.append("All concepts appear well-covered.")
    lines.append("")

    # --- Missing links ---
    lines.append("## Referenced But Not Developed")
    lines.append("")
    if missing:
        lines.append("These are mentioned in cross-references but have no dedicated article:")
        lines.append("")
        for item in missing[:10]:
            lines.append(f"- **{item['link']}** ({item['references']} reference(s))")
    else:
        lines.append("All referenced concepts have articles.")
    lines.append("")

    # --- Time gaps ---
    lines.append("## Source Freshness")
    lines.append("")
    if time_gaps:
        lines.append("| Source | Last Compiled | Age (days) |")
        lines.append("|--------|---------------|------------|")
        for item in time_gaps[:15]:
            lines.append(f"| {item['title'][:50]} | {item['last_compiled']} | {item['age_days']} |")
    lines.append("")

    # --- Trending cross-refs ---
    lines.append("## Most Cross-Referenced Concepts")
    lines.append("")
    if trending:
        for link, count in trending[:10]:
            name = link.replace("concepts/", "").replace("-", " ").title()
            lines.append(f"- **{name}** ({count} references)")
    lines.append("")

    # --- Suggestions ---
    lines.append("## Suggested Research Queries")
    lines.append("")
    if suggestions:
        lines.append("Run these to expand the knowledge base:")
        lines.append("")
        for s in suggestions:
            lines.append(f"- `./kb research \"{s['query']}\"`")
            lines.append(f"  Reason: {s['reason']}")
            lines.append("")
    else:
        lines.append("No suggestions at this time.")
    lines.append("")

    # --- Summary ---
    lines.append("## Quick Actions")
    lines.append("")
    lines.append("```bash")
    lines.append("# Check for new content across all topics")
    lines.append("./tools/monitor/discover")
    lines.append("")
    lines.append("# Auto-ingest anything found")
    lines.append("./tools/monitor/discover --ingest")
    lines.append("")
    lines.append("# Check RSS feeds")
    lines.append("./tools/monitor/discover --feeds")
    lines.append("```")
    lines.append("")

    report_text = "\n".join(lines)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_text)
    print(f"Report written to: {output_path}")
    print(f"  {len(concepts)} concepts analyzed")
    print(f"  {len(sources)} sources analyzed")
    print(f"  {len(thin)} thinly covered topic(s)")
    print(f"  {len(missing)} referenced-but-missing link(s)")
    print(f"  {len(suggestions)} research suggestion(s)")

    return report_text


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Discovery Report Generator — suggest research directions"
    )
    parser.add_argument(
        "--output", type=str, default=None,
        help="Output path for the report (default: output/reports/discovery-suggestions.md)"
    )
    args = parser.parse_args()

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = OUTPUT_DIR / "discovery-suggestions.md"

    generate_report(output_path)


if __name__ == "__main__":
    main()
