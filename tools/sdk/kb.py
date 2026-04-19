#!/usr/bin/env python3
"""
Core SDK for the LLM Knowledge Base.

Provides programmatic access to all wiki content, metadata, search,
link graph traversal, and statistics. Stdlib only.

Usage:
    from tools.sdk.kb import KnowledgeBase
    kb = KnowledgeBase()
    stats = kb.get_stats()
    results = kb.search("knowledge graph")
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from typing import Optional


class KnowledgeBase:
    """Python SDK for reading, searching, and analyzing the LLM knowledge base."""

    def __init__(self, path: Optional[str] = None):
        """Initialize the KnowledgeBase with the root path of the project.

        Args:
            path: Absolute path to the KB project root. Defaults to the
                  repo root computed from this file's location, or the
                  KB_PATH environment variable if set.
        """
        if path is None:
            path = os.environ.get("KB_PATH") or str(Path(__file__).resolve().parents[2])
        self.root = Path(path)
        self.wiki_dir = self.root / "wiki"
        self.raw_dir = self.root / "raw"
        self.output_dir = self.root / "output"

        if not self.wiki_dir.exists():
            raise FileNotFoundError(f"Wiki directory not found: {self.wiki_dir}")

        # Cache for parsed articles (path_str -> parsed dict)
        self._article_cache: dict[str, dict] = {}
        # Cache for the full link graph
        self._link_graph: Optional[dict] = None

    # ------------------------------------------------------------------ #
    #  Parsing utilities
    # ------------------------------------------------------------------ #

    def parse_frontmatter(self, content: str) -> tuple[dict, str]:
        """Parse YAML-like frontmatter from markdown content.

        Handles the subset of YAML used in the wiki: scalars, lists of
        strings (inline JSON-style or dash-style), and quoted strings.

        Args:
            content: Raw markdown string.

        Returns:
            Tuple of (frontmatter_dict, body_text_without_frontmatter).
        """
        if not content.startswith("---"):
            return {}, content

        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}, content

        fm_text = parts[1].strip()
        body = parts[2].strip()
        meta: dict = {}

        for line in fm_text.split("\n"):
            line = line.strip()
            if not line or ":" not in line:
                continue
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()

            # Strip surrounding quotes
            if (value.startswith('"') and value.endswith('"')) or \
               (value.startswith("'") and value.endswith("'")):
                value = value[1:-1]

            # Inline JSON-style list: ["a", "b"]
            if value.startswith("["):
                try:
                    parsed = json.loads(value)
                    meta[key] = parsed
                except json.JSONDecodeError:
                    # Fallback: extract quoted strings
                    meta[key] = re.findall(r'"([^"]*)"', value)
            else:
                meta[key] = value

        return meta, body

    def extract_wikilinks(self, content: str) -> list[str]:
        """Extract all [[wikilink]] targets from markdown content.

        Handles [[link]] and [[link|display]] formats. Removes duplicates
        while preserving first-seen order.

        Args:
            content: Markdown text to scan.

        Returns:
            De-duplicated list of wikilink targets (the path portion).
        """
        matches = re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)
        seen: set[str] = set()
        result: list[str] = []
        for m in matches:
            m = m.strip()
            if m not in seen:
                seen.add(m)
                result.append(m)
        return result

    def resolve_wikilink(self, link: str) -> Optional[str]:
        """Resolve a wikilink target to an actual file path relative to wiki/.

        Tries exact match first, then searches all .md files for a
        basename match.

        Args:
            link: Wikilink target string (e.g. "concepts/llm-knowledge-base").

        Returns:
            Relative path from wiki/ (without .md extension) if found, else None.
        """
        # Exact match
        candidate = self.wiki_dir / (link + ".md")
        if candidate.exists():
            return link

        # Search by basename
        target_name = link.split("/")[-1]
        for md_file in self.wiki_dir.rglob("*.md"):
            if md_file.stem == target_name:
                return str(md_file.relative_to(self.wiki_dir))[:-3]  # strip .md

        return None

    # ------------------------------------------------------------------ #
    #  Reading
    # ------------------------------------------------------------------ #

    def get_index(self) -> dict:
        """Read and parse the master wiki index (_index.md).

        Returns:
            Dict with keys: frontmatter (dict), content (str),
            links (list of wikilink targets).
        """
        return self.get_article("_index")

    def get_summaries(self) -> list[dict]:
        """Get one-line summaries for all articles from _meta/summaries.md.

        Returns:
            List of dicts with keys: path (str), summary (str).
        """
        summaries_path = self.wiki_dir / "_meta" / "summaries.md"
        if not summaries_path.exists():
            return []

        content = summaries_path.read_text(encoding="utf-8")
        results: list[dict] = []

        for line in content.split("\n"):
            # Lines like: - [[path/name]] -- summary text
            m = re.match(r'^- \[\[([^\]]+)\]\]\s*[-—]+\s*(.+)', line)
            if m:
                results.append({"path": m.group(1).strip(), "summary": m.group(2).strip()})

        return results

    def get_article(self, path: str) -> dict:
        """Read and parse a single wiki article.

        Args:
            path: Relative path from wiki/ without .md extension.
                  Example: "concepts/llm-knowledge-base"

        Returns:
            Dict with keys: path (str), frontmatter (dict), content (str),
            links (list of wikilink targets).

        Raises:
            FileNotFoundError: If the article does not exist.
        """
        if path in self._article_cache:
            return self._article_cache[path]

        file_path = self.wiki_dir / (path + ".md")
        if not file_path.exists():
            raise FileNotFoundError(f"Article not found: {file_path}")

        raw = file_path.read_text(encoding="utf-8")
        fm, body = self.parse_frontmatter(raw)
        links = self.extract_wikilinks(raw)

        article = {
            "path": path,
            "frontmatter": fm,
            "content": body,
            "links": links,
        }
        self._article_cache[path] = article
        return article

    def get_articles(self, type: Optional[str] = None, tag: Optional[str] = None) -> list[dict]:
        """List all wiki articles, optionally filtered by type or tag.

        Args:
            type: Filter by frontmatter 'type' value (e.g. "concept",
                  "source-summary", "entity"). Case-insensitive.
            tag: Filter by frontmatter 'tags' list or inline #tag.

        Returns:
            List of article dicts (same shape as get_article output).
        """
        articles: list[dict] = []
        for md_file in sorted(self.wiki_dir.rglob("*.md")):
            rel = str(md_file.relative_to(self.wiki_dir))[:-3]
            try:
                article = self.get_article(rel)
            except Exception:
                continue

            if type is not None:
                fm_type = article["frontmatter"].get("type", "")
                if fm_type.lower() != type.lower():
                    continue

            if tag is not None:
                fm_tags = article["frontmatter"].get("tags", [])
                tag_normalized = tag if tag.startswith("#") else f"#{tag}"
                if isinstance(fm_tags, list):
                    if tag_normalized not in fm_tags and tag not in fm_tags:
                        # Also check inline tags in content
                        if tag_normalized not in article["content"]:
                            continue
                else:
                    if tag_normalized not in article["content"]:
                        continue

            articles.append(article)
        return articles

    def get_log(self, n: int = 10) -> list[dict]:
        """Parse the activity log and return the most recent entries.

        Args:
            n: Number of recent entries to return.

        Returns:
            List of dicts with keys: date (str), action (str), description (str),
            details (list of str). Most recent first.
        """
        log_path = self.wiki_dir / "log.md"
        if not log_path.exists():
            return []

        content = log_path.read_text(encoding="utf-8")
        entries: list[dict] = []
        current: Optional[dict] = None

        for line in content.split("\n"):
            # Entries start with ## [date] action | description
            m = re.match(r'^## \[(\d{4}-\d{2}-\d{2})\]\s+(\w+)\s*\|\s*(.+)', line)
            if m:
                if current is not None:
                    entries.append(current)
                current = {
                    "date": m.group(1),
                    "action": m.group(2),
                    "description": m.group(3).strip(),
                    "details": [],
                }
            elif current is not None and line.startswith("- "):
                current["details"].append(line[2:].strip())

        if current is not None:
            entries.append(current)

        # Reverse so most recent is first (they're already chronological)
        entries.reverse()
        return entries[:n]

    # ------------------------------------------------------------------ #
    #  Search
    # ------------------------------------------------------------------ #

    def search(self, query: str, type: Optional[str] = None, top_k: int = 10) -> list[dict]:
        """Full-text search across all wiki articles.

        Scores articles by number of case-insensitive query-term matches
        in title, summary, and content. Fast and simple -- no dependencies.

        Args:
            query: Search query string (space-separated terms).
            type: Optional type filter (e.g. "concept").
            top_k: Maximum results to return.

        Returns:
            List of dicts with keys: path, title, summary, type, score.
            Sorted by descending score.
        """
        terms = query.lower().split()
        if not terms:
            return []

        articles = self.get_articles(type=type)
        scored: list[dict] = []

        for article in articles:
            fm = article["frontmatter"]
            title = fm.get("title", "").lower()
            summary = fm.get("summary", "").lower()
            content_lower = article["content"].lower()

            score = 0
            for term in terms:
                # Title matches are worth 5x
                score += title.count(term) * 5
                # Summary matches are worth 3x
                score += summary.count(term) * 3
                # Content matches
                score += content_lower.count(term)

            if score > 0:
                scored.append({
                    "path": article["path"],
                    "title": fm.get("title", article["path"]),
                    "summary": fm.get("summary", ""),
                    "type": fm.get("type", ""),
                    "score": score,
                })

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]

    # ------------------------------------------------------------------ #
    #  Graph
    # ------------------------------------------------------------------ #

    def _build_link_graph(self) -> dict:
        """Build the complete directed link graph from all articles.

        Returns:
            Dict with 'outgoing' and 'incoming' keys, each mapping
            article paths to lists of linked article paths.
        """
        if self._link_graph is not None:
            return self._link_graph

        outgoing: dict[str, list[str]] = defaultdict(list)
        incoming: dict[str, list[str]] = defaultdict(list)

        for md_file in self.wiki_dir.rglob("*.md"):
            rel = str(md_file.relative_to(self.wiki_dir))[:-3]
            try:
                article = self.get_article(rel)
            except Exception:
                continue

            for link in article["links"]:
                resolved = self.resolve_wikilink(link)
                if resolved and resolved != rel:
                    if resolved not in outgoing[rel]:
                        outgoing[rel].append(resolved)
                    if rel not in incoming[resolved]:
                        incoming[resolved].append(rel)

        self._link_graph = {
            "outgoing": dict(outgoing),
            "incoming": dict(incoming),
        }
        return self._link_graph

    def get_links(self, article: Optional[str] = None) -> dict:
        """Get the link graph, optionally for a single article.

        Args:
            article: If provided, return links for just this article.
                     Otherwise return the full graph.

        Returns:
            If article is specified: {"outgoing": [...], "incoming": [...]}.
            If not: full graph dict with outgoing/incoming maps.
        """
        graph = self._build_link_graph()
        if article is None:
            return graph

        return {
            "outgoing": graph["outgoing"].get(article, []),
            "incoming": graph["incoming"].get(article, []),
        }

    def get_backlinks(self, article: str) -> list[str]:
        """Get all articles that link TO the given article.

        Args:
            article: Path relative to wiki/ without .md.

        Returns:
            List of article paths that contain a wikilink to this article.
        """
        graph = self._build_link_graph()
        return graph["incoming"].get(article, [])

    def get_related(self, article: str, depth: int = 1) -> list[str]:
        """Get articles related to the given article via link traversal.

        Walks outgoing and incoming links up to `depth` hops, collecting
        all reachable articles (excluding the starting article).

        Args:
            article: Starting article path.
            depth: Number of hops to traverse (default 1).

        Returns:
            List of related article paths, sorted alphabetically.
        """
        graph = self._build_link_graph()
        visited: set[str] = set()
        frontier: set[str] = {article}

        for _ in range(depth):
            next_frontier: set[str] = set()
            for node in frontier:
                for neighbor in graph["outgoing"].get(node, []):
                    if neighbor not in visited and neighbor != article:
                        next_frontier.add(neighbor)
                for neighbor in graph["incoming"].get(node, []):
                    if neighbor not in visited and neighbor != article:
                        next_frontier.add(neighbor)
            visited.update(next_frontier)
            frontier = next_frontier

        return sorted(visited)

    def get_orphans(self) -> list[str]:
        """Find articles with no incoming links (orphans).

        Excludes meta files (_index, _meta/*, log, Dashboard, etc.)
        since those are structural.

        Returns:
            List of orphaned article paths.
        """
        graph = self._build_link_graph()
        all_articles: set[str] = set()

        for md_file in self.wiki_dir.rglob("*.md"):
            rel = str(md_file.relative_to(self.wiki_dir))[:-3]
            all_articles.add(rel)

        # Structural files to exclude from orphan detection
        structural = {"_index", "log", "Dashboard", "Graph", "Queries", "Tags"}
        structural_prefixes = ("_meta/",)

        orphans: list[str] = []
        for article in sorted(all_articles):
            if article in structural:
                continue
            if any(article.startswith(p) for p in structural_prefixes):
                continue
            if not graph["incoming"].get(article):
                orphans.append(article)

        return orphans

    def get_hubs(self, top_k: int = 10) -> list[dict]:
        """Find the most-connected articles (hubs).

        Ranks by total connections (incoming + outgoing).

        Args:
            top_k: Number of top hubs to return.

        Returns:
            List of dicts with keys: path, incoming (int), outgoing (int),
            total (int). Sorted by total descending.
        """
        graph = self._build_link_graph()
        all_articles: set[str] = set()

        for md_file in self.wiki_dir.rglob("*.md"):
            rel = str(md_file.relative_to(self.wiki_dir))[:-3]
            all_articles.add(rel)

        hubs: list[dict] = []
        for article in all_articles:
            out_count = len(graph["outgoing"].get(article, []))
            in_count = len(graph["incoming"].get(article, []))
            hubs.append({
                "path": article,
                "incoming": in_count,
                "outgoing": out_count,
                "total": in_count + out_count,
            })

        hubs.sort(key=lambda x: x["total"], reverse=True)
        return hubs[:top_k]

    # ------------------------------------------------------------------ #
    #  Stats
    # ------------------------------------------------------------------ #

    def get_stats(self) -> dict:
        """Compute comprehensive statistics about the knowledge base.

        Returns:
            Dict with keys: total_articles, by_type (dict), total_words,
            total_links, avg_words_per_article, orphan_count,
            raw_files (int), article_paths (list).
        """
        articles = self.get_articles()
        by_type: dict[str, int] = defaultdict(int)
        total_words = 0
        paths: list[str] = []

        for article in articles:
            fm_type = article["frontmatter"].get("type", "unknown")
            by_type[fm_type] += 1
            total_words += len(article["content"].split())
            paths.append(article["path"])

        graph = self._build_link_graph()
        total_links = sum(len(v) for v in graph["outgoing"].values())

        raw_count = 0
        if self.raw_dir.exists():
            raw_count = len(list(self.raw_dir.glob("*.md")))

        n = len(articles) or 1

        return {
            "total_articles": len(articles),
            "by_type": dict(by_type),
            "total_words": total_words,
            "total_links": total_links,
            "avg_words_per_article": total_words // n,
            "orphan_count": len(self.get_orphans()),
            "raw_files": raw_count,
            "article_paths": sorted(paths),
        }

    def get_word_count(self, path: Optional[str] = None) -> int:
        """Get word count for a single article or the entire wiki.

        Args:
            path: Article path (relative, no .md). If None, counts all articles.

        Returns:
            Word count as integer.
        """
        if path is not None:
            article = self.get_article(path)
            return len(article["content"].split())

        total = 0
        for md_file in self.wiki_dir.rglob("*.md"):
            rel = str(md_file.relative_to(self.wiki_dir))[:-3]
            try:
                article = self.get_article(rel)
                total += len(article["content"].split())
            except Exception:
                continue
        return total

    def get_tag_cloud(self) -> dict[str, int]:
        """Build a tag cloud from frontmatter tags and inline #tags.

        Returns:
            Dict mapping tag names to article counts, sorted by
            count descending.
        """
        tag_counts: dict[str, int] = defaultdict(int)

        for md_file in self.wiki_dir.rglob("*.md"):
            rel = str(md_file.relative_to(self.wiki_dir))[:-3]
            try:
                article = self.get_article(rel)
            except Exception:
                continue

            # Frontmatter tags
            fm_tags = article["frontmatter"].get("tags", [])
            if isinstance(fm_tags, list):
                for tag in fm_tags:
                    tag = tag.strip().lstrip("#")
                    if tag:
                        tag_counts[tag] += 1

            # Inline #tags (excluding things inside code blocks and links)
            content = article["content"]
            # Remove code blocks
            content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
            # Remove inline code
            content = re.sub(r'`[^`]+`', '', content)
            # Find #tags
            inline_tags = re.findall(r'(?<!\[)#([a-zA-Z][a-zA-Z0-9_-]+)', content)
            for tag in inline_tags:
                tag_counts[tag] += 1

        # Sort by count descending
        return dict(sorted(tag_counts.items(), key=lambda x: x[1], reverse=True))

    # ------------------------------------------------------------------ #
    #  Export
    # ------------------------------------------------------------------ #

    def export_all(self) -> dict:
        """Export the entire wiki as a single JSON-serializable dict.

        Returns:
            Dict with keys: articles (list), link_graph (dict),
            stats (dict), summaries (list).
        """
        articles = []
        for md_file in sorted(self.wiki_dir.rglob("*.md")):
            rel = str(md_file.relative_to(self.wiki_dir))[:-3]
            try:
                articles.append(self.get_article(rel))
            except Exception:
                continue

        return {
            "articles": articles,
            "link_graph": self._build_link_graph(),
            "stats": self.get_stats(),
            "summaries": self.get_summaries(),
        }


if __name__ == "__main__":
    kb = KnowledgeBase()
    stats = kb.get_stats()
    print(json.dumps(stats, indent=2))
