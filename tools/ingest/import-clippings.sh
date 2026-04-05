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

    # Generate a safe output filename
    SAFE_NAME=$(echo "$BASENAME" | \
        tr '[:upper:]' '[:lower:]' | \
        sed 's/[^a-z0-9 @_-]//g' | \
        sed 's/  \+/ /g; s/^ //; s/ $//' | \
        tr ' ' '-' | \
        cut -c1-80)
    OUTPUT_FILE="$RAW_DIR/clip-${SAFE_NAME}.md"

    # Check if already imported
    if [ -f "$OUTPUT_FILE" ]; then
        echo "  SKIP: Already exists at $OUTPUT_FILE"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # Read the clipping file and normalize frontmatter
    python3 << PYEOF
import re
import sys
from datetime import date

input_path = """$CLIP_FILE"""
output_path = """$OUTPUT_FILE"""
today = "$TODAY"

try:
    with open(input_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Parse existing frontmatter
    frontmatter = {}
    body = content

    fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if fm_match:
        fm_text = fm_match.group(1)
        body = fm_match.group(2)

        # Simple YAML-like parsing for common fields
        current_key = None
        for line in fm_text.split('\n'):
            stripped = line.strip()
            # Continuation list item (e.g. "  - value")
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
                # Handle Obsidian wikilink format [[@name]]
                value = re.sub(r'\[\[(@?[^\]]+)\]\]', r'\1', value)
                current_key = key
                if value and value != '(null)':
                    frontmatter[key] = value
                elif not value:
                    # Key with no inline value; list items may follow
                    frontmatter.setdefault(key, '')
            else:
                current_key = None

    # Map Obsidian clipper fields to our standard format
    title = frontmatter.get('title', '$BASENAME')
    source = frontmatter.get('source', frontmatter.get('url', frontmatter.get('link', '')))
    author = frontmatter.get('author', frontmatter.get('authors', frontmatter.get('creator', '')))
    # Handle author lists
    if isinstance(author, str):
        author = re.sub(r'^\s*-\s*', '', author)

    published = frontmatter.get('published', frontmatter.get('date_published',
                frontmatter.get('date', frontmatter.get('created', ''))))
    description = frontmatter.get('description', frontmatter.get('excerpt', ''))

    # Detect type from source URL
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

    # Collect original tags
    tags_raw = frontmatter.get('tags', '')
    tags = ['clipping']
    if tags_raw:
        # Handle both comma-separated and YAML list formats
        for t in re.split(r'[,\n]', tags_raw):
            t = t.strip().strip('-').strip().strip('"').strip("'")
            if t and t not in tags:
                tags.append(t)

    # Write normalized output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: "{title}"\n')
        f.write(f'source: "{source}"\n')
        f.write(f'author: "{author}"\n')
        f.write(f'date_published: {published}\n')
        f.write(f'date_ingested: {today}\n')
        if description:
            f.write(f'description: "{description[:200]}"\n')
        f.write(f'tags: [{", ".join(tags)}]\n')
        f.write(f'type: {content_type}\n')
        f.write(f'status: raw\n')
        f.write(f'imported_from: clippings\n')
        f.write('---\n\n')
        f.write(body)

    print(f"  OK: {output_path}")

except Exception as e:
    print(f"  ERROR: {e}", file=sys.stderr)
    sys.exit(1)
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
