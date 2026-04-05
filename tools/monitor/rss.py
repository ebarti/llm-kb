#!/usr/bin/env python3
"""
RSS/Atom Feed Watcher — checks feeds for new entries relevant to wiki topics.

Reads feeds.json, checks each feed for new entries since last check,
filters by keyword relevance, and outputs new relevant entries.

Stores last-check timestamps in tools/monitor/.state/

Usage:
    python3 tools/monitor/rss.py
    python3 tools/monitor/rss.py --all          # show all new entries, not just relevant ones
    python3 tools/monitor/rss.py --since 3       # entries from last 3 days (default: 7)
    python3 tools/monitor/rss.py --json          # output as JSON
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
KB_DIR = SCRIPT_DIR.parent.parent
FEEDS_FILE = SCRIPT_DIR / "feeds.json"
STATE_DIR = SCRIPT_DIR / ".state"
LOG_DIR = SCRIPT_DIR / ".logs"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_feeds_config():
    """Load feed configuration."""
    with open(FEEDS_FILE) as f:
        return json.load(f)


def load_feed_state(feed_name):
    """Load last-check state for a specific feed."""
    state_file = STATE_DIR / f"feed_{sanitize_name(feed_name)}.json"
    if state_file.exists():
        with open(state_file) as f:
            return json.load(f)
    return {"last_check": None, "seen_ids": []}


def save_feed_state(feed_name, state):
    """Save feed state."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_file = STATE_DIR / f"feed_{sanitize_name(feed_name)}.json"
    state["last_check"] = datetime.now(timezone.utc).isoformat()
    # Keep only last 200 seen IDs to prevent unbounded growth
    state["seen_ids"] = state.get("seen_ids", [])[-200:]
    with open(state_file, "w") as f:
        json.dump(state, f, indent=2)


def sanitize_name(name):
    """Create a filesystem-safe name."""
    return re.sub(r'[^a-z0-9_-]', '_', name.lower())


def fetch_feed(url):
    """Fetch and return feed XML content."""
    headers = {
        "User-Agent": "KBMonitor/1.0 (personal knowledge base feed reader)"
    }
    req = Request(url, headers=headers)
    with urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


# ---------------------------------------------------------------------------
# Feed parsing (supports RSS 2.0 and Atom)
# ---------------------------------------------------------------------------

