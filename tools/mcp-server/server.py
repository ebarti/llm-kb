#!/usr/bin/env python3
"""
MCP (Model Context Protocol) server for the LLM Knowledge Base wiki.

Exposes the wiki at WIKI_ROOT as tools over JSON-RPC 2.0 stdio.
Uses only Python stdlib — no pip packages required.
"""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────────────────

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", os.getcwd()))
WIKI_DIR = WIKI_ROOT / "wiki"
RAW_DIR = WIKI_ROOT / "raw"

PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "kb-wiki"
SERVER_VERSION = "1.0.0"

# ── Tool definitions ──────────────────────────────────────────────────────

TOOLS = [
    {
        "name": "wiki_search",
        "description": (
            "Search the knowledge-base wiki. Returns ranked results with "
            "title, path, summary snippet, and relevance score."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query (keywords or phrase)",
                },
                "type": {
                    "type": "string",
                    "enum": ["concept", "source", "entity", "comparison"],
                    "description": "Optional: restrict to article type",
                },
                "top_k": {
                    "type": "integer",
                    "description": "Max results to return (default 10)",
                    "default": 10,
                },
            },
            "required": ["query"],
        },
    },
    {
        "name": "wiki_read",
        "description": "Read the full markdown content of a wiki article.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": (
                        "Path relative to wiki root, e.g. "
                        '"concepts/llm-knowledge-base" or '
                        '"sources/karpathy-llm-knowledge-bases"'
                    ),
                }
            },
            "required": ["path"],
        },
    },
    {
        "name": "wiki_index",
        "description": "Get the master wiki index (table of contents).",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "wiki_summaries",
        "description": "Get one-line summaries of every wiki article.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "wiki_links",
        "description": "Get the backlink / link-graph for the wiki or a specific article.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "article": {
                    "type": "string",
                    "description": (
                        "Optional article path (e.g. 'concepts/llm-knowledge-base'). "
                        "If omitted returns the full link graph."
                    ),
                }
            },
        },
    },
    {
        "name": "wiki_stats",
        "description": "Get wiki statistics: article counts by type, total words, last updated.",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "wiki_log",
        "description": "Get recent activity-log entries from the wiki.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "n": {
                    "type": "integer",
                    "description": "Number of recent log entries (default 10)",
                    "default": 10,
                }
            },
        },
    },
    {
        "name": "wiki_related",
        "description": "Find articles related to a given article via backlinks and shared concepts.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "article": {
                    "type": "string",
                    "description": "Article path, e.g. 'concepts/llm-knowledge-base'",
                }
            },
            "required": ["article"],
        },
    },
]

# ── Helpers ────────────────────────────────────────────────────────────────


def _read_file(path: Path) -> str | None:
    """Read a file, return None if missing."""
    try:
        return path.read_text(encoding="utf-8")
    except (FileNotFoundError, IsADirectoryError):
        return None


def _list_md(directory: Path) -> list[Path]:
    """List .md files in a directory (non-recursive)."""
    if not directory.is_dir():
        return []
    return sorted(p for p in directory.iterdir() if p.suffix == ".md")


def _extract_title(text: str) -> str:
    """Pull title from YAML front-matter or first heading."""
    m = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        return m.group(1)
    return "(untitled)"


def _word_count(text: str) -> int:
    return len(text.split())


def _score_document(query_terms: list[str], text: str, title: str) -> float:
    """Simple TF-based relevance scoring."""
    text_lower = text.lower()
    title_lower = title.lower()
    score = 0.0
    for term in query_terms:
        t = term.lower()
        # title match is worth more
        if t in title_lower:
            score += 10.0
        count = text_lower.count(t)
        if count:
            score += min(count, 20)  # cap per-term
    return score


def _snippet(text: str, query_terms: list[str], context: int = 120) -> str:
    """Extract a snippet around the first query-term match."""
    text_clean = re.sub(r"^---.*?---", "", text, count=1, flags=re.DOTALL).strip()
    lower = text_clean.lower()
    best_pos = len(text_clean)
    for t in query_terms:
        pos = lower.find(t.lower())
        if pos != -1 and pos < best_pos:
            best_pos = pos
    if best_pos == len(text_clean):
        # no match — return beginning
        return text_clean[:context * 2].replace("\n", " ").strip() + "..."
    start = max(0, best_pos - context)
    end = min(len(text_clean), best_pos + context)
    snippet = text_clean[start:end].replace("\n", " ").strip()
    if start > 0:
        snippet = "..." + snippet
    if end < len(text_clean):
        snippet = snippet + "..."
    return snippet


