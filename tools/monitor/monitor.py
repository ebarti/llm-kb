#!/usr/bin/env python3
"""
Topic Monitor — searches the web for new content matching tracked topics.

Reads topics.json, searches for each query using date filters,
compares against the wiki manifest to skip already-ingested URLs,
and outputs new sources to ingest.

Usage:
    python3 tools/monitor/monitor.py              # print new sources found
    python3 tools/monitor/monitor.py --ingest      # also trigger ingestion via ./kb ingest
    python3 tools/monitor/monitor.py --days 7      # look back 7 days (default: 3)
    python3 tools/monitor/monitor.py --topic "RAG"  # only check topics matching name
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import quote_plus, urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError
import html.parser

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
KB_DIR = SCRIPT_DIR.parent.parent
TOPICS_FILE = SCRIPT_DIR / "topics.json"
MANIFEST_FILE = KB_DIR / "wiki" / "_meta" / "manifest.md"
STATE_FILE = SCRIPT_DIR / ".state" / "monitor_state.json"
LOG_DIR = SCRIPT_DIR / ".logs"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_topics():
    """Load topic configuration."""
    with open(TOPICS_FILE) as f:
        return json.load(f)


def load_manifest_urls():
    """Extract URLs/source identifiers already in the manifest."""
    known = set()
    if not MANIFEST_FILE.exists():
        return known
    text = MANIFEST_FILE.read_text()
    # Extract raw file stems — these correspond to ingested sources
    for m in re.finditer(r'`raw/([\w\-]+)\.md`', text):
        known.add(m.group(1).lower())
    return known


def load_raw_filenames():
    """Get all raw file stems so we can skip already-ingested content."""
    raw_dir = KB_DIR / "raw"
    stems = set()
    if raw_dir.exists():
        for f in raw_dir.iterdir():
            if f.suffix == ".md":
                stems.add(f.stem.lower())
    return stems


def load_state():
    """Load persistent monitor state (last-run timestamps, seen URLs)."""
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"seen_urls": [], "last_run": None}


def save_state(state):
    """Persist monitor state."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state["last_run"] = datetime.now().isoformat()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def is_excluded(url, exclude_domains):
    """Check if a URL belongs to an excluded domain."""
    try:
        domain = urlparse(url).netloc.lower()
        return any(ex in domain for ex in exclude_domains)
    except Exception:
        return False


def is_preferred(url, prefer_domains):
    """Check if a URL belongs to a preferred domain."""
    try:
        domain = urlparse(url).netloc.lower()
        return any(pref in domain for pref in prefer_domains)
    except Exception:
        return False


def slug_from_url(url):
    """Create a slug from a URL for comparison against known sources."""
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "-")
    slug = re.sub(r'[^a-z0-9\-]', '', path.lower())
    return slug


# ---------------------------------------------------------------------------
# Web search via DuckDuckGo HTML (stdlib only, no API key)
# ---------------------------------------------------------------------------

class DDGParser(html.parser.HTMLParser):
    """Minimal parser to extract result links from DuckDuckGo HTML search."""

    def __init__(self):
        super().__init__()
        self.results = []
        self._in_result = False
        self._current = {}

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        # DuckDuckGo lite result links
        if tag == "a" and "href" in attrs_dict:
            href = attrs_dict["href"]
            if href.startswith("http") and "duckduckgo.com" not in href:
                self.results.append({"url": href, "title": ""})

    def handle_data(self, data):
        if self.results and not self.results[-1].get("title"):
            self.results[-1]["title"] = data.strip()