def parse_date(date_str):
    """Parse various date formats found in feeds."""
    if not date_str:
        return None

    # Try RFC 2822 (common in RSS)
    try:
        return parsedate_to_datetime(date_str)
    except Exception:
        pass

    # Try ISO 8601 / Atom format
    for fmt in [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%dT%H:%M:%S.%f%z",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ]:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue

    return None


def parse_feed(xml_text):
    """
    Parse RSS or Atom feed XML into a list of entries.
    Each entry: {"id": str, "title": str, "url": str, "date": datetime|None, "summary": str}
    """
    entries = []

    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return entries

    # Detect namespace
    ns = ""
    if root.tag.startswith("{"):
        ns = root.tag.split("}")[0] + "}"

    # Atom feed
    if "atom" in ns.lower() or root.tag.endswith("feed"):
        for entry in root.findall(f"{ns}entry"):
            title_el = entry.find(f"{ns}title")
            link_el = entry.find(f"{ns}link")
            id_el = entry.find(f"{ns}id")
            updated_el = entry.find(f"{ns}updated") or entry.find(f"{ns}published")
            summary_el = entry.find(f"{ns}summary") or entry.find(f"{ns}content")

            url = ""
            if link_el is not None:
                url = link_el.get("href", link_el.text or "")

            entries.append({
                "id": (id_el.text if id_el is not None else url) or "",
                "title": (title_el.text if title_el is not None else "") or "",
                "url": url,
                "date": parse_date(updated_el.text if updated_el is not None else None),
                "summary": (summary_el.text if summary_el is not None else "") or "",
            })
        return entries

    # RSS 2.0
    channel = root.find("channel") or root
    for item in channel.findall("item"):
        title_el = item.find("title")
        link_el = item.find("link")
        guid_el = item.find("guid")
        date_el = item.find("pubDate") or item.find("dc:date")
        desc_el = item.find("description")

        url = (link_el.text if link_el is not None else "") or ""
        entry_id = (guid_el.text if guid_el is not None else url) or ""

        entries.append({
            "id": entry_id,
            "title": (title_el.text if title_el is not None else "") or "",
            "url": url,
            "date": parse_date(date_el.text if date_el is not None else None),
            "summary": (desc_el.text if desc_el is not None else "") or "",
        })

    # Also try items at root level (some RSS variants)
    if not entries:
        for item in root.findall(f"{ns}item"):
            title_el = item.find(f"{ns}title")
            link_el = item.find(f"{ns}link")
            entries.append({
                "id": (link_el.text if link_el is not None else "") or "",
                "title": (title_el.text if title_el is not None else "") or "",
                "url": (link_el.text if link_el is not None else "") or "",
                "date": None,
                "summary": "",
            })

    return entries


# ---------------------------------------------------------------------------
# Relevance filtering
# ---------------------------------------------------------------------------

def is_relevant(entry, keywords):
    """Check if an entry matches any keyword (case-insensitive)."""
    text = f"{entry['title']} {entry['summary']}".lower()
    # Strip HTML tags for matching
    text = re.sub(r'<[^>]+>', ' ', text)
    for kw in keywords:
        if kw.lower() in text:
            return True
    return False


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def check_feeds(config, since_days=7, show_all=False):
    """
    Check all configured feeds for new relevant entries.
    Returns list of {"feed": ..., "entries": [...]}
    """
    keywords = config.get("keywords", [])
    cutoff = datetime.now(timezone.utc) - timedelta(days=since_days)
    results = []

    for feed_info in config.get("feeds", []):
        feed_url = feed_info["url"]
        feed_name = feed_info.get("name", feed_url)

        print(f"  Checking: {feed_name}...", end=" ", flush=True)

        state = load_feed_state(feed_name)
        seen_ids = set(state.get("seen_ids", []))

        try:
            xml_text = fetch_feed(feed_url)
            entries = parse_feed(xml_text)
        except (URLError, OSError, TimeoutError) as e:
            print(f"[error: {e}]")
            continue

        new_entries = []
        new_ids = list(seen_ids)

        for entry in entries:
            # Skip if already seen
            if entry["id"] in seen_ids:
                continue

            # Skip if too old (when date is available)
            if entry["date"] and entry["date"] < cutoff:
                continue

            # Check relevance
            relevant = is_relevant(entry, keywords) if keywords else True

            if relevant or show_all:
                new_entries.append({
                    **entry,
                    "date": entry["date"].isoformat() if entry["date"] else "unknown",
                    "relevant": relevant,
                })

            new_ids.append(entry["id"])

        print(f"{len(new_entries)} new" + ("" if not keywords else f" ({len(entries)} total)"))

        if new_entries:
            results.append({"feed": feed_name, "entries": new_entries})

        # Update state
        state["seen_ids"] = new_ids[-200:]
        save_feed_state(feed_name, state)

    return results


def print_results(results):
    """Pretty-print feed check results."""
    if not results:
        print("\nNo new relevant entries found.")
        return

    total = sum(len(r["entries"]) for r in results)
    print(f"\n{'='*60}")
    print(f"  {total} new relevant entry/entries across {len(results)} feed(s)")
    print(f"{'='*60}")

    for r in results:
        print(f"\n  [{r['feed']}]")
        for entry in r["entries"]:
            relevance = " [relevant]" if entry.get("relevant") else ""
            print(f"    {entry['title'][:70]}{relevance}")
            if entry["url"]:
                print(f"    {entry['url']}")
            print(f"    Date: {entry['date']}")
            print()


def log_run(results):
    """Log the feed check run."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    log_file = LOG_DIR / "rss.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = sum(len(r["entries"]) for r in results)
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] Checked feeds, found {total} new entries\n")
        for r in results:
            for entry in r["entries"]:
                f.write(f"  {r['feed']}: {entry['title'][:60]} — {entry['url']}\n")
        f.write("\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="RSS/Atom Feed Watcher — check feeds for new relevant entries"
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Show all new entries, not just relevant ones"
    )
    parser.add_argument(
        "--since", type=int, default=7,
        help="Look back N days (default: 7)"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--reset", action="store_true",
        help="Reset feed state (treat everything as new)"
    )
    args = parser.parse_args()

    config = load_feeds_config()

    if args.reset:
        import shutil
        for f in STATE_DIR.glob("feed_*.json"):
            f.unlink()
        print("Feed state reset.")

    print("RSS Feed Watcher")
    print(f"Checking {len(config.get('feeds', []))} feed(s)...")
    print()

    results = check_feeds(config, since_days=args.since, show_all=args.all)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print_results(results)

    log_run(results)


if __name__ == "__main__":
    main()
