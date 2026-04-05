#!/usr/bin/env python3
"""
Citation checker plugin — verifies concept articles cite their sources.

Hook: on_lint
Flags articles that make claims but have no source links in frontmatter
or body text.
"""

import os
import re


def register():
    return {"on_lint": run_on_lint}


# Patterns that suggest claims are being made
CLAIM_PATTERNS = [
    r"\baccording to\b",
    r"\bresearch shows\b",
    r"\bstudies (?:show|suggest|indicate)\b",
    r"\bit (?:has been|is) (?:shown|demonstrated|proven)\b",
    r"\bevidence suggests\b",
    r"\bdata (?:shows|indicates)\b",
    r"\bexperts (?:say|believe|argue)\b",
]


def has_source_references(content, frontmatter):
    """Check if the article references sources."""
    # Check frontmatter for sources field
    if re.search(r"sources:\s*\[.+\]", frontmatter):
        return True
    # Check body for wikilinks to sources/
    if re.search(r"\[\[sources/", content):
        return True
    # Check for external URLs
    if re.search(r"\[.+?\]\(https?://", content):
        return True
    # Check for source/reference section
    if re.search(r"^#+\s*(sources|references|citations|bibliography)", content,
                 re.MULTILINE | re.IGNORECASE):
        return True
    return False


def find_unsourced_claims(content):
    """Find lines that look like claims without inline citations."""
    issues = []
    lines = content.split("\n")
    for i, line in enumerate(lines, 1):
        for pattern in CLAIM_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                # Check if this line has a citation nearby
                context = "\n".join(lines[max(0, i-3):min(len(lines), i+2)])
                if not re.search(r"\[\[sources/|\]\(https?://", context):
                    issues.append((i, line.strip()[:100], pattern))
                break
    return issues


def run_on_lint(root, *args):
    """Check all concept articles for proper citations."""
    wiki_dir = os.path.join(root, "wiki")
    concepts_dir = os.path.join(wiki_dir, "concepts")

    if not os.path.isdir(concepts_dir):
        print("  [citation_checker] No concepts/ directory found, skipping.")
        return

    issues_found = 0
    articles_checked = 0

    report_lines = ["# Citation Check Report", ""]

    for fname in sorted(os.listdir(concepts_dir)):
        if not fname.endswith(".md"):
            continue

        fpath = os.path.join(concepts_dir, fname)
        try:
            with open(fpath, "r", errors="replace") as f:
                content = f.read()
        except OSError:
            continue

        articles_checked += 1

        # Split frontmatter and body
        fm_match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
        if fm_match:
            frontmatter = fm_match.group(1)
            body = fm_match.group(2)
        else:
            frontmatter = ""
            body = content

        article_issues = []

        # Check for source references
        if not has_source_references(content, frontmatter):
            article_issues.append("No source references found (frontmatter or body)")

        # Check for unsourced claim patterns
        claims = find_unsourced_claims(body)
        for line_no, text, pattern in claims:
            article_issues.append(f"Line {line_no}: possible unsourced claim: {text}")

        if article_issues:
            issues_found += len(article_issues)
            article_name = fname.replace(".md", "")
            report_lines.append(f"## {article_name}")
            for issue in article_issues:
                report_lines.append(f"- {issue}")
            report_lines.append("")
            print(f"  [citation_checker] {article_name}: {len(article_issues)} issue(s)")

    if issues_found == 0:
        report_lines.append("All concept articles have proper citations.")
        print(f"  [citation_checker] All {articles_checked} articles have proper citations.")
    else:
        print(f"  [citation_checker] Found {issues_found} issue(s) across "
              f"{articles_checked} articles.")

    # Write report
    report_path = os.path.join(wiki_dir, "_meta", "citation-report.md")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        f.write("\n".join(report_lines) + "\n")
    print(f"  [citation_checker] Report: wiki/_meta/citation-report.md")