def search_web(query, max_results=5, days_back=3):
    """
    Search the web using DuckDuckGo Lite (no API key needed).
    Returns list of {"url": ..., "title": ...}.
    Falls back gracefully on network errors.
    """
    # Add date filter to query
    date_str = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    full_query = f"{query} after:{date_str}"

    url = f"https://lite.duckduckgo.com/lite/?q={quote_plus(full_query)}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        req = Request(url, headers=headers)
        with urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", errors="replace")

        parser = DDGParser()
        parser.feed(body)
        # Deduplicate by URL
        seen = set()
        unique = []
        for r in parser.results:
            if r["url"] not in seen:
                seen.add(r["url"])
                unique.append(r)
            if len(unique) >= max_results:
                break
        return unique
    except (URLError, OSError, TimeoutError) as e:
        print(f"  [warn] Search failed for '{query}': {e}", file=sys.stderr)
        return []


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def discover_new_sources(topics_config, days_back=3, topic_filter=None):
    """
    For each topic, search the web and return new (not-yet-ingested) sources.
    Returns: list of {"topic": ..., "url": ..., "title": ..., "preferred": bool}
    """
    manifest_slugs = load_manifest_urls()
    raw_stems = load_raw_filenames()
    known = manifest_slugs | raw_stems
    state = load_state()
    seen_urls = set(state.get("seen_urls", []))

    max_results = topics_config.get("max_results_per_query", 5)
    exclude = topics_config.get("exclude_domains", [])
    prefer = topics_config.get("prefer_domains", [])

    new_sources = []

    for topic in topics_config.get("topics", []):
        name = topic["name"]
        if topic_filter and topic_filter.lower() not in name.lower():
            continue

        print(f"\n--- {name} ---")
        for query in topic.get("queries", []):
            print(f"  Searching: {query}")
            results = search_web(query, max_results=max_results, days_back=days_back)

            for r in results:
                url = r["url"]
                title = r.get("title", "")

                # Skip excluded domains
                if is_excluded(url, exclude):
                    continue

                # Skip already-known URLs
                slug = slug_from_url(url)
                if slug in known or url in seen_urls:
                    continue

                preferred = is_preferred(url, prefer)
                entry = {
                    "topic": name,
                    "url": url,
                    "title": title,
                    "preferred": preferred,
                }
                new_sources.append(entry)
                seen_urls.add(url)

    # Sort: preferred domains first
    new_sources.sort(key=lambda x: (not x["preferred"], x["topic"]))

    # Update state
    state["seen_urls"] = list(seen_urls)[-500:]  # keep last 500
    save_state(state)

    return new_sources


def print_sources(sources):
    """Pretty-print discovered sources."""
    if not sources:
        print("\nNo new sources found.")
        return

    print(f"\n{'='*60}")
    print(f"  Found {len(sources)} new source(s)")
    print(f"{'='*60}")

    current_topic = None
    for s in sources:
        if s["topic"] != current_topic:
            current_topic = s["topic"]
            print(f"\n  [{current_topic}]")
        star = " *" if s["preferred"] else ""
        print(f"    {s['title'][:70]}")
        print(f"    {s['url']}{star}")
        print()


def ingest_sources(sources):
    """Trigger ingestion for each discovered source via ./kb ingest."""
    if not sources:
        print("Nothing to ingest.")
        return

    kb_script = KB_DIR / "kb"
    if not kb_script.exists():
        print(f"[error] kb script not found at {kb_script}", file=sys.stderr)
        return

    urls = [s["url"] for s in sources]
    print(f"\nIngesting {len(urls)} source(s) via ./kb ingest ...")
    for url in urls:
        print(f"  -> {url}")
        try:
            subprocess.run(
                [str(kb_script), "ingest", url],
                cwd=str(KB_DIR),
                timeout=120,
            )
        except subprocess.TimeoutExpired:
            print(f"  [warn] Timed out ingesting {url}", file=sys.stderr)
        except Exception as e:
            print(f"  [warn] Failed to ingest {url}: {e}", file=sys.stderr)


def log_run(sources):
    """Append a log entry for this run."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOG_DIR / "monitor.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] Found {len(sources)} new source(s)\n")
        for s in sources:
            f.write(f"  {s['topic']}: {s['url']}\n")
        f.write("\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Topic Monitor — discover new content for the knowledge base"
    )
    parser.add_argument(
        "--ingest", action="store_true",
        help="Also trigger ingestion via ./kb ingest"
    )
    parser.add_argument(
        "--days", type=int, default=3,
        help="Look back N days (default: 3)"
    )
    parser.add_argument(
        "--topic", type=str, default=None,
        help="Only check topics matching this name"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be found without updating state"
    )
    args = parser.parse_args()

    config = load_topics()

    print("Topic Monitor")
    print(f"Looking back {args.days} day(s)...")

    sources = discover_new_sources(
        config,
        days_back=args.days,
        topic_filter=args.topic,
    )

    print_sources(sources)
    log_run(sources)

    if args.ingest and sources:
        ingest_sources(sources)

    # Exit code: 0 if new sources found, 1 if none
    sys.exit(0 if sources else 1)


if __name__ == "__main__":
    main()
