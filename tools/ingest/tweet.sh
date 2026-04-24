#!/bin/bash
# tweet.sh — Fetch a Twitter/X thread
# Usage: ./tools/ingest/tweet.sh https://x.com/user/status/123456789
#
# Tries multiple approaches:
#   1. Nitter instances (public mirrors)
#   2. Direct curl + parse from x.com/twitter.com
#   3. FixTweet / FxTwitter / VxTwitter API

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
RAW_DIR="$PROJECT_DIR/raw"
mkdir -p "$RAW_DIR"

URL="${1:-}"
if [ -z "$URL" ]; then
    echo "Usage: tweet.sh <tweet-url>"
    echo "Example: ./tools/ingest/tweet.sh 'https://x.com/karpathy/status/123456789'"
    exit 1
fi

TODAY=$(date +%Y-%m-%d)

# --- Parse tweet URL ---
USERNAME=""
TWEET_ID=""

# Normalize URL: support x.com and twitter.com
if echo "$URL" | grep -qE '(twitter\.com|x\.com)/[^/]+/status/[0-9]+'; then
    USERNAME=$(echo "$URL" | grep -oE '(twitter\.com|x\.com)/([^/]+)/status/' | sed 's|.*\.com/||; s|/status/||')
    TWEET_ID=$(echo "$URL" | grep -oE 'status/[0-9]+' | sed 's|status/||')
fi

if [ -z "$TWEET_ID" ]; then
    echo "ERROR: Could not parse tweet ID from URL: $URL"
    exit 1
fi

echo "User: @${USERNAME}"
echo "Tweet ID: $TWEET_ID"

CANONICAL_URL="https://x.com/${USERNAME}/status/${TWEET_ID}"
CONTENT=""
AUTHOR_NAME=""
DATE_PUBLISHED=""
METHOD=""

# --- Method 1: FxTwitter/FixTweet API (JSON) ---
echo "Trying FxTwitter API..."
FX_JSON=$(curl -sL --max-time 20 \
    -H "Accept: application/json" \
    "https://api.fxtwitter.com/${USERNAME}/status/${TWEET_ID}" 2>/dev/null || true)

if [ -n "$FX_JSON" ] && echo "$FX_JSON" | python3 -c "import json,sys; json.load(sys.stdin)" 2>/dev/null; then
    PARSED=$(python3 << 'PYEOF'
import json, sys
try:
    data = json.loads(sys.stdin.read())
    tweet = data.get('tweet', {})
    if tweet:
        author = tweet.get('author', {})
        print(f"AUTHOR_NAME={author.get('name', '')}")
        print(f"AUTHOR_HANDLE={author.get('screen_name', '')}")
        print(f"DATE={tweet.get('created_at', '')[:10] if tweet.get('created_at') else ''}")
        print(f"LIKES={tweet.get('likes', 0)}")
        print(f"RETWEETS={tweet.get('retweets', 0)}")
        print(f"REPLIES={tweet.get('replies', 0)}")
        text = tweet.get('text', '')
        print(f"TEXT_START")
        print(text)
        print(f"TEXT_END")

        # Check for media
        media = tweet.get('media', {})
        if media and media.get('all'):
            for m in media['all']:
                if m.get('type') == 'photo':
                    print(f"MEDIA_PHOTO={m.get('url', '')}")

        # Check for thread (quote tweets, etc.)
        quote = tweet.get('quote', {})
        if quote:
            qauthor = quote.get('author', {})
            print(f"QUOTE_AUTHOR={qauthor.get('name', '')} (@{qauthor.get('screen_name', '')})")
            print(f"QUOTE_TEXT_START")
            print(quote.get('text', ''))
            print(f"QUOTE_TEXT_END")
except Exception as e:
    print(f"ERROR={e}")
PYEOF
) <<< "$FX_JSON"

    if [ -n "$PARSED" ] && ! echo "$PARSED" | grep -q '^ERROR='; then
        CONTENT=$(echo "$PARSED" | sed -n '/^TEXT_START$/,/^TEXT_END$/p' | sed '1d;$d')
        AUTHOR_NAME=$(echo "$PARSED" | grep '^AUTHOR_NAME=' | sed 's/^AUTHOR_NAME=//')
        AUTHOR_HANDLE=$(echo "$PARSED" | grep '^AUTHOR_HANDLE=' | sed 's/^AUTHOR_HANDLE=//')
        DATE_PUBLISHED=$(echo "$PARSED" | grep '^DATE=' | sed 's/^DATE=//')
        LIKES=$(echo "$PARSED" | grep '^LIKES=' | sed 's/^LIKES=//')
        RETWEETS=$(echo "$PARSED" | grep '^RETWEETS=' | sed 's/^RETWEETS=//')
        REPLIES_COUNT=$(echo "$PARSED" | grep '^REPLIES=' | sed 's/^REPLIES=//')
        MEDIA_PHOTOS=$(echo "$PARSED" | grep '^MEDIA_PHOTO=' | sed 's/^MEDIA_PHOTO=//')
        QUOTE_AUTHOR=$(echo "$PARSED" | grep '^QUOTE_AUTHOR=' | sed 's/^QUOTE_AUTHOR=//')
        QUOTE_TEXT=$(echo "$PARSED" | sed -n '/^QUOTE_TEXT_START$/,/^QUOTE_TEXT_END$/p' | sed '1d;$d')

        if [ -n "$CONTENT" ]; then
            METHOD="fxtwitter"
            echo "Got tweet via FxTwitter API"
        fi
    fi
