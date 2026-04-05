#!/usr/bin/env python3
"""
Glossary builder plugin — extracts defined terms and builds a glossary.

Hook: post_compile
Scans all articles for defined terms:
  - Bold text patterns: **term**
  - Definition patterns: "X is...", "X refers to..."
Builds wiki/Glossary.md with definitions and links to source articles.
"""

import os
import re
from collections import defaultdict


def register():
    return {"post_compile": run_post_compile}


# Patterns for finding definitions
DEFINITION_PATTERNS = [
    # **Term** is/are/refers to ...
    r"\*\*([^*]{2,60})\*\*\s+(?:is|are|refers to|means|describes?|represents?)\s+(.{20,200}?)(?:\.|$)",
    # A **term** is ...
    r"[Aa]n?\s+\*\*([^*]{2,60})\*\*\s+(?:is|are|refers to)\s+(.{20,200}?)(?:\.|$)",
    # "Term" is defined as ...
    r'"([^"]{2,60})"\s+(?:is defined as|is|means)\s+(.{20,200}?)(?:\.|$)',
]

# Pattern for standalone bold terms (potential glossary entries)
BOLD_TERM_PATTERN = r"\*\*([^*]{2,60})\*\*"


def clean_definition(text):
    """Clean a definition string."""
    # Remove markdown links but keep text
    text = re.sub(r"\[\[([^\]|]*?)(?:\|([^\]]*))?\]\]", lambda m: m.group(2) or m.group(1), text)
    text = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", text)
    # Remove remaining markdown
    text = re.sub(r"\*\*([^*]*)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]*)\*", r"\1", text)
    text = text.strip()
    # Capitalize first letter
    if text and text[0].islower():
        text = text[0].upper() + text[1:]
    # Ensure ends with period
    if text and not text.endswith("."):
        text += "."
    return text


def run_post_compile(root, *args):
    """Build the glossary from all wiki articles."""
    wiki_dir = os.path.join(root, "wiki")

    # term -> list of (definition, source_article)
    glossary = defaultdict(list)

    for dirpath, _, filenames in os.walk(wiki_dir):
        rel_dir = os.path.relpath(dirpath, wiki_dir)
        if rel_dir.startswith("_meta"):
            continue
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            # Skip the glossary itself and other generated files
            if fname in ("Glossary.md", "Reading-List.md", "Changelog.md"):
                continue

            fpath = os.path.join(dirpath, fname)
            relpath = os.path.relpath(fpath, wiki_dir).replace(".md", "")

            try:
                with open(fpath, "r", errors="replace") as f:
                    content = f.read()
            except OSError:
                continue

            # Strip frontmatter for searching
            body = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

            # Find explicit definitions
            for pattern in DEFINITION_PATTERNS:
                for match in re.finditer(pattern, body, re.MULTILINE):
                    term = match.group(1).strip()
                    definition = match.group(2).strip()
                    if len(term) > 2 and len(definition) > 10:
                        glossary[term.lower()].append({
                            "term": term,
                            "definition": clean_definition(definition),
                            "source": relpath,
                        })

    if not glossary:
        print("  [glossary_builder] No defined terms found.")
        return

    # Deduplicate: keep the longest definition per term
    final_glossary = {}
    for key in sorted(glossary.keys()):
        entries = glossary[key]
        # Pick the entry with the longest definition
        best = max(entries, key=lambda e: len(e["definition"]))
        # Collect all sources
        sources = sorted(set(e["source"] for e in entries))
        final_glossary[key] = {
            "term": best["term"],
            "definition": best["definition"],
            "sources": sources,
        }

    # Generate Glossary.md
    lines = [
        "---",
        'title: "Glossary"',
        "type: meta",
        f"last_updated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d')}",
        f"entries: {len(final_glossary)}",
        "---",
        "",
        "# Glossary",
        "",
        "Auto-generated glossary of defined terms found across wiki articles.",
        "",
    ]

    # Group by first letter
    by_letter = defaultdict(list)
    for key, entry in sorted(final_glossary.items()):
        letter = entry["term"][0].upper()
        by_letter[letter].append(entry)

    for letter in sorted(by_letter.keys()):
        lines.append(f"## {letter}")
        lines.append("")
        for entry in by_letter[letter]:
            source_links = ", ".join(f"[[{s}]]" for s in entry["sources"])
            lines.append(f"**{entry['term']}**")
            lines.append(f": {entry['definition']}")
            lines.append(f": _Source: {source_links}_")
            lines.append("")

    glossary_path = os.path.join(wiki_dir, "Glossary.md")
    with open(glossary_path, "w") as f:
        f.write("\n".join(lines))

    print(f"  [glossary_builder] Built glossary with {len(final_glossary)} terms")
    print(f"  [glossary_builder] Written to wiki/Glossary.md")
