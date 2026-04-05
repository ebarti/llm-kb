#!/usr/bin/env python3
"""
Freshness scorer plugin — scores articles by how current they are.

Hook: on_lint
Scoring based on:
  - Age of underlying sources (from frontmatter dates)
  - Time since last compilation (last_compiled field)
  - Whether sources are still accessible (optional URL check, off by default)
"""

import os
import re
from datetime import datetime, timedelta


def register():
    return {"on_lint": run_on_lint}


# Scoring weights
MAX_AGE_DAYS = 365  # Articles older than this get score 0 for age
COMPILE_WEIGHT = 0.5
SOURCE_AGE_WEIGHT = 0.5


def parse_date(date_str):
    """Try to parse a date string in common formats."""
    if not date_str:
        return None
    date_str = date_str.strip().strip('"').strip("'")
    for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%dT%H:%M:%S",
                "%B %d, %Y", "%b %d, %Y", "%Y"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def extract_dates(content):
    """Extract relevant dates from frontmatter."""
    dates = {}
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return dates

    fm = fm_match.group(1)

    # last_compiled
    m = re.search(r"last_compiled:\s*(.+)$", fm, re.MULTILINE)
    if m:
        d = parse_date(m.group(1))
        if d:
            dates["last_compiled"] = d

    # date / published
    for field in ("date", "published", "created"):
        m = re.search(rf"{field}:\s*(.+)$", fm, re.MULTILINE)
        if m:
            d = parse_date(m.group(1))
            if d:
                dates["source_date"] = d
                break

    return dates


def compute_freshness(dates, now):
    """Compute a freshness score from 0.0 (stale) to 1.0 (fresh)."""
    scores = []

    # Compilation freshness
    if "last_compiled" in dates:
        age_days = (now - dates["last_compiled"]).days
        score = max(0.0, 1.0 - (age_days / MAX_AGE_DAYS))
        scores.append(("compile_age", score, COMPILE_WEIGHT))
    else:
        scores.append(("compile_age", 0.0, COMPILE_WEIGHT))

    # Source age freshness
    if "source_date" in dates:
        age_days = (now - dates["source_date"]).days
        score = max(0.0, 1.0 - (age_days / (MAX_AGE_DAYS * 2)))
        scores.append(("source_age", score, SOURCE_AGE_WEIGHT))
    else:
        scores.append(("source_age", 0.3, SOURCE_AGE_WEIGHT))  # unknown = neutral-low

    # Weighted average
    total_weight = sum(w for _, _, w in scores)
    if total_weight == 0:
        return 0.0, scores
    weighted = sum(s * w for _, s, w in scores) / total_weight
    return round(weighted, 3), scores


def run_on_lint(root, *args):
    """Score all wiki articles by freshness."""
    wiki_dir = os.path.join(root, "wiki")
    now = datetime.now()

    results = []

    for dirpath, _, filenames in os.walk(wiki_dir):
        rel_dir = os.path.relpath(dirpath, wiki_dir)
        if rel_dir.startswith("_meta"):
            continue
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            relpath = os.path.relpath(fpath, wiki_dir)

            try:
                with open(fpath, "r", errors="replace") as f:
                    content = f.read()
            except OSError:
                continue

            dates = extract_dates(content)
            score, details = compute_freshness(dates, now)
            results.append({
                "file": relpath,
                "score": score,
                "details": {name: round(s, 3) for name, s, _ in details},
                "last_compiled": dates.get("last_compiled", "unknown"),
            })

    # Sort by freshness (stalest first)
    results.sort(key=lambda x: x["score"])

    # Generate report
    report_lines = [
        "# Freshness Report",
        "",
        f"Generated: {now.strftime('%Y-%m-%d %H:%M')}",
        "",
        "Score ranges: 0.0 (stale) to 1.0 (fresh)",
        "",
        "## Articles by Freshness (stalest first)",
        "",
        "| Score | Article | Last Compiled |",
        "|-------|---------|---------------|",
    ]

    for r in results:
        lc = r["last_compiled"]
        if isinstance(lc, datetime):
            lc = lc.strftime("%Y-%m-%d")
        score_bar = "█" * int(r["score"] * 10) + "░" * (10 - int(r["score"] * 10))
        report_lines.append(
            f"| {r['score']:.2f} {score_bar} | {r['file']} | {lc} |"
        )

    # Summary stats
    if results:
        avg = sum(r["score"] for r in results) / len(results)
        stale = sum(1 for r in results if r["score"] < 0.3)
        report_lines.extend([
            "",
            "## Summary",
            "",
            f"- **Average freshness**: {avg:.2f}",
            f"- **Total articles**: {len(results)}",
            f"- **Stale articles** (score < 0.3): {stale}",
        ])

    report_path = os.path.join(wiki_dir, "_meta", "freshness-report.md")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines) + "\n")

    print(f"  [freshness_scorer] Scored {len(results)} articles")
    if results:
        avg = sum(r["score"] for r in results) / len(results)
        stale = sum(1 for r in results if r["score"] < 0.3)
        print(f"  [freshness_scorer] Average freshness: {avg:.2f}, stale: {stale}")
    print(f"  [freshness_scorer] Report: wiki/_meta/freshness-report.md")
