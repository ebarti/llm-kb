#!/usr/bin/env bash
#
# Full Test Runner
# Runs all tests in sequence with color-coded output and summary.
#
# Usage: ./tools/tests/run-all.sh [--json]
#

set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

JSON_MODE=false
if [[ "${1:-}" == "--json" ]]; then
    JSON_MODE=true
fi

GREEN="\033[32m"
RED="\033[31m"
YELLOW="\033[33m"
BOLD="\033[1m"
RESET="\033[0m"

TOTAL=0
PASSED=0
FAILED=0
SUITE_RESULTS=()

run_suite() {
    local name="$1"
    local cmd="$2"
    TOTAL=$((TOTAL + 1))

    if ! $JSON_MODE; then
        echo ""
        echo -e "${BOLD}Running: $name${RESET}"
        echo "Command: $cmd"
        echo "---"
    fi

    local output
    local rc=0

    if $JSON_MODE; then
        output=$(eval "$cmd --json" 2>&1) || rc=$?
    else
        output=$(eval "$cmd" 2>&1) || rc=$?
        echo "$output"
    fi

    if [[ $rc -eq 0 ]]; then
        PASSED=$((PASSED + 1))
        if ! $JSON_MODE; then
            echo -e "${GREEN}>>> $name: PASSED${RESET}"
        fi
        SUITE_RESULTS+=("{\"name\": \"$name\", \"passed\": true, \"returncode\": $rc}")
    else
        FAILED=$((FAILED + 1))
        if ! $JSON_MODE; then
            echo -e "${RED}>>> $name: FAILED (exit code $rc)${RESET}"
        fi
        SUITE_RESULTS+=("{\"name\": \"$name\", \"passed\": false, \"returncode\": $rc}")
    fi
}

if ! $JSON_MODE; then
    echo -e "${BOLD}============================================================${RESET}"
    echo -e "${BOLD}  Full Test Suite${RESET}"
    echo -e "${BOLD}============================================================${RESET}"
fi

# Run all test suites
run_suite "Wiki Integrity Check" \
    "python3 '$SCRIPT_DIR/check-integrity.py'"

run_suite "Link Graph Validator" \
    "python3 '$SCRIPT_DIR/check-links.py'"

run_suite "Index Validator" \
    "python3 '$SCRIPT_DIR/check-index.py'"

run_suite "Content Quality Check" \
    "python3 '$SCRIPT_DIR/check-quality.py'"

run_suite "Template Leak Checker Tests" \
    "python3 '$SCRIPT_DIR/test-template-leaks.py'"

run_suite "Template Placeholder Leaks" \
    "python3 '$SCRIPT_DIR/check-template-leaks.py'"

run_suite "Search Engine Tests" \
    "python3 '$SCRIPT_DIR/test-search.py'"

run_suite "Smoke Tests" \
    "bash '$SCRIPT_DIR/smoke-test.sh'"

# --- Summary ---

if $JSON_MODE; then
    echo "{"
    echo "  \"total_suites\": $TOTAL,"
    echo "  \"passed\": $PASSED,"
    echo "  \"failed\": $FAILED,"
    echo "  \"ok\": $([ $FAILED -eq 0 ] && echo 'true' || echo 'false'),"
    echo "  \"suites\": ["
    for i in "${!SUITE_RESULTS[@]}"; do
        if [[ $i -lt $((${#SUITE_RESULTS[@]} - 1)) ]]; then
            echo "    ${SUITE_RESULTS[$i]},"
        else
            echo "    ${SUITE_RESULTS[$i]}"
        fi
    done
    echo "  ]"
    echo "}"
else
    echo ""
    echo -e "${BOLD}============================================================${RESET}"
    echo -e "${BOLD}  Summary${RESET}"
    echo -e "${BOLD}============================================================${RESET}"
    echo ""
    for r in "${SUITE_RESULTS[@]}"; do
        # Parse the JSON-ish string for display
        name=$(echo "$r" | sed 's/.*"name": "\([^"]*\)".*/\1/')
        passed=$(echo "$r" | sed 's/.*"passed": \([a-z]*\).*/\1/')
        if [[ "$passed" == "true" ]]; then
            echo -e "  ${GREEN}✓${RESET} $name"
        else
            echo -e "  ${RED}✗${RESET} $name"
        fi
    done
    echo ""
    echo "Total: $TOTAL  Passed: $PASSED  Failed: $FAILED"
    echo ""
    if [[ $FAILED -eq 0 ]]; then
        echo -e "${GREEN}${BOLD}ALL TESTS PASSED${RESET}"
    else
        echo -e "${RED}${BOLD}$FAILED SUITE(S) FAILED${RESET}"
    fi
    echo ""
fi

exit $([[ $FAILED -eq 0 ]] && echo 0 || echo 1)
