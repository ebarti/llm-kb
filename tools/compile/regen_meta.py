#!/usr/bin/env python3
"""
Deterministic Wiki Metadata Regenerator.

Walks ``wiki/`` and ``raw/`` and rebuilds the five ``wiki/_meta/`` files
from ground truth:

  * ``stats.json``          -- file + word counts per directory
  * ``manifest.md``         -- every raw file, with a content hash
  * ``summaries.md``        -- one line per wiki article (from frontmatter)
  * ``links.md``            -- backlink graph from actual ``[[wikilinks]]``
  * ``freshness-report.md`` -- last_compiled vs. threshold, flagged stale

Design goals
------------

* **Deterministic (within a run / within a day).** Running twice in a
  row is a no-op: every emitted file is byte-identical on the second
  invocation. Four of the five outputs (``stats.json``, ``manifest.md``,
  ``summaries.md``, ``links.md``) are fully input-derived -- their
  "generated at" marker is the latest ``last_compiled`` date across
  wiki articles rather than ``datetime.now()``, so they are stable
  across arbitrary reruns as long as the inputs do not change.

  ``freshness-report.md`` is the one exception: it is **wall-clock
  anchored** to ``date.today()`` (captured once per ``regenerate()``
  call so a single run cannot straddle midnight) because its whole
  purpose is to surface articles that have aged out relative to *now*.
  That means determinism for the freshness file is **idempotent within
  the same day / run**, not across days: two runs on different
  calendar days will produce different ``last_updated`` and
  ``age_days`` values even if no wiki content changed. Tests that
  assert byte-for-byte equality across runs must either stay within a
  single ``regenerate()`` call, inject a fixed ``today_date``, or
  exclude the freshness file.
* **Stdlib only.** No third-party dependencies.
* **Sorted.** Everything is emitted in sorted order by path so diffs
  are minimal and reviewable.
* **Safe to call before the LLM compile step.** Intended to be invoked
  by ``./kb compile`` so the meta files cannot silently drift out of
  sync with reality.

Usage
-----

    python3 tools/compile/regen_meta.py              # regenerate
    python3 tools/compile/regen_meta.py --check      # exit 1 if writes needed
    python3 tools/compile/regen_meta.py --quiet

"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent
WIKI_DIR = BASE_DIR / "wiki"
RAW_DIR = BASE_DIR / "raw"
META_DIR = WIKI_DIR / "_meta"


# Real article subdirectories under wiki/. Anything outside these is
# treated as a structural / pseudo-article (Dashboard, log, _index, ...)
# and excluded from summaries.md / orphan detection. Used consistently
# across render_summaries() and render_links() to avoid the hazard of
# the inlined tuple drifting out of sync.
ARTICLE_SUBDIRS: tuple[str, ...] = ("concepts", "sources", "entities", "comparisons")
ARTICLE_SUBDIRS_SET: frozenset[str] = frozenset(ARTICLE_SUBDIRS)

WIKILINK_RE = re.compile(r"\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")

# Score thresholds (days). Articles whose last_compiled is older than
# STALE_DAYS are flagged as stale; FRESH_DAYS marks the upper cutoff
# for a 1.0 score. These match the behaviour of the existing
# freshness_scorer plugin (MAX_AGE_DAYS = 365).
STALE_DAYS = 90
FRESH_WINDOW_DAYS = 365

# Category buckets used in summaries.md. Keys are frontmatter ``type``
# values; the order here controls the section order of the output.
SUMMARY_SECTIONS: list[tuple[str, str, str]] = [
    ("source-summary", "sources", "Sources"),
    ("concept", "concepts", "Concepts"),
    ("entity", "entities", "Entities"),
    ("comparison", "comparisons", "Comparisons"),
]


# --------------------------------------------------------------------- #
#  Frontmatter / content parsing
# --------------------------------------------------------------------- #

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML-ish frontmatter, returning ``(meta_dict, body)``.

    Handles quoted strings and the inline JSON-style lists used in
    this codebase (``related: ["[[x]]", "[[y]]"]``). Unknown syntax is
    tolerated -- best effort.
    """
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[4:end]
    body = text[end + 4:]
    meta: dict = {}
    for raw_line in fm_block.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        colon = line.find(":")
        if colon == -1:
            continue
        key = line[:colon].strip()
        value = line[colon + 1:].strip()
        if value.startswith("["):
            # Try JSON first, fall back to regex-extracted strings.
            try:
                meta[key] = json.loads(value)
                continue
            except json.JSONDecodeError:
                meta[key] = re.findall(r'"([^"]*)"', value)
                continue
        # Strip matched surrounding quotes
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        meta[key] = value
    return meta, body


