#!/bin/bash
# import-clippings.sh — Import Obsidian Web Clipper files from Clippings/ into raw/
# Usage: ./tools/ingest/import-clippings.sh
#
# Reads markdown files from the Clippings/ directory, normalizes their
# frontmatter to match the project's standard format, and copies them
# into raw/ with appropriate filenames.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
RAW_DIR="$PROJECT_DIR/raw"
CLIPPINGS_DIR="$PROJECT_DIR/Clippings"

mkdir -p "$RAW_DIR"

if [ ! -d "$CLIPPINGS_DIR" ]; then
    echo "ERROR: Clippings directory not found at: $CLIPPINGS_DIR"
    exit 1
fi

TODAY=$(date +%Y-%m-%d)

# Count clipping files
TOTAL=$(find "$CLIPPINGS_DIR" -maxdepth 2 -name "*.md" -type f 2>/dev/null | wc -l | tr -d ' ')

if [ "$TOTAL" -eq 0 ]; then
    echo "No markdown files found in $CLIPPINGS_DIR"
    exit 0
fi

echo "=== Importing Clippings ==="
echo "Source: $CLIPPINGS_DIR"
echo "Destination: $RAW_DIR"
echo "Files found: $TOTAL"
echo ""

IMPORTED=0
SKIPPED=0
FAILED=0

find "$CLIPPINGS_DIR" -maxdepth 2 -name "*.md" -type f | sort | while IFS= read -r CLIP_FILE; do
    BASENAME=$(basename "$CLIP_FILE" .md)
    echo "Processing: $BASENAME"

    # Generate a safe slug
    SAFE_NAME=$(echo "$BASENAME" | \
        tr '[:upper:]' '[:lower:]' | \
        sed 's/[^a-z0-9 @_-]//g' | \
        sed 's/  \+/ /g; s/^ //; s/ $//' | \
        tr ' ' '-' | \
        cut -c1-80)
    SLUG="clip-${SAFE_NAME}"
    TARGET_DIR="$RAW_DIR/$SLUG"

    # Check if already imported (both new layout and legacy flat file)
    if [ -d "$TARGET_DIR" ] && [ -f "$TARGET_DIR/clean.md" ]; then
        echo "  SKIP: Already exists at $TARGET_DIR/"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi
    if [ -f "$RAW_DIR/${SLUG}.md" ]; then
        echo "  SKIP: Legacy flat file exists at $RAW_DIR/${SLUG}.md"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Build the normalised clean.md in a temp file, then persist via the writer
    python3 - "$CLIP_FILE" "$BASENAME" "$TODAY" "$SLUG" "$PROJECT_DIR" <<'PYEOF'
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

input_path, basename, today, slug, project_dir = sys.argv[1:6]

with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

frontmatter = {}
body = content
fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
if fm_match:
    fm_text = fm_match.group(1)
    body = fm_match.group(2)
    current_key = None
    for line in fm_text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('-') and current_key:
            val = stripped.lstrip('-').strip().strip('"').strip("'")
            val = re.sub(r'\[\[(@?[^\]]+)\]\]', r'\1', val)
            if val:
                existing = frontmatter.get(current_key, '')
                frontmatter[current_key] = (existing + ', ' + val).lstrip(', ')
            continue
        if ':' in stripped and not stripped.startswith('#'):
            key, _, value = stripped.partition(':')
            key = key.strip().lower()
            value = value.strip().strip('"').strip("'")
            value = re.sub(r'\[\[(@?[^\]]+)\]\]', r'\1', value)
            current_key = key
            if value and value != '(null)':
                frontmatter[key] = value
            elif not value:
                frontmatter.setdefault(key, '')
        else:
            current_key = None

title = frontmatter.get('title', basename)
source = frontmatter.get('source', frontmatter.get('url', frontmatter.get('link', '')))
author = frontmatter.get('author', frontmatter.get('authors', frontmatter.get('creator', '')))
if isinstance(author, str):
    author = re.sub(r'^\s*-\s*', '', author)
published = frontmatter.get('published', frontmatter.get('date_published',
            frontmatter.get('date', frontmatter.get('created', ''))))
description = frontmatter.get('description', frontmatter.get('excerpt', ''))

content_type = 'article'
if source:
    if 'youtube.com' in source or 'youtu.be' in source:
        content_type = 'youtube'
    elif 'twitter.com' in source or 'x.com' in source:
        content_type = 'tweet'
    elif 'arxiv.org' in source:
        content_type = 'arxiv'
    elif 'github.com' in source:
        content_type = 'github'

tags_raw = frontmatter.get('tags', '')
tags = ['clipping']
if tags_raw:
    for t in re.split(r'[,\n]', tags_raw):
        t = t.strip().strip('-').strip().strip('"').strip("'")
        if t and t not in tags:
            tags.append(t)

# Write normalised clean.md to a temp file
clean_path = Path(tempfile.mkstemp(suffix='.md', prefix='clip-clean-')[1])
lines = [
    '---',
    f'title: "{title}"',
    f'source: "{source}"',
    f'author: "{author}"',
    f'date_published: {published}',
    f'date_ingested: {today}',
]
if description:
    lines.append(f'description: "{description[:200]}"')
lines.append(f'tags: [{", ".join(tags)}]')
lines.append(f'type: {content_type}')
lines.append('status: raw')
lines.append('imported_from: clippings')
lines.append('---')
lines.append('')
lines.append(body)
clean_path.write_text('\n'.join(lines), encoding='utf-8')

extra_meta = json.dumps({
    "title": title,
    "author": str(author or ''),
    "date_published": str(published or ''),
    "imported_from": "clippings",
    "original_file": input_path,
})

writer = Path(project_dir) / "tools/ingest/_raw_writer.py"
# Clipping files ARE the original bytes (user already saved them) — pass as raw.md
result = subprocess.run([
    "python3", str(writer),
    "--slug", slug,
    "--url", str(source or ''),
    "--fetcher", "clippings",
    "--clean-path", str(clean_path),
    "--raw-path", input_path,
    "--raw-ext", "md",
    "--content-type", "markdown",
    "--extra-meta-json", extra_meta,
], capture_output=True, text=True)
clean_path.unlink(missing_ok=True)
if result.returncode not in (0, 2):
    print(f"  ERROR: {result.stderr}", file=sys.stderr)
    sys.exit(1)
print(f"  OK: raw/{slug}/")
PYEOF

    if [ $? -eq 0 ]; then
        IMPORTED=$((IMPORTED + 1))
    else
        FAILED=$((FAILED + 1))
    fi

done

echo ""
echo "=== Import Complete ==="
echo "Processed: $TOTAL files"
echo "Check raw/ for imported files with 'clip-' prefix."
