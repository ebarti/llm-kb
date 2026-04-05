#!/usr/bin/env python3
"""
HTTP server for the wiki search engine web UI.
Serves the web interface and provides a JSON search API.
Default port: 8888
"""

import json
import os
import re
import sys
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

# Import search engine
sys.path.insert(0, str(Path(__file__).resolve().parent))
from search import (
    get_index, search_with_snippets, parse_frontmatter, tokenize,
    WIKI_DIR, extract_wikilinks
)

WEB_DIR = Path(__file__).resolve().parent / "web"
PORT = 8888


def markdown_to_html(md_text):
    """Simple markdown-to-HTML conversion (stdlib only)."""
    html = md_text

    # Escape HTML entities first (but preserve our own tags added later)
    html = html.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Headers
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    # Bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)

    # Wikilinks → clickable links
    def wikilink_replace(m):
        target = m.group(1)
        label = target.split("/")[-1].replace("-", " ").title()
        return f'<a class="wikilink" href="#" data-target="{target}">{label}</a>'
    html = re.sub(r'\[\[([^\]]+)\]\]', wikilink_replace, html)

    # Regular links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank">\1</a>', html)

    # Unordered lists
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    # Wrap consecutive <li> in <ul>
    html = re.sub(r'((?:<li>.*?</li>\n?)+)', r'<ul>\1</ul>', html)

    # Horizontal rule
    html = re.sub(r'^---+$', '<hr>', html, flags=re.MULTILINE)

    # Paragraphs (double newline)
    parts = re.split(r'\n\n+', html)
    processed = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith('<h') or part.startswith('<ul') or part.startswith('<hr'):
            processed.append(part)
        else:
            processed.append(f'<p>{part}</p>')
    html = '\n'.join(processed)

    # Single newlines → <br> within paragraphs
    html = re.sub(r'(?<!</li>)\n(?!<)', '<br>\n', html)

    return html


class SearchHandler(SimpleHTTPRequestHandler):
    """Handle search API and static file requests."""

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/search":
            self.handle_search(parsed.query)
        elif path == "/api/article":
            self.handle_article(parsed.query)
        elif path == "/api/stats":
            self.handle_stats()
        elif path == "/api/graph":
            self.handle_graph()
        elif path == "/api/tags":
            self.handle_tags()
        else:
            self.serve_static(path)

    def send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(body))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def handle_search(self, query_string):
        params = urllib.parse.parse_qs(query_string)
        q = params.get("q", [""])[0]
        doc_type = params.get("type", [None])[0]
        tags = params.get("tags", [None])[0]
        top = int(params.get("top", [20])[0])

        if not q:
            self.send_json({"results": [], "query": ""})
            return

        index = get_index()
        tag_list = [t.strip() for t in tags.split(",")] if tags else None

        results = search_with_snippets(
            q, index,
            doc_type=doc_type if doc_type and doc_type != "all" else None,
            tags=tag_list,
            top_n=top,
        )
        self.send_json({"results": results, "query": q})

    def handle_article(self, query_string):
        params = urllib.parse.parse_qs(query_string)
        doc_id = params.get("id", [""])[0]

        if not doc_id:
            self.send_json({"error": "Missing id"}, 400)
            return

        path = WIKI_DIR / (doc_id + ".md")
        if not path.exists():
            self.send_json({"error": "Not found"}, 404)
            return

        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        html_body = markdown_to_html(body)

        index = get_index()
        doc_info = index["docs"].get(doc_id, {})
        backlinks = index["backlinks"].get(doc_id, [])

        # Find related articles with titles
        related = []
        for link in doc_info.get("links", []):
            link_clean = link.replace("[[", "").replace("]]", "")
            if link_clean in index["docs"]:
                related.append({
                    "id": link_clean,
                    "title": index["docs"][link_clean]["title"]
                })

        # Backlinks with titles
        backlink_details = []
        for bl in backlinks:
            if bl in index["docs"]:
                backlink_details.append({
                    "id": bl,
                    "title": index["docs"][bl]["title"]
                })

        self.send_json({
            "id": doc_id,
            "title": meta.get("title", doc_id),
            "type": doc_info.get("type", "unknown"),
            "date": doc_info.get("date", ""),
            "summary": meta.get("summary", ""),
            "body_html": html_body,
            "body_md": body,
            "related": related,
            "backlinks": backlink_details,
            "tags": doc_info.get("tags", []),
        })

    def handle_stats(self):
        index = get_index()
        from collections import Counter
        types = Counter(d["type"] for d in index["docs"].values())
        self.send_json({
            "total": len(index["docs"]),
            "concepts": types.get("concept", 0),
            "sources": types.get("source", 0),
            "entities": types.get("entity", 0),
            "comparisons": types.get("comparison", 0),
            "vocabulary": len(index.get("vocab", [])),
        })

    def handle_graph(self):
        index = get_index()
        nodes = []
        edges = []
        seen_nodes = set()

        for doc_id, doc_info in index["docs"].items():
            nodes.append({
                "id": doc_id,
                "title": doc_info["title"],
                "type": doc_info["type"],
            })
            seen_nodes.add(doc_id)

        for doc_id, doc_info in index["docs"].items():
            for link in doc_info.get("links", []):
                link_clean = link.replace("[[", "").replace("]]", "")
                if link_clean in seen_nodes:
                    edges.append({
                        "source": doc_id,
                        "target": link_clean,
                    })

        self.send_json({"nodes": nodes, "edges": edges})

    def handle_tags(self):
        index = get_index()
        from collections import Counter
        tag_counts = Counter()
        for doc_info in index["docs"].values():
            for tag in doc_info.get("tags", []):
                tag_counts[tag] += 1
        self.send_json({"tags": dict(tag_counts)})

    def serve_static(self, path):
        if path == "/" or path == "":
            path = "/index.html"

        file_path = WEB_DIR / path.lstrip("/")
        if not file_path.exists() or not file_path.is_file():
            self.send_error(404)
            return

        content = file_path.read_bytes()
        ext = file_path.suffix.lower()
        content_types = {
            ".html": "text/html",
            ".css": "text/css",
            ".js": "application/javascript",
            ".json": "application/json",
            ".svg": "image/svg+xml",
            ".png": "image/png",
            ".ico": "image/x-icon",
        }
        ctype = content_types.get(ext, "application/octet-stream")

        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)

    def log_message(self, fmt, *args):
        # Quieter logging
        if "/api/" in (args[0] if args else ""):
            return
        super().log_message(fmt, *args)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Wiki search engine web server")
    parser.add_argument("--port", type=int, default=PORT, help=f"Port (default: {PORT})")
    parser.add_argument("--rebuild", action="store_true", help="Force index rebuild on start")
    args = parser.parse_args()

    # Ensure index exists
    print("Loading search index...")
    get_index(force_rebuild=args.rebuild)
    print("Index ready.")

    server = HTTPServer(("0.0.0.0", args.port), SearchHandler)
    print(f"Wiki search server running at http://localhost:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
