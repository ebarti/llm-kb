#!/usr/bin/env bash
# Generate all wiki visualizations into output/images/
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$BASE_DIR/output/images"

mkdir -p "$OUTPUT_DIR"

echo "=== Wiki Visualization Generator ==="
echo "Base: $BASE_DIR"
echo "Output: $OUTPUT_DIR"
echo

echo "[1/5] Knowledge Graph..."
python3 "$SCRIPT_DIR/graph.py"
echo

echo "[2/5] Timeline..."
python3 "$SCRIPT_DIR/timeline.py"
echo

echo "[3/5] Concept Map..."
python3 "$SCRIPT_DIR/concept-map.py"
echo

echo "[4/5] Statistics Dashboard..."
python3 "$SCRIPT_DIR/stats.py" --html
echo

echo "[5/5] Obsidian Canvas (master)..."
python3 "$SCRIPT_DIR/canvas.py" --all
echo

echo "=== Done ==="
echo "Generated files:"
ls -la "$OUTPUT_DIR/"*.html "$OUTPUT_DIR/"*.svg 2>/dev/null || true
echo
if [ -f "$BASE_DIR/wiki/master-canvas.canvas" ]; then
    echo "Canvas: $BASE_DIR/wiki/master-canvas.canvas"
fi