# ── Tool implementations ──────────────────────────────────────────────────


def tool_wiki_search(arguments: dict) -> str:
    query = arguments.get("query", "")
    article_type = arguments.get("type")
    top_k = arguments.get("top_k", 10)

    query_terms = [t for t in query.lower().split() if len(t) > 1]
    if not query_terms:
        return json.dumps({"results": [], "message": "Empty query"})

    type_dirs = {
        "concept": "concepts",
        "source": "sources",
        "entity": "entities",
        "comparison": "comparisons",
    }

    dirs_to_search: list[tuple[str, Path]] = []
    if article_type and article_type in type_dirs:
        d = WIKI_DIR / type_dirs[article_type]
        dirs_to_search.append((article_type, d))
    else:
        for t, dirname in type_dirs.items():
            d = WIKI_DIR / dirname
            dirs_to_search.append((t, d))

    results = []
    for atype, directory in dirs_to_search:
        for md in _list_md(directory):
            text = _read_file(md) or ""
            title = _extract_title(text)
            score = _score_document(query_terms, text, title)
            if score > 0:
                rel_path = f"{atype}s/{md.stem}" if not md.parent.name.endswith("s") else f"{md.parent.name}/{md.stem}"
                results.append(
                    {
                        "title": title,
                        "path": rel_path,
                        "summary": _snippet(text, query_terms, 100),
                        "relevance_score": round(score, 2),
                        "snippet": _snippet(text, query_terms),
                    }
                )

    results.sort(key=lambda r: r["relevance_score"], reverse=True)
    return json.dumps({"results": results[:top_k]}, indent=2)


def tool_wiki_read(arguments: dict) -> str:
    rel = arguments.get("path", "")
    # Normalise: strip leading wiki/, add .md if needed
    rel = rel.removeprefix("wiki/")
    if not rel.endswith(".md"):
        rel += ".md"
    full = WIKI_DIR / rel
    content = _read_file(full)
    if content is None:
        return f"Error: article not found at wiki/{rel}"
    return content


def tool_wiki_index(_arguments: dict) -> str:
    content = _read_file(WIKI_DIR / "_index.md")
    return content or "Error: _index.md not found"


def tool_wiki_summaries(_arguments: dict) -> str:
    content = _read_file(WIKI_DIR / "_meta" / "summaries.md")
    return content or "Error: summaries.md not found"


def tool_wiki_links(arguments: dict) -> str:
    content = _read_file(WIKI_DIR / "_meta" / "links.md")
    if content is None:
        return "Error: links.md not found"

    article = arguments.get("article")
    if not article:
        return content

    # Extract section for specific article
    article_clean = article.removeprefix("wiki/").removesuffix(".md")
    lines = content.split("\n")
    result_lines: list[str] = []
    capture = False
    for line in lines:
        if line.startswith("## "):
            heading_path = line[3:].strip()
            if heading_path == article_clean:
                capture = True
                result_lines.append(line)
                continue
            elif capture:
                break
        if capture:
            result_lines.append(line)

    if not result_lines:
        return f"No link data found for article: {article_clean}"
    return "\n".join(result_lines)


def tool_wiki_stats(_arguments: dict) -> str:
    stats: dict = {}
    total_words = 0

    for label, dirname in [
        ("total_sources", "sources"),
        ("total_concepts", "concepts"),
        ("total_entities", "entities"),
        ("total_comparisons", "comparisons"),
    ]:
        d = WIKI_DIR / dirname
        files = _list_md(d)
        stats[label] = len(files)
        for f in files:
            text = _read_file(f) or ""
            total_words += _word_count(text)

    stats["total_words"] = total_words

    # last_updated from _index.md front-matter
    idx = _read_file(WIKI_DIR / "_index.md") or ""
    m = re.search(r"last_updated:\s*(\S+)", idx)
    stats["last_updated"] = m.group(1) if m else "unknown"

    return json.dumps(stats, indent=2)


def tool_wiki_log(arguments: dict) -> str:
    n = arguments.get("n", 10)
    content = _read_file(WIKI_DIR / "log.md")
    if content is None:
        return "Error: log.md not found"

    # Each entry starts with ## [date]
    entries = re.split(r"(?=^## \[)", content, flags=re.MULTILINE)
    # First chunk is the header
    header_parts = [e for e in entries if not e.startswith("## [")]
    log_entries = [e.strip() for e in entries if e.startswith("## [")]

    recent = log_entries[:n]
    if not recent:
        return "No log entries found."
    return "\n\n".join(recent)