def extract_wikilinks(text: str) -> list[str]:
    """Return the list of wikilink targets appearing in ``text``.

    Order is preserved; duplicates are retained (callers decide).
    """
    return [m.strip() for m in WIKILINK_RE.findall(text)]


def strip_wikilinks(link: str) -> str:
    """Normalise a wikilink target: drop any ``.md`` suffix."""
    if link.endswith(".md"):
        return link[:-3]
    return link


def count_words(body: str) -> int:
    """Count words in an article body, mirroring the word_count plugin."""
    text = body
    # Resolve wikilinks -> displayed text so brackets do not inflate.
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or m.group(1), text)
    # Drop markdown link syntax, keep the label.
    text = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", text)
    # Drop fenced code blocks.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Drop inline code.
    text = re.sub(r"`[^`]*`", "", text)
    # Drop heading markers.
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    return len(text.split())


# --------------------------------------------------------------------- #
#  Collection helpers
# --------------------------------------------------------------------- #

def _iter_wiki_md_files() -> list[Path]:
    """All ``.md`` files under ``wiki/`` excluding ``_meta/``.

    Sorted by relative path for determinism.
    """
    files: list[Path] = []
    if not WIKI_DIR.is_dir():
        return files
    for fp in WIKI_DIR.rglob("*.md"):
        rel = fp.relative_to(WIKI_DIR)
        parts = rel.parts
        if parts and parts[0] == "_meta":
            continue
        files.append(fp)
    files.sort(key=lambda p: str(p.relative_to(WIKI_DIR)))
    return files


def _iter_raw_files() -> list[Path]:
    """All ``.md`` files directly under ``raw/``, sorted."""
    if not RAW_DIR.is_dir():
        return []
    return sorted((p for p in RAW_DIR.iterdir() if p.suffix == ".md"),
                  key=lambda p: p.name)


def _rel_wiki_id(fp: Path) -> str:
    """Path relative to ``wiki/`` without the ``.md`` extension."""
    return fp.relative_to(WIKI_DIR).as_posix()[:-3]


