#!/bin/bash
# search.sh — Full-text search over the wiki
# Usage: ./tools/search.sh <query> [directory]
#
# Searches wiki/ by default, can also search raw/
# Returns ranked results with context snippets

set -euo pipefail

QUERY="$1"
SEARCH_DIR="${2:-wiki}"

if [ -z "$QUERY" ]; then
    echo "Usage: search.sh <query> [directory]"
    echo "  directory: wiki (default), raw, or all"
    exit 1
fi

BASE_DIR="$(cd "$(dirname "$0")/.." && pwd)"

case "$SEARCH_DIR" in
    all)
        DIRS=("$BASE_DIR/wiki" "$BASE_DIR/raw" "$BASE_DIR/output")
        ;;
    wiki)
        DIRS=("$BASE_DIR/wiki")
        ;;
    raw)
        DIRS=("$BASE_DIR/raw")
        ;;
    output)
        DIRS=("$BASE_DIR/output")
        ;;
    *)
        DIRS=("$BASE_DIR/$SEARCH_DIR")
        ;;
esac

# Search with context, case-insensitive
echo "=== Search results for: '$QUERY' ==="
echo ""

TOTAL_MATCHES=0

for dir in "${DIRS[@]}"; do
    if [ -d "$dir" ]; then
        # Use grep for search (available everywhere)
        RESULTS=$(grep -ril --include="*.md" "$QUERY" "$dir" 2>/dev/null || true)

        if [ -n "$RESULTS" ]; then
            while IFS= read -r file; do
                REL_PATH="${file#$BASE_DIR/}"
                MATCH_COUNT=$(grep -ci "$QUERY" "$file" 2>/dev/null || echo "0")
                TOTAL_MATCHES=$((TOTAL_MATCHES + MATCH_COUNT))

                # Extract title from frontmatter
                TITLE=$(grep -m1 '^title:' "$file" 2>/dev/null | sed 's/^title:[[:space:]]*//' | sed 's/^"//;s/"$//' || echo "")

                echo "--- $REL_PATH ($MATCH_COUNT matches) ---"
                if [ -n "$TITLE" ]; then
                    echo "  Title: $TITLE"
                fi

                # Show context around matches
                grep -ni -C 1 "$QUERY" "$file" 2>/dev/null | head -15
                echo ""
            done <<< "$RESULTS"
        fi
    fi
done

echo "=== Total: $TOTAL_MATCHES matches ==="
