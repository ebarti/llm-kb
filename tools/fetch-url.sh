#!/bin/bash
# fetch-url.sh — Fetch a URL and convert to markdown
# Usage: ./tools/fetch-url.sh <url> [output_name]
#
# Fetches the raw HTML/text from a URL and saves it to raw/
# Claude then processes this into clean markdown

set -euo pipefail

URL="$1"
OUTPUT_NAME="${2:-}"

if [ -z "$URL" ]; then
    echo "Usage: fetch-url.sh <url> [output_name]"
    exit 1
fi

# Derive a filename from the URL if not provided
if [ -z "$OUTPUT_NAME" ]; then
    OUTPUT_NAME=$(echo "$URL" | sed 's|https\?://||' | sed 's|[^a-zA-Z0-9]|_|g' | sed 's|_\+|_|g' | sed 's|_$||' | cut -c1-80)
fi

RAW_DIR="$(cd "$(dirname "$0")/.." && pwd)/raw"
mkdir -p "$RAW_DIR"

OUTPUT_FILE="$RAW_DIR/${OUTPUT_NAME}.md"
IMAGES_DIR="$RAW_DIR/${OUTPUT_NAME}_images"

# Fetch the page content
echo "Fetching: $URL"

# Try to get clean text content. We use multiple approaches:
# 1. Try readability-cli if available
# 2. Fall back to curl + basic extraction
CONTENT=""

# Use curl to get raw HTML
RAW_HTML=$(curl -sL --max-time 30 --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" "$URL" 2>/dev/null || true)

if [ -z "$RAW_HTML" ]; then
    echo "ERROR: Failed to fetch $URL"
    exit 1
fi

# Try to extract text content using textutil if available (macOS)
# Otherwise just save the raw HTML for Claude to process
TEMP_HTML=$(mktemp /tmp/fetch-XXXXXX.html)
echo "$RAW_HTML" > "$TEMP_HTML"

# Try pandoc first (best HTML→MD conversion)
if command -v pandoc &>/dev/null; then
    CONTENT=$(pandoc -f html -t markdown --wrap=none "$TEMP_HTML" 2>/dev/null || true)
fi

# Fall back to textutil (macOS built-in)
if [ -z "$CONTENT" ] && command -v textutil &>/dev/null; then
    TEMP_TXT=$(mktemp /tmp/fetch-XXXXXX.txt)
    textutil -convert txt -output "$TEMP_TXT" "$TEMP_HTML" 2>/dev/null || true
    if [ -f "$TEMP_TXT" ]; then
        CONTENT=$(cat "$TEMP_TXT")
        rm -f "$TEMP_TXT"
    fi
fi

# Last resort: strip HTML tags with sed
if [ -z "$CONTENT" ]; then
    CONTENT=$(sed 's/<[^>]*>//g; s/&nbsp;/ /g; s/&amp;/\&/g; s/&lt;/</g; s/&gt;/>/g; s/&quot;/"/g' "$TEMP_HTML" | sed '/^[[:space:]]*$/d')
fi

rm -f "$TEMP_HTML"

# Extract page title from HTML
TITLE=$(echo "$RAW_HTML" | grep -oi '<title>[^<]*</title>' | head -1 | sed 's/<[^>]*>//g' || echo "$OUTPUT_NAME")

# Try to download images referenced in the page
mkdir -p "$IMAGES_DIR"
IMAGE_URLS=$(echo "$RAW_HTML" | grep -oP 'src="(https?://[^"]+\.(jpg|jpeg|png|gif|webp|svg))"' | sed 's/src="//;s/"$//' | head -20 || true)

IMAGE_COUNT=0
if [ -n "$IMAGE_URLS" ]; then
    while IFS= read -r img_url; do
        if [ -n "$img_url" ]; then
            img_filename=$(basename "$img_url" | sed 's/[?#].*//' | cut -c1-100)
            if curl -sL --max-time 10 -o "$IMAGES_DIR/$img_filename" "$img_url" 2>/dev/null; then
                IMAGE_COUNT=$((IMAGE_COUNT + 1))
            fi
        fi
    done <<< "$IMAGE_URLS"
fi

# Remove images dir if empty
if [ "$IMAGE_COUNT" -eq 0 ]; then
    rmdir "$IMAGES_DIR" 2>/dev/null || true
fi

# Get current date
TODAY=$(date +%Y-%m-%d)

# Write the output file with frontmatter
cat > "$OUTPUT_FILE" << HEREDOC
---
title: "${TITLE//\"/\\\"}"
source: "$URL"
author: ""
date_published:
date_ingested: $TODAY
tags: []
type: article
status: raw
---

$CONTENT
HEREDOC

echo "Saved to: $OUTPUT_FILE"
if [ "$IMAGE_COUNT" -gt 0 ]; then
    echo "Downloaded $IMAGE_COUNT images to: $IMAGES_DIR/"
fi
echo "File size: $(wc -c < "$OUTPUT_FILE" | tr -d ' ') bytes"