def _content_hash(fp: Path) -> str:
    """Short sha256 of ``fp``'s raw bytes."""
    h = hashlib.sha256()
    with fp.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def _parse_iso_date(value: object) -> date | None:
    """Parse an ISO date (``YYYY-MM-DD``) out of a frontmatter value."""
    if not isinstance(value, str):
        return None
    value = value.strip().strip('"').strip("'")
    if not value:
        return None
    try:
        return datetime.strptime(value[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def _load_existing_stats_history() -> list[dict[str, object]]:
    """Load the prior ``stats.json`` history, ignoring malformed entries."""
    stats_path = META_DIR / "stats.json"
    if not stats_path.exists():
        return []
    try:
        data = json.loads(stats_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []

    history = data.get("history", [])
    if not isinstance(history, list):
        return []

    cleaned: list[dict[str, object]] = []
    for entry in history:
        if not isinstance(entry, dict):
            continue
        timestamp = entry.get("timestamp")
        total_words = entry.get("total_words")
        total_files = entry.get("total_files")
        if not isinstance(timestamp, str):
            continue
        if not isinstance(total_words, int) or not isinstance(total_files, int):
            continue
        cleaned.append(
            {
                "timestamp": timestamp,
                "total_words": total_words,
                "total_files": total_files,
            }
        )
    return cleaned


def _merge_stats_history(
    existing_history: list[dict[str, object]],
    current_entry: dict[str, object],
) -> list[dict[str, object]]:
    """Merge the deterministic snapshot into the prior history."""
    by_timestamp: dict[str, dict[str, object]] = {}
    for entry in existing_history:
        timestamp = entry["timestamp"]
        timestamp_key = _parse_iso_date(timestamp)
        by_timestamp[
            timestamp_key.isoformat() if timestamp_key is not None else str(timestamp)
        ] = dict(entry)
    current_timestamp = current_entry["timestamp"]
    current_timestamp_key = _parse_iso_date(current_timestamp)
    by_timestamp[
        current_timestamp_key.isoformat()
        if current_timestamp_key is not None
        else str(current_timestamp)
    ] = dict(current_entry)
    timestamps = sorted(by_timestamp)
    return [by_timestamp[timestamp] for timestamp in timestamps][-100:]


# --------------------------------------------------------------------- #
#  Core walker
# --------------------------------------------------------------------- #

class WikiScan:
    """Holds the parsed state used to emit each meta file.

    The same scan feeds all five generators so we only read disk once.
    """

    def __init__(self, today_date: date | None = None) -> None:
        self.articles: dict[str, dict] = {}
        self.raw_files: list[Path] = []
        self.file_word_counts: dict[str, int] = {}
        self.dir_word_counts: dict[str, int] = {}
        self.total_words: int = 0
        self.total_files: int = 0
        # today_date is the wall-clock anchor used for age-sensitive
        # scoring (freshness). Captured once -- either injected by the
        # caller (tests / a single regenerate() pass) or defaulted to
        # ``date.today()`` -- so two back-to-back calls that happen to
        # straddle midnight within the same ``regenerate()`` still
        # agree on "today". Kept separate from generated_date so the
        # freshness report keeps aging even when the wiki sits
        # untouched.
        resolved_today = today_date if today_date is not None else date.today()
        self.today_date: date = resolved_today
        # generated_date is input-derived (latest last_compiled) and is
        # used in file headers to keep output deterministic across runs.
        # We seed it with today_date so that empty wikis (no article
        # has a last_compiled yet) still get a stable value during a
        # single run.
        self.generated_date: date = resolved_today

    # ----- collection --------------------------------------------------

    def scan(self) -> None:
        latest_compiled: date | None = None

        for fp in _iter_wiki_md_files():
            rel = _rel_wiki_id(fp)
            raw_text = fp.read_text(encoding="utf-8", errors="replace")
            meta, body = parse_frontmatter(raw_text)
            wc = count_words(body)
            raw_links = [strip_wikilinks(l) for l in extract_wikilinks(raw_text)]

            rel_path = fp.relative_to(WIKI_DIR).as_posix()
            top_dir = rel_path.split("/", 1)[0] if "/" in rel_path else "(root)"
            self.file_word_counts[rel_path] = wc
            self.dir_word_counts[top_dir] = self.dir_word_counts.get(top_dir, 0) + wc
            self.total_words += wc
            self.total_files += 1

            lc = _parse_iso_date(meta.get("last_compiled"))
            if lc and (latest_compiled is None or lc > latest_compiled):
                latest_compiled = lc

            self.articles[rel] = {
                "path": rel,
                "rel_path": rel_path,
                "file_path": fp,
                "frontmatter": meta,
                "body": body,
                "word_count": wc,
                "links": raw_links,
                "last_compiled": lc,
            }

        self.raw_files = _iter_raw_files()
        if latest_compiled is not None:
            self.generated_date = latest_compiled

    # ----- derived graph ----------------------------------------------

    def build_link_graph(self) -> tuple[dict[str, set[str]], dict[str, set[str]]]:
        """Return ``(outgoing, incoming)`` maps keyed by article id.

        Only links that resolve to an actual wiki article are kept; links
        to ``raw/`` or to nonexistent targets are dropped so we never
        emit phantom entries.
        """
        known = set(self.articles.keys())
        outgoing: dict[str, set[str]] = defaultdict(set)
        incoming: dict[str, set[str]] = defaultdict(set)

        for article_id, data in self.articles.items():
            for link in data["links"]:
                # Ignore anchors / sub-headings.
                target = link.split("#", 1)[0].strip()
                if not target:
                    continue
                if target.startswith("raw/"):
                    continue
                if target in known:
                    outgoing[article_id].add(target)
                    incoming[target].add(article_id)
        return outgoing, incoming


# --------------------------------------------------------------------- #
#  File emitters
# --------------------------------------------------------------------- #

def render_stats(scan: WikiScan) -> str:
    """Render ``stats.json``.

    The structure matches (and supersedes) the existing ``word_count``
    plugin -- ``current`` (snapshot) and ``history`` (merged time
    series). Prior history entries are preserved, while the current
    deterministic snapshot replaces any existing sample with the same
    timestamp so reruns on the same input stay idempotent.
    """
    top_files = sorted(scan.file_word_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:20]
    timestamp = scan.generated_date.isoformat()
    current_entry = {
        "timestamp": timestamp,
        "total_words": scan.total_words,
        "total_files": scan.total_files,
    }
    history = _merge_stats_history(_load_existing_stats_history(), current_entry)
    data = {
        "current": {
            "total_words": scan.total_words,
            "total_files": scan.total_files,
            "by_directory": dict(sorted(scan.dir_word_counts.items())),
            "timestamp": timestamp,
            "top_files": [
                {"file": f.replace(os.sep, "/"), "words": w}
                for f, w in top_files
            ],
        },
        "history": history,
    }
    return json.dumps(data, indent=2, sort_keys=False) + "\n"


def render_manifest(scan: WikiScan) -> str:
    """Render ``manifest.md`` covering every file in ``raw/``.

    Each row carries a short content hash so that downstream tooling
    can detect raw-file edits without re-reading them.
    """
    ts = scan.generated_date.isoformat()
    n = len(scan.raw_files)
    lines: list[str] = [
        "---",
        'title: "Compilation Manifest"',
        "type: meta",
        f"last_updated: {ts}",
        "---",
        "",
        "# Compilation Manifest",
        "",
        f"Tracks which raw files are present and their content hashes. "
        f"Regenerated deterministically by `tools/compile/regen_meta.py`.",
        "",
        f"Total raw files: **{n}**",
        "",
        "| Raw File | Hash | Size (bytes) |",
        "|----------|------|--------------|",
    ]
    for fp in scan.raw_files:
        size = fp.stat().st_size
        h = _content_hash(fp)
        lines.append(f"| `raw/{fp.name}` | `{h}` | {size} |")
    lines.append("")
    return "\n".join(lines)


def render_summaries(scan: WikiScan) -> str:
    """Render ``summaries.md``: one line per article, grouped by type.

    Articles are grouped by their declared ``type`` frontmatter; when
    that is missing we fall back to the directory name. Each section
    lists its articles sorted by path so the output is stable.
    """
    ts = scan.generated_date.isoformat()
    lines: list[str] = [
        "---",
        'title: "Article Summaries"',
        "type: meta",
        f"last_updated: {ts}",
        "---",
        "",
        "# Article Summaries",
        "",
        "One-line summaries of all wiki articles, grouped by type. This "
        "file is the primary cheat-sheet used for Q&A context loading "
        "and is regenerated deterministically from frontmatter by "
        "`tools/compile/regen_meta.py`.",
        "",
    ]

    # Group by type, then fall back into an "Other" bucket for
    # anything that doesn't advertise a recognised type.
    buckets: dict[str, list[dict]] = defaultdict(list)
    for art in scan.articles.values():
        rel = art["path"]
        top_dir = rel.split("/", 1)[0] if "/" in rel else ""
        if top_dir not in ARTICLE_SUBDIRS_SET:
            # Root-level pseudo-articles (Dashboard, log, ...) are not
            # listed as proper summaries -- they are structural pages.
            continue
        ftype = art["frontmatter"].get("type", "")
        # Normalise to directory bucket when type is missing so we
        # never drop an article on the floor.
        dir_to_type = {
            "sources": "source-summary",
            "concepts": "concept",
            "entities": "entity",
            "comparisons": "comparison",
        }
        effective = ftype or dir_to_type.get(top_dir, "")
        if effective not in {s[0] for s in SUMMARY_SECTIONS}:
            effective = dir_to_type.get(top_dir, effective)
        buckets[effective].append(art)

    total_listed = 0
    for type_key, dir_hint, header in SUMMARY_SECTIONS:
        items = buckets.get(type_key, [])
        if not items:
            continue
        items.sort(key=lambda a: a["path"])
        lines.append(f"## {header}")
        lines.append("")
        for art in items:
            summary = str(art["frontmatter"].get("summary", "")).strip()
            if not summary:
                # Fall back to title so the entry remains useful.
                summary = f"_(no summary: {art['frontmatter'].get('title', art['path'])})_"
            lines.append(f"- [[{art['path']}]] — {summary}")
            total_listed += 1
        lines.append("")

    # Surface anything we could not bucket so issues are discoverable.
    other = []
    bucketed = set()
    for type_key, _dir_hint, _header in SUMMARY_SECTIONS:
        bucketed.update(a["path"] for a in buckets.get(type_key, []))
    for art in scan.articles.values():
        top_dir = art["path"].split("/", 1)[0] if "/" in art["path"] else ""
        if top_dir not in ARTICLE_SUBDIRS_SET:
            continue
        if art["path"] in bucketed:
            continue
        other.append(art)
    if other:
        other.sort(key=lambda a: a["path"])
        lines.append("## Other")
        lines.append("")
        for art in other:
            summary = str(art["frontmatter"].get("summary", "")).strip() or art["path"]
            lines.append(f"- [[{art['path']}]] — {summary}")
            total_listed += 1
        lines.append("")

    lines.append(f"_Total articles listed: {total_listed}_")
    lines.append("")
    return "\n".join(lines)


def render_links(scan: WikiScan) -> str:
    """Render ``links.md`` from the actual link graph.

    Articles are emitted in sorted order; each block lists incoming
    then outgoing links, both sorted. Phantom (unresolved) targets are
    never written.
    """
    ts = scan.generated_date.isoformat()
    outgoing, incoming = scan.build_link_graph()
    lines: list[str] = [
        "---",
        'title: "Link Graph"',
        "type: meta",
        f"last_updated: {ts}",
        "---",
        "",
        "# Link Graph",
        "",
        "Backlink map of all wiki articles. Regenerated deterministically "
        "by `tools/compile/regen_meta.py` from actual wiki-link syntax. "
        "All listed targets resolve to existing wiki articles -- no "
        "phantom entries.",
        "",
    ]

    for article_id in sorted(scan.articles.keys()):
        out = sorted(outgoing.get(article_id, set()))
        inc = sorted(incoming.get(article_id, set()))
        lines.append(f"## {article_id}")
        if inc:
            lines.append("\u2190 " + ", ".join(f"[[{p}]]" for p in inc))
        else:
            lines.append("\u2190 (no incoming wikilinks)")
        if out:
            lines.append("\u2192 " + ", ".join(f"[[{p}]]" for p in out))
        else:
            lines.append("\u2192 (no outgoing links)")
        lines.append("")

    # Orphans: no incoming links AND not structural.
    orphans = []
    for article_id in sorted(scan.articles.keys()):
        top_dir = article_id.split("/", 1)[0] if "/" in article_id else ""
        if top_dir not in ARTICLE_SUBDIRS_SET:
            continue
        if not incoming.get(article_id):
            orphans.append(article_id)
    if orphans:
        lines.append("## Orphan Pages")
        lines.append("")
        lines.append("Articles with no incoming wikilinks in the article graph:")
        lines.append("")
        for o in orphans:
            lines.append(f"- [[{o}]]")
        lines.append("")

    return "\n".join(lines)


def render_freshness(scan: WikiScan) -> str:
    """Render ``freshness-report.md``.

    Scoring: ``1.0 - age_days / FRESH_WINDOW_DAYS``, clamped to
    ``[0.0, 1.0]``. Articles without a parseable ``last_compiled`` get
    the neutral-low score ``0.15`` (matching the existing plugin).
    Articles older than ``STALE_DAYS`` are flagged.

    Ages are anchored to ``scan.today_date`` (wall-clock ``date.today()``
    by default). Using the input-derived ``generated_date`` here would
    make every article look "current" relative to the newest
    ``last_compiled`` in the wiki, so staleness detection would stop
    aging as soon as the wiki sat untouched.
    """
    today = scan.today_date

    scored: list[dict] = []
    for article_id in sorted(scan.articles.keys()):
        art = scan.articles[article_id]
        lc = art["last_compiled"]
        if lc is None:
            score = 0.15
            lc_display = "unknown"
            age_days: int | None = None
        else:
            age_days = max(0, (today - lc).days)
            score = max(0.0, min(1.0, 1.0 - age_days / FRESH_WINDOW_DAYS))
            lc_display = lc.isoformat()
        scored.append(
            {
                "path": art["rel_path"],
                "score": round(score, 2),
                "last_compiled": lc_display,
                "age_days": age_days,
            }
        )

    scored.sort(key=lambda x: (x["score"], x["path"]))

    lines: list[str] = [
        "---",
        'title: "Freshness Report"',
        "type: meta",
        f"last_updated: {today.isoformat()}",
        "---",
        "",
        "# Freshness Report",
        "",
        f"Age anchor (wall clock): {today.isoformat()}",
        "",
        f"Score = 1.0 - age_days / {FRESH_WINDOW_DAYS}. Articles with "
        f"`last_compiled` older than {STALE_DAYS} days are flagged as "
        f"stale.",
        "",
        "## Articles by Freshness (stalest first)",
        "",
        "| Score | Article | Last Compiled | Age (days) |",
        "|-------|---------|---------------|------------|",
    ]
    for r in scored:
        bar = "\u2588" * int(r["score"] * 10) + "\u2591" * (10 - int(r["score"] * 10))
        age_txt = str(r["age_days"]) if r["age_days"] is not None else "—"
        lines.append(
            f"| {r['score']:.2f} {bar} | {r['path']} | {r['last_compiled']} | {age_txt} |"
        )

    if scored:
        scores_only = [r["score"] for r in scored]
        avg = sum(scores_only) / len(scores_only)
        stale = sum(
            1
            for r in scored
            if r["age_days"] is not None and r["age_days"] > STALE_DAYS
        )
        unknown = sum(1 for r in scored if r["age_days"] is None)
        lines.extend(
            [
                "",
                "## Summary",
                "",
                f"- Total articles: {len(scored)}",
                f"- Average freshness: {avg:.2f}",
                f"- Stale (> {STALE_DAYS} days old): {stale}",
                f"- Unknown `last_compiled`: {unknown}",
                "",
            ]
        )

    return "\n".join(lines)


# --------------------------------------------------------------------- #
#  Driver
# --------------------------------------------------------------------- #

OUTPUT_SPECS: list[tuple[str, str]] = [
    ("stats.json", "render_stats"),
    ("manifest.md", "render_manifest"),
    ("summaries.md", "render_summaries"),
    ("links.md", "render_links"),
    ("freshness-report.md", "render_freshness"),
]


def regenerate(
    check: bool = False,
    quiet: bool = False,
    today_date: date | None = None,
) -> int:
    """Run the full regeneration.

    When ``check`` is true we compare existing files against freshly
    rendered content and return non-zero if any file would change.

    ``today_date`` may be supplied to pin the wall-clock anchor (used
    by ``freshness-report.md``) for tests or for callers that need to
    treat a whole batch of runs as happening "now". When omitted we
    capture ``date.today()`` exactly once here and hand it to the
    ``WikiScan`` so no subsequent call to ``date.today()`` can observe
    a different value mid-run.
    """
    resolved_today = today_date if today_date is not None else date.today()
    scan = WikiScan(today_date=resolved_today)
    scan.scan()

    renderers = {
        "render_stats": render_stats,
        "render_manifest": render_manifest,
        "render_summaries": render_summaries,
        "render_links": render_links,
        "render_freshness": render_freshness,
    }

    META_DIR.mkdir(parents=True, exist_ok=True)

    changed = 0
    for name, renderer_key in OUTPUT_SPECS:
        target = META_DIR / name
        new_content = renderers[renderer_key](scan)
        existing = target.read_text(encoding="utf-8") if target.exists() else None
        if existing != new_content:
            changed += 1
            if not check:
                target.write_text(new_content, encoding="utf-8")
            if not quiet:
                action = "WOULD WRITE" if check else "wrote"
                print(f"  [regen_meta] {action} wiki/_meta/{name}")
        else:
            if not quiet:
                print(f"  [regen_meta] unchanged wiki/_meta/{name}")

    if not quiet:
        print(
            f"  [regen_meta] wiki files: {scan.total_files} | "
            f"raw files: {len(scan.raw_files)} | "
            f"total words: {scan.total_words:,} | "
            f"generated_date: {scan.generated_date.isoformat()}"
        )

    if check:
        return 1 if changed else 0
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0] if __doc__ else "regen meta")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write; exit 1 if any meta file would change.",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress output.",
    )
    args = parser.parse_args()
    return regenerate(check=args.check, quiet=args.quiet)


if __name__ == "__main__":
    sys.exit(main())
