#!/bin/bash
# github.sh — Summarize a GitHub repository
# Usage: ./tools/ingest/github.sh https://github.com/owner/repo
#
# Captures: README, description, language stats, directory tree, key files
# Uses `gh` CLI if available, otherwise falls back to GitHub API via curl

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
RAW_DIR="$PROJECT_DIR/raw"
mkdir -p "$RAW_DIR"

INPUT="${1:-}"
if [ -z "$INPUT" ]; then
    echo "Usage: github.sh <github-repo-url>"
    echo "Example: ./tools/ingest/github.sh https://github.com/anthropics/claude-code"
    exit 1
fi

TODAY=$(date +%Y-%m-%d)

# --- Parse owner/repo ---
OWNER_REPO=""
if echo "$INPUT" | grep -qE 'github\.com/[^/]+/[^/]+'; then
    OWNER_REPO=$(echo "$INPUT" | grep -oE 'github\.com/[^/]+/[^/?#]+' | sed 's|github\.com/||; s|\.git$||')
elif echo "$INPUT" | grep -qE '^[^/]+/[^/]+$'; then
    OWNER_REPO="$INPUT"
fi

if [ -z "$OWNER_REPO" ]; then
    echo "ERROR: Could not parse owner/repo from: $INPUT"
    exit 1
fi

OWNER=$(echo "$OWNER_REPO" | cut -d/ -f1)
REPO=$(echo "$OWNER_REPO" | cut -d/ -f2)
echo "Repository: $OWNER/$REPO"

# --- Helper: GitHub API fetch ---
gh_api() {
    local endpoint="$1"
    if command -v gh &>/dev/null; then
        gh api "$endpoint" 2>/dev/null || true
    else
        curl -sL --max-time 30 \
            -H "Accept: application/vnd.github.v3+json" \
            "https://api.github.com/$endpoint" 2>/dev/null || true
    fi
}

gh_api_raw() {
    local endpoint="$1"
    if command -v gh &>/dev/null; then
        gh api "$endpoint" -H "Accept: application/vnd.github.v3.raw" 2>/dev/null || true
    else
        curl -sL --max-time 30 \
            -H "Accept: application/vnd.github.v3.raw" \
            "https://api.github.com/$endpoint" 2>/dev/null || true
    fi
}

# --- Fetch repo metadata ---
echo "Fetching repository metadata..."
REPO_JSON=$(gh_api "repos/$OWNER/$REPO")

if [ -z "$REPO_JSON" ] || echo "$REPO_JSON" | grep -q '"message": "Not Found"'; then
    echo "ERROR: Repository not found: $OWNER/$REPO"
    exit 1
fi

# Parse with python3
REPO_META=$(python3 << 'PYEOF'
import json, sys
try:
    data = json.loads(sys.stdin.read())
    print(f"DESCRIPTION={data.get('description', '') or ''}")
    print(f"STARS={data.get('stargazers_count', 0)}")
    print(f"FORKS={data.get('forks_count', 0)}")
    print(f"LANGUAGE={data.get('language', '') or ''}")
    print(f"LICENSE={data.get('license', {}).get('spdx_id', '') if data.get('license') else ''}")
    print(f"CREATED={str(data.get('created_at', ''))[:10]}")
    print(f"UPDATED={str(data.get('updated_at', ''))[:10]}")
    print(f"PUSHED={str(data.get('pushed_at', ''))[:10]}")
    print(f"DEFAULT_BRANCH={data.get('default_branch', 'main')}")
    print(f"OPEN_ISSUES={data.get('open_issues_count', 0)}")
    print(f"SIZE={data.get('size', 0)}")
    topics = data.get('topics', []) or []
    print(f"TOPICS={', '.join(topics)}")
    print(f"HOMEPAGE={data.get('homepage', '') or ''}")
    print(f"ARCHIVED={'true' if data.get('archived') else 'false'}")
except Exception as e:
    print(f"ERROR={e}")
PYEOF
) <<< "$REPO_JSON"

