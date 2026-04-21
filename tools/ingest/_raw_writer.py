#!/usr/bin/env python3
"""
_raw_writer.py — Shared helper for the new raw/<slug>/ layout (v2).

Produces the directory structure:

    raw/<slug>/
        raw.<ext>       # original bytes as fetched (optional)
        clean.md        # derived cleaned markdown
        meta.json       # provenance metadata

meta.json schema:
    {
        "slug": "<slug>",
        "url": "https://...",
        "fetched_at": "YYYY-MM-DDTHH:MM:SSZ",
        "fetcher": "youtube|arxiv|github|pdf|tweet|web|clippings",
        "fetcher_version": "v2.0.0",
        "content_type": "html|pdf|json|txt|xml|vtt|markdown|...",
        "sha256_raw": "hex...",      # sha256 of raw.<ext> bytes, or None if not saved
        "sha256_clean": "hex...",    # sha256 of clean.md
        "size_bytes_raw": N,         # size of raw.<ext>, or None if not saved
        "size_bytes_clean": N,
        "raw_bytes_available": true|false,
        "migrated_legacy": false,    # true if moved from flat raw/<slug>.md
        "raw_extension": "html"      # None if no raw bytes saved
    }

Idempotency: if raw/<slug>/meta.json exists and either sha256_raw matches the
newly fetched bytes or sha256_clean matches a raw-less write, writes are
skipped.

Usage (CLI):
    python3 tools/ingest/_raw_writer.py \
        --slug <slug> \
        --url <url> \
        --fetcher <fetcher> \
        --raw-path /tmp/fetched.html \
        --raw-ext html \
        --clean-path /tmp/clean.md \
        --content-type html

Exit codes:
    0  — wrote or skipped (success, idempotent no-op is success)
    1  — error
    2  — skipped due to hash match (no-op); caller may key off this
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

FETCHER_VERSION = "v2.0.0"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def raw_root(base_dir: Path) -> Path:
    return base_dir / "raw"


def slug_dir(base_dir: Path, slug: str) -> Path:
    return raw_root(base_dir) / slug


def meta_path(base_dir: Path, slug: str) -> Path:
    return slug_dir(base_dir, slug) / "meta.json"


def clean_path(base_dir: Path, slug: str) -> Path:
    return slug_dir(base_dir, slug) / "clean.md"


def write_raw(
    base_dir: Path,
    slug: str,
    url: str,
    fetcher: str,
    clean_content: str,
    *,
    raw_bytes: Optional[bytes] = None,
    raw_src_path: Optional[Path] = None,
    raw_ext: str = "",
    content_type: str = "",
    extra_meta: Optional[dict] = None,
    fetcher_version: str = FETCHER_VERSION,
    force: bool = False,
) -> dict:
    """
    Write the raw/<slug>/ bundle. Idempotent on raw hash match, or clean hash
    match when no raw bytes are available.

    Returns a dict {
        "status": "wrote" | "skipped_hash_match",
        "slug": slug,
        "dir": <path>,
        "meta": <meta dict>,
    }

    raw_bytes OR raw_src_path may be provided (not both). If neither, no raw.<ext>
    file is saved — sha256_raw will be None and raw_bytes_available=false.
    """
    if raw_bytes is not None and raw_src_path is not None:
        raise ValueError("pass raw_bytes OR raw_src_path, not both")

    d = slug_dir(base_dir, slug)
    d.mkdir(parents=True, exist_ok=True)

    if isinstance(clean_content, bytes):
        clean_bytes = clean_content
    else:
        clean_bytes = clean_content.encode("utf-8")
    new_sha_clean = sha256_bytes(clean_bytes)
    clean_size = len(clean_bytes)

    # Compute candidate sha256 of new raw bytes before overwriting anything
    new_sha_raw: Optional[str] = None
    raw_size = 0
    if raw_bytes is not None:
        new_sha_raw = sha256_bytes(raw_bytes)
        raw_size = len(raw_bytes)
    elif raw_src_path is not None:
        if not raw_src_path.exists():
            raise FileNotFoundError(f"raw_src_path does not exist: {raw_src_path}")
        new_sha_raw = sha256_file(raw_src_path)
        raw_size = raw_src_path.stat().st_size

    # Idempotency check: prefer raw-byte hash when we have it, otherwise fall
    # back to the cleaned content hash for fetchers that cannot persist raw
    # bytes on a retry path.
    existing_meta_path = meta_path(base_dir, slug)
    if existing_meta_path.exists() and not force:
        try:
            existing = json.loads(existing_meta_path.read_text(encoding="utf-8"))
            existing_sha_raw = existing.get("sha256_raw")
            existing_sha_clean = existing.get("sha256_clean")
            if new_sha_raw is not None and existing_sha_raw == new_sha_raw:
                return {
                    "status": "skipped_hash_match",
                    "slug": slug,
                    "dir": str(d),
                    "meta": existing,
                }
            if new_sha_raw is None and existing_sha_clean == new_sha_clean:
                return {
                    "status": "skipped_hash_match",
                    "slug": slug,
                    "dir": str(d),
                    "meta": existing,
                }
        except (json.JSONDecodeError, OSError):
            pass  # fall through, rewrite

    # Write raw.<ext> if we have bytes
    raw_bytes_available = False
    raw_final_ext: Optional[str] = None
    # On a raw-less rewrite, preserve the prior raw blob + its metadata so we
    # never silently lose bytes we previously saved. We re-read the existing
    # meta.json and carry forward sha256_raw / size_bytes_raw / raw_extension
    # / raw_bytes_available if a real raw.<ext> still lives on disk.
    preserved_sha_raw: Optional[str] = None
    preserved_raw_size: Optional[int] = None
    if raw_bytes is not None or raw_src_path is not None:
        raw_final_ext = (raw_ext or "").lstrip(".")
        if not raw_final_ext:
            raw_final_ext = "bin"
        raw_out = d / f"raw.{raw_final_ext}"
        # Purge any raw.* with a different extension so only one canonical
        # raw blob ever lives in the bundle.
        for stale in d.glob("raw.*"):
            if stale.name != raw_out.name:
                try:
                    stale.unlink()
                except OSError:
                    pass
        if raw_bytes is not None:
            raw_out.write_bytes(raw_bytes)
        else:
            # Move/copy the source; we use copy so callers with tempfiles don't lose them prematurely
            shutil.copy2(raw_src_path, raw_out)  # type: ignore[arg-type]
        raw_bytes_available = True
    else:
        # Raw-less rewrite: prefer preserving any pre-existing raw blob rather
        # than deleting it, so a retry that only has clean content does not
        # drop bytes we legitimately captured on a previous ingest. We read
        # the prior meta.json (if any) and carry its raw.* metadata forward
        # when the referenced raw file still exists on disk.
        if existing_meta_path.exists():
            try:
                existing = json.loads(existing_meta_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                existing = {}
            prev_ext = (existing.get("raw_extension") or "").lstrip(".")
            prev_raw = d / f"raw.{prev_ext}" if prev_ext else None
            if (
                existing.get("raw_bytes_available")
                and prev_raw is not None
                and prev_raw.exists()
            ):
                raw_bytes_available = True
                raw_final_ext = prev_ext
                preserved_sha_raw = existing.get("sha256_raw")
                preserved_raw_size = (
                    existing.get("size_bytes_raw") or prev_raw.stat().st_size
                )
            else:
                # No usable prior blob — scrub any lingering raw.* so the
                # bundle matches meta.raw_bytes_available=false.
                for stale in d.glob("raw.*"):
                    try:
                        stale.unlink()
                    except OSError:
                        pass
        else:
            # No prior meta.json — scrub any orphan raw.* files.
            for stale in d.glob("raw.*"):
                try:
                    stale.unlink()
                except OSError:
                    pass

    # Write clean.md
    clean_out = d / "clean.md"
    clean_out.write_bytes(clean_bytes)

    # If we're preserving a prior raw blob on a raw-less rewrite, carry its
    # hash/size forward. Otherwise use the freshly computed values (or None
    # when no raw bytes were ever captured).
    if preserved_sha_raw is not None:
        meta_sha_raw: Optional[str] = preserved_sha_raw
        meta_size_raw = preserved_raw_size
    else:
        meta_sha_raw = new_sha_raw
        meta_size_raw = raw_size if raw_bytes_available else None

    meta = {
        "slug": slug,
        "url": url,
        "fetched_at": iso_now(),
        "fetcher": fetcher,
        "fetcher_version": fetcher_version,
        "content_type": content_type or "",
        "sha256_raw": meta_sha_raw,
        "sha256_clean": new_sha_clean,
        "size_bytes_raw": meta_size_raw,
        "size_bytes_clean": clean_size,
        "raw_bytes_available": raw_bytes_available,
        "raw_extension": raw_final_ext if raw_bytes_available else None,
        "migrated_legacy": False,
    }
    if extra_meta:
        # Preserve our keys over caller's keys for known fields
        for k, v in extra_meta.items():
            if k not in meta:
                meta[k] = v

    (d / "meta.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    return {
        "status": "wrote",
        "slug": slug,
        "dir": str(d),
        "meta": meta,
    }


def cli() -> int:
    p = argparse.ArgumentParser(
        description="Write the raw/<slug>/ bundle (raw.<ext>, clean.md, meta.json)"
    )
    p.add_argument("--base-dir", default=None, help="Project root (default: detect from script)")
    p.add_argument("--slug", required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--fetcher", required=True)
    p.add_argument("--clean-path", required=True, help="Path to pre-built clean.md content")
    p.add_argument("--raw-path", default=None, help="Path to raw bytes (optional)")
    p.add_argument("--raw-ext", default="", help="Extension for raw file (e.g. html, pdf)")
    p.add_argument("--content-type", default="", help="content type label (html, pdf, json, ...)")
    p.add_argument("--fetcher-version", default=FETCHER_VERSION)
    p.add_argument("--force", action="store_true", help="Skip idempotency check")
    p.add_argument("--extra-meta-json", default=None, help="JSON string of extra meta fields")
    args = p.parse_args()

    base_dir = Path(args.base_dir).resolve() if args.base_dir else Path(__file__).resolve().parent.parent.parent
    clean_content = Path(args.clean_path).read_text(encoding="utf-8", errors="replace")
    raw_src = Path(args.raw_path) if args.raw_path else None

    extra_meta = None
    if args.extra_meta_json:
        try:
            extra_meta = json.loads(args.extra_meta_json)
        except json.JSONDecodeError as e:
            print(f"ERROR: invalid --extra-meta-json: {e}", file=sys.stderr)
            return 1

    try:
        result = write_raw(
            base_dir=base_dir,
            slug=args.slug,
            url=args.url,
            fetcher=args.fetcher,
            clean_content=clean_content,
            raw_src_path=raw_src,
            raw_ext=args.raw_ext,
            content_type=args.content_type,
            fetcher_version=args.fetcher_version,
            extra_meta=extra_meta,
            force=args.force,
        )
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2))
    return 0 if result["status"] == "wrote" else 2


if __name__ == "__main__":
    sys.exit(cli())
