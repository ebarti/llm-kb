#!/usr/bin/env bash
# Install/remove the hourly discovery queue worker.
#
# Usage:
#   tools/worker/setup-schedule.sh           # macOS launchd
#   tools/worker/setup-schedule.sh --cron    # Linux cron
#   tools/worker/setup-schedule.sh --remove  # remove launchd/cron entry

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
KB_DIR="${KB_DIR:-$(cd "$SCRIPT_DIR/../.." && pwd)}"
RUNNER="$KB_DIR/tools/worker/run_hourly.py"
LOG_DIR="$KB_DIR/tools/worker/.logs"
LABEL="com.llm-kb.discovery-worker"
CRON_TAG="# $LABEL"
PLIST_TEMPLATE="$SCRIPT_DIR/$LABEL.plist"
PLIST_PATH="$HOME/Library/LaunchAgents/$LABEL.plist"
PYTHON_BIN="${PYTHON_BIN:-$(command -v python3)}"

mkdir -p "$LOG_DIR"

shell_quote() {
    printf "%q" "$1"
}

xml_escape() {
    printf "%s" "$1" | sed \
        -e 's/&/\&amp;/g' \
        -e 's/</\&lt;/g' \
        -e 's/>/\&gt;/g'
}

sed_replacement() {
    printf "%s" "$1" | sed -e 's/[\\&|]/\\&/g'
}

remove_cron() {
    local tmp
    tmp="$(mktemp)"
    crontab -l 2>/dev/null > "$tmp" || true
    grep -F -v "$LABEL" "$tmp" | crontab - || true
    rm -f "$tmp"
}

if [[ "${1:-}" == "--remove" ]]; then
    if [[ "$(uname)" == "Darwin" ]]; then
        if [[ -f "$PLIST_PATH" ]]; then
            launchctl unload "$PLIST_PATH" 2>/dev/null || true
            rm -f "$PLIST_PATH"
            echo "Removed launchd plist: $PLIST_PATH"
        else
            echo "No launchd plist found at $PLIST_PATH"
        fi
    else
        remove_cron
        echo "Removed discovery worker crontab entry."
    fi
    exit 0
fi

if [[ ! -f "$RUNNER" ]]; then
    echo "error: worker not found: $RUNNER" >&2
    exit 1
fi

if [[ "${1:-}" == "--cron" ]]; then
    quoted_kb="$(shell_quote "$KB_DIR")"
    quoted_runner="$(shell_quote "$RUNNER")"
    quoted_python="$(shell_quote "$PYTHON_BIN")"
    quoted_log="$(shell_quote "$LOG_DIR/worker-cron.log")"
    CRON_ENTRY="0 * * * * cd $quoted_kb && KB_DIR=$quoted_kb $quoted_python $quoted_runner >> $quoted_log 2>&1 $CRON_TAG"

    if crontab -l 2>/dev/null | grep -F -q "$LABEL"; then
        echo "Crontab entry already exists."
        crontab -l | grep -F "$LABEL"
    else
        (crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -
        echo "Installed hourly crontab entry:"
        echo "  $CRON_ENTRY"
    fi
    exit 0
fi

if [[ "$(uname)" != "Darwin" ]]; then
    echo "Not on macOS. Use --cron for Linux crontab setup." >&2
    exit 1
fi

mkdir -p "$(dirname "$PLIST_PATH")"

plist_python="$(sed_replacement "$(xml_escape "$PYTHON_BIN")")"
plist_runner="$(sed_replacement "$(xml_escape "$RUNNER")")"
plist_kb_dir="$(sed_replacement "$(xml_escape "$KB_DIR")")"
plist_log_dir="$(sed_replacement "$(xml_escape "$LOG_DIR")")"

sed \
    -e "s|__PYTHON__|$plist_python|g" \
    -e "s|__RUNNER__|$plist_runner|g" \
    -e "s|__KB_DIR__|$plist_kb_dir|g" \
    -e "s|__LOG_DIR__|$plist_log_dir|g" \
    "$PLIST_TEMPLATE" > "$PLIST_PATH"

launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH"

echo "Installed launchd plist: $PLIST_PATH"
echo "Label: $LABEL"
echo "Schedule: hourly"
echo "Logs: $LOG_DIR"
echo ""
echo "Verify with:"
echo "  launchctl list | grep llm-kb"
