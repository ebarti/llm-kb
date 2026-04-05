#!/bin/bash
# pdf.sh — Extract text from a PDF file or URL
# Usage: ./tools/ingest/pdf.sh /path/to/paper.pdf
# Usage: ./tools/ingest/pdf.sh https://arxiv.org/pdf/2401.00001
#
# Extraction approaches (in order):
#   1. pdftotext (poppler, if installed)
#   2. python3 with pdfminer.six or PyPDF2
#   3. macOS textutil (limited PDF support)
#   4. strings fallback

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
RAW_DIR="$PROJECT_DIR/raw"
mkdir -p "$RAW_DIR"

INPUT="${1:-}"
if [ -z "$INPUT" ]; then
    echo "Usage: pdf.sh <pdf-path-or-url>"
    echo "Examples:"
    echo "  ./tools/ingest/pdf.sh /path/to/paper.pdf"
    echo "  ./tools/ingest/pdf.sh https://arxiv.org/pdf/2401.00001"
    exit 1
fi

TODAY=$(date +%Y-%m-%d)
TMPDIR=$(mktemp -d /tmp/pdf-ingest-XXXXXX)
trap "rm -rf '$TMPDIR'" EXIT

PDF_PATH=""
SOURCE_URL=""
ORIGINAL_NAME=""

# --- Determine if input is URL or local file ---
if echo "$INPUT" | grep -qE '^https?://'; then
    SOURCE_URL="$INPUT"
    echo "Downloading PDF from: $INPUT"
    PDF_PATH="$TMPDIR/download.pdf"
    HTTP_CODE=$(curl -sL --max-time 120 -o "$PDF_PATH" -w '%{http_code}' \
        --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
        "$INPUT" 2>/dev/null || echo "000")
    if [ "$HTTP_CODE" != "200" ] || [ ! -s "$PDF_PATH" ]; then
        echo "ERROR: Failed to download PDF (HTTP $HTTP_CODE)"
        exit 1
    fi
    ORIGINAL_NAME=$(basename "$INPUT" | sed 's/[?#].*//' | sed 's/\.pdf$//')
    echo "Downloaded: $(wc -c < "$PDF_PATH" | tr -d ' ') bytes"
else
    if [ ! -f "$INPUT" ]; then
        echo "ERROR: File not found: $INPUT"
        exit 1
    fi
    PDF_PATH="$INPUT"
    SOURCE_URL="file://$INPUT"
    ORIGINAL_NAME=$(basename "$INPUT" | sed 's/\.pdf$//')
fi

# --- Extract metadata using mdls (macOS) ---
TITLE=""
AUTHOR=""
PAGE_COUNT=""
CREATION_DATE=""

if command -v mdls &>/dev/null && [ -f "$PDF_PATH" ]; then
    TITLE=$(mdls -name kMDItemTitle "$PDF_PATH" 2>/dev/null | sed 's/kMDItemTitle *= *//; s/^"//; s/"$//' | grep -v '(null)' || true)
    AUTHOR=$(mdls -name kMDItemAuthors "$PDF_PATH" 2>/dev/null | grep '"' | head -1 | sed 's/.*"//; s/".*//' | grep -v '(null)' || true)
    PAGE_COUNT=$(mdls -name kMDItemNumberOfPages "$PDF_PATH" 2>/dev/null | sed 's/kMDItemNumberOfPages *= *//' | grep -v '(null)' || true)
    CREATION_DATE=$(mdls -name kMDItemContentCreationDate "$PDF_PATH" 2>/dev/null | sed 's/kMDItemContentCreationDate *= *//' | grep -v '(null)' | cut -c1-10 || true)
fi

