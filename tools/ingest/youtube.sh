#!/bin/bash
# youtube.sh — Fetch YouTube video transcript and metadata
# Usage: ./tools/ingest/youtube.sh "https://youtube.com/watch?v=VIDEO_ID"
#
# Tries multiple approaches:
#   1. yt-dlp --write-auto-sub
#   2. python3 youtube-transcript-api
#   3. curl to YouTube timedtext API

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
RAW_DIR="$PROJECT_DIR/raw"
mkdir -p "$RAW_DIR"

URL="${1:-}"
if [ -z "$URL" ]; then
    echo "Usage: youtube.sh <youtube-url>"
    echo "Example: ./tools/ingest/youtube.sh 'https://youtube.com/watch?v=dQw4w9WgXcQ'"
    exit 1
fi

# Extract video ID from various URL formats
VIDEO_ID=""
if echo "$URL" | grep -qE 'v=([a-zA-Z0-9_-]{11})'; then
    VIDEO_ID=$(echo "$URL" | grep -oE 'v=([a-zA-Z0-9_-]{11})' | head -1 | cut -d= -f2)
elif echo "$URL" | grep -qE 'youtu\.be/([a-zA-Z0-9_-]{11})'; then
    VIDEO_ID=$(echo "$URL" | grep -oE 'youtu\.be/([a-zA-Z0-9_-]{11})' | head -1 | sed 's|youtu.be/||')
elif echo "$URL" | grep -qE 'shorts/([a-zA-Z0-9_-]{11})'; then
    VIDEO_ID=$(echo "$URL" | grep -oE 'shorts/([a-zA-Z0-9_-]{11})' | head -1 | sed 's|shorts/||')
fi

if [ -z "$VIDEO_ID" ]; then
    echo "ERROR: Could not extract video ID from URL: $URL"
    exit 1
fi

echo "Video ID: $VIDEO_ID"

CANONICAL_URL="https://www.youtube.com/watch?v=${VIDEO_ID}"
TODAY=$(date +%Y-%m-%d)
TMPDIR=$(mktemp -d /tmp/yt-ingest-XXXXXX)
trap "rm -rf '$TMPDIR'" EXIT

