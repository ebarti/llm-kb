#!/usr/bin/env python3
"""Wiki Growth Report — analyzes git history to show wiki growth over time."""

import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / "wiki"
IMG_OUTPUT = ROOT / "output" / "images" / "wiki-growth.html"
RPT_OUTPUT = ROOT / "output" / "reports" / "growth-report.md"


def git(*args, cwd=None):
    result = subprocess.run(
        ["git"] + list(args),
        capture_output=True, text=True,
        cwd=cwd or ROOT,
    )
    return result.stdout.strip()


def get_all_commits():
    """Get all commits with wiki file changes."""
    raw = git("log", "--all", "--pretty=format:%H|%ai|%s", "--name-status")
    commits = []
    current = None
    for line in raw.splitlines():
        if "|" in line and len(line.split("|")) >= 3 and not line.startswith(("A\t", "M\t", "D\t", "R")):
            parts = line.split("|", 2)
            current = {
                "hash": parts[0],
                "date": parts[1].strip().split(" ")[0],
                "subject": parts[2],
                "files": [],
            }
            commits.append(current)
        elif current and line.strip():
            parts = line.split("\t")
            if len(parts) >= 2:
                op = parts[0][0]
                fpath = parts[-1]
                if fpath.startswith("wiki/"):
                    current["files"].append((op, fpath))
    return commits


def count_words_at_commit(commit_hash):
    """Count total words in wiki/ at a given commit."""
    files = git("ls-tree", "-r", "--name-only", commit_hash, "--", "wiki/")
    if not files:
        return 0
    total = 0
    for f in files.splitlines():
        if f.endswith(".md"):
            content = git("show", f"{commit_hash}:{f}")
            total += len(content.split())
    return total


def get_diff_stats(commit_hash):
    """Get lines added/removed for wiki files at a commit."""
    stat = git("diff", "--numstat", f"{commit_hash}~1..{commit_hash}", "--", "wiki/")
    if not stat:
        # First commit — count all as additions
        stat = git("diff", "--numstat", "--no-index", "/dev/null", f"{commit_hash}", "--", "wiki/")
    added = 0
    removed = 0
    for line in stat.splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            try:
                added += int(parts[0]) if parts[0] != "-" else 0
                removed += int(parts[1]) if parts[1] != "-" else 0
            except ValueError:
                pass
    return added, removed


def current_wiki_stats():
    """Get current wiki stats by walking the filesystem."""
    stats = {
        "total_files": 0,
        "concepts": 0,
        "sources": 0,
        "entities": 0,
        "comparisons": 0,
        "other": 0,
        "total_words": 0,
        "total_lines": 0,
    }
    for md in WIKI.rglob("*.md"):
        stats["total_files"] += 1
        text = md.read_text(errors="ignore")
        stats["total_words"] += len(text.split())
        stats["total_lines"] += text.count("\n")
        rel = str(md.relative_to(WIKI))
        if rel.startswith("concepts/"):
            stats["concepts"] += 1
        elif rel.startswith("sources/"):
            stats["sources"] += 1
        elif rel.startswith("entities/"):
            stats["entities"] += 1
        elif rel.startswith("comparisons/"):
            stats["comparisons"] += 1
        else:
            stats["other"] += 1
    return stats


def build_daily_data(commits):
    """Build per-day aggregated data."""
    by_date = defaultdict(lambda: {
        "files_added": 0, "files_modified": 0, "files_deleted": 0,
        "concepts_added": 0, "sources_added": 0,
        "entities_added": 0, "comparisons_added": 0,
    })
    for c in commits:
        date = c["date"]
        for op, fpath in c["files"]:
            if op == "A":
                by_date[date]["files_added"] += 1
                if "concepts/" in fpath:
                    by_date[date]["concepts_added"] += 1
                elif "sources/" in fpath:
                    by_date[date]["sources_added"] += 1
                elif "entities/" in fpath:
                    by_date[date]["entities_added"] += 1
                elif "comparisons/" in fpath:
                    by_date[date]["comparisons_added"] += 1
            elif op == "M":
                by_date[date]["files_modified"] += 1
            elif op == "D":
                by_date[date]["files_deleted"] += 1
    return dict(by_date)