DESCRIPTION=$(echo "$REPO_META" | grep '^DESCRIPTION=' | sed 's/^DESCRIPTION=//')
STARS=$(echo "$REPO_META" | grep '^STARS=' | sed 's/^STARS=//')
FORKS=$(echo "$REPO_META" | grep '^FORKS=' | sed 's/^FORKS=//')
LANGUAGE=$(echo "$REPO_META" | grep '^LANGUAGE=' | sed 's/^LANGUAGE=//')
LICENSE=$(echo "$REPO_META" | grep '^LICENSE=' | sed 's/^LICENSE=//')
CREATED=$(echo "$REPO_META" | grep '^CREATED=' | sed 's/^CREATED=//')
UPDATED=$(echo "$REPO_META" | grep '^UPDATED=' | sed 's/^UPDATED=//')
PUSHED=$(echo "$REPO_META" | grep '^PUSHED=' | sed 's/^PUSHED=//')
DEFAULT_BRANCH=$(echo "$REPO_META" | grep '^DEFAULT_BRANCH=' | sed 's/^DEFAULT_BRANCH=//')
TOPICS=$(echo "$REPO_META" | grep '^TOPICS=' | sed 's/^TOPICS=//')
HOMEPAGE=$(echo "$REPO_META" | grep '^HOMEPAGE=' | sed 's/^HOMEPAGE=//')
ARCHIVED=$(echo "$REPO_META" | grep '^ARCHIVED=' | sed 's/^ARCHIVED=//')
OPEN_ISSUES=$(echo "$REPO_META" | grep '^OPEN_ISSUES=' | sed 's/^OPEN_ISSUES=//')
REPO_SIZE=$(echo "$REPO_META" | grep '^SIZE=' | sed 's/^SIZE=//')

echo "Description: $DESCRIPTION"
echo "Stars: $STARS | Forks: $FORKS | Language: $LANGUAGE"

# --- Fetch languages ---
echo "Fetching language stats..."
LANGUAGES_JSON=$(gh_api "repos/$OWNER/$REPO/languages")
LANGUAGES_MD=""
if [ -n "$LANGUAGES_JSON" ] && [ "$LANGUAGES_JSON" != "{}" ]; then
    LANGUAGES_MD=$(python3 << 'PYEOF'
import json, sys
try:
    data = json.loads(sys.stdin.read())
    total = sum(data.values())
    for lang, bytes_count in sorted(data.items(), key=lambda x: -x[1]):
        pct = (bytes_count / total * 100) if total > 0 else 0
        print(f"- {lang}: {pct:.1f}%")
except:
    pass
PYEOF
) <<< "$LANGUAGES_JSON"
fi

# --- Fetch directory tree (top-level + one level deep for key dirs) ---
echo "Fetching directory tree..."
TREE_JSON=$(gh_api "repos/$OWNER/$REPO/git/trees/${DEFAULT_BRANCH}?recursive=1")
DIR_TREE=""
if [ -n "$TREE_JSON" ]; then
    DIR_TREE=$(python3 << 'PYEOF'
import json, sys
try:
    data = json.loads(sys.stdin.read())
    items = data.get('tree', [])
    # Show items up to depth 2, and limit total output
    lines = []
    for item in items[:500]:
        path = item.get('path', '')
        item_type = item.get('type', '')
        depth = path.count('/')
        if depth <= 2:
            prefix = "  " * depth
            suffix = "/" if item_type == "tree" else ""
            lines.append(f"{prefix}{path.split('/')[-1]}{suffix}")
    # Truncate if too long
    if len(lines) > 150:
        lines = lines[:150]
        lines.append("... (truncated)")
    print('\n'.join(lines))
except:
    pass
PYEOF
) <<< "$TREE_JSON"
fi

# --- Fetch README ---
echo "Fetching README..."
README_CONTENT=""
for readme_name in "README.md" "readme.md" "README.rst" "README" "README.txt"; do
    README_CONTENT=$(gh_api_raw "repos/$OWNER/$REPO/contents/$readme_name")
    if [ -n "$README_CONTENT" ] && ! echo "$README_CONTENT" | grep -q '"message"'; then
        break
    fi
    README_CONTENT=""
done

