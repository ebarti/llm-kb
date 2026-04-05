#!/usr/bin/env bash
# Export all formats from the LLM knowledge base wiki.
# Usage: bash tools/export/export-all.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$ROOT"

echo "========================================"
echo "  LLM Knowledge Base - Export All"
echo "========================================"
echo ""

# Ensure output directory exists
mkdir -p output

# 1. Static site
echo "[1/4] Building static site..."
python3 tools/export/build-site.py
echo ""

# 2. Print-ready HTML (PDF)
echo "[2/4] Building print-ready HTML..."
python3 tools/export/build-pdf.py
echo ""

# 3. EPUB
echo "[3/4] Building EPUB..."
python3 tools/export/build-epub.py
echo ""

# 4. Markdown bundle
echo "[4/4] Building markdown bundle..."
python3 tools/export/bundle.py
echo ""

# Report
echo "========================================"
echo "  Export Complete - File Sizes"
echo "========================================"
echo ""

report_size() {
    local path="$1"
    local label="$2"
    if [ -e "$path" ]; then
        local size
        size=$(du -sh "$path" 2>/dev/null | cut -f1)
        printf "  %-30s %s\n" "$label" "$size"
    else
        printf "  %-30s %s\n" "$label" "(not found)"
    fi
}

report_size "output/site/"           "Static site (directory)"
report_size "output/wiki-export.html" "Print-ready HTML"
report_size "output/wiki.epub"        "EPUB ebook"
report_size "output/wiki-bundle.md"   "Markdown bundle"

echo ""

# Count files in site
if [ -d "output/site" ]; then
    count=$(find output/site -name "*.html" | wc -l | tr -d ' ')
    echo "  Static site pages: $count"
fi

echo ""
echo "Done!"
