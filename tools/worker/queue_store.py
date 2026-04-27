"""Filesystem-backed discovery review queue.

The queue lives under ``<kb_dir>/.queue`` and intentionally uses one JSON file
per candidate so humans can inspect or edit entries from Obsidian, a shell, or
git. Active candidates are direct children of ``.queue``. Reviewed candidates
move into ``.queue/.approved`` or ``.queue/.rejected`` so their URLs and content
hashes continue to suppress rediscovery.
"""

from __future__ import annotations

import datetime as _dt
import hashlib
import html
import ipaddress
import json
import re
import socket
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import urlsplit, urlunsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


QUEUE_DIR_NAME = ".queue"
APPROVED_DIR_NAME = ".approved"
REJECTED_DIR_NAME = ".rejected"
_QUEUE_GITIGNORE = "*\n!.gitignore\n"


class QueueError(Exception):
    """Base class for queue lookup and mutation errors."""


class QueueItemNotFound(QueueError):
    """Raised when a queue id or prefix does not match a pending item."""


class QueueItemAmbiguous(QueueError):
    """Raised when a queue id prefix matches multiple pending items."""


@dataclass(frozen=True)
class FetchResult:
    content_hash: str
    hash_source: str
    fetch_preview: dict[str, Any]


@dataclass(frozen=True)
class EnqueueResult:
    queue_dir: Path
    created: list[dict[str, Any]]
    skipped: list[dict[str, Any]]


Fetcher = Callable[[str], FetchResult]


class UnsafeFetchURL(ValueError):
    """Raised when a preview URL targets a disallowed scheme or network."""


class _SafeRedirectHandler(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[override]
        _validate_fetch_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


_URL_OPENER = build_opener(_SafeRedirectHandler)


def utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat()


def queue_dir(kb_dir: Path | str) -> Path:
    return Path(kb_dir) / QUEUE_DIR_NAME


def approved_dir(kb_dir: Path | str) -> Path:
    return queue_dir(kb_dir) / APPROVED_DIR_NAME


def rejected_dir(kb_dir: Path | str) -> Path:
    return queue_dir(kb_dir) / REJECTED_DIR_NAME


def normalize_url(url: str) -> str:
    """Normalize a URL for queue duplicate checks without dropping queries."""
    parsed = urlsplit(url.strip())
    return urlunsplit(
        (
            parsed.scheme.lower(),
            parsed.netloc.lower(),
            parsed.path or "",
            parsed.query,
            "",
        )
    )


def fetch_url_preview(
    url: str,
    *,
    timeout: int = 20,
    max_bytes: int = 1024 * 1024,
    preview_chars: int = 700,
) -> FetchResult:
    """Fetch a bounded preview and return a content hash plus metadata.

    Network failures still produce a candidate-safe result using a URL hash as
    a fallback. Successful fetches always hash the fetched bytes.
    """
    fetched_at = utc_now()
    headers = {"User-Agent": "llm-kb-discovery-worker/1.0"}
    clean_url = url.strip()
    try:
        _validate_fetch_url(clean_url)
        req = Request(clean_url, headers=headers)
        with _URL_OPENER.open(req, timeout=timeout) as resp:  # nosec - validated URL
            raw = resp.read(max_bytes + 1)
            status = getattr(resp, "status", None) or resp.getcode()
            content_type = resp.headers.get("content-type", "")
            final_url = resp.geturl()
            _validate_fetch_url(final_url)
        truncated = len(raw) > max_bytes
        body = raw[:max_bytes]
        decoded = _decode_body(body, content_type)
        plain_text = _html_to_text(decoded)
        title = _extract_title(decoded)
        return FetchResult(
            content_hash=f"sha256:{_sha256(body)}",
            hash_source="content",
            fetch_preview={
                "ok": True,
                "status": status,
                "content_type": content_type,
                "bytes_read": len(body),
                "truncated": truncated,
                "title": title,
                "text": plain_text[:preview_chars],
                "fetched_at": fetched_at,
                "final_url": final_url,
            },
        )
    except Exception as exc:  # pragma: no cover - exercised through injected fetchers
        normalized = normalize_url(url)
        return FetchResult(
            content_hash=f"url-sha256:{_sha256(normalized.encode('utf-8'))}",
            hash_source="url-fallback",
            fetch_preview={
                "ok": False,
                "error": f"{type(exc).__name__}: {exc}",
                "title": None,
                "text": "",
                "fetched_at": fetched_at,
            },
        )


def _validate_fetch_url(url: str) -> None:
    parsed = urlsplit(url.strip())
    if parsed.scheme.lower() not in {"http", "https"}:
        raise UnsafeFetchURL(f"unsupported URL scheme: {parsed.scheme or '<none>'}")

    hostname = parsed.hostname
    if not hostname:
        raise UnsafeFetchURL("URL must include a host")

    host = hostname.rstrip(".").lower()
    if host == "localhost" or host.endswith(".localhost"):
        raise UnsafeFetchURL("localhost URLs are not fetchable")

    port = parsed.port or (443 if parsed.scheme.lower() == "https" else 80)
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        try:
            infos = socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)
        except OSError as exc:
            raise UnsafeFetchURL(f"could not resolve host: {hostname}") from exc
        for info in infos:
            resolved = info[4][0]
            try:
                address = ipaddress.ip_address(resolved)
            except ValueError:
                continue
            _reject_unsafe_address(address, hostname)
    else:
        _reject_unsafe_address(address, hostname)


