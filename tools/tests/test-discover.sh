#!/usr/bin/env bash
#
# Focused regression tests for tools/monitor/discover dispatch behavior.
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

TMP_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/discover-test.XXXXXX")"
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

assert_contains() {
    local haystack="$1"
    local needle="$2"

    [[ "$haystack" == *"$needle"* ]] || fail "expected output to contain: $needle"
}

assert_not_contains() {
    local haystack="$1"
    local needle="$2"

    [[ "$haystack" != *"$needle"* ]] || fail "expected output to omit: $needle"
}

assert_fails_with_stderr() {
    local expected_exit="$1"
    local expected_stderr="$2"
    shift 2

    local stderr_file
    stderr_file="$(mktemp "$TMP_ROOT/stderr.XXXXXX")"

    set +e
    "$@" >/dev/null 2>"$stderr_file"
    local rc=$?
    set -e

    [[ "$rc" -eq "$expected_exit" ]] || fail "expected exit $expected_exit, got $rc"

    local stderr
    stderr="$(cat "$stderr_file")"
    assert_contains "$stderr" "$expected_stderr"
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

    fixture="$(make_fixture)"
    bash "$fixture/discover" --days 7 >/dev/null
    assert_file_content "$fixture/monitor.args" '["--days", "7"]'
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

test_header_notes_ignored_modifiers() {
    local fixture output

    fixture="$(make_fixture)"
    output="$("$fixture/discover" --report --topic RAG --days 7)"
    assert_contains "$output" "Note: --days 7 ignored for selected mode(s)"
    assert_contains "$output" "Note: --topic 'RAG' ignored for selected mode(s)"
    assert_not_contains "$output" "Window: last 7 day(s)"
    assert_not_contains "$output" "Topic filter: RAG"
}

test_header_shows_only_active_modifiers() {
    local fixture output

    fixture="$(make_fixture)"
    output="$("$fixture/discover" --feeds --topic RAG --days 7)"
    assert_contains "$output" "Window: last 7 day(s)"
    assert_contains "$output" "Note: --topic 'RAG' ignored for selected mode(s)"
    assert_not_contains "$output" "Topic filter: RAG"
}

test_argument_validation_failures() {
    local fixture

    fixture="$(make_fixture)"
    assert_fails_with_stderr 2 "error: --topic requires an argument" \
        "$fixture/discover" --topic

    fixture="$(make_fixture)"
    assert_fails_with_stderr 2 "error: --topic requires an argument" \
        "$fixture/discover" --topic --report

    fixture="$(make_fixture)"
    assert_fails_with_stderr 2 "error: --days expects a positive integer (>= 1), got 'abc'" \
        "$fixture/discover" --days abc
}

test_modifier_only_invocations_default_to_topics
test_rss_passthrough_flags_are_preserved
test_topic_modifier_does_not_activate_monitor_with_report
test_topic_modifier_does_not_activate_monitor_with_feeds
test_topic_modifier_alone_still_defaults_to_topics
test_header_notes_ignored_modifiers
test_header_shows_only_active_modifiers
test_argument_validation_failures

echo "discover regression tests passed"
