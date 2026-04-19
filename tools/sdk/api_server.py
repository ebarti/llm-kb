#!/usr/bin/env python3
"""
JSON API Server for the LLM Knowledge Base.

Simple HTTP server using stdlib http.server. CORS enabled.
Default port: 8889.

Endpoints:
    GET /api/index          -- Wiki index
    GET /api/articles       -- List articles (?type=concept)
    GET /api/article/<path> -- Single article (e.g. /api/article/concepts/llm-knowledge-base)
    GET /api/search         -- Search (?q=query&type=concept&top_k=10)
    GET /api/stats          -- Statistics
    GET /api/links          -- Link graph (?article=path)
    GET /api/tags           -- Tag cloud
    GET /api/log            -- Activity log (?n=10)
    GET /api/summaries      -- Article summaries
    GET /api/orphans        -- Orphan articles
    GET /api/hubs           -- Hub articles (?top_k=10)
    GET /api/backlinks      -- Backlinks (?article=path)

Usage:
    python3 tools/sdk/api_server.py
    python3 tools/sdk/api_server.py --port 9000
    python3 tools/sdk/api_server.py --kb-path /path/to/kb
"""

import sys
import os
import json
import argparse
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb import KnowledgeBase


# Module-level reference set by main()
_kb: KnowledgeBase = None  # type: ignore


class KBRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for the KB JSON API."""

    def _send_json(self, data: object, status: int = 200):
        """Send a JSON response with CORS headers."""
        body = json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_error(self, status: int, message: str):
        """Send a JSON error response."""
        self._send_json({"error": message}, status=status)

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        """Route GET requests to the appropriate handler."""
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        params = parse_qs(parsed.query)

        # Helper to get single query param
        def param(name: str, default=None):
            vals = params.get(name, [])
            return vals[0] if vals else default

        try:
            if path == "/api/index":
                self._send_json(_kb.get_index())

            elif path == "/api/articles":
                articles = _kb.get_articles(
                    type=param("type"),
                    tag=param("tag"),
                )
                # Return lightweight list (no full content by default)
                lightweight = []
                for a in articles:
                    lightweight.append({
                        "path": a["path"],
                        "title": a["frontmatter"].get("title", a["path"]),
                        "type": a["frontmatter"].get("type", ""),
                        "summary": a["frontmatter"].get("summary", ""),
                    })
                self._send_json(lightweight)

            elif path.startswith("/api/article/"):
                article_path = path[len("/api/article/"):]
                if not article_path:
                    self._send_error(400, "Article path required")
                    return
                try:
                    self._send_json(_kb.get_article(article_path))
                except FileNotFoundError:
                    self._send_error(404, f"Article not found: {article_path}")

            elif path == "/api/search":
                query = param("q", "")
                if not query:
                    self._send_error(400, "Query parameter 'q' required")
                    return
                top_k = int(param("top_k", "10"))
                results = _kb.search(query, type=param("type"), top_k=top_k)
                self._send_json(results)

            elif path == "/api/stats":
                self._send_json(_kb.get_stats())

            elif path == "/api/links":
                article = param("article")
                self._send_json(_kb.get_links(article=article))

            elif path == "/api/tags":
                self._send_json(_kb.get_tag_cloud())

            elif path == "/api/log":
                n = int(param("n", "10"))
                self._send_json(_kb.get_log(n=n))

            elif path == "/api/summaries":
                self._send_json(_kb.get_summaries())

            elif path == "/api/orphans":
                self._send_json(_kb.get_orphans())

            elif path == "/api/hubs":
                top_k = int(param("top_k", "10"))
                self._send_json(_kb.get_hubs(top_k=top_k))

            elif path == "/api/backlinks":
                article = param("article")
                if not article:
                    self._send_error(400, "Query parameter 'article' required")
                    return
                self._send_json(_kb.get_backlinks(article))

            elif path == "/" or path == "":
                self._send_json({
                    "name": "LLM Knowledge Base API",
                    "version": "1.0.0",
                    "endpoints": [
                        "GET /api/index",
                        "GET /api/articles?type=&tag=",
                        "GET /api/article/<path>",
                        "GET /api/search?q=&type=&top_k=",
                        "GET /api/stats",
                        "GET /api/links?article=",
                        "GET /api/tags",
                        "GET /api/log?n=",
                        "GET /api/summaries",
                        "GET /api/orphans",
                        "GET /api/hubs?top_k=",
                        "GET /api/backlinks?article=",
                    ],
                })

            else:
                self._send_error(404, f"Unknown endpoint: {path}")

        except Exception as e:
            self._send_error(500, str(e))

    def log_message(self, format, *args):
        """Quieter logging -- just method, path, status."""
        sys.stderr.write(f"[KB API] {args[0]}\n")


def main():
    parser = argparse.ArgumentParser(description="LLM Knowledge Base JSON API Server")
    parser.add_argument("--port", type=int, default=8889, help="Port (default: 8889)")
    parser.add_argument("--host", default="localhost", help="Host (default: localhost)")
    parser.add_argument("--kb-path", default=None,
                        help="Path to the knowledge base root (defaults to repo root or $KB_PATH)")
    args = parser.parse_args()

    global _kb
    _kb = KnowledgeBase(path=args.kb_path)

    server = HTTPServer((args.host, args.port), KBRequestHandler)
    print(f"KB API Server running at http://{args.host}:{args.port}")
    print(f"Knowledge base: {args.kb_path}")
    print(f"Try: http://{args.host}:{args.port}/api/stats")
    print("Press Ctrl+C to stop.\n")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        server.server_close()


if __name__ == "__main__":
    main()
