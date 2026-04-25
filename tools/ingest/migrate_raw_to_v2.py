#!/usr/bin/env python3
"""
migrate_raw_to_v2.py — Migrate flat raw/<slug>.md files to raw/<slug>/ layout.

Before:
    raw/adaline-inside-reasoning-models.md

After:
    raw/adaline-inside-reasoning-models/
        clean.md           # copy of the original file
        meta.json          # provenance with migrated_legacy: true

Notes:
  - No raw.<ext> is created; we never had the original bytes.
    meta.json records sha256_raw = null, size_bytes_raw = null,
    raw_extension = null, and raw_bytes_available = false.
  - meta.json records sha256_clean (sha256 of the .md text).
  - Existing YAML frontmatter is parsed best-effort to populate url/type/fetched_at.
  - By default, the original flat file is LEFT IN PLACE (backward-compat window).
    Pass --delete-originals to remove them once you have verified the migration.
  - The migration is reversible: the clean.md is byte-identical to the original.
    Pass --verify to compare sha256 of every clean.md against its legacy source.
  - Idempotent: re-running is a no-op if the target already matches.

Usage:
    # Dry-run (default)
    python3 tools/ingest/migrate_raw_to_v2.py --dry-run

    # Apply migration
    python3 tools/ingest/migrate_raw_to_v2.py

    # Verify reversibility on already-migrated data
    python3 tools/ingest/migrate_raw_to_v2.py --verify

    # Apply, then delete originals
    python3 tools/ingest/migrate_raw_to_v2.py --delete-originals

Exit codes:
    0 — success / all good
    1 — at least one error
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "raw"
FETCHER_VERSION = "v2.0.0-migration"

# Patterns recognised in legacy filenames
# yt-, arxiv-, gh-, pdf-, tweet-, clip-, (anything else = web)
PREFIX_TO_TYPE = [
    ("yt-", "youtube"),
    ("arxiv-", "arxiv"),
    ("gh-", "github"),
    ("pdf-", "pdf"),
    ("tweet-", "tweet"),
    ("clip-", "clippings"),
]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_frontmatter(text: str) -> tuple[Optional[dict], str]:
    """Minimal YAML frontmatter parser (dict, body)."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = text[4:end]
    body = text[end + 4:].lstrip("\n")

    meta: dict = {}
    current_key: Optional[str] = None
    for line in fm.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        # list item (e.g. "  - value")
        if stripped.startswith("-") and current_key:
            val = stripped.lstrip("-").strip().strip('"').strip("'")
            if val:
                existing = meta.get(current_key)
                if isinstance(existing, list):
                    existing.append(val)
                elif existing in (None, ""):
                    meta[current_key] = [val]
                else:
                    meta[current_key] = [existing, val]
            continue
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip()
            current_key = key
            if value:
                # strip quotes
                v = value.strip('"').strip("'")
                # inline lists like [a, b, c]
                if v.startswith("[") and v.endswith("]"):
                    inner = v[1:-1]
                    meta[key] = [s.strip().strip('"').strip("'") for s in inner.split(",") if s.strip()]
                else:
                    meta[key] = v
            else:
                meta[key] = ""
        else:
            current_key = None
    return meta, body


def infer_fetcher(filename_stem: str, meta: Optional[dict]) -> str:
    if meta:
        t = (meta.get("type") or "").strip().lower()
        mapping = {
            "youtube": "youtube",
            "arxiv": "arxiv",
            "github": "github",
            "pdf": "pdf",
            "tweet": "tweet",
            "article": "web",
        }
        if t in mapping:
            return mapping[t]
    for prefix, fetcher in PREFIX_TO_TYPE:
        if filename_stem.startswith(prefix):
            return fetcher
    return "web"


def infer_content_type(fetcher: str) -> str:
    return {
        "youtube": "transcript",
        "arxiv": "pdf",
        "github": "markdown",
        "pdf": "pdf",
        "tweet": "json",
        "clippings": "markdown",
        "web": "html",
    }.get(fetcher, "")


