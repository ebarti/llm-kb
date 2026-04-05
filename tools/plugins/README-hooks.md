# Plugin & Hooks System

A lightweight plugin framework for the LLM knowledge base. Plugins are Python files that hook into the knowledge base lifecycle at defined points.

## Quick Start

```bash
# List all plugins and their status
./tools/plugins/manage.sh list

# Enable a plugin
./tools/plugins/manage.sh enable auto_tag

# Disable a plugin
./tools/plugins/manage.sh disable auto_tag

# Run all enabled plugins for a hook
./tools/plugins/manage.sh run post_compile

# Run with arguments (e.g., file path for ingest hooks)
./tools/plugins/manage.sh run post_ingest raw/my-new-source.md
```

## Available Hook Points

| Hook | When it runs | Typical args |
|------|-------------|--------------|
| `pre_ingest` | Before a new source is ingested | file path |
| `post_ingest` | After a new source is ingested | file path |
| `pre_compile` | Before wiki compilation starts | (none) |
| `post_compile` | After wiki compilation finishes | (none) |
| `pre_query` | Before a query is executed | query string |
| `post_query` | After a query returns results | query string, result path |
| `on_lint` | During linting / health checks | (none) |

## Writing a New Plugin

Create a Python file in `tools/plugins/available/` with a `register()` function:

```python
#!/usr/bin/env python3
"""
My plugin — short description.

Hook: post_compile
"""

def register():
    """Return a dict mapping hook names to handler functions."""
    return {
        "post_compile": run_post_compile,
    }

def run_post_compile(root, *args):
    """
    Handler function.

    Args:
        root: Absolute path to the project root directory.
        *args: Additional arguments passed via the CLI.

    The root path gives you access to:
        - root/raw/         Raw source documents
        - root/wiki/        Compiled wiki articles
        - root/wiki/_meta/  Metadata files (stats, links, etc.)
    """
    # Your plugin logic here
    print("  [my_plugin] Did something useful.")
```

### Plugin API

Every handler function receives:

1. `root` (str) — absolute path to the project root (e.g., `/path/to/agentic-ai`)
2. `*args` — any additional arguments passed on the command line

Your plugin should:
- Use only the Python standard library (no pip dependencies)
- Print status messages prefixed with `[plugin_name]` for consistent output
- Handle missing files/directories gracefully
- Not modify files outside the project root

### Plugin Lifecycle

1. **Discovery**: The framework scans `tools/plugins/available/` for `.py` files
2. **Loading**: Each file is imported and checked for a `register()` function
3. **Registration**: `register()` returns `{hook_name: callable}` mappings
4. **Filtering**: Only plugins listed in `config.json` `"enabled"` array are active
5. **Execution**: When a hook runs, all enabled plugins for that hook execute in alphabetical order

### Configuration

Plugin state is stored in `tools/plugins/config.json`:

```json
{
  "enabled": [
    "word_count",
    "reading_time",
    "backlink_updater"
  ]
}
```

Use `manage.sh enable/disable` to modify this, or edit directly.

## Built-in Plugins

| Plugin | Hook | Description |
|--------|------|-------------|
| `auto_tag` | post_ingest | Suggests tags via TF-IDF keyword extraction |
| `word_count` | post_compile | Tracks word count stats in `_meta/stats.json` |
| `reading_time` | post_compile | Adds reading time estimates to frontmatter |
| `duplicate_detector` | pre_ingest | Checks for similar existing articles (Jaccard similarity) |
| `backlink_updater` | post_compile | Rebuilds `_meta/links.md` and detects orphan pages |
| `citation_checker` | on_lint | Verifies concept articles cite their sources |
| `freshness_scorer` | on_lint | Scores articles by freshness, flags stale content |
| `glossary_builder` | post_compile | Builds `Glossary.md` from defined terms |
| `reading_list` | post_compile | Generates prioritized `Reading-List.md` by topic |
| `changelog` | post_compile | Generates `Changelog.md` from git history |

## Integration with Existing Tools

To call hooks from your existing ingest/compile scripts, add:

```bash
# At the end of an ingest script:
python3 tools/plugins/framework.py run post_ingest "$FILE_PATH"

# At the end of a compile step:
python3 tools/plugins/framework.py run post_compile

# In a lint script:
python3 tools/plugins/framework.py run on_lint
```

Or use the shell wrapper:

```bash
./tools/plugins/manage.sh run post_compile
```
