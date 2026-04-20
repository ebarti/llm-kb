#!/usr/bin/env python3
"""
check-raw-v2.py — Validate the raw/ v2 layout (immutable bytes + derived clean).

Checks:
  - Every raw/<slug>/ directory has clean.md and meta.json
  - meta.json is valid JSON with required fields
  - sha256_clean in meta.json matches actual sha256 of clean.md bytes
  - If raw_bytes_available is true, raw.<ext> exists and its sha256 matches sha256_raw
  - Migrated-legacy entries (sha256_raw is null, raw_bytes_available: false) are valid
  - Slug matches directory name
  - No unexpected files at the slug level
  - Legacy flat raw/<slug>.md files are still OK (backward compat) — but warn if a
    matching raw/<slug>/ dir also exists and clean.md differs

Usage:
    python3 tools/tests/check-raw-v2.py [--json]

Exit codes:
    0 — all checks passed
    1 — issues found
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DIR = BASE_DIR / "raw"

REQUIRED_META_FIELDS = {
    "slug",
    "url",
    "fetched_at",
    "fetcher",
    "fetcher_version",
    "sha256_clean",
    "raw_bytes_available",
    "migrated_legacy",
}

# Files that are allowed inside raw/<slug>/ beyond the required three
ALLOWED_EXTRAS = {"images"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def collect_slugs() -> tuple[list[Path], list[Path]]:
    """Return (v2_dirs, legacy_flat_files)."""
    v2 = []
    legacy = []
    if not RAW_DIR.is_dir():
        return v2, legacy
    for item in sorted(RAW_DIR.iterdir()):
        if item.is_dir():
            v2.append(item)
        elif item.is_file() and item.suffix == ".md":
            legacy.append(item)
    return v2, legacy


def check_v2_dir(d: Path) -> list[str]:
    """Return list of error messages for this slug directory."""
    errs: list[str] = []
    slug = d.name
    clean_file = d / "clean.md"
    meta_file = d / "meta.json"

    if not clean_file.exists():
        errs.append(f"{slug}: missing clean.md")
    if not meta_file.exists():
        errs.append(f"{slug}: missing meta.json")
    if errs:
        return errs

    try:
        meta = json.loads(meta_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        errs.append(f"{slug}: invalid meta.json: {e}")
        return errs

    missing = REQUIRED_META_FIELDS - set(meta.keys())
    if missing:
        errs.append(f"{slug}: meta.json missing fields: {sorted(missing)}")

    if meta.get("slug") and meta["slug"] != slug:
        errs.append(f"{slug}: meta.json slug '{meta['slug']}' does not match directory name")

    # Verify sha256_clean matches clean.md
    declared_clean = meta.get("sha256_clean")
    actual_clean = sha256_file(clean_file)
    if declared_clean != actual_clean:
        errs.append(
            f"{slug}: sha256_clean mismatch "
            f"(declared={declared_clean}, actual={actual_clean})"
        )

    # Verify raw.<ext> if it should exist
    raw_avail = meta.get("raw_bytes_available", False)
    raw_ext = meta.get("raw_extension", "") or ""
    raw_candidates = list(d.glob("raw.*"))
    if raw_avail:
        if not raw_candidates:
            errs.append(f"{slug}: raw_bytes_available=true but no raw.* file present")
        else:
            expected_raw = d / f"raw.{raw_ext}" if raw_ext else raw_candidates[0]
            if not expected_raw.exists():
                # Fallback to whichever raw.* file exists
                expected_raw = raw_candidates[0]
            declared_raw = meta.get("sha256_raw")
            actual_raw = sha256_file(expected_raw)
            if declared_raw != actual_raw:
                errs.append(
                    f"{slug}: sha256_raw mismatch for {expected_raw.name} "
                    f"(declared={declared_raw}, actual={actual_raw})"
                )
    else:
        # Migrated legacy entries should have raw_bytes_available=false and sha256_raw=null
        if meta.get("sha256_raw") is not None and not raw_candidates:
            errs.append(f"{slug}: sha256_raw set but no raw.* file and not migrated")
        if raw_candidates and not meta.get("migrated_legacy"):
            errs.append(f"{slug}: raw.* files present but raw_bytes_available=false")

    # Check for stray files
    for entry in d.iterdir():
        name = entry.name
        if name in {"clean.md", "meta.json"}:
            continue
        if name in ALLOWED_EXTRAS and entry.is_dir():
            continue
        if entry.is_file() and name.startswith("raw."):
            continue
        errs.append(f"{slug}: unexpected entry '{name}'")

    return errs


def run_checks() -> dict:
    v2_dirs, legacy = collect_slugs()
    all_errors: list[str] = []
    bad_dirs = 0

    # Check v2 layout
    for d in v2_dirs:
        errs = check_v2_dir(d)
        if errs:
            bad_dirs += 1
            all_errors.extend(errs)

    # Warn about hybrid (legacy flat file + v2 dir with same slug)
    hybrid_warnings: list[str] = []
    v2_names = {d.name for d in v2_dirs}
    for f in legacy:
        if f.stem in v2_names:
            # See if the clean.md matches
            legacy_sha = sha256_file(f)
            clean = RAW_DIR / f.stem / "clean.md"
            if clean.exists():
                v2_sha = sha256_file(clean)
                if legacy_sha != v2_sha:
                    hybrid_warnings.append(
                        f"{f.stem}: legacy raw/{f.name} differs from raw/{f.stem}/clean.md"
                    )

    return {
        "v2_dirs": len(v2_dirs),
        "legacy_flat_files": len(legacy),
        "bad_dirs": bad_dirs,
        "errors": all_errors,
        "hybrid_warnings": hybrid_warnings,
        "ok": bad_dirs == 0,
    }


def print_report(result: dict) -> None:
    print("=" * 60)
    print("  Raw Layout v2 Check")
    print("=" * 60)
    print(f"\nv2 slug directories: {result['v2_dirs']}")
    print(f"Legacy flat files:   {result['legacy_flat_files']}")
    print(f"Bad directories:     {result['bad_dirs']}")
    if result["errors"]:
        print("\nErrors:")
        for e in result["errors"]:
            print(f"  - {e}")
    if result["hybrid_warnings"]:
        print("\nHybrid warnings (legacy + v2 disagree):")
        for w in result["hybrid_warnings"]:
            print(f"  - {w}")
    print()
    if result["ok"]:
        print("\033[32mAll v2 raw-layout checks passed.\033[0m")
    else:
        print(f"\033[31m{result['bad_dirs']} directory(ies) have issues.\033[0m")
    print()


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    result = run_checks()
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
