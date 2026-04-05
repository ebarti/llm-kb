#!/usr/bin/env bash
#
# Test script for the MCP wiki server.
# Sends JSON-RPC requests over stdin and validates responses.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
SERVER="$SCRIPT_DIR/server.py"

PASS=0
FAIL=0

# ── Helpers ──────────────────────────────────────────────────────────────

send_and_check() {
    local label="$1"
    shift
    # remaining args are the JSON lines to send
    local input=""
    for msg in "$@"; do
        input+="$msg"$'\n'
    done

    local output
    output=$(echo "$input" | python3 "$SERVER" 2>/dev/null)

    # We check the LAST line of output (responses accumulate, one per line)
    local last_line
    last_line=$(echo "$output" | tail -n1)

    if echo "$last_line" | python3 -c "import sys,json; json.load(sys.stdin)" 2>/dev/null; then
        echo "  PASS  $label"
        PASS=$((PASS + 1))
    else
        echo "  FAIL  $label — invalid JSON response"
        echo "        Got: $last_line"
        FAIL=$((FAIL + 1))
    fi

    # Return the last response for further checks
    LAST_RESPONSE="$last_line"
}

assert_contains() {
    local label="$1"
    local haystack="$2"
    local needle="$3"
    if echo "$haystack" | grep -q "$needle"; then
        echo "  PASS  $label"
        PASS=$((PASS + 1))
    else
        echo "  FAIL  $label — expected to find '$needle'"
        FAIL=$((FAIL + 1))
    fi
}

# ── Build standard request helpers ───────────────────────────────────────

INIT='{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test"}}}'
NOTIFY='{"jsonrpc":"2.0","method":"notifications/initialized"}'

echo "=== MCP Wiki Server Tests ==="
echo ""

# ── 1. Initialize ────────────────────────────────────────────────────────

echo "— initialize"
send_and_check "initialize returns valid JSON" "$INIT"
assert_contains "has protocolVersion" "$LAST_RESPONSE" "protocolVersion"
assert_contains "has serverInfo" "$LAST_RESPONSE" "kb-wiki"

# ── 2. tools/list ────────────────────────────────────────────────────────

echo "— tools/list"
LIST='{"jsonrpc":"2.0","id":2,"method":"tools/list"}'
send_and_check "tools/list returns valid JSON" "$INIT" "$NOTIFY" "$LIST"
assert_contains "lists wiki_search" "$LAST_RESPONSE" "wiki_search"
assert_contains "lists wiki_read" "$LAST_RESPONSE" "wiki_read"
assert_contains "lists wiki_index" "$LAST_RESPONSE" "wiki_index"
assert_contains "lists wiki_stats" "$LAST_RESPONSE" "wiki_stats"
assert_contains "lists wiki_related" "$LAST_RESPONSE" "wiki_related"

# ── 3. wiki_index ────────────────────────────────────────────────────────

echo "— wiki_index"
CALL_INDEX='{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"wiki_index","arguments":{}}}'
send_and_check "wiki_index returns valid JSON" "$INIT" "$NOTIFY" "$CALL_INDEX"
assert_contains "index has content" "$LAST_RESPONSE" "Knowledge Base Index"

# ── 4. wiki_summaries ────────────────────────────────────────────────────

echo "— wiki_summaries"
CALL_SUM='{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"wiki_summaries","arguments":{}}}'
send_and_check "wiki_summaries returns valid JSON" "$INIT" "$NOTIFY" "$CALL_SUM"
assert_contains "summaries has content" "$LAST_RESPONSE" "Article Summaries"

# ── 5. wiki_read ─────────────────────────────────────────────────────────

echo "— wiki_read"
CALL_READ='{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"wiki_read","arguments":{"path":"concepts/llm-knowledge-base"}}}'
send_and_check "wiki_read returns valid JSON" "$INIT" "$NOTIFY" "$CALL_READ"
assert_contains "read returns article content" "$LAST_RESPONSE" "knowledge base"

# ── 6. wiki_search ───────────────────────────────────────────────────────

echo "— wiki_search"
CALL_SEARCH='{"jsonrpc":"2.0","id":6,"method":"tools/call","params":{"name":"wiki_search","arguments":{"query":"knowledge graph","top_k":5}}}'
send_and_check "wiki_search returns valid JSON" "$INIT" "$NOTIFY" "$CALL_SEARCH"
assert_contains "search has results" "$LAST_RESPONSE" "relevance_score"

# ── 7. wiki_stats ────────────────────────────────────────────────────────

echo "— wiki_stats"
CALL_STATS='{"jsonrpc":"2.0","id":7,"method":"tools/call","params":{"name":"wiki_stats","arguments":{}}}'
send_and_check "wiki_stats returns valid JSON" "$INIT" "$NOTIFY" "$CALL_STATS"
assert_contains "stats has total_sources" "$LAST_RESPONSE" "total_sources"
assert_contains "stats has total_words" "$LAST_RESPONSE" "total_words"

# ── 8. wiki_links ────────────────────────────────────────────────────────

echo "— wiki_links (full)"
CALL_LINKS='{"jsonrpc":"2.0","id":8,"method":"tools/call","params":{"name":"wiki_links","arguments":{}}}'
send_and_check "wiki_links full returns valid JSON" "$INIT" "$NOTIFY" "$CALL_LINKS"
assert_contains "links has graph content" "$LAST_RESPONSE" "Link Graph"

echo "— wiki_links (filtered)"
CALL_LINKS_F='{"jsonrpc":"2.0","id":9,"method":"tools/call","params":{"name":"wiki_links","arguments":{"article":"sources/karpathy-llm-knowledge-bases"}}}'
send_and_check "wiki_links filtered returns valid JSON" "$INIT" "$NOTIFY" "$CALL_LINKS_F"
assert_contains "filtered links has article" "$LAST_RESPONSE" "karpathy"

# ── 9. wiki_log ──────────────────────────────────────────────────────────

echo "— wiki_log"
CALL_LOG='{"jsonrpc":"2.0","id":10,"method":"tools/call","params":{"name":"wiki_log","arguments":{"n":5}}}'
send_and_check "wiki_log returns valid JSON" "$INIT" "$NOTIFY" "$CALL_LOG"
assert_contains "log has entries" "$LAST_RESPONSE" "2026"

# ── 10. wiki_related ─────────────────────────────────────────────────────

echo "— wiki_related"
CALL_RELATED='{"jsonrpc":"2.0","id":11,"method":"tools/call","params":{"name":"wiki_related","arguments":{"article":"sources/karpathy-llm-knowledge-bases"}}}'
send_and_check "wiki_related returns valid JSON" "$INIT" "$NOTIFY" "$CALL_RELATED"
assert_contains "related has results" "$LAST_RESPONSE" "related"

# ── Summary ──────────────────────────────────────────────────────────────

echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="

if [ "$FAIL" -gt 0 ]; then
    exit 1
fi