# Also try python to get PDF metadata
if [ -z "$TITLE" ] && command -v python3 &>/dev/null; then
    PDF_META=$(python3 -c "
import sys
try:
    from PyPDF2 import PdfReader
    reader = PdfReader('$PDF_PATH')
    info = reader.metadata
    if info:
        title = info.get('/Title', '') or ''
        author = info.get('/Author', '') or ''
        print(f'TITLE={title}')
        print(f'AUTHOR={author}')
        print(f'PAGES={len(reader.pages)}')
except:
    pass
try:
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdfdocument import PDFDocument
    with open('$PDF_PATH', 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        info = doc.info[0] if doc.info else {}
        title = info.get('Title', b'')
        author = info.get('Author', b'')
        if isinstance(title, bytes): title = title.decode('utf-8', errors='ignore')
        if isinstance(author, bytes): author = author.decode('utf-8', errors='ignore')
        if title: print(f'TITLE={title}')
        if author: print(f'AUTHOR={author}')
except:
    pass
" 2>/dev/null || true)
    if [ -n "$PDF_META" ]; then
        META_TITLE=$(echo "$PDF_META" | grep '^TITLE=' | head -1 | sed 's/^TITLE=//')
        META_AUTHOR=$(echo "$PDF_META" | grep '^AUTHOR=' | head -1 | sed 's/^AUTHOR=//')
        META_PAGES=$(echo "$PDF_META" | grep '^PAGES=' | head -1 | sed 's/^PAGES=//')
        [ -z "$TITLE" ] && TITLE="$META_TITLE"
        [ -z "$AUTHOR" ] && AUTHOR="$META_AUTHOR"
        [ -z "$PAGE_COUNT" ] && PAGE_COUNT="$META_PAGES"
    fi
fi

TITLE="${TITLE:-$ORIGINAL_NAME}"
echo "Title: $TITLE"
echo "Author: ${AUTHOR:-unknown}"

# --- Extract text content ---
TEXT=""
METHOD=""

# Method 1: pdftotext (poppler)
if [ -z "$TEXT" ] && command -v pdftotext &>/dev/null; then
    echo "Trying pdftotext..."
    TEXT=$(pdftotext -layout "$PDF_PATH" - 2>/dev/null || true)
    if [ -n "$TEXT" ]; then
        METHOD="pdftotext"
        echo "Extracted via pdftotext (${#TEXT} chars)"
    fi
fi

# Method 2: python3 pdfminer or PyPDF2
if [ -z "$TEXT" ] && command -v python3 &>/dev/null; then
    echo "Trying python3 PDF extraction..."
    TEXT=$(python3 -c "
import sys
text = ''
try:
    from pdfminer.high_level import extract_text
    text = extract_text('$PDF_PATH')
except ImportError:
    pass
if not text:
    try:
        from PyPDF2 import PdfReader
        reader = PdfReader('$PDF_PATH')
        parts = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                parts.append(t)
        text = '\n\n'.join(parts)
    except ImportError:
        pass
if text:
    print(text)
" 2>/dev/null || true)
    if [ -n "$TEXT" ]; then
        METHOD="python3"
        echo "Extracted via python3 (${#TEXT} chars)"
    fi
fi

# Method 3: macOS textutil
if [ -z "$TEXT" ] && command -v textutil &>/dev/null; then
    echo "Trying textutil..."
    TEMP_TXT="$TMPDIR/output.txt"
    if textutil -convert txt -output "$TEMP_TXT" "$PDF_PATH" 2>/dev/null; then
        TEXT=$(cat "$TEMP_TXT" 2>/dev/null || true)
        if [ -n "$TEXT" ]; then
            METHOD="textutil"
            echo "Extracted via textutil (${#TEXT} chars)"
        fi
    fi
fi

# Method 4: strings fallback
if [ -z "$TEXT" ]; then
    echo "Trying strings fallback..."
    TEXT=$(strings "$PDF_PATH" | head -5000)
    if [ -n "$TEXT" ]; then
        METHOD="strings (low quality)"
        echo "WARNING: Using strings fallback - quality will be low"
    fi
fi

if [ -z "$TEXT" ]; then
    echo "ERROR: Could not extract any text from PDF"
    exit 1
fi

# --- Generate output filename ---
SAFE_TITLE=$(echo "$TITLE" | \
    tr '[:upper:]' '[:lower:]' | \
    sed 's/[^a-z0-9 ]//g' | \
    sed 's/  \+/ /g; s/^ //; s/ $//' | \
    tr ' ' '-' | \
    cut -c1-80)
OUTPUT_FILE="$RAW_DIR/pdf-${SAFE_TITLE:-$ORIGINAL_NAME}.md"

# --- Write output ---
cat > "$OUTPUT_FILE" << HEREDOC
---
title: "$(echo "$TITLE" | sed 's/"/\\"/g')"
source: "$SOURCE_URL"
author: "$(echo "${AUTHOR:-}" | sed 's/"/\\"/g')"
date_published: ${CREATION_DATE:-}
date_ingested: $TODAY
pages: ${PAGE_COUNT:-}
tags: [pdf, paper]
type: pdf
status: raw
extraction_method: $METHOD
---

# $TITLE

**Author:** ${AUTHOR:-Unknown}
**Pages:** ${PAGE_COUNT:-Unknown}
**Source:** $SOURCE_URL

## Content

$TEXT
HEREDOC

echo ""
echo "Saved to: $OUTPUT_FILE"
echo "File size: $(wc -c < "$OUTPUT_FILE" | tr -d ' ') bytes"
echo "Extraction method: $METHOD"
