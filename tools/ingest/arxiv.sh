#!/bin/bash
# arxiv.sh — Fetch an arXiv paper: metadata, abstract, and full text
# Usage: ./tools/ingest/arxiv.sh 2401.00001
# Usage: ./tools/ingest/arxiv.sh https://arxiv.org/abs/2401.00001
#
# Uses the arXiv API for metadata, then downloads PDF and extracts text
# via the pdf.sh companion script.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
RAW_DIR="$PROJECT_DIR/raw"
mkdir -p "$RAW_DIR"

INPUT="${1:-}"
if [ -z "$INPUT" ]; then
    echo "Usage: arxiv.sh <arxiv-id-or-url>"
    echo "Examples:"
    echo "  ./tools/ingest/arxiv.sh 2401.00001"
    echo "  ./tools/ingest/arxiv.sh https://arxiv.org/abs/2401.00001"
    exit 1
fi

TODAY=$(date +%Y-%m-%d)
TMPDIR=$(mktemp -d /tmp/arxiv-ingest-XXXXXX)
trap "rm -rf '$TMPDIR'" EXIT

# --- Extract arXiv ID ---
ARXIV_ID=""
# Strip version suffix for API query but keep for download
if echo "$INPUT" | grep -qE 'arxiv\.org/(abs|pdf)/'; then
    ARXIV_ID=$(echo "$INPUT" | grep -oE '(abs|pdf)/[0-9]+\.[0-9]+(v[0-9]+)?' | sed 's|^(abs\|pdf)/||; s|^abs/||; s|^pdf/||')
fi
if [ -z "$ARXIV_ID" ]; then
    # Assume raw ID was given
    ARXIV_ID=$(echo "$INPUT" | sed 's|\.pdf$||')
fi

if [ -z "$ARXIV_ID" ]; then
    echo "ERROR: Could not parse arXiv ID from: $INPUT"
    exit 1
fi

echo "arXiv ID: $ARXIV_ID"

# --- Fetch metadata from arXiv API ---
echo "Fetching metadata from arXiv API..."
API_URL="https://export.arxiv.org/api/query?id_list=${ARXIV_ID}"
API_XML=$(curl -sL --max-time 30 "$API_URL" 2>/dev/null || true)

if [ -z "$API_XML" ]; then
    echo "ERROR: Failed to fetch arXiv API response"
    exit 1
fi