fi

# --- Method 2: VxTwitter API ---
if [ -z "$CONTENT" ]; then
    echo "Trying VxTwitter API..."
    VX_JSON=$(curl -sL --max-time 20 \
        "https://api.vxtwitter.com/${USERNAME}/status/${TWEET_ID}" 2>/dev/null || true)

    if [ -n "$VX_JSON" ] && echo "$VX_JSON" | python3 -c "import json,sys; json.load(sys.stdin)" 2>/dev/null; then
        PARSED=$(python3 << 'PYEOF'
import json, sys
try:
    data = json.loads(sys.stdin.read())
    print(f"AUTHOR_NAME={data.get('user_name', '')}")
    print(f"AUTHOR_HANDLE={data.get('user_screen_name', '')}")
    print(f"DATE={data.get('date', '')[:10] if data.get('date') else ''}")
    print(f"LIKES={data.get('likes', 0)}")
    print(f"RETWEETS={data.get('retweets', 0)}")
    text = data.get('text', '')
    print(f"TEXT_START")
    print(text)
    print(f"TEXT_END")
except Exception as e:
    print(f"ERROR={e}")
PYEOF
) <<< "$VX_JSON"

        if [ -n "$PARSED" ] && ! echo "$PARSED" | grep -q '^ERROR='; then
            CONTENT=$(echo "$PARSED" | sed -n '/^TEXT_START$/,/^TEXT_END$/p' | sed '1d;$d')
            [ -z "$AUTHOR_NAME" ] && AUTHOR_NAME=$(echo "$PARSED" | grep '^AUTHOR_NAME=' | sed 's/^AUTHOR_NAME=//')
            [ -z "$DATE_PUBLISHED" ] && DATE_PUBLISHED=$(echo "$PARSED" | grep '^DATE=' | sed 's/^DATE=//')
            [ -z "$LIKES" ] && LIKES=$(echo "$PARSED" | grep '^LIKES=' | sed 's/^LIKES=//')
            [ -z "$RETWEETS" ] && RETWEETS=$(echo "$PARSED" | grep '^RETWEETS=' | sed 's/^RETWEETS=//')
            if [ -n "$CONTENT" ]; then
                METHOD="vxtwitter"
                echo "Got tweet via VxTwitter API"
            fi
        fi
    fi
fi

