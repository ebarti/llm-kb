#!/usr/bin/env bash
#
# Focused regression tests for tools/monitor/discover dispatch behavior.
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

TMP_ROOT="$(mktemp -d)"
trap 'rm -rf "$TMP_ROOT"' EXIT

fail() {
    echo "FAIL: $1" >&2
    exit 1
}

assert_file_content() {
    local path="$1"
    local expected="$2"

    [[ -f "$path" ]] || fail "expected file $path to exist"

    local actual
    actual="$(cat "$path")"
    [[ "$actual" == "$expected" ]] || fail "expected $path to contain $expected, got $actual"
}

assert_missing() {
    local path="$1"
    [[ ! -e "$path" ]] || fail "expected $path to be absent"
}

make_fixture() {
    local fixture
    fixture="$(mktemp -d "$TMP_ROOT/discover-fixture.XXXXXX")"

    cp "$BASE_DIR/tools/monitor/discover" "$fixture/discover"
    chmod +x "$fixture/discover"

    cat > "$fixture/monitor.py" <<'PY'
#!/usr/bin/env python3
import json
import sys
from pathlib import Path

Path(__file__).with_name("monitor.args").write_text(json.dumps(sys.argv[1:]))
PY

    cat > "$fixture/rss.py" <<'PY'
#!/usr/bin/env python3
import json
import sys
from pathlib import Path

Path(__file__).with_name("rss.args").write_text(json.dumps(sys.argv[1:]))
PY

    cat > "$fixture/report.py" <<'PY'
#!/usr/bin/env python3
from pathlib import Path

Path(__file__).with_name("report.ran").write_text("ran")
PY

    chmod +x "$fixture/monitor.py" "$fixture/rss.py" "$fixture/report.py"
    printf '%s\n' "$fixture"
}

test_modifier_only_invocations_default_to_topics() {
    local fixture

    fixture="$(make_fixture)"
    "$fixture/discover" --days 7 >/dev/null
    assert_file_content "$fixture/monitor.args" '["--days", "7"]'
    assert_missing "$fixture/rss.args"
    assert_missing "$fixture/report.ran"

    fixture="$(make_fixture)"
    "$fixture/discover" --dry-run >/dev/null
    assert_file_content "$fixture/monitor.args" '["--dry-run"]'
    assert_missing "$fixture/rss.args"
    assert_missing "$fixture/report.ran"
}

test_rss_passthrough_flags_are_preserved() {
    local fixture

    fixture="$(make_fixture)"
    "$fixture/discover" --feeds --days 5 --json --reset >/dev/null
    assert_file_content "$fixture/rss.args" '["--since", "5", "--json", "--reset"]'
    assert_missing "$fixture/monitor.args"
    assert_missing "$fixture/report.ran"
}

test_topic_modifier_does_not_activate_monitor_with_report() {
    local fixture

    # --report --topic RAG must run report.py only. Previously --topic
    # unilaterally enabled DO_TOPICS, which pulled monitor.py in and
    # tripped the multi-module extra-flag guard.
    fixture="$(make_fixture)"
    "$fixture/discover" --report --topic RAG >/dev/null
    assert_file_content "$fixture/report.ran" "ran"
    assert_missing "$fixture/monitor.args"
    assert_missing "$fixture/rss.args"
}

test_topic_modifier_does_not_activate_monitor_with_feeds() {
    local fixture

    # --feeds --topic RAG must dispatch only to rss.py, not monitor.py.
    fixture="$(make_fixture)"
    "$fixture/discover" --feeds --topic RAG >/dev/null
    assert_file_content "$fixture/rss.args" "[]"
    assert_missing "$fixture/monitor.args"
    assert_missing "$fixture/report.ran"
}

test_topic_modifier_alone_still_defaults_to_topics() {
    local fixture

    fixture="$(make_fixture)"
    "$fixture/discover" --topic RAG >/dev/null
    assert_file_content "$fixture/monitor.args" '["--topic", "RAG"]'
    assert_missing "$fixture/rss.args"
    assert_missing "$fixture/report.ran"
}

test_modifier_only_invocations_default_to_topics
test_rss_passthrough_flags_are_preserved
test_topic_modifier_does_not_activate_monitor_with_report
test_topic_modifier_does_not_activate_monitor_with_feeds
test_topic_modifier_alone_still_defaults_to_topics

echo "discover regression tests passed"
