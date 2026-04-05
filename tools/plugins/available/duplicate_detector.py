#!/usr/bin/env python3
"""
Duplicate detector plugin — checks for similar existing articles before ingest.

Hook: pre_ingest
Uses Jaccard similarity on word n-grams to detect potential duplicates.
"""

import os
import re
from collections import Counter


def register():
    return {"pre_ingest": run_pre_ingest}


SIMILARITY_THRESHOLD = 0.3  # Flag if Jaccard similarity exceeds this
NGRAM_SIZE = 3


def tokenize(text):
    """Extract lowercase words from text."""
    return re.findall(r"[a-z][a-z0-9]+", text.lower())


def ngrams(tokens, n=NGRAM_SIZE):
    """Generate word n-grams as a set of tuples."""
    if len(tokens) < n:
        return set(tuple(tokens))
    return set(tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1))


def jaccard(set_a, set_b):
    """Compute Jaccard similarity between two sets."""
    if not set_a or not set_b:
        return 0.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union > 0 else 0.0


def extract_title(content):
    """Extract title from frontmatter or first heading."""
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        title_match = re.search(r'title:\s*"([^"]*)"', fm_match.group(1))
        if title_match:
            return title_match.group(1)
    # Fallback: first H1 or H2
    heading = re.search(r"^##?\s+(.+)$", content, re.MULTILINE)
    if heading:
        return heading.group(1).strip()
    return None


def title_similarity(t1, t2):
    """Simple word overlap similarity between two titles."""
    if not t1 or not t2:
        return 0.0
    w1 = set(t1.lower().split())
    w2 = set(t2.lower().split())
    if not w1 or not w2:
        return 0.0
    return len(w1 & w2) / len(w1 | w2)


def run_pre_ingest(root, *args):
    """Check if a similar article already exists."""
    if not args:
        print("  [duplicate_detector] No file path provided, skipping.")
        return

    file_path = args[0]
    if not os.path.isabs(file_path):
        file_path = os.path.join(root, file_path)

    if not os.path.exists(file_path):
        print(f"  [duplicate_detector] File not found: {file_path}")
        return

    # Read the new file
    with open(file_path, "r", errors="replace") as f:
        new_content = f.read()

    new_title = extract_title(new_content)
    new_tokens = tokenize(new_content)
    new_ngrams = ngrams(new_tokens)

    # Scan existing raw/ and wiki/sources/ for duplicates
    duplicates = []
    search_dirs = [
        os.path.join(root, "raw"),
        os.path.join(root, "wiki", "sources"),
    ]

    for search_dir in search_dirs:
        if not os.path.isdir(search_dir):
            continue
        for fname in os.listdir(search_dir):
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(search_dir, fname)
            if os.path.abspath(fpath) == os.path.abspath(file_path):
                continue

            try:
                with open(fpath, "r", errors="replace") as f:
                    existing_content = f.read()
            except OSError:
                continue

            existing_title = extract_title(existing_content)
            existing_tokens = tokenize(existing_content)
            existing_ngrams = ngrams(existing_tokens)

            # Compute similarities
            content_sim = jaccard(new_ngrams, existing_ngrams)
            t_sim = title_similarity(new_title, existing_title)

            # Combined score (weighted)
            combined = 0.6 * content_sim + 0.4 * t_sim

            if combined > SIMILARITY_THRESHOLD or content_sim > 0.4 or t_sim > 0.6:
                duplicates.append({
                    "file": os.path.relpath(fpath, root),
                    "title": existing_title or fname,
                    "content_similarity": round(content_sim, 3),
                    "title_similarity": round(t_sim, 3),
                    "combined": round(combined, 3),
                })

    if duplicates:
        duplicates.sort(key=lambda x: -x["combined"])
        print(f"  [duplicate_detector] WARNING: Potential duplicates found for "
              f"'{new_title or os.path.basename(file_path)}':")
        for d in duplicates:
            print(f"    - {d['file']} (title: {d['title_similarity']}, "
                  f"content: {d['content_similarity']}, combined: {d['combined']})")
    else:
        print(f"  [duplicate_detector] No duplicates found. Clear to ingest.")
