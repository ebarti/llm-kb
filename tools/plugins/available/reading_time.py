#!/usr/bin/env python3
"""
Reading time plugin — adds estimated reading time to article frontmatter.

Hook: post_compile
Average reading speed: 200 words/minute.
"""

import math
import os
import re


def register():
    return {"post_compile": run_post_compile}


WORDS_PER_MINUTE = 200


def count_words(text):
    """Count words in body text (after frontmatter)."""
    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    return len(body.split())


def update_frontmatter(content, reading_min):
    """Add or update reading_time in the YAML frontmatter."""
    fm_match = re.match(r"^(---\n)(.*?)(\n---\n)", content, re.DOTALL)
    if not fm_match:
        return content  # no frontmatter, skip

    prefix = fm_match.group(1)
    fm_body = fm_match.group(2)
    suffix = fm_match.group(3)
    rest = content[fm_match.end():]

    tag = f"reading_time: \"{reading_min} min\""

    # Replace existing reading_time or append
    if re.search(r"^reading_time:.*$", fm_body, re.MULTILINE):
        fm_body = re.sub(r"^reading_time:.*$", tag, fm_body, flags=re.MULTILINE)
    else:
        fm_body = fm_body.rstrip() + "\n" + tag

    return prefix + fm_body + suffix + rest


def run_post_compile(root, *args):
    """Add reading time estimates to all wiki articles."""
    wiki_dir = os.path.join(root, "wiki")
    updated = 0

    for dirpath, _, filenames in os.walk(wiki_dir):
        # Skip _meta directory
        if "_meta" in dirpath:
            continue
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r", errors="replace") as f:
                    content = f.read()
            except OSError:
                continue

            # Only process files with frontmatter
            if not content.startswith("---\n"):
                continue

            wc = count_words(content)
            reading_min = max(1, math.ceil(wc / WORDS_PER_MINUTE))

            new_content = update_frontmatter(content, reading_min)
            if new_content != content:
                with open(fpath, "w") as f:
                    f.write(new_content)
                updated += 1

    print(f"  [reading_time] Updated reading time in {updated} article(s)")
