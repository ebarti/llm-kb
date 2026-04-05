#!/usr/bin/env bash
#
# Plugin Manager for the LLM knowledge base.
#
# Usage:
#   ./tools/plugins/manage.sh list               — list available plugins
#   ./tools/plugins/manage.sh enable <plugin>     — enable a plugin
#   ./tools/plugins/manage.sh disable <plugin>    — disable a plugin
#   ./tools/plugins/manage.sh run <hook> [args..] — run all plugins for a hook
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FRAMEWORK="$SCRIPT_DIR/framework.py"

if [[ $# -lt 1 ]]; then
    echo "Usage: $0 {list|enable|disable|run} [args...]"
    echo ""
    echo "Commands:"
    echo "  list               List all available plugins and their status"
    echo "  enable <plugin>    Enable a plugin"
    echo "  disable <plugin>   Disable a plugin"
    echo "  run <hook> [args]  Run all enabled plugins for a hook"
    echo ""
    echo "Available hooks:"
    echo "  pre_ingest, post_ingest, pre_compile, post_compile,"
    echo "  pre_query, post_query, on_lint"
    exit 1
fi

CMD="$1"
shift

case "$CMD" in
    list)
        python3 "$FRAMEWORK" list
        ;;
    enable)
        if [[ $# -lt 1 ]]; then
            echo "Usage: $0 enable <plugin_name>"
            exit 1
        fi
        python3 "$FRAMEWORK" enable "$1"
        ;;
    disable)
        if [[ $# -lt 1 ]]; then
            echo "Usage: $0 disable <plugin_name>"
            exit 1
        fi
        python3 "$FRAMEWORK" disable "$1"
        ;;
    run)
        if [[ $# -lt 1 ]]; then
            echo "Usage: $0 run <hook_name> [args...]"
            exit 1
        fi
        python3 "$FRAMEWORK" run "$@"
        ;;
    *)
        echo "Unknown command: $CMD"
        echo "Usage: $0 {list|enable|disable|run} [args...]"
        exit 1
        ;;
esac
