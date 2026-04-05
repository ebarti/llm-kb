#!/bin/bash
# setup-cron.sh — Set up periodic monitoring via macOS launchd
#
# Creates a launchd plist to run the monitor daily at 8am.
# Also supports crontab fallback for Linux.
#
# Usage:
#   ./tools/monitor/setup-cron.sh           # install launchd plist (macOS)
#   ./tools/monitor/setup-cron.sh --remove  # remove the plist
#   ./tools/monitor/setup-cron.sh --cron    # use crontab instead (Linux)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
KB_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
DISCOVER="$SCRIPT_DIR/discover"
LOG_DIR="$SCRIPT_DIR/.logs"
PLIST_NAME="com.kb.monitor"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_NAME}.plist"

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

mkdir -p "$LOG_DIR"

# --- Remove ---
if [[ "${1:-}" == "--remove" ]]; then
    if [[ "$(uname)" == "Darwin" ]]; then
        if [[ -f "$PLIST_PATH" ]]; then
            launchctl unload "$PLIST_PATH" 2>/dev/null || true
            rm -f "$PLIST_PATH"
            echo -e "${GREEN}Removed${NC} launchd plist: $PLIST_PATH"
        else
            echo "No plist found at $PLIST_PATH"
        fi
    else
        crontab -l 2>/dev/null | grep -v "$DISCOVER" | crontab -
        echo -e "${GREEN}Removed${NC} crontab entry."
    fi
    exit 0
fi

# --- Crontab (Linux / fallback) ---
if [[ "${1:-}" == "--cron" ]]; then
    CRON_ENTRY="0 8 * * * $DISCOVER --ingest >> $LOG_DIR/cron.log 2>&1"

    # Check if already installed
    if crontab -l 2>/dev/null | grep -q "$DISCOVER"; then
        echo "Crontab entry already exists."
        crontab -l | grep "$DISCOVER"
    else
        (crontab -l 2>/dev/null; echo "$CRON_ENTRY") | crontab -
        echo -e "${GREEN}Installed${NC} crontab entry:"
        echo "  $CRON_ENTRY"
    fi
    exit 0
fi

# --- macOS launchd ---
if [[ "$(uname)" != "Darwin" ]]; then
    echo "Not on macOS. Use --cron for crontab setup."
    exit 1
fi

mkdir -p "$(dirname "$PLIST_PATH")"

cat > "$PLIST_PATH" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_NAME}</string>
    <key>ProgramArguments</key>
    <array>
        <string>${DISCOVER}</string>
        <string>--ingest</string>
    </array>
    <key>WorkingDirectory</key>
    <string>${KB_DIR}</string>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>8</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
    <key>StandardOutPath</key>
    <string>${LOG_DIR}/launchd-stdout.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_DIR}/launchd-stderr.log</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
PLIST

# Load the plist
launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH"

echo -e "${GREEN}Installed${NC} launchd plist:"
echo "  Path: $PLIST_PATH"
echo "  Schedule: Daily at 8:00 AM"
echo "  Logs: $LOG_DIR/"
echo ""
echo "To test now:"
echo "  launchctl start $PLIST_NAME"
echo ""
echo "To remove:"
echo "  $0 --remove"
