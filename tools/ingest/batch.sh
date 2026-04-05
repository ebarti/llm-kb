#!/bin/bash
# batch.sh — Batch import URLs from a file
# Usage: ./tools/ingest/batch.sh urls.txt
#
# Each line in the input file should contain one URL.
# Lines starting with # are treated as comments and skipped.
# Detects URL type and routes to the appropriate ingest tool.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

INPUT_FILE="${1:-}"
if [ -z "$INPUT_FILE" ]; then
    echo "Usage: batch.sh <urls-file>"
    echo "Example: ./tools/ingest/batch.sh urls.txt"
    echo ""
    echo "File format: one URL per line. Lines starting with # are comments."
    exit 1
fi

# Resolve relative paths
if [[ "$INPUT_FILE" != /* ]]; then
    INPUT_FILE="$(pwd)/$INPUT_FILE"
fi

if [ ! -f "$INPUT_FILE" ]; then
    echo "ERROR: File not found: $INPUT_FILE"
    exit 1
fi

# Count non-empty, non-comment lines
TOTAL=$(grep -cvE '^\s*(#|$)' "$INPUT_FILE" || echo "0")
echo "=== Batch Ingest ==="
echo "Input file: $INPUT_FILE"
echo "URLs to process: $TOTAL"
echo ""

SUCCESS=0
FAILED=0
SKIPPED=0
LINE_NUM=0

while IFS= read -r LINE || [ -n "$LINE" ]; do
    LINE_NUM=$((LINE_NUM + 1))

    # Strip whitespace
    LINE=$(echo "$LINE" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')

    # Skip empty lines and comments
    if [ -z "$LINE" ] || echo "$LINE" | grep -q '^#'; then
        continue
    fi

    URL="$LINE"
    CURRENT=$((SUCCESS + FAILED + 1))
    echo "--- [$CURRENT/$TOTAL] $URL ---"

    # Detect URL type and route to appropriate tool
    TOOL=""
    if echo "$URL" | grep -qiE '(youtube\.com|youtu\.be)/'; then
        TOOL="youtube"
    elif echo "$URL" | grep -qiE 'arxiv\.org/(abs|pdf)/'; then
        TOOL="arxiv"
    elif echo "$URL" | grep -qiE '^[0-9]{4}\.[0-9]+'; then
        TOOL="arxiv"
    elif echo "$URL" | grep -qiE 'github\.com/[^/]+/[^/]+'; then
        TOOL="github"
    elif echo "$URL" | grep -qiE '(twitter\.com|x\.com)/[^/]+/status/'; then
        TOOL="tweet"
    elif echo "$URL" | grep -qiE '\.pdf($|\?)'; then
        TOOL="pdf"
    else
        TOOL="web"
    fi

    echo "  Detected type: $TOOL"

    # Execute the appropriate tool
    RESULT=0
    case "$TOOL" in
        youtube)
            "$SCRIPT_DIR/youtube.sh" "$URL" 2>&1 | sed 's/^/  /' || RESULT=1
            ;;
        arxiv)
            "$SCRIPT_DIR/arxiv.sh" "$URL" 2>&1 | sed 's/^/  /' || RESULT=1
            ;;
        github)
            "$SCRIPT_DIR/github.sh" "$URL" 2>&1 | sed 's/^/  /' || RESULT=1
            ;;
        tweet)
            "$SCRIPT_DIR/tweet.sh" "$URL" 2>&1 | sed 's/^/  /' || RESULT=1
            ;;
        pdf)
            "$SCRIPT_DIR/pdf.sh" "$URL" 2>&1 | sed 's/^/  /' || RESULT=1
            ;;
        web)
            # Fall back to the generic fetch-url.sh
            if [ -f "$PROJECT_DIR/tools/fetch-url.sh" ]; then
                "$PROJECT_DIR/tools/fetch-url.sh" "$URL" 2>&1 | sed 's/^/  /' || RESULT=1
            else
                echo "  WARNING: No handler for generic web URLs (fetch-url.sh not found)"
                RESULT=1
            fi
            ;;
    esac

    if [ "$RESULT" -eq 0 ]; then
        SUCCESS=$((SUCCESS + 1))
        echo "  OK"
    else
        FAILED=$((FAILED + 1))
        echo "  FAILED"
    fi
    echo ""

done < "$INPUT_FILE"

echo "=== Batch Complete ==="
echo "Total:   $TOTAL"
echo "Success: $SUCCESS"
echo "Failed:  $FAILED"

if [ "$FAILED" -gt 0 ]; then
    exit 1
fi
