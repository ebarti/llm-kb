#!/usr/bin/env python3
"""
Content Quality Checker
Evaluates the quality of each wiki article.

Checks per article:
  - Word count (flag if < 50 words)
  - Number of wikilinks (flag if 0)
  - Has Overview/Key Ideas sections (for concepts)
  - Has Key Points/Detailed Summary (for sources)
  - Has Comparison Table (for comparisons)
  - Frontmatter completeness score

Usage: python3 tools/tests/check-quality.py [--json]
"""

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = BASE_DIR / "wiki"
TEMPLATE_LEAK_CHECKER_PATH = BASE_DIR / "tools" / "tests" / "check-template-leaks.py"

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]")

# All possible frontmatter fields we might expect
ALL_FM_FIELDS = [
    "title", "type", "summary", "last_compiled", "source", "sources",
    "related", "entity_type",
]

# Expected sections per type
EXPECTED_SECTIONS = {
    "concept": {
        "required": ["Overview"],
        "optional": ["Key Ideas", "Key Contributions", "Sources", "Related Concepts"],
    },
    "source-summary": {
        "required": ["Key Points"],
        "optional": ["Detailed Summary", "Sources", "Related Concepts"],
    },
    "comparison": {
        "required": ["Comparison"],
        "optional": ["Overview", "Sources"],
    },
    "entity": {
        "required": ["Overview"],
        "optional": ["Key Contributions", "Sources", "Related"],
    },
}

MIN_WORD_COUNT = 50


def load_template_leak_checker():
    spec = importlib.util.spec_from_file_location(
        "check_template_leaks",
        TEMPLATE_LEAK_CHECKER_PATH,
    )
    if spec is None or spec.loader is None:
        raise ImportError(
            f"Unable to load checker module from {TEMPLATE_LEAK_CHECKER_PATH}"
        )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[4:end]
    body = text[end + 4:]
    meta = {}
    for line in fm_block.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        colon = line.find(":")
        if colon == -1:
            continue
        key = line[:colon].strip()
        val = line[colon + 1:].strip().strip('"').strip("'")
        meta[key] = val
    return meta, body


def extract_headings(body):
    """Extract ## headings from the body."""
    headings = []
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+)", line)
        if m:
            headings.append(m.group(1).strip())
    return headings