# --- Fetch metadata from YouTube page ---
echo "Fetching video metadata..."
PAGE_HTML=$(curl -sL --max-time 30 \
    --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36" \
    "$CANONICAL_URL" 2>/dev/null || true)

TITLE=""
CHANNEL=""
DATE_PUBLISHED=""
DURATION=""

if [ -n "$PAGE_HTML" ]; then
    # Extract title
    TITLE=$(echo "$PAGE_HTML" | grep -oP '"title":"[^"]*"' | head -1 | sed 's/"title":"//;s/"$//' || true)
    if [ -z "$TITLE" ]; then
        TITLE=$(echo "$PAGE_HTML" | grep -oi '<title>[^<]*</title>' | head -1 | sed 's/<[^>]*>//g; s/ - YouTube$//' || true)
    fi

    # Extract channel name
    CHANNEL=$(echo "$PAGE_HTML" | grep -oP '"ownerChannelName":"[^"]*"' | head -1 | sed 's/"ownerChannelName":"//;s/"$//' || true)
    if [ -z "$CHANNEL" ]; then
        CHANNEL=$(echo "$PAGE_HTML" | grep -oP '"author":"[^"]*"' | head -1 | sed 's/"author":"//;s/"$//' || true)
    fi

    # Extract publish date
    DATE_PUBLISHED=$(echo "$PAGE_HTML" | grep -oP '"publishDate":"[^"]*"' | head -1 | sed 's/"publishDate":"//;s/"$//' || true)
    if [ -z "$DATE_PUBLISHED" ]; then
        DATE_PUBLISHED=$(echo "$PAGE_HTML" | grep -oP '"uploadDate":"[^"]*"' | head -1 | sed 's/"uploadDate":"//;s/"$//' || true)
    fi
    # Trim to date only
    DATE_PUBLISHED=$(echo "$DATE_PUBLISHED" | cut -c1-10)

    # Extract duration
    DURATION=$(echo "$PAGE_HTML" | grep -oP '"lengthSeconds":"[0-9]+"' | head -1 | sed 's/"lengthSeconds":"//;s/"$//' || true)
    if [ -n "$DURATION" ] && [ "$DURATION" -gt 0 ] 2>/dev/null; then
        HOURS=$((DURATION / 3600))
        MINS=$(( (DURATION % 3600) / 60 ))
        SECS=$((DURATION % 60))
        if [ "$HOURS" -gt 0 ]; then
            DURATION="${HOURS}h${MINS}m${SECS}s"
        else
            DURATION="${MINS}m${SECS}s"
        fi
    fi
fi

TITLE="${TITLE:-YouTube Video $VIDEO_ID}"
echo "Title: $TITLE"
echo "Channel: ${CHANNEL:-unknown}"

# --- Fetch transcript ---
TRANSCRIPT=""
METHOD=""

# Method 1: yt-dlp
if [ -z "$TRANSCRIPT" ] && command -v yt-dlp &>/dev/null; then
    echo "Trying yt-dlp..."
    if yt-dlp --skip-download --write-auto-sub --sub-lang en --sub-format vtt \
        -o "$TMPDIR/%(id)s" "$CANONICAL_URL" 2>/dev/null; then
        VTT_FILE=$(ls "$TMPDIR"/*.vtt 2>/dev/null | head -1)
        if [ -n "$VTT_FILE" ] && [ -f "$VTT_FILE" ]; then
            # Convert VTT to plain text: strip headers, timestamps, positioning
            TRANSCRIPT=$(cat "$VTT_FILE" | \
                sed '/^WEBVTT/d; /^Kind:/d; /^Language:/d; /^$/d' | \
                grep -v '^[0-9][0-9]:[0-9][0-9]' | \
                grep -v '^\s*$' | \
                grep -v '^NOTE' | \
                grep -v '<[0-9][0-9]:[0-9][0-9]' | \
                sed 's/<[^>]*>//g' | \
                awk '!seen[$0]++' | \
                tr '\n' ' ' | \
                sed 's/  \+/ /g')
            if [ -n "$TRANSCRIPT" ]; then
                METHOD="yt-dlp"
                echo "Got transcript via yt-dlp (${#TRANSCRIPT} chars)"
            fi
        fi
    fi
fi

# Method 2: python3 youtube-transcript-api
if [ -z "$TRANSCRIPT" ] && command -v python3 &>/dev/null; then
    echo "Trying python3 youtube-transcript-api..."
    TRANSCRIPT=$(python3 -c "
try:
    from youtube_transcript_api import YouTubeTranscriptApi
    transcript = YouTubeTranscriptApi.get_transcript('${VIDEO_ID}', languages=['en'])
    for entry in transcript:
        print(entry['text'])
except Exception as e:
    pass
" 2>/dev/null || true)
    if [ -n "$TRANSCRIPT" ]; then
        METHOD="youtube-transcript-api"
        echo "Got transcript via youtube-transcript-api (${#TRANSCRIPT} chars)"
    fi
fi

# Method 3: curl to YouTube timedtext API
if [ -z "$TRANSCRIPT" ] && [ -n "$PAGE_HTML" ]; then
    echo "Trying YouTube timedtext API..."
    # Extract the captionTracks URL from the page
    CAPTION_URL=$(echo "$PAGE_HTML" | grep -oP '"captionTracks":\[.*?\]' | \
        grep -oP '"baseUrl":"[^"]*"' | head -1 | \
        sed 's/"baseUrl":"//;s/"$//' | \
        sed 's/\\u0026/\&/g' || true)

    if [ -n "$CAPTION_URL" ]; then
        CAPTION_XML=$(curl -sL --max-time 20 "$CAPTION_URL" 2>/dev/null || true)
        if [ -n "$CAPTION_XML" ]; then
            TRANSCRIPT=$(echo "$CAPTION_XML" | \
                sed 's/<[^>]*>//g' | \
                python3 -c "import sys, html; print(html.unescape(sys.stdin.read()))" 2>/dev/null | \
                sed '/^$/d' | \
                tr '\n' ' ' | \
                sed 's/  \+/ /g')
            if [ -n "$TRANSCRIPT" ]; then
                METHOD="timedtext-api"
                echo "Got transcript via timedtext API (${#TRANSCRIPT} chars)"
            fi
        fi
    fi
fi

if [ -z "$TRANSCRIPT" ]; then
    echo "WARNING: Could not fetch transcript. Saving metadata only."
    TRANSCRIPT="[Transcript unavailable - video may not have captions enabled]"
    METHOD="none"
fi

# --- Generate output filename ---
SAFE_TITLE=$(echo "$TITLE" | \
    tr '[:upper:]' '[:lower:]' | \
    sed 's/[^a-z0-9 ]//g' | \
    sed 's/  \+/ /g; s/^ //; s/ $//' | \
    tr ' ' '-' | \
    cut -c1-80)
SLUG="yt-${SAFE_TITLE:-$VIDEO_ID}"

# --- Format transcript into paragraphs ---
# Split roughly every 3-4 sentences for readability
FORMATTED_TRANSCRIPT=$(echo "$TRANSCRIPT" | fold -s -w 500 | sed 's/^[[:space:]]*//')

# --- Compose clean.md ---
CLEAN_FILE=$(mktemp /tmp/yt-clean-XXXXXX.md)
trap "rm -f '$CLEAN_FILE'" EXIT
cat > "$CLEAN_FILE" << HEREDOC
---
title: "$(echo "$TITLE" | sed 's/"/\\"/g')"
source: "$CANONICAL_URL"
channel: "$(echo "${CHANNEL:-}" | sed 's/"/\\"/g')"
date_published: ${DATE_PUBLISHED:-}
date_ingested: $TODAY
duration: "${DURATION:-}"
tags: [youtube, video, transcript]
type: youtube
status: raw
transcript_method: $METHOD
---

# $TITLE

**Channel:** ${CHANNEL:-Unknown}
**Published:** ${DATE_PUBLISHED:-Unknown}
**Duration:** ${DURATION:-Unknown}
**Source:** $CANONICAL_URL

## Transcript

$FORMATTED_TRANSCRIPT
HEREDOC

# --- Persist page HTML as raw bytes if we have it ---
RAW_BYTES_FILE=""
RAW_EXT=""
CONTENT_TYPE="transcript"
if [ -n "${PAGE_HTML:-}" ]; then
    RAW_BYTES_FILE=$(mktemp /tmp/yt-raw-XXXXXX.html)
    echo "$PAGE_HTML" > "$RAW_BYTES_FILE"
    RAW_EXT="html"
    CONTENT_TYPE="html"
fi

RAW_ARGS=()
if [ -n "$RAW_BYTES_FILE" ]; then
    RAW_ARGS+=(--raw-path "$RAW_BYTES_FILE" --raw-ext "$RAW_EXT")
fi

EXTRA_META=$(python3 - <<PYEOF
import json
print(json.dumps({
    "title": """$TITLE""".replace('"', r'\"'),
    "video_id": "$VIDEO_ID",
    "channel": """${CHANNEL:-}""".replace('"', r'\"'),
    "date_published": "${DATE_PUBLISHED:-}",
    "duration": "${DURATION:-}",
    "transcript_method": "$METHOD",
}))
PYEOF
)

python3 "$PROJECT_DIR/tools/ingest/_raw_writer.py" \
    --slug "$SLUG" \
    --url "$CANONICAL_URL" \
    --fetcher youtube \
    --clean-path "$CLEAN_FILE" \
    --content-type "$CONTENT_TYPE" \
    --extra-meta-json "$EXTRA_META" \
    "${RAW_ARGS[@]}" >/dev/null

[ -n "$RAW_BYTES_FILE" ] && rm -f "$RAW_BYTES_FILE"
rm -f "$CLEAN_FILE"

echo ""
echo "Saved to: $RAW_DIR/$SLUG/"
echo "Transcript method: $METHOD"