def _reject_unsafe_address(
    address: ipaddress.IPv4Address | ipaddress.IPv6Address,
    hostname: str,
) -> None:
    if (
        address.is_loopback
        or address.is_link_local
        or address.is_private
        or address.is_multicast
        or address.is_reserved
        or address.is_unspecified
    ):
        raise UnsafeFetchURL(f"host resolves to a non-public address: {hostname}")


def list_pending_items(kb_dir: Path | str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for path in _pending_paths(queue_dir(kb_dir)):
        item = _read_json(path)
        if item is not None:
            items.append(item)
    return sorted(items, key=lambda item: (item.get("created_at", ""), item.get("id", "")))


def read_pending_item(kb_dir: Path | str, item_id: str) -> dict[str, Any]:
    path = resolve_pending_path(kb_dir, item_id)
    item = _read_json(path)
    if item is None:
        raise QueueItemNotFound(f"queue item is unreadable: {item_id}")
    return item


def resolve_pending_path(kb_dir: Path | str, item_id: str) -> Path:
    qdir = queue_dir(kb_dir)
    paths = _pending_paths(qdir)
    exact = [path for path in paths if path.stem == item_id]
    if exact:
        return exact[0]
    prefix = [path for path in paths if path.stem.startswith(item_id)]
    if not prefix:
        raise QueueItemNotFound(f"queue item not found: {item_id}")
    if len(prefix) > 1:
        matches = ", ".join(path.stem for path in prefix[:5])
        raise QueueItemAmbiguous(f"queue id prefix is ambiguous: {item_id} ({matches})")
    return prefix[0]


def archive_item(
    kb_dir: Path | str,
    item_id: str,
    status: str,
    *,
    metadata: dict[str, Any] | None = None,
    now: str | None = None,
) -> dict[str, Any]:
    if status not in {"approved", "rejected"}:
        raise ValueError("status must be approved or rejected")

    src = resolve_pending_path(kb_dir, item_id)
    item = _read_json(src)
    if item is None:
        raise QueueItemNotFound(f"queue item is unreadable: {item_id}")

    item["status"] = status
    item[f"{status}_at"] = now or utc_now()
    if metadata:
        item.update(metadata)

    _ensure_queue_dir(queue_dir(kb_dir))
    target_dir = approved_dir(kb_dir) if status == "approved" else rejected_dir(kb_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / src.name
    _write_json(target, item)
    src.unlink()
    return item


def enqueue_discovered_sources(
    kb_dir: Path | str,
    discovered_sources: Iterable[dict[str, Any]],
    *,
    fetcher: Fetcher = fetch_url_preview,
    limit: int | None = None,
    dry_run: bool = False,
    now: str | None = None,
) -> EnqueueResult:
    """Write new discovery candidates into ``.queue``.

    Duplicate suppression checks active, approved, and rejected candidates by
    normalized URL and by content hash. That keeps rejected items from
    resurfacing and keeps approved items from being queued again later.
    """
    kb_path = Path(kb_dir)
    qdir = queue_dir(kb_path)
    created: list[dict[str, Any]] = []
    skipped: list[dict[str, Any]] = []
    known_hashes, known_urls = _known_hashes_and_urls(qdir)
    created_at = now or utc_now()

    if not dry_run:
        _ensure_queue_dir(qdir)

    for source in discovered_sources:
        if limit is not None and len(created) >= limit:
            break

        url = str(source.get("url", "")).strip()
        if not url:
            skipped.append({"source": source, "reason": "missing_url"})
            continue

        normalized = normalize_url(url)
        if normalized in known_urls:
            skipped.append({"url": url, "reason": "known_url"})
            continue

        fetch_result = _safe_fetch(fetcher, url)
        if fetch_result.content_hash in known_hashes:
            skipped.append(
                {
                    "url": url,
                    "reason": "known_content_hash",
                    "content_hash": fetch_result.content_hash,
                }
            )
            continue

        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            "status": "pending",
            "topic": source.get("topic") or source.get("feed") or "discovery",
            "url": url,
            "title": source.get("title") or fetch_result.fetch_preview.get("title") or "",
            "source": _json_safe(source),
            "content_hash": fetch_result.content_hash,
            "hash_source": fetch_result.hash_source,
            "fetch_preview": fetch_result.fetch_preview,
            "created_at": created_at,
        }
        created.append(item)
        known_urls.add(normalized)
        known_hashes.add(fetch_result.content_hash)

        if not dry_run:
            _write_json(qdir / f"{item_id}.json", item)

    return EnqueueResult(queue_dir=qdir, created=created, skipped=skipped)


def _safe_fetch(fetcher: Fetcher, url: str) -> FetchResult:
    try:
        return fetcher(url)
    except Exception as exc:
        normalized = normalize_url(url)
        return FetchResult(
            content_hash=f"url-sha256:{_sha256(normalized.encode('utf-8'))}",
            hash_source="url-fallback",
            fetch_preview={
                "ok": False,
                "error": f"{type(exc).__name__}: {exc}",
                "title": None,
                "text": "",
                "fetched_at": utc_now(),
            },
        )


def _known_hashes_and_urls(qdir: Path) -> tuple[set[str], set[str]]:
    hashes: set[str] = set()
    urls: set[str] = set()
    for path in _all_queue_paths(qdir):
        item = _read_json(path)
        if not item:
            continue
        content_hash = item.get("content_hash")
        if isinstance(content_hash, str) and content_hash:
            hashes.add(content_hash)
        url = item.get("url") or (item.get("source") or {}).get("url")
        if isinstance(url, str) and url:
            urls.add(normalize_url(url))
    return hashes, urls


def _pending_paths(qdir: Path) -> list[Path]:
    if not qdir.exists():
        return []
    return sorted(path for path in qdir.glob("*.json") if path.is_file())


def _ensure_queue_dir(qdir: Path) -> None:
    qdir.mkdir(parents=True, exist_ok=True)
    gitignore = qdir / ".gitignore"
    if not gitignore.exists():
        gitignore.write_text(_QUEUE_GITIGNORE, encoding="utf-8")


def _all_queue_paths(qdir: Path) -> list[Path]:
    paths = _pending_paths(qdir)
    for archive_name in (APPROVED_DIR_NAME, REJECTED_DIR_NAME):
        archive = qdir / archive_name
        if archive.exists():
            paths.extend(sorted(path for path in archive.glob("*.json") if path.is_file()))
    return paths


def _read_json(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _decode_body(body: bytes, content_type: str) -> str:
    match = re.search(r"charset=([^;\s]+)", content_type, flags=re.IGNORECASE)
    encodings = [match.group(1)] if match else []
    encodings.extend(["utf-8", "latin-1"])
    for encoding in encodings:
        try:
            return body.decode(encoding, errors="replace")
        except LookupError:
            continue
    return body.decode("utf-8", errors="replace")


def _extract_title(text: str) -> str | None:
    match = re.search(r"<title[^>]*>(.*?)</title>", text, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return None
    return html.unescape(re.sub(r"\s+", " ", match.group(1)).strip()) or None


def _html_to_text(text: str) -> str:
    text = re.sub(r"(?is)<(script|style).*?>.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def _json_safe(value: Any) -> Any:
    try:
        json.dumps(value)
        return value
    except TypeError:
        if isinstance(value, dict):
            return {str(k): _json_safe(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [_json_safe(v) for v in value]
        return str(value)