def score_article(filepath):
    """Score a single article. Returns a dict with scores and flags."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(text)
    rel_path = str(filepath.relative_to(WIKI_DIR)).replace(".md", "")
    article_type = meta.get("type", "unknown")

    result = {
        "path": rel_path,
        "type": article_type,
        "flags": [],
        "scores": {},
    }

    # Word count
    words = body.split()
    word_count = len(words)
    result["scores"]["word_count"] = word_count
    if word_count < MIN_WORD_COUNT:
        result["flags"].append(f"Low word count: {word_count} (min {MIN_WORD_COUNT})")

    # Wikilinks
    links = WIKILINK_RE.findall(body)
    link_count = len(links)
    result["scores"]["wikilink_count"] = link_count
    if link_count == 0:
        result["flags"].append("No wikilinks in body")

    # Frontmatter completeness
    fm_fields_present = sum(1 for f in ALL_FM_FIELDS if f in meta and meta[f])
    fm_score = round(fm_fields_present / len(ALL_FM_FIELDS) * 100, 1)
    result["scores"]["frontmatter_completeness"] = fm_score

    # Section checks
    headings = extract_headings(body)
    heading_names = [h.lower() for h in headings]

    expected = EXPECTED_SECTIONS.get(article_type, {})
    required_sections = expected.get("required", [])
    optional_sections = expected.get("optional", [])

    found_required = 0
    missing_required = []
    for sec in required_sections:
        # Fuzzy match: check if any heading contains the section name
        if any(sec.lower() in h for h in heading_names):
            found_required += 1
        else:
            missing_required.append(sec)

    if missing_required:
        result["flags"].append(f"Missing expected sections: {', '.join(missing_required)}")

    found_optional = sum(1 for sec in optional_sections if any(sec.lower() in h for h in heading_names))

    total_expected = len(required_sections) + len(optional_sections)
    sections_found = found_required + found_optional
    section_score = round(sections_found / total_expected * 100, 1) if total_expected > 0 else 100.0
    result["scores"]["section_completeness"] = section_score

    # Has comparison table (for comparisons)
    if article_type == "comparison":
        has_table = "|" in body and "---" in body
        if not has_table:
            result["flags"].append("Missing comparison table")
        result["scores"]["has_table"] = has_table

    # Overall quality score (weighted)
    word_score = min(100, word_count / 2)  # 200 words = 100%
    link_score = min(100, link_count * 20)  # 5 links = 100%
    overall = round((word_score * 0.3 + link_score * 0.2 + fm_score * 0.2 + section_score * 0.3), 1)
    result["scores"]["overall"] = overall

    return result


def apply_template_leak_flags(articles, leak_result):
    article_map = {article["path"]: article for article in articles}
    global_flags = []

    for rel_path, leaks in sorted(leak_result["leaks_by_file"].items()):
        article_path = rel_path
        if article_path.startswith("wiki/"):
            article_path = article_path[len("wiki/"):]
        if article_path.endswith(".md"):
            article_path = article_path[:-3]
        unique_tokens = ", ".join(sorted({leak["token"] for leak in leaks}))

        article = article_map.get(article_path)
        if article is not None:
            article["flags"].append(f"Template placeholder leaks: {unique_tokens}")
            continue

        global_flags.append(
            f"Template placeholder leaks in {rel_path}: {unique_tokens}"
        )

    return global_flags


def run_checks():
    template_leak_checker = load_template_leak_checker()
    articles = []
    for subdir in ["concepts", "sources", "comparisons", "entities"]:
        dirpath = WIKI_DIR / subdir
        if dirpath.is_dir():
            for f in sorted(dirpath.iterdir()):
                if f.suffix == ".md":
                    articles.append(score_article(f))

    template_leak_result = template_leak_checker.run_checks()
    global_flags = apply_template_leak_flags(articles, template_leak_result)

    total_flags = sum(len(a["flags"]) for a in articles) + len(global_flags)
    avg_overall = round(sum(a["scores"]["overall"] for a in articles) / len(articles), 1) if articles else 0
    avg_words = round(sum(a["scores"]["word_count"] for a in articles) / len(articles), 1) if articles else 0

    return {
        "total_articles": len(articles),
        "total_flags": total_flags,
        "avg_quality_score": avg_overall,
        "avg_word_count": avg_words,
        "global_flags": global_flags,
        "template_leak_check": {
            "ok": template_leak_result["ok"],
            "files_with_leaks": template_leak_result["files_with_leaks"],
            "total_leaks": template_leak_result["total_leaks"],
        },
        "articles": articles,
        "ok": total_flags == 0 and template_leak_result["ok"],
    }


def print_report(result):
    print("=" * 60)
    print("  Content Quality Report")
    print("=" * 60)
    print(f"\nArticles: {result['total_articles']}")
    print(f"Avg quality score: {result['avg_quality_score']}%")
    print(f"Avg word count: {result['avg_word_count']}")
    print(f"Total flags: {result['total_flags']}")
    print(
        "Template leak check: "
        f"{result['template_leak_check']['total_leaks']} leak(s) in "
        f"{result['template_leak_check']['files_with_leaks']} file(s)"
    )
    print()

    # Print per-article summary
    print(f"{'Article':<50} {'Score':>6} {'Words':>6} {'Links':>6} {'Flags':>6}")
    print("-" * 80)
    for a in result["articles"]:
        score = a["scores"]["overall"]
        words = a["scores"]["word_count"]
        links = a["scores"]["wikilink_count"]
        flags = len(a["flags"])
        color = "\033[32m" if flags == 0 else "\033[33m" if flags <= 1 else "\033[31m"
        reset = "\033[0m"
        print(f"{color}{a['path']:<50} {score:>5.1f}% {words:>6} {links:>6} {flags:>6}{reset}")

    # Print flagged articles
    flagged = [a for a in result["articles"] if a["flags"]]
    if flagged:
        print(f"\n--- Flagged Articles ---")
        for a in flagged:
            print(f"\n  {a['path']}:")
            for flag in a["flags"]:
                print(f"    - {flag}")

    if result["global_flags"]:
        print(f"\n--- Global Flags ---")
        for flag in result["global_flags"]:
            print(f"  - {flag}")

    print()
    if result["ok"]:
        print("\033[32mNo quality issues found.\033[0m")
    else:
        print(f"\033[33m{result['total_flags']} quality flag(s) found.\033[0m")
    print()


def main():
    parser = argparse.ArgumentParser(description="Content Quality Checker")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    result = run_checks()

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    sys.exit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
