#!/bin/bash
# fetch-url.sh — Fetch a URL and convert to markdown (v2 layout)
# Usage: ./tools/fetch-url.sh <url> [output_name]
#
# Saves the raw HTML as raw/<slug>/raw.html and a cleaned markdown
# as raw/<slug>/clean.md, plus meta.json with provenance.

set -euo pipefail

URL="$1"
OUTPUT_NAME="${2:-}"

if [ -z "$URL" ]; then
    echo "Usage: fetch-url.sh <url> [output_name]"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
RAW_DIR="$PROJECT_DIR/raw"

# Derive a slug from the URL if not provided
if [ -z "$OUTPUT_NAME" ]; then
    OUTPUT_NAME=$(echo "$URL" | sed 's|https\?://||' | sed 's|[^a-zA-Z0-9]|_|g' | sed 's|_\+|_|g' | sed 's|_$||' | cut -c1-80)
fi
SLUG="$OUTPUT_NAME"

mkdir -p "$RAW_DIR/$SLUG"
IMAGES_DIR="$RAW_DIR/$SLUG/images"

# Fetch the page content
echo "Fetching: $URL"

RAW_HTML_FILE="$(mktemp /tmp/fetch-XXXXXX.html)"
trap "rm -f '$RAW_HTML_FILE'" EXIT

HTTP_CODE=$(curl -sL --max-time 30 -o "$RAW_HTML_FILE" -w '%{http_code}' \
    --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
    "$URL" 2>/dev/null || echo "000")

if [ ! -s "$RAW_HTML_FILE" ]; then
    echo "ERROR: Failed to fetch $URL (HTTP $HTTP_CODE)"
    exit 1
fi

RAW_HTML=$(cat "$RAW_HTML_FILE")

# Convert HTML → markdown. Try pandoc → textutil → sed fallback.
CONTENT=""
if command -v pandoc &>/dev/null; then
    CONTENT=$(pandoc -f html -t markdown --wrap=none "$RAW_HTML_FILE" 2>/dev/null || true)
fi
if [ -z "$CONTENT" ] && command -v textutil &>/dev/null; then
    TEMP_TXT=$(mktemp /tmp/fetch-XXXXXX.txt)
    if textutil -convert txt -output "$TEMP_TXT" "$RAW_HTML_FILE" 2>/dev/null; then
        CONTENT=$(cat "$TEMP_TXT")
    fi
    rm -f "$TEMP_TXT"
fi
if [ -z "$CONTENT" ]; then
    CONTENT=$(sed 's/<[^>]*>//g; s/&nbsp;/ /g; s/&amp;/\&/g; s/&lt;/</g; s/&gt;/>/g; s/&quot;/"/g' "$RAW_HTML_FILE" | sed '/^[[:space:]]*$/d')
fi

# Title
TITLE=$(echo "$RAW_HTML" | grep -oi '<title>[^<]*</title>' | head -1 | sed 's/<[^>]*>//g' || echo "$SLUG")

# Download referenced images (best-effort)
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
[ "$IMAGE_COUNT" -eq 0 ] && rmdir "$IMAGES_DIR" 2>/dev/null || true

TODAY=$(date +%Y-%m-%d)

# Compose clean.md
CLEAN_FILE=$(mktemp /tmp/clean-XXXXXX.md)
cat > "$CLEAN_FILE" << HEREDOC
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

# Persist via the shared writer
python3 "$PROJECT_DIR/tools/ingest/_raw_writer.py" \
    --slug "$SLUG" \
    --url "$URL" \
    --fetcher web \
    --clean-path "$CLEAN_FILE" \
    --raw-path "$RAW_HTML_FILE" \
    --raw-ext html \
    --content-type html \
    --extra-meta-json "{\"title\": \"${TITLE//\"/\\\"}\", \"http_code\": \"$HTTP_CODE\"}" \
    >/dev/null

rm -f "$CLEAN_FILE"

echo "Saved to: $RAW_DIR/$SLUG/"
if [ "$IMAGE_COUNT" -gt 0 ]; then
    echo "Downloaded $IMAGE_COUNT images to: $IMAGES_DIR/"
fi
