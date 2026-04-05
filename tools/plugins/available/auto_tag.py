#!/usr/bin/env python3
"""
Auto-tag plugin — suggests tags for newly ingested content.

Hook: post_ingest
Uses TF-IDF-style keyword extraction against existing tags to suggest
consistent tagging for new source documents.
"""

import math
import os
import re
from collections import Counter


def register():
    return {"post_ingest": run_post_ingest}


# Common English stop words to ignore
STOP_WORDS = set(
    "a an the and or but in on at to for of is it that this with as by from"
    " be are was were been being have has had do does did will would shall"
    " should may might can could not no nor so if than too very just about"
    " also how what when where which who whom why all each every both few"
    " more most other some such their them then there these they through"
    " between into during before after above below up down out off over"
    " under again further once here only own same its our your".split()
)


def tokenize(text):
    """Extract lowercase word tokens, filtering stop words and short tokens."""
    words = re.findall(r"[a-z][a-z0-9-]+", text.lower())
    return [w for w in words if w not in STOP_WORDS and len(w) > 2]


def extract_existing_tags(wiki_dir):
    """Scan wiki articles for existing tags used in frontmatter."""
    tag_counts = Counter()
    for dirpath, _, filenames in os.walk(wiki_dir):
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", errors="replace") as f:
                    content = f.read(2000)  # frontmatter is at the top
            except OSError:
                continue
            # Look for tags in frontmatter
            fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if fm_match:
                fm = fm_match.group(1)
                tags_match = re.search(r"tags:\s*\[([^\]]*)\]", fm)
                if tags_match:
                    raw = tags_match.group(1)
                    for tag in re.findall(r'"([^"]+)"', raw):
                        tag_counts[tag.lower().strip()] += 1
    return tag_counts


def compute_tfidf(tokens, doc_count, doc_freq):
    """Compute TF-IDF scores for tokens in a single document."""
    tf = Counter(tokens)
    total = len(tokens) if tokens else 1
    scores = {}
    for term, count in tf.items():
        tf_score = count / total
        df = doc_freq.get(term, 0) + 1
        idf = math.log(doc_count / df) if doc_count > 0 else 1
        scores[term] = tf_score * idf
    return scores


def build_doc_freq(wiki_dir):
    """Build document frequency counts across all wiki markdown files."""
    doc_freq = Counter()
    doc_count = 0
    for dirpath, _, filenames in os.walk(wiki_dir):
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", errors="replace") as f:
                    text = f.read()
            except OSError:
                continue
            doc_count += 1
            unique_tokens = set(tokenize(text))
            for token in unique_tokens:
                doc_freq[token] += 1
    return doc_count, doc_freq


def run_post_ingest(root, *args):
    """Suggest tags for a newly ingested file."""
    if not args:
        print("  [auto_tag] No file path provided, skipping.")
        return

    file_path = args[0]
    if not os.path.isabs(file_path):
        file_path = os.path.join(root, file_path)

    if not os.path.exists(file_path):
        print(f"  [auto_tag] File not found: {file_path}")
        return

    wiki_dir = os.path.join(root, "wiki")

    # Read the new file
    with open(file_path, "r", errors="replace") as f:
        content = f.read()
    tokens = tokenize(content)

    if not tokens:
        print("  [auto_tag] No meaningful tokens found.")
        return

    # Build corpus stats
    doc_count, doc_freq = build_doc_freq(wiki_dir)

    # Compute TF-IDF for the new document
    scores = compute_tfidf(tokens, max(doc_count, 1), doc_freq)

    # Get existing tags for boosting consistency
    existing_tags = extract_existing_tags(wiki_dir)

    # Boost scores for terms that match existing tags
    for term in scores:
        if term in existing_tags:
            scores[term] *= 2.0
        # Also boost hyphenated compound terms that appear in tags
        for tag in existing_tags:
            if term in tag.split("-"):
                scores[term] *= 1.5

    # Top suggestions
    top = sorted(scores.items(), key=lambda x: -x[1])[:10]
    suggested = [term for term, _ in top]

    print(f"  [auto_tag] Suggested tags for {os.path.basename(file_path)}:")
    for i, tag in enumerate(suggested, 1):
        marker = " (existing)" if tag in existing_tags else ""
        print(f"    {i}. {tag}{marker}")

    # Write suggestions to a sidecar file
    suggestion_path = file_path + ".tags-suggested"
    with open(suggestion_path, "w") as f:
        f.write("# Auto-suggested tags\n")
        for tag in suggested:
            f.write(f"- {tag}\n")
    print(f"  [auto_tag] Suggestions written to {suggestion_path}")