if [ -n "$README_CONTENT" ]; then
    # Truncate very long READMEs
    README_CHARS=${#README_CONTENT}
    if [ "$README_CHARS" -gt 20000 ]; then
        README_CONTENT="${README_CONTENT:0:20000}

... (README truncated at 20,000 characters)"
    fi
    echo "Got README: ${README_CHARS} chars"
else
    README_CONTENT="[No README found]"
fi

# --- Fetch key config files (package.json, Cargo.toml, pyproject.toml, etc.) ---
echo "Fetching key config files..."
KEY_FILES_MD=""
for config_file in "package.json" "Cargo.toml" "pyproject.toml" "setup.py" "go.mod" "Makefile" "Dockerfile" "docker-compose.yml" ".github/workflows" "CONTRIBUTING.md"; do
    CONFIG_CONTENT=$(gh_api_raw "repos/$OWNER/$REPO/contents/$config_file" 2>/dev/null || true)
    if [ -n "$CONFIG_CONTENT" ] && ! echo "$CONFIG_CONTENT" | grep -q '"message"'; then
        # Truncate long config files
        if [ ${#CONFIG_CONTENT} -gt 3000 ]; then
            CONFIG_CONTENT="${CONFIG_CONTENT:0:3000}
... (truncated)"
        fi
        KEY_FILES_MD="${KEY_FILES_MD}
### \`$config_file\`

\`\`\`
$CONFIG_CONTENT
\`\`\`
"
    fi
done

# --- Fetch recent releases ---
echo "Fetching recent releases..."
RELEASES_JSON=$(gh_api "repos/$OWNER/$REPO/releases?per_page=5")
RELEASES_MD=""
if [ -n "$RELEASES_JSON" ] && [ "$RELEASES_JSON" != "[]" ]; then
    RELEASES_MD=$(python3 << 'PYEOF'
import json, sys
try:
    data = json.loads(sys.stdin.read())
    if isinstance(data, list):
        for rel in data[:5]:
            tag = rel.get('tag_name', '')
            name = rel.get('name', '')
            date = str(rel.get('published_at', ''))[:10]
            prerelease = " (pre-release)" if rel.get('prerelease') else ""
            print(f"- **{tag}** {name} ({date}){prerelease}")
except:
    pass
PYEOF
) <<< "$RELEASES_JSON"
fi

# --- Generate output ---
SAFE_NAME=$(echo "${OWNER}-${REPO}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
OUTPUT_FILE="$RAW_DIR/gh-${SAFE_NAME}.md"

cat > "$OUTPUT_FILE" << HEREDOC
---
title: "${OWNER}/${REPO}"
source: "https://github.com/${OWNER}/${REPO}"
description: "$(echo "$DESCRIPTION" | sed 's/"/\\"/g')"
language: "$LANGUAGE"
stars: $STARS
forks: $FORKS
license: "$LICENSE"
date_created: ${CREATED:-}
date_updated: ${PUSHED:-}
date_ingested: $TODAY
topics: [$(echo "$TOPICS" | sed 's/, /,/g' | sed 's/[^,]*/"&"/g')]
tags: [github, repo, ${LANGUAGE:-code}]
type: github
status: raw
${ARCHIVED:+archived: $ARCHIVED}
${HOMEPAGE:+homepage: "$HOMEPAGE"}
---

# ${OWNER}/${REPO}

> $DESCRIPTION

**Language:** $LANGUAGE | **Stars:** $STARS | **Forks:** $FORKS | **License:** ${LICENSE:-N/A}
**Created:** ${CREATED:-?} | **Last pushed:** ${PUSHED:-?} | **Open issues:** ${OPEN_ISSUES:-0}
${HOMEPAGE:+**Homepage:** $HOMEPAGE}
${TOPICS:+**Topics:** $TOPICS}

## Language Breakdown

${LANGUAGES_MD:-No language data available.}

## Directory Structure

\`\`\`
${DIR_TREE:-[Could not fetch directory tree]}
\`\`\`

## README

${README_CONTENT}

${RELEASES_MD:+## Recent Releases

$RELEASES_MD
}
${KEY_FILES_MD:+## Key Configuration Files
$KEY_FILES_MD}
HEREDOC

echo ""
echo "Saved to: $OUTPUT_FILE"
echo "File size: $(wc -c < "$OUTPUT_FILE" | tr -d ' ') bytes"