def tool_wiki_related(arguments: dict) -> str:
    article = arguments.get("article", "").removeprefix("wiki/").removesuffix(".md")
    if not article:
        return "Error: article parameter required"

    links_content = _read_file(WIKI_DIR / "_meta" / "links.md") or ""

    # Parse the link graph
    outgoing: dict[str, set[str]] = {}
    incoming: dict[str, set[str]] = {}
    current_article = None

    for line in links_content.split("\n"):
        if line.startswith("## "):
            current_article = line[3:].strip()
        elif current_article and line.startswith("→"):
            refs = re.findall(r"\[\[(.+?)\]\]", line)
            outgoing.setdefault(current_article, set()).update(refs)
            for ref in refs:
                incoming.setdefault(ref, set()).add(current_article)
        elif current_article and line.startswith("←"):
            refs = re.findall(r"\[\[(.+?)\]\]", line)
            incoming.setdefault(current_article, set()).update(refs)

    related: dict[str, str] = {}  # path -> reason

    # 1. Direct outgoing links
    for target in outgoing.get(article, set()):
        related[target] = "directly linked from this article"

    # 2. Articles that link to this one
    for source in incoming.get(article, set()):
        if source not in related:
            related[source] = "links to this article"

    # 3. Articles sharing outgoing links (co-citation)
    my_targets = outgoing.get(article, set())
    for other_article, other_targets in outgoing.items():
        if other_article == article or other_article in related:
            continue
        shared = my_targets & other_targets
        if len(shared) >= 2:
            shared_list = ", ".join(sorted(shared)[:3])
            related[other_article] = f"shares links to {shared_list}"

    results = [{"path": k, "reason": v} for k, v in sorted(related.items())]
    return json.dumps({"article": article, "related": results}, indent=2)


TOOL_DISPATCH = {
    "wiki_search": tool_wiki_search,
    "wiki_read": tool_wiki_read,
    "wiki_index": tool_wiki_index,
    "wiki_summaries": tool_wiki_summaries,
    "wiki_links": tool_wiki_links,
    "wiki_stats": tool_wiki_stats,
    "wiki_log": tool_wiki_log,
    "wiki_related": tool_wiki_related,
}

# ── JSON-RPC server loop ─────────────────────────────────────────────────


def _send(obj: dict) -> None:
    """Write a JSON-RPC message to stdout."""
    data = json.dumps(obj)
    sys.stdout.write(data + "\n")
    sys.stdout.flush()


def _error_response(req_id, code: int, message: str) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": code, "message": message}}


def _result_response(req_id, result) -> dict:
    return {"jsonrpc": "2.0", "id": req_id, "result": result}


def handle_initialize(req_id, _params: dict) -> dict:
    return _result_response(
        req_id,
        {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        },
    )


def handle_tools_list(req_id, _params: dict) -> dict:
    return _result_response(req_id, {"tools": TOOLS})


def handle_tools_call(req_id, params: dict) -> dict:
    name = params.get("name", "")
    arguments = params.get("arguments", {})

    handler = TOOL_DISPATCH.get(name)
    if not handler:
        return _error_response(req_id, -32602, f"Unknown tool: {name}")

    try:
        text = handler(arguments)
    except Exception as e:
        text = f"Error executing {name}: {e}"

    return _result_response(
        req_id,
        {"content": [{"type": "text", "text": text}]},
    )


def main() -> None:
    """Read JSON-RPC messages from stdin, dispatch, respond on stdout."""
    # Redirect any accidental prints to stderr
    log = sys.stderr

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        try:
            msg = json.loads(line)
        except json.JSONDecodeError as e:
            log.write(f"[mcp-server] Bad JSON: {e}\n")
            continue

        method = msg.get("method", "")
        req_id = msg.get("id")
        params = msg.get("params", {})

        # Notifications (no id) — just acknowledge silently
        if req_id is None:
            log.write(f"[mcp-server] Notification: {method}\n")
            continue

        if method == "initialize":
            _send(handle_initialize(req_id, params))
        elif method == "tools/list":
            _send(handle_tools_list(req_id, params))
        elif method == "tools/call":
            _send(handle_tools_call(req_id, params))
        else:
            _send(_error_response(req_id, -32601, f"Method not found: {method}"))


if __name__ == "__main__":
    main()