# Parse XML with python3 for reliability
METADATA=$(python3 << 'PYEOF'
import sys
import xml.etree.ElementTree as ET

xml_text = sys.stdin.read()
ns = {'atom': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

try:
    root = ET.fromstring(xml_text)
    entry = root.find('atom:entry', ns)
    if entry is None:
        print("ERROR=No entry found")
        sys.exit(0)

    title = entry.find('atom:title', ns)
    title = ' '.join(title.text.strip().split()) if title is not None and title.text else ''

    summary = entry.find('atom:summary', ns)
    summary = summary.text.strip() if summary is not None and summary.text else ''

    published = entry.find('atom:published', ns)
    published = published.text.strip()[:10] if published is not None and published.text else ''

    updated = entry.find('atom:updated', ns)
    updated = updated.text.strip()[:10] if updated is not None and updated.text else ''

    authors = []
    for author in entry.findall('atom:author', ns):
        name = author.find('atom:name', ns)
        if name is not None and name.text:
            authors.append(name.text.strip())

    categories = []
    for cat in entry.findall('atom:category', ns):
        term = cat.get('term', '')
        if term:
            categories.append(term)

    # Primary category
    primary = entry.find('arxiv:primary_category', ns)
    primary_cat = primary.get('term', '') if primary is not None else ''

    # DOI and journal ref
    doi = entry.find('arxiv:doi', ns)
    doi = doi.text.strip() if doi is not None and doi.text else ''

    journal = entry.find('arxiv:journal_ref', ns)
    journal = journal.text.strip() if journal is not None and journal.text else ''

    # Comment (often has page count)
    comment = entry.find('arxiv:comment', ns)
    comment = comment.text.strip() if comment is not None and comment.text else ''

    print(f"TITLE={title}")
    print(f"AUTHORS={', '.join(authors)}")
    print(f"PUBLISHED={published}")
    print(f"UPDATED={updated}")
    print(f"CATEGORIES={', '.join(categories)}")
    print(f"PRIMARY_CATEGORY={primary_cat}")
    print(f"DOI={doi}")
    print(f"JOURNAL={journal}")
    print(f"COMMENT={comment}")
    print(f"ABSTRACT_START")
    print(summary)
    print(f"ABSTRACT_END")
except Exception as e:
    print(f"ERROR={e}")
PYEOF
) <<< "$API_XML"

# Parse the metadata output
TITLE=$(echo "$METADATA" | grep '^TITLE=' | head -1 | sed 's/^TITLE=//')
AUTHORS=$(echo "$METADATA" | grep '^AUTHORS=' | head -1 | sed 's/^AUTHORS=//')
PUBLISHED=$(echo "$METADATA" | grep '^PUBLISHED=' | head -1 | sed 's/^PUBLISHED=//')
UPDATED=$(echo "$METADATA" | grep '^UPDATED=' | head -1 | sed 's/^UPDATED=//')
CATEGORIES=$(echo "$METADATA" | grep '^CATEGORIES=' | head -1 | sed 's/^CATEGORIES=//')
PRIMARY_CAT=$(echo "$METADATA" | grep '^PRIMARY_CATEGORY=' | head -1 | sed 's/^PRIMARY_CATEGORY=//')
DOI=$(echo "$METADATA" | grep '^DOI=' | head -1 | sed 's/^DOI=//')
JOURNAL=$(echo "$METADATA" | grep '^JOURNAL=' | head -1 | sed 's/^JOURNAL=//')
COMMENT=$(echo "$METADATA" | grep '^COMMENT=' | head -1 | sed 's/^COMMENT=//')
ABSTRACT=$(echo "$METADATA" | sed -n '/^ABSTRACT_START$/,/^ABSTRACT_END$/p' | sed '1d;$d')

if echo "$METADATA" | grep -q '^ERROR='; then
    echo "WARNING: API parse issue: $(echo "$METADATA" | grep '^ERROR=')"
fi

echo "Title: $TITLE"
echo "Authors: $AUTHORS"
echo "Categories: $CATEGORIES"

# --- Download and extract PDF ---
PDF_URL="https://arxiv.org/pdf/${ARXIV_ID}.pdf"
echo "Downloading PDF from: $PDF_URL"
PDF_PATH="$TMPDIR/paper.pdf"

HTTP_CODE=$(curl -sL --max-time 120 -o "$PDF_PATH" -w '%{http_code}' \
    --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
    "$PDF_URL" 2>/dev/null || echo "000")

FULL_TEXT=""
EXTRACTION_METHOD=""

if [ "$HTTP_CODE" = "200" ] && [ -s "$PDF_PATH" ]; then
    echo "Downloaded PDF: $(wc -c < "$PDF_PATH" | tr -d ' ') bytes"

    # Extract text using same methods as pdf.sh
    if command -v pdftotext &>/dev/null; then
        FULL_TEXT=$(pdftotext -layout "$PDF_PATH" - 2>/dev/null || true)
        [ -n "$FULL_TEXT" ] && EXTRACTION_METHOD="pdftotext"
    fi

    if [ -z "$FULL_TEXT" ] && command -v python3 &>/dev/null; then
        FULL_TEXT=$(python3 -c "
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
            if t: parts.append(t)
        text = '\n\n'.join(parts)
    except ImportError:
        pass
if text:
    print(text)
" 2>/dev/null || true)
        [ -n "$FULL_TEXT" ] && EXTRACTION_METHOD="python3"
    fi

    if [ -z "$FULL_TEXT" ]; then
        FULL_TEXT="[PDF text extraction failed - install pdftotext or pdfminer.six]"
        EXTRACTION_METHOD="none"
    else
        echo "Extracted text: ${#FULL_TEXT} chars via $EXTRACTION_METHOD"
    fi
else
    echo "WARNING: Could not download PDF (HTTP $HTTP_CODE)"
    FULL_TEXT="[PDF download failed]"
    EXTRACTION_METHOD="none"
fi

# --- Generate output filename ---
SAFE_TITLE=$(echo "$TITLE" | \
    tr '[:upper:]' '[:lower:]' | \
    sed 's/[^a-z0-9 ]//g' | \
    sed 's/  \+/ /g; s/^ //; s/ $//' | \
    tr ' ' '-' | \
    cut -c1-80)
SLUG="arxiv-${SAFE_TITLE:-$ARXIV_ID}"

# Format authors as YAML list
AUTHORS_YAML=""
IFS=',' read -ra AUTH_ARRAY <<< "$AUTHORS"
for auth in "${AUTH_ARRAY[@]}"; do
    auth=$(echo "$auth" | sed 's/^ *//')
    AUTHORS_YAML="${AUTHORS_YAML}  - \"${auth}\"
"
done

# Format categories as YAML list
CAT_YAML=""
IFS=',' read -ra CAT_ARRAY <<< "$CATEGORIES"
for cat in "${CAT_ARRAY[@]}"; do
    cat=$(echo "$cat" | sed 's/^ *//')
    CAT_YAML="${CAT_YAML}  - \"${cat}\"
"
done

# --- Compose clean.md ---
CLEAN_FILE=$(mktemp /tmp/arxiv-clean-XXXXXX.md)
cat > "$CLEAN_FILE" << HEREDOC
---
title: "$(echo "$TITLE" | sed 's/"/\\"/g')"
source: "https://arxiv.org/abs/${ARXIV_ID}"
arxiv_id: "$ARXIV_ID"
authors:
${AUTHORS_YAML}date_published: ${PUBLISHED:-}
date_updated: ${UPDATED:-}
date_ingested: $TODAY
categories:
${CAT_YAML}primary_category: "$PRIMARY_CAT"
doi: "${DOI:-}"
journal_ref: "${JOURNAL:-}"
comment: "$(echo "${COMMENT:-}" | sed 's/"/\\"/g')"
tags: [arxiv, paper, research]
type: arxiv
status: raw
extraction_method: $EXTRACTION_METHOD
---

# $TITLE

**Authors:** $AUTHORS
**Published:** ${PUBLISHED:-Unknown} | **Updated:** ${UPDATED:-Unknown}
**arXiv:** [${ARXIV_ID}](https://arxiv.org/abs/${ARXIV_ID}) | **PDF:** [link](https://arxiv.org/pdf/${ARXIV_ID}.pdf)
**Categories:** $CATEGORIES
${DOI:+**DOI:** $DOI}
${JOURNAL:+**Journal:** $JOURNAL}

## Abstract

$ABSTRACT

## Full Text

$FULL_TEXT
HEREDOC

# --- Persist PDF bytes if we have them ---
RAW_ARGS=()
CONTENT_TYPE="pdf"
if [ -s "$PDF_PATH" ]; then
    RAW_ARGS+=(--raw-path "$PDF_PATH" --raw-ext "pdf")
else
    CONTENT_TYPE=""
fi

EXTRA_META=$(python3 - <<PYEOF
import json
print(json.dumps({
    "title": """$TITLE""".replace('"', r'\"'),
    "arxiv_id": "$ARXIV_ID",
    "authors": """$AUTHORS""".replace('"', r'\"'),
    "date_published": "${PUBLISHED:-}",
    "primary_category": "$PRIMARY_CAT",
    "extraction_method": "$EXTRACTION_METHOD",
    "api_url": "$API_URL",
}))
PYEOF
)

python3 "$PROJECT_DIR/tools/ingest/_raw_writer.py" \
    --slug "$SLUG" \
    --url "https://arxiv.org/abs/${ARXIV_ID}" \
    --fetcher arxiv \
    --clean-path "$CLEAN_FILE" \
    --content-type "$CONTENT_TYPE" \
    --extra-meta-json "$EXTRA_META" \
    "${RAW_ARGS[@]}" >/dev/null

rm -f "$CLEAN_FILE"

echo ""
echo "Saved to: $RAW_DIR/$SLUG/"