def generate_svg_chart(daily_data, current_stats):
    """Generate an embedded SVG bar chart in HTML."""
    dates = sorted(daily_data.keys())
    if not dates:
        return "<p>No data to chart.</p>"

    # Cumulative file count
    cumulative = []
    running = 0
    for d in dates:
        running += daily_data[d]["files_added"] - daily_data[d]["files_deleted"]
        cumulative.append((d, running))

    max_val = max(v for _, v in cumulative) if cumulative else 1
    chart_w = max(600, len(dates) * 80)
    chart_h = 300
    bar_w = min(60, (chart_w - 40) // max(len(dates), 1))
    padding = 40

    bars_svg = []
    labels_svg = []
    for i, (date, count) in enumerate(cumulative):
        x = padding + i * (bar_w + 10)
        bar_h = (count / max_val) * (chart_h - 60) if max_val > 0 else 0
        y = chart_h - 30 - bar_h

        # Stacked bar: concepts (blue) + sources (green) + other (gray)
        ca = daily_data[date]["concepts_added"]
        sa = daily_data[date]["sources_added"]
        ea = daily_data[date]["entities_added"]
        cpa = daily_data[date]["comparisons_added"]
        total_new = daily_data[date]["files_added"]
        oa = total_new - ca - sa - ea - cpa

        # Simple bar for total cumulative
        bars_svg.append(
            f'<rect x="{x}" y="{y}" width="{bar_w}" height="{bar_h}" '
            f'fill="#4A90D9" rx="3" opacity="0.85"/>'
        )
        bars_svg.append(
            f'<text x="{x + bar_w // 2}" y="{y - 5}" text-anchor="middle" '
            f'font-size="11" fill="#333">{count}</text>'
        )
        labels_svg.append(
            f'<text x="{x + bar_w // 2}" y="{chart_h - 10}" text-anchor="middle" '
            f'font-size="10" fill="#666">{date[-5:]}</text>'
        )

    svg = f"""<svg width="{chart_w}" height="{chart_h}" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#fafafa" rx="8"/>
  <text x="{chart_w // 2}" y="20" text-anchor="middle" font-size="14" font-weight="bold" fill="#333">
    Wiki Growth — Cumulative File Count
  </text>
  {''.join(bars_svg)}
  {''.join(labels_svg)}
</svg>"""

    # Build breakdown chart
    if dates:
        latest = dates[-1]
        d = daily_data[latest]
        breakdown_items = [
            ("Concepts", d["concepts_added"], "#4A90D9"),
            ("Sources", d["sources_added"], "#50C878"),
            ("Entities", d["entities_added"], "#F5A623"),
            ("Comparisons", d["comparisons_added"], "#BD10E0"),
        ]
        total = sum(x[1] for x in breakdown_items)
        pie_parts = []
        offset = 0
        for label, val, color in breakdown_items:
            if val > 0 and total > 0:
                pct = val / total * 100
                pie_parts.append(f'<div style="display:inline-block;margin:0 12px;">'
                                 f'<span style="color:{color};font-size:20px;">&#9632;</span> '
                                 f'{label}: {val} ({pct:.0f}%)</div>')
        breakdown_html = "".join(pie_parts)
    else:
        breakdown_html = ""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Wiki Growth Report</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; color: #333; }}
  h1 {{ color: #2c3e50; border-bottom: 2px solid #4A90D9; padding-bottom: 8px; }}
  .stat-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; margin: 20px 0; }}
  .stat-card {{ background: #f8f9fa; border-radius: 8px; padding: 16px; text-align: center; border: 1px solid #e9ecef; }}
  .stat-card .number {{ font-size: 28px; font-weight: bold; color: #4A90D9; }}
  .stat-card .label {{ font-size: 13px; color: #666; margin-top: 4px; }}
  .chart-container {{ margin: 30px 0; overflow-x: auto; }}
  .breakdown {{ margin: 20px 0; padding: 16px; background: #f8f9fa; border-radius: 8px; }}
</style>
</head>
<body>
<h1>Wiki Growth Report</h1>
<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>

<div class="stat-grid">
  <div class="stat-card"><div class="number">{current_stats['total_files']}</div><div class="label">Total Files</div></div>
  <div class="stat-card"><div class="number">{current_stats['total_words']:,}</div><div class="label">Total Words</div></div>
  <div class="stat-card"><div class="number">{current_stats['concepts']}</div><div class="label">Concepts</div></div>
  <div class="stat-card"><div class="number">{current_stats['sources']}</div><div class="label">Sources</div></div>
  <div class="stat-card"><div class="number">{current_stats['entities']}</div><div class="label">Entities</div></div>
  <div class="stat-card"><div class="number">{current_stats['comparisons']}</div><div class="label">Comparisons</div></div>
</div>

<div class="chart-container">
{svg}
</div>

<div class="breakdown">
<strong>Composition (latest day):</strong><br>
{breakdown_html}
</div>

</body>
</html>"""
    return html


def generate_report(daily_data, current_stats):
    """Generate markdown growth report."""
    lines = ["# Wiki Growth Report", ""]
    lines.append(f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("")

    lines.append("## Current State")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total files | {current_stats['total_files']} |")
    lines.append(f"| Total words | {current_stats['total_words']:,} |")
    lines.append(f"| Total lines | {current_stats['total_lines']:,} |")
    lines.append(f"| Concepts | {current_stats['concepts']} |")
    lines.append(f"| Sources | {current_stats['sources']} |")
    lines.append(f"| Entities | {current_stats['entities']} |")
    lines.append(f"| Comparisons | {current_stats['comparisons']} |")
    lines.append(f"| Other | {current_stats['other']} |")
    lines.append("")

    lines.append("## Daily Activity")
    lines.append("")
    lines.append("| Date | Added | Modified | Deleted | Concepts | Sources |")
    lines.append("|------|-------|----------|---------|----------|---------|")

    for date in sorted(daily_data.keys(), reverse=True):
        d = daily_data[date]
        lines.append(
            f"| {date} | {d['files_added']} | {d['files_modified']} | {d['files_deleted']} "
            f"| +{d['concepts_added']} | +{d['sources_added']} |"
        )
    lines.append("")

    # Totals
    total_added = sum(d["files_added"] for d in daily_data.values())
    total_modified = sum(d["files_modified"] for d in daily_data.values())
    total_deleted = sum(d["files_deleted"] for d in daily_data.values())
    lines.append(f"**Totals:** {total_added} added, {total_modified} modified, {total_deleted} deleted")
    lines.append("")

    lines.append("## Chart")
    lines.append("")
    lines.append(f"Open [wiki-growth.html](../../output/images/wiki-growth.html) for an interactive SVG chart.")
    lines.append("")

    return "\n".join(lines) + "\n"


def main():
    print("Analyzing wiki growth from git history...")
    commits = get_all_commits()
    daily_data = build_daily_data(commits)
    current_stats = current_wiki_stats()

    # Generate HTML chart
    html = generate_svg_chart(daily_data, current_stats)
    IMG_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    IMG_OUTPUT.write_text(html)
    print(f"HTML chart written to {IMG_OUTPUT}")

    # Generate markdown report
    report = generate_report(daily_data, current_stats)
    RPT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    RPT_OUTPUT.write_text(report)
    print(f"Growth report written to {RPT_OUTPUT}")

    # Summary
    print()
    print(f"Wiki: {current_stats['total_files']} files, {current_stats['total_words']:,} words")
    print(f"  Concepts: {current_stats['concepts']}, Sources: {current_stats['sources']}, "
          f"Entities: {current_stats['entities']}, Comparisons: {current_stats['comparisons']}")


if __name__ == "__main__":
    main()