# --- Method 3: Nitter instances ---
if [ -z "$CONTENT" ]; then
    echo "Trying Nitter instances..."
    NITTER_INSTANCES=(
        "nitter.privacydev.net"
        "nitter.poast.org"
        "nitter.1d4.us"
    )

    for NITTER in "${NITTER_INSTANCES[@]}"; do
        echo "  Trying $NITTER..."
        NITTER_HTML=$(curl -sL --max-time 15 \
            --user-agent "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)" \
            "https://${NITTER}/${USERNAME}/status/${TWEET_ID}" 2>/dev/null || true)

        if [ -n "$NITTER_HTML" ] && echo "$NITTER_HTML" | grep -q 'tweet-content'; then
            CONTENT=$(echo "$NITTER_HTML" | python3 -c "
import sys, re, html
raw = sys.stdin.read()
# Find tweet content divs
matches = re.findall(r'<div class=\"tweet-content[^\"]*\"[^>]*>(.*?)</div>', raw, re.DOTALL)
for m in matches:
    text = re.sub(r'<[^>]+>', '', m)
    text = html.unescape(text).strip()
    if text:
        print(text)
        print()
" 2>/dev/null || true)

            if [ -n "$CONTENT" ]; then
                METHOD="nitter ($NITTER)"
                echo "Got tweet via Nitter"
                break
            fi
        fi
    done
fi

# --- Method 4: Direct curl to x.com (limited, but try) ---
if [ -z "$CONTENT" ]; then
    echo "Trying direct curl to x.com..."
    XCOM_HTML=$(curl -sL --max-time 20 \
        --user-agent "Mozilla/5.0 (compatible; Googlebot/2.1)" \
        "$CANONICAL_URL" 2>/dev/null || true)

    if [ -n "$XCOM_HTML" ]; then
        # Try to extract og:description which often has the tweet text
        OG_DESC=$(echo "$XCOM_HTML" | grep -oP 'property="og:description"\s+content="[^"]*"' | head -1 | sed 's/.*content="//; s/"$//')
        if [ -n "$OG_DESC" ]; then
            CONTENT=$(python3 -c "import html; print(html.unescape('''$OG_DESC'''))" 2>/dev/null || echo "$OG_DESC")
            METHOD="og:description"
            echo "Got tweet via og:description meta tag"
        fi
    fi
fi

if [ -z "$CONTENT" ]; then
    echo "WARNING: Could not fetch tweet content. Saving URL reference only."
    CONTENT="[Tweet content unavailable - may require authentication or the tweet has been deleted]"
    METHOD="none"
fi

AUTHOR_NAME="${AUTHOR_NAME:-$USERNAME}"

# --- Generate output filename ---
SAFE_NAME=$(echo "${USERNAME}-${TWEET_ID}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g' | cut -c1-80)
SLUG="tweet-${SAFE_NAME}"

# --- Build content sections ---
MEDIA_SECTION=""
if [ -n "${MEDIA_PHOTOS:-}" ]; then
    MEDIA_SECTION="
## Media

"
    while IFS= read -r photo_url; do
        [ -n "$photo_url" ] && MEDIA_SECTION="${MEDIA_SECTION}![image](${photo_url})
"
    done <<< "$MEDIA_PHOTOS"
fi

QUOTE_SECTION=""
if [ -n "${QUOTE_TEXT:-}" ]; then
    QUOTE_SECTION="
## Quoted Tweet

> **${QUOTE_AUTHOR:-Unknown}:**
$(echo "$QUOTE_TEXT" | sed 's/^/> /')
"
fi

# --- Compose clean.md ---
CLEAN_FILE=$(mktemp /tmp/tweet-clean-XXXXXX.md)
trap "rm -f '$CLEAN_FILE'" EXIT
cat > "$CLEAN_FILE" << HEREDOC
---
title: "Tweet by @${USERNAME} (${TWEET_ID})"
source: "$CANONICAL_URL"
author: "$(echo "$AUTHOR_NAME" | sed 's/"/\\"/g')"
author_handle: "@${USERNAME}"
date_published: ${DATE_PUBLISHED:-}
date_ingested: $TODAY
likes: ${LIKES:-}
retweets: ${RETWEETS:-}
tags: [twitter, tweet]
type: tweet
status: raw
fetch_method: $METHOD
---

# Tweet by ${AUTHOR_NAME} (@${USERNAME})

**Date:** ${DATE_PUBLISHED:-Unknown}
**Source:** $CANONICAL_URL
${LIKES:+**Likes:** $LIKES | **Retweets:** $RETWEETS}

---

$CONTENT
${MEDIA_SECTION}${QUOTE_SECTION}
HEREDOC

# --- Persist API JSON as raw bytes if we got it ---
RAW_BYTES_FILE=""
RAW_EXT=""
CONTENT_TYPE="text"
if [ -n "${FX_JSON:-}" ]; then
    RAW_BYTES_FILE=$(mktemp /tmp/tweet-raw-XXXXXX.json)
    echo "$FX_JSON" > "$RAW_BYTES_FILE"
    RAW_EXT="json"
    CONTENT_TYPE="json"
elif [ -n "${VX_JSON:-}" ]; then
    RAW_BYTES_FILE=$(mktemp /tmp/tweet-raw-XXXXXX.json)
    echo "$VX_JSON" > "$RAW_BYTES_FILE"
    RAW_EXT="json"
    CONTENT_TYPE="json"
fi

RAW_ARGS=()
if [ -n "$RAW_BYTES_FILE" ]; then
    RAW_ARGS+=(--raw-path "$RAW_BYTES_FILE" --raw-ext "$RAW_EXT")
fi

EXTRA_META=$(python3 - <<PYEOF
import json
print(json.dumps({
    "username": "$USERNAME",
    "tweet_id": "$TWEET_ID",
    "author_name": """$AUTHOR_NAME""".replace('"', r'\"'),
    "fetch_method": "$METHOD",
    "date_published": "${DATE_PUBLISHED:-}",
    "likes": "${LIKES:-}",
    "retweets": "${RETWEETS:-}",
}))
PYEOF
)

python3 "$PROJECT_DIR/tools/ingest/_raw_writer.py" \
    --slug "$SLUG" \
    --url "$CANONICAL_URL" \
    --fetcher tweet \
    --clean-path "$CLEAN_FILE" \
    --content-type "$CONTENT_TYPE" \
    --extra-meta-json "$EXTRA_META" \
    "${RAW_ARGS[@]}" >/dev/null

[ -n "$RAW_BYTES_FILE" ] && rm -f "$RAW_BYTES_FILE"
rm -f "$CLEAN_FILE"

echo ""
echo "Saved to: $RAW_DIR/$SLUG/"
echo "Fetch method: $METHOD"