def migrate_one(md_file: Path, *, dry_run: bool) -> dict:
    """Migrate a single flat raw/<slug>.md file into raw/<slug>/ layout."""
    slug = md_file.stem
    target_dir = RAW_DIR / slug
    clean_out = target_dir / "clean.md"
    meta_out = target_dir / "meta.json"

    content_bytes = md_file.read_bytes()
    content_text = content_bytes.decode("utf-8", errors="replace")
    sha_clean = sha256_bytes(content_bytes)
    fm, _body = parse_frontmatter(content_text)

    fetcher = infer_fetcher(slug, fm)
    url = ""
    date_ingested = ""
    if fm:
        url = fm.get("source", "") or fm.get("url", "") or ""
        if isinstance(url, list):
            url = url[0] if url else ""
        date_ingested = fm.get("date_ingested", "") or ""

    # Idempotency: if meta.json exists and matches sha, no-op
    if meta_out.exists():
        try:
            existing = json.loads(meta_out.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing = None
        if isinstance(existing, dict):
            if existing.get("sha256_clean") == sha_clean and existing.get("migrated_legacy"):
                return {"slug": slug, "status": "already_migrated", "action": "noop"}
            # Conflict: a live v2 bundle exists (non-migrated, or migrated
            # with a different sha). Do NOT overwrite it with the legacy
            # flat-file snapshot — that would clobber freshly ingested
            # content. Surface a clear warning and leave both files in
            # place for human review.
            is_v2_bundle = (
                "raw_bytes_available" in existing or existing.get("migrated_legacy")
            )
            if is_v2_bundle:
                return {
                    "slug": slug,
                    "status": "conflict",
                    "action": "skipped",
                    "error": (
                        f"raw/{slug}/ already contains a v2 bundle; refusing to "
                        f"overwrite from legacy raw/{md_file.name}. "
                        f"Resolve manually (delete legacy file or rename slug)."
                    ),
                    "target_dir": str(target_dir.relative_to(BASE_DIR)),
                }

    # Name-collision safety: target_dir must not be a file
    if target_dir.exists() and not target_dir.is_dir():
        return {
            "slug": slug,
            "status": "error",
            "error": f"{target_dir} exists and is not a directory",
        }

    meta = {
        "slug": slug,
        "url": url,
        "fetched_at": _best_fetched_at(date_ingested),
        "fetcher": fetcher,
        "fetcher_version": FETCHER_VERSION,
        "content_type": infer_content_type(fetcher),
        "sha256_raw": None,
        "sha256_clean": sha_clean,
        "size_bytes_raw": None,
        "size_bytes_clean": len(content_bytes),
        "raw_bytes_available": False,
        "raw_extension": None,
        "migrated_legacy": True,
        "legacy_path": f"raw/{md_file.name}",
    }

    if dry_run:
        return {
            "slug": slug,
            "status": "would_migrate",
            "action": "dry_run",
            "target_dir": str(target_dir.relative_to(BASE_DIR)),
            "fetcher": fetcher,
            "url": url,
        }

    target_dir.mkdir(parents=True, exist_ok=True)
    clean_out.write_bytes(content_bytes)  # byte-exact copy for reversibility
    meta_out.write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    return {
        "slug": slug,
        "status": "migrated",
        "action": "wrote",
        "target_dir": str(target_dir.relative_to(BASE_DIR)),
        "fetcher": fetcher,
    }


def _best_fetched_at(date_str: str) -> str:
    if not date_str:
        return iso_now()
    date_str = date_str.strip()
    # accept YYYY-MM-DD → append T00:00:00Z
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        return f"{date_str}T00:00:00Z"
    # already an ISO?
    if "T" in date_str and (date_str.endswith("Z") or "+" in date_str):
        return date_str
    return iso_now()


def verify_all() -> int:
    """For every migrated slug, verify clean.md sha256 matches legacy file sha256."""
    issues = 0
    checked = 0
    for d in sorted(RAW_DIR.iterdir()):
        if not d.is_dir():
            continue
        meta_file = d / "meta.json"
        clean_file = d / "clean.md"
        if not (meta_file.exists() and clean_file.exists()):
            continue
        try:
            meta = json.loads(meta_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"  ERROR: invalid meta.json for {d.name}")
            issues += 1
            continue
        if not meta.get("migrated_legacy"):
            continue
        checked += 1
        declared = meta.get("sha256_clean")
        actual = sha256_bytes(clean_file.read_bytes())
        if declared != actual:
            print(f"  FAIL: {d.name} sha256_clean mismatch (declared={declared}, actual={actual})")
            issues += 1
            continue

        # Compare against legacy flat file if present
        legacy = RAW_DIR / f"{d.name}.md"
        if legacy.exists():
            legacy_sha = sha256_bytes(legacy.read_bytes())
            if legacy_sha != actual:
                print(f"  FAIL: {d.name} clean.md differs from legacy raw/{d.name}.md")
                issues += 1

    print(f"\nVerified {checked} migrated slugs; {issues} issue(s)")
    return 0 if issues == 0 else 1


def main() -> int:
    p = argparse.ArgumentParser(description="Migrate raw/ to the v2 layout")
    p.add_argument("--dry-run", action="store_true", help="Show what would happen")
    p.add_argument(
        "--delete-originals",
        action="store_true",
        help="After migration, delete the flat raw/<slug>.md files",
    )
    p.add_argument(
        "--verify",
        action="store_true",
        help="Verify clean.md matches original (requires legacy files still present)",
    )
    p.add_argument("--json", action="store_true", help="Emit JSON summary")
    args = p.parse_args()

    if args.verify:
        return verify_all()

    if not RAW_DIR.is_dir():
        print(f"ERROR: {RAW_DIR} does not exist", file=sys.stderr)
        return 1

    flat_files = sorted([p for p in RAW_DIR.iterdir() if p.is_file() and p.suffix == ".md"])
    print(f"Found {len(flat_files)} flat raw/*.md files")

    results: list[dict] = []
    errors = 0
    for md_file in flat_files:
        try:
            r = migrate_one(md_file, dry_run=args.dry_run)
        except Exception as e:
            r = {"slug": md_file.stem, "status": "error", "error": str(e)}
        if r.get("status") == "error":
            errors += 1
            print(f"  ERROR: {r['slug']}: {r.get('error')}")
        elif r.get("status") == "conflict":
            # Not an error (we intentionally skipped), but warn loudly so
            # the operator can resolve the hybrid state.
            if not args.json:
                print(f"  WARN: {r['slug']}: {r.get('error')}")
        elif not args.json:
            status = r.get("status")
            if status == "already_migrated":
                # Keep output quiet for no-ops
                pass
            elif status == "would_migrate":
                print(f"  [dry-run] {r['slug']} → {r['target_dir']} (fetcher={r['fetcher']})")
            else:
                print(f"  migrated {r['slug']} ({r.get('fetcher', '?')})")
        results.append(r)

    summary = {
        "total": len(flat_files),
        "migrated": sum(1 for r in results if r.get("status") == "migrated"),
        "already_migrated": sum(1 for r in results if r.get("status") == "already_migrated"),
        "would_migrate": sum(1 for r in results if r.get("status") == "would_migrate"),
        "conflicts": sum(1 for r in results if r.get("status") == "conflict"),
        "errors": errors,
        "dry_run": args.dry_run,
    }

    print()
    print(f"Total:            {summary['total']}")
    print(f"Migrated:         {summary['migrated']}")
    print(f"Would migrate:    {summary['would_migrate']}")
    print(f"Already migrated: {summary['already_migrated']}")
    print(f"Conflicts:        {summary['conflicts']}")
    print(f"Errors:           {summary['errors']}")

    if not args.dry_run and args.delete_originals and errors == 0:
        # Never delete a legacy flat file whose slug ended in a conflict —
        # the operator needs both files visible to resolve the hybrid state.
        conflict_slugs = {r["slug"] for r in results if r.get("status") == "conflict"}
        deleted = 0
        for md_file in flat_files:
            if md_file.stem in conflict_slugs:
                continue
            target_dir = RAW_DIR / md_file.stem
            if (target_dir / "clean.md").exists() and (target_dir / "meta.json").exists():
                md_file.unlink()
                deleted += 1
        print(f"\nDeleted {deleted} original flat .md files")

    if args.json:
        print(json.dumps({"summary": summary, "results": results}, indent=2))

    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
