#!/bin/bash
# history.sh — Wrapper for wiki history tools
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

usage() {
  cat <<'EOF'
Wiki History Tools
==================

Usage:
  ./tools/history/history.sh <command> [args...]

Commands:
  changelog            Generate wiki/Changelog.md from git history
  growth               Generate growth report and SVG chart
  diff [from] [to]     Summarize wiki changes between commits (default: last commit vs HEAD)
  snapshot [save|compare|list] [args...]
                       Save or compare point-in-time wiki snapshots
  article <path>       Show full edit history of a wiki article

Examples:
  ./tools/history/history.sh changelog
  ./tools/history/history.sh growth
  ./tools/history/history.sh diff
  ./tools/history/history.sh diff abc123 def456
  ./tools/history/history.sh snapshot save
  ./tools/history/history.sh snapshot compare 2026-04-05 2026-04-06
  ./tools/history/history.sh snapshot list
  ./tools/history/history.sh article wiki/concepts/llm-knowledge-base.md
EOF
}

if [ $# -lt 1 ]; then
  usage
  exit 1
fi

COMMAND="$1"
shift

case "$COMMAND" in
  changelog)
    python3 "$SCRIPT_DIR/changelog.py" "$@"
    ;;
  growth)
    python3 "$SCRIPT_DIR/growth.py" "$@"
    ;;
  diff)
    python3 "$SCRIPT_DIR/diff-summary.py" "$@"
    ;;
  snapshot)
    python3 "$SCRIPT_DIR/snapshot.py" "$@"
    ;;
  article)
    python3 "$SCRIPT_DIR/article-history.py" "$@"
    ;;
  help|--help|-h)
    usage
    ;;
  *)
    echo "Unknown command: $COMMAND"
    echo "Run with --help for usage."
    exit 1
    ;;
esac
