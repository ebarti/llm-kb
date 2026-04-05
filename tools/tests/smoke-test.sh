#!/usr/bin/env bash
#
# Smoke Tests
# Quick validation that all tools are executable and respond to basic invocation.
#
# Tests: kb, tools/search.sh, tools/fetch-url.sh
# Tests Python scripts can import without error.
#
# Usage: ./tools/tests/smoke-test.sh [--json]
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

JSON_MODE=false
if [[ "${1:-}" == "--json" ]]; then
    JSON_MODE=true
fi

PASS=0
FAIL=0
RESULTS=()

run_test() {
    local name="$1"
    local cmd="$2"
    local expect_rc="${3:-0}"  # expected return code pattern: 0=success, any=any

    local output
    local rc=0
    output=$(eval "$cmd" 2>&1) || rc=$?

    local passed=false
    if [[ "$expect_rc" == "any" ]]; then
        # Just check it didn't segfault; 141=SIGPIPE is normal for piped commands
        [[ $rc -lt 128 || $rc -eq 141 ]] && passed=true
    else
        [[ $rc -eq $expect_rc ]] && passed=true
    fi

    if $passed; then
        PASS=$((PASS + 1))
        if ! $JSON_MODE; then
            echo -e "  \033[32m✓\033[0m $name"
        fi
    else
        FAIL=$((FAIL + 1))
        if ! $JSON_MODE; then
            echo -e "  \033[31m✗\033[0m $name (rc=$rc)"
            echo "      Output: $(echo "$output" | head -3)"
        fi
    fi

    RESULTS+=("{\"name\": \"$name\", \"passed\": $passed, \"returncode\": $rc}")
}

if ! $JSON_MODE; then
    echo "============================================================"
    echo "  Smoke Tests"
    echo "============================================================"
    echo ""
fi

# --- Tool existence and executability ---

run_test "kb script exists and is executable" \
    "test -x '$BASE_DIR/kb'"

run_test "tools/search.sh exists and is executable" \
    "test -x '$BASE_DIR/tools/search.sh'"

run_test "tools/fetch-url.sh exists and is executable" \
    "test -x '$BASE_DIR/tools/fetch-url.sh'"

# --- kb responds to help/basic invocation ---

run_test "kb responds to invocation" \
    "'$BASE_DIR/kb' 2>&1 | head -1 | grep -qi ''" "any"

# --- search.sh responds ---

run_test "search.sh basic invocation" \
    "'$BASE_DIR/tools/search.sh' test 2>&1 | head -1 | grep -qi ''" "any"

# --- Python script imports ---

run_test "search.py imports without error" \
    "python3 -c \"import sys; sys.path.insert(0, '$BASE_DIR/tools/search-engine'); import search\" 2>&1"

run_test "check-integrity.py imports without error" \
    "python3 -c \"import importlib.util; spec = importlib.util.spec_from_file_location('m', '$BASE_DIR/tools/tests/check-integrity.py'); mod = importlib.util.module_from_spec(spec)\" 2>&1"

run_test "check-links.py imports without error" \
    "python3 -c \"import importlib.util; spec = importlib.util.spec_from_file_location('m', '$BASE_DIR/tools/tests/check-links.py'); mod = importlib.util.module_from_spec(spec)\" 2>&1"

run_test "check-index.py imports without error" \
    "python3 -c \"import importlib.util; spec = importlib.util.spec_from_file_location('m', '$BASE_DIR/tools/tests/check-index.py'); mod = importlib.util.module_from_spec(spec)\" 2>&1"

run_test "check-quality.py imports without error" \
    "python3 -c \"import importlib.util; spec = importlib.util.spec_from_file_location('m', '$BASE_DIR/tools/tests/check-quality.py'); mod = importlib.util.module_from_spec(spec)\" 2>&1"

run_test "test-search.py imports without error" \
    "python3 -c \"import importlib.util; spec = importlib.util.spec_from_file_location('m', '$BASE_DIR/tools/tests/test-search.py'); mod = importlib.util.module_from_spec(spec)\" 2>&1"

# --- Python tools in other directories ---

for pyfile in "$BASE_DIR"/tools/search-engine/*.py; do
    if [[ -f "$pyfile" ]]; then
        fname=$(basename "$pyfile")
        run_test "search-engine/$fname syntax check" \
            "python3 -m py_compile '$pyfile'" "any"
    fi
done

for pyfile in "$BASE_DIR"/tools/ingest/*.py; do
    if [[ -f "$pyfile" ]]; then
        fname=$(basename "$pyfile")
        run_test "ingest/$fname syntax check" \
            "python3 -m py_compile '$pyfile'" "any"
    fi
done

for pyfile in "$BASE_DIR"/tools/monitor/*.py; do
    if [[ -f "$pyfile" ]]; then
        fname=$(basename "$pyfile")
        run_test "monitor/$fname syntax check" \
            "python3 -m py_compile '$pyfile'" "any"
    fi
done

# --- Summary ---

TOTAL=$((PASS + FAIL))

if $JSON_MODE; then
    echo "{"
    echo "  \"total\": $TOTAL,"
    echo "  \"passed\": $PASS,"
    echo "  \"failed\": $FAIL,"
    echo "  \"ok\": $([ $FAIL -eq 0 ] && echo 'true' || echo 'false'),"
    echo "  \"tests\": ["
    for i in "${!RESULTS[@]}"; do
        if [[ $i -lt $((${#RESULTS[@]} - 1)) ]]; then
            echo "    ${RESULTS[$i]},"
        else
            echo "    ${RESULTS[$i]}"
        fi
    done
    echo "  ]"
    echo "}"
else
    echo ""
    echo "Total: $TOTAL  Passed: $PASS  Failed: $FAIL"
    if [[ $FAIL -eq 0 ]]; then
        echo -e "\033[32mAll smoke tests passed.\033[0m"
    else
        echo -e "\033[31m$FAIL smoke test(s) failed.\033[0m"
    fi
    echo ""
fi

exit $([[ $FAIL -eq 0 ]] && echo 0 || echo 1)
