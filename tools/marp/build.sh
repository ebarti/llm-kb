#!/usr/bin/env bash
# ==========================================================================
# Marp Build Script — LLM Knowledge Base
# ==========================================================================
#
# Converts Marp markdown slides to HTML (and optionally PDF) using marp-cli.
#
# Usage:
#   ./tools/marp/build.sh output/slides/              # Build all .md files in directory
#   ./tools/marp/build.sh output/slides/topic.md       # Build a single file
#   ./tools/marp/build.sh output/slides/ --pdf         # Build as PDF (requires Chrome/Chromium)
#   ./tools/marp/build.sh --watch output/slides/       # Watch mode for live editing
#
# Requirements:
#   - marp-cli: npm install -g @marp-team/marp-cli
#   - For PDF: Chrome or Chromium must be installed
#
# ==========================================================================

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Resolve paths relative to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
THEME_PATH="$SCRIPT_DIR/kb-theme.css"

# Defaults
FORMAT="html"
WATCH_MODE=false
TARGET=""

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --pdf)
      FORMAT="pdf"
      shift
      ;;
    --pptx)
      FORMAT="pptx"
      shift
      ;;
    --watch|-w)
      WATCH_MODE=true
      shift
      ;;
    --help|-h)
      echo "Usage: $0 [OPTIONS] <path>"
      echo ""
      echo "Arguments:"
      echo "  <path>       A .md file or directory containing .md files"
      echo ""
      echo "Options:"
      echo "  --pdf        Output PDF instead of HTML (requires Chrome)"
      echo "  --pptx       Output PPTX instead of HTML"
      echo "  --watch, -w  Watch for changes and rebuild automatically"
      echo "  --help, -h   Show this help message"
      echo ""
      echo "Examples:"
      echo "  $0 output/slides/                  # Build all slides to HTML"
      echo "  $0 output/slides/topic.md          # Build single file"
      echo "  $0 output/slides/ --pdf            # Build all as PDF"
      echo "  $0 --watch output/slides/topic.md  # Live rebuild on save"
      exit 0
      ;;
    *)
      TARGET="$1"
      shift
      ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo -e "${RED}Error: No target path specified.${NC}"
  echo "Usage: $0 [OPTIONS] <path>"
  exit 1
fi

# Resolve target to absolute path if relative
if [[ ! "$TARGET" = /* ]]; then
  TARGET="$PROJECT_ROOT/$TARGET"
fi

# Check if theme file exists
if [[ ! -f "$THEME_PATH" ]]; then
  echo -e "${RED}Error: Theme file not found at $THEME_PATH${NC}"
  exit 1
fi

# Check if marp-cli is available
if command -v marp &> /dev/null; then
  MARP_CMD="marp"
elif command -v npx &> /dev/null; then
  # Try npx as fallback
  echo -e "${YELLOW}marp-cli not found globally, trying npx...${NC}"
  MARP_CMD="npx @marp-team/marp-cli"
else
  echo -e "${YELLOW}===========================================================${NC}"
  echo -e "${YELLOW}  marp-cli is not installed.${NC}"
  echo -e "${YELLOW}===========================================================${NC}"
  echo ""
  echo "The Marp markdown files are valid and can be viewed with:"
  echo ""
  echo "  1. Obsidian + Marp Slides plugin (recommended)"
  echo "     Install from: Community Plugins > Marp Slides"
  echo ""
  echo "  2. VS Code + Marp for VS Code extension"
  echo "     Install from: Extensions marketplace"
  echo ""
  echo "  3. Install marp-cli for command-line builds:"
  echo "     npm install -g @marp-team/marp-cli"
  echo ""
  echo -e "${CYAN}Slide files ready for viewing:${NC}"
  if [[ -d "$TARGET" ]]; then
    find "$TARGET" -name "*.md" -type f | sort | while read -r f; do
      echo "  - $f"
    done
  else
    echo "  - $TARGET"
  fi
  exit 0
fi

# Build function for a single file
build_file() {
  local input_file="$1"
  local filename
  filename="$(basename "$input_file" .md)"
  local output_dir
  output_dir="$(dirname "$input_file")"
  local output_file="$output_dir/${filename}.${FORMAT}"

  echo -e "${CYAN}Building:${NC} $(basename "$input_file") -> ${filename}.${FORMAT}"

  $MARP_CMD \
    --theme "$THEME_PATH" \
    --allow-local-files \
    --${FORMAT} \
    --output "$output_file" \
    "$input_file"

  echo -e "${GREEN}  Done:${NC} $output_file"
}

# Main execution
echo -e "${GREEN}===========================================================${NC}"
echo -e "${GREEN}  LLM Knowledge Base — Marp Slide Builder${NC}"
echo -e "${GREEN}===========================================================${NC}"
echo -e "  Theme:  $THEME_PATH"
echo -e "  Format: $FORMAT"
echo -e "  Target: $TARGET"
echo ""

if [[ "$WATCH_MODE" = true ]]; then
  if [[ -d "$TARGET" ]]; then
    echo -e "${CYAN}Watching directory for changes...${NC}"
    $MARP_CMD \
      --theme "$THEME_PATH" \
      --allow-local-files \
      --${FORMAT} \
      --watch \
      --input-dir "$TARGET"
  else
    echo -e "${CYAN}Watching file for changes...${NC}"
    $MARP_CMD \
      --theme "$THEME_PATH" \
      --allow-local-files \
      --${FORMAT} \
      --watch \
      "$TARGET"
  fi
elif [[ -d "$TARGET" ]]; then
  # Build all .md files in directory
  count=0
  while IFS= read -r -d '' file; do
    build_file "$file"
    ((count++))
  done < <(find "$TARGET" -name "*.md" -type f -print0 | sort -z)

  if [[ $count -eq 0 ]]; then
    echo -e "${YELLOW}No .md files found in $TARGET${NC}"
    exit 1
  fi

  echo ""
  echo -e "${GREEN}Built $count slide deck(s) as $FORMAT.${NC}"
elif [[ -f "$TARGET" ]]; then
  build_file "$TARGET"
else
  echo -e "${RED}Error: $TARGET is not a file or directory.${NC}"
  exit 1
fi
