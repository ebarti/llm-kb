#!/usr/bin/env python3
"""Review gate for LLM-authored wiki markdown writes.

The compiler writes markdown directly into ``wiki/``. This module snapshots
reviewable markdown files before a compile phase runs, validates changed wiki
writes afterward, and quarantines rejected drafts before they can be committed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Iterable, Optional


ARTICLE_DIRS: tuple[str, ...] = ("sources", "concepts", "entities", "comparisons")

DIR_TYPE_MAP: dict[str, str] = {
    "sources": "source-summary",
    "concepts": "concept",
    "entities": "entity",
    "comparisons": "comparison",
}

REQUIRED_FIELDS: dict[str, tuple[str, ...]] = {
    "default": ("title", "type", "summary", "last_compiled"),
    "source-summary": ("title", "type", "summary", "last_compiled", "source"),
    "concept": ("title", "type", "summary", "last_compiled", "sources"),
    "entity": ("title", "type", "summary", "last_compiled", "entity_type"),
    "comparison": ("title", "type", "summary", "last_compiled", "subjects"),
}

MIN_WORDS_BY_TYPE: dict[str, int] = {
    "source-summary": 80,
    "concept": 80,
    "entity": 60,
    "comparison": 100,
    "default": 50,
}

PLACEHOLDER_WIKILINKS: frozenset[str] = frozenset(
    {
        "concept-name",
        "source-name",
        "entity-name",
        "tool-name",
        "comparison-name",
        "wikilinks",
        "wikilink",
        "x",
        "y",
        "foo",
        "bar",
        "title",
        "name",
        "filename",
        "date",
        "summary",
    }
)

WIKILINK_RE = re.compile(r"\[\[(.*?)\]\]")
MUSTACHE_PLACEHOLDER_RE = re.compile(r"\{\{[^{}]+\}\}")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass
class ReviewIssue:
    """One validation failure for a candidate article."""

    code: str
    message: str
    line: Optional[int] = None
    token: Optional[str] = None

    def as_dict(self) -> dict[str, object]:
        data: dict[str, object] = {"code": self.code, "message": self.message}
        if self.line is not None:
            data["line"] = self.line
        if self.token is not None:
            data["token"] = self.token
        return data


@dataclass
class ArticleCandidate:
    """A new or modified wiki article being reviewed."""

    path: Path
    rel_path: str
    text: str
    metadata: dict[str, object]
    body: str
    article_type: str
    is_article: bool


@dataclass
class ArticleReview:
    """Validation result for one article candidate."""

    rel_path: str
    article_type: str
    accepted: bool = True
    issues: list[ReviewIssue] = field(default_factory=list)
    warnings: list[ReviewIssue] = field(default_factory=list)
    quarantined_to: Optional[str] = None

    def reject(self, issue: ReviewIssue) -> None:
        self.accepted = False
        self.issues.append(issue)

    def warn(self, issue: ReviewIssue) -> None:
        self.warnings.append(issue)

    def as_dict(self) -> dict[str, object]:
        return {
            "path": self.rel_path,
            "type": self.article_type,
            "accepted": self.accepted,
            "quarantined_to": self.quarantined_to,
            "issues": [issue.as_dict() for issue in self.issues],
            "warnings": [warning.as_dict() for warning in self.warnings],
        }


@dataclass
class LLMReviewDecision:
    """Decision returned by an optional LLM reviewer."""

    ok: bool
    notes: list[str] = field(default_factory=list)
    usage: dict[str, int] = field(default_factory=dict)


@dataclass
class ReviewerConfig:
    """Runtime configuration for the review gate."""

    enable_llm: bool = False
    llm_model: str = "haiku"
    quarantine_invalid: bool = True
    log_review: bool = True
    max_article_chars_for_llm: int = 16_000
    max_context_chars_for_llm: int = 8_000

    @classmethod
    def from_env(cls) -> "ReviewerConfig":
        enable = os.environ.get("KB_REVIEW_LLM", "").strip().lower()
        return cls(
            enable_llm=enable in {"1", "true", "yes", "on"},
            llm_model=os.environ.get("KB_REVIEW_MODEL", "haiku"),
            quarantine_invalid=os.environ.get("KB_REVIEW_QUARANTINE", "1")
            .strip()
            .lower()
            not in {"0", "false", "no", "off"},
            log_review=os.environ.get("KB_REVIEW_LOG", "1").strip().lower()
            not in {"0", "false", "no", "off"},
        )


@dataclass
class ReviewOutcome:
    """Aggregate result for a review pass."""

    ok: bool
    candidates: int
    accepted: list[ArticleReview] = field(default_factory=list)
    rejected: list[ArticleReview] = field(default_factory=list)
    llm_enabled: bool = False
    llm_model: Optional[str] = None
    llm_cost: dict[str, int] = field(default_factory=dict)
    log_path: Optional[str] = None
    quarantine_batch: Optional[str] = None

    def as_dict(self) -> dict[str, object]:
        return {
            "ok": self.ok,
            "candidates": self.candidates,
            "accepted": len(self.accepted),
            "rejected": len(self.rejected),
            "llm_enabled": self.llm_enabled,
            "llm_model": self.llm_model,
            "llm_cost": self.llm_cost,
            "log_path": self.log_path,
            "quarantine_batch": self.quarantine_batch,
            "articles": [r.as_dict() for r in self.accepted + self.rejected],
        }

    def rejection_summary(self) -> str:
        root_lines: list[str] = []
        dependent_targets: dict[str, int] = {}
        dependent_count = 0

        for review in self.rejected:
            root_issues = [
                issue
                for issue in review.issues
                if issue.code != "wikilink_rejected_target"
            ]
            if root_issues:
                messages = "; ".join(issue.message for issue in root_issues[:3])
                extra = ""
                if len(root_issues) > 3:
                    extra = f" (+{len(root_issues) - 3} more)"
                root_lines.append(f"{review.rel_path}: {messages}{extra}")
                continue

            dependent_count += 1
            for issue in review.issues:
                if issue.code != "wikilink_rejected_target":
                    continue
                target = issue.token or issue.message.rsplit(": ", 1)[-1]
                dependent_targets[target] = dependent_targets.get(target, 0) + 1

        if root_lines:
            parts = [
                (
                    f"{len(self.rejected)} rejected / {self.candidates} candidates; "
                    f"{len(root_lines)} root rejection(s), "
                    f"{dependent_count} dependent rejection(s)"
                ),
                "Root rejections:",
                *[f"- {line}" for line in root_lines[:20]],
            ]
            if len(root_lines) > 20:
                parts.append(f"- ... {len(root_lines) - 20} more root rejection(s)")
            if dependent_targets:
                parts.append("Dependent rejection targets:")
                sorted_targets = sorted(
                    dependent_targets.items(),
                    key=lambda item: (-item[1], item[0]),
                )
                for target, count in sorted_targets[:10]:
                    parts.append(f"- {target}: {count} article(s)")
                if len(sorted_targets) > 10:
                    parts.append(
                        f"- ... {len(sorted_targets) - 10} more rejected target(s)"
                    )
            if self.quarantine_batch:
                parts.append(f"Quarantine: wiki/{self.quarantine_batch}")
            if self.log_path:
                parts.append(f"Review log: {self.log_path}")
            return "\n".join(parts)

        parts: list[str] = []
        for review in self.rejected:
            messages = "; ".join(issue.message for issue in review.issues[:3])
            extra = ""
            if len(review.issues) > 3:
                extra = f" (+{len(review.issues) - 3} more)"
            parts.append(f"{review.rel_path}: {messages}{extra}")
        return "\n".join(parts)


LLMReviewer = Callable[[ArticleCandidate, str, ReviewerConfig], LLMReviewDecision]


def snapshot_articles(wiki_dir: Path) -> dict[str, str]:
    """Return current reviewable wiki markdown keyed by wiki-relative path."""
    snapshot: dict[str, str] = {}
    for path in iter_article_paths(wiki_dir):
        try:
            rel = path.relative_to(wiki_dir).as_posix()
            snapshot[rel] = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
    return snapshot


def iter_article_paths(wiki_dir: Path) -> Iterable[Path]:
    """Yield reviewable wiki markdown files.

    Canonical article directories receive all checks. Structural markdown
    files such as ``wiki/_index.md``, ``wiki/log.md``, and ``wiki/_meta/*.md``
    still need the gate for template leaks and broken links, but they do not
    follow article frontmatter/length requirements.
    """
    if not wiki_dir.is_dir():
        return
    for path in sorted(wiki_dir.rglob("*.md")):
        rel = path.relative_to(wiki_dir)
        if rel.parts and rel.parts[0] == ".pending":
            continue
        if path.is_file():
            yield path


def changed_article_paths(wiki_dir: Path, before: Optional[dict[str, str]]) -> list[Path]:
    """Return article paths to review.

    If ``before`` is ``None`` every canonical article is reviewed. Otherwise
    only new or modified articles are returned.
    """
    paths: list[Path] = []
    for path in iter_article_paths(wiki_dir):
        rel = path.relative_to(wiki_dir).as_posix()
        if before is None:
            paths.append(path)
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if before.get(rel) != text:
            paths.append(path)
    return paths


def review_wiki_writes(
    kb_dir: Path,
    *,
    before_snapshot: Optional[dict[str, str]],
    config: Optional[ReviewerConfig] = None,
    llm_reviewer: Optional[LLMReviewer] = None,
) -> ReviewOutcome:
    """Validate changed wiki markdown writes and quarantine rejected drafts."""
    cfg = config or ReviewerConfig.from_env()
    kb_dir = Path(kb_dir)
    wiki_dir = kb_dir / "wiki"
    paths = changed_article_paths(wiki_dir, before_snapshot)

    llm_cost = _empty_cost()
    if not paths:
        return ReviewOutcome(
            ok=True,
            candidates=0,
            llm_enabled=cfg.enable_llm,
            llm_model=cfg.llm_model if cfg.enable_llm else None,
            llm_cost=llm_cost,
        )

    known_targets = collect_known_targets(kb_dir)
    candidates = [_load_candidate(path, wiki_dir) for path in paths]
    reviews: dict[str, ArticleReview] = {}
    review_context: Optional[str] = None

    for candidate in candidates:
        review = ArticleReview(
            rel_path=candidate.rel_path,
            article_type=candidate.article_type,
        )
        for issue in validate_candidate(candidate, known_targets):
            review.reject(issue)

        if cfg.enable_llm and review.accepted:
            if review_context is None:
                review_context = _load_review_context(wiki_dir, cfg)
            decision = (llm_reviewer or default_llm_reviewer)(
                candidate,
                review_context,
                cfg,
            )
            _add_cost(llm_cost, decision.usage)
            if not decision.ok:
                for note in decision.notes or ["LLM reviewer rejected article"]:
                    review.reject(ReviewIssue(code="llm_reviewer", message=note))

        reviews[candidate.rel_path] = review
        for warning in check_min_length(candidate):
            review.warn(warning)

    _reject_links_to_rejected_candidates(reviews, candidates)

    rejected = [review for review in reviews.values() if not review.accepted]
    accepted = [review for review in reviews.values() if review.accepted]
    quarantine_batch: Optional[str] = None
    if rejected and cfg.quarantine_invalid:
        quarantine_batch = quarantine_invalid_articles(
            wiki_dir=wiki_dir,
            reviews=rejected,
            before_snapshot=before_snapshot or {},
        )

    outcome = ReviewOutcome(
        ok=not rejected,
        candidates=len(paths),
        accepted=accepted,
        rejected=rejected,
        llm_enabled=cfg.enable_llm,
        llm_model=cfg.llm_model if cfg.enable_llm else None,
        llm_cost=llm_cost,
        quarantine_batch=quarantine_batch,
    )

    if cfg.log_review:
        outcome.log_path = append_review_log(kb_dir, outcome)

    return outcome


def validate_candidate(
    candidate: ArticleCandidate,
    known_targets: dict[str, str],
) -> list[ReviewIssue]:
    """Run deterministic validation rules for one article."""
    issues: list[ReviewIssue] = []
    issues.extend(check_template_placeholders(candidate.text))
    issues.extend(check_frontmatter(candidate))
    issues.extend(check_wikilinks(candidate, known_targets))
    return issues


def parse_frontmatter(text: str) -> tuple[dict[str, object], str]:
    """Parse the YAML-ish frontmatter used by this project."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    block = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    meta: dict[str, object] = {}
    lines = block.splitlines()
    index = 0
    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()
        index += 1
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            meta[key] = _parse_yamlish_value(value)
            continue

        items: list[str] = []
        while index < len(lines):
            child = lines[index]
            child_stripped = child.strip()
            if not child.startswith((" ", "\t")):
                break
            index += 1
            if child_stripped.startswith("- "):
                items.append(str(_parse_yamlish_value(child_stripped[2:].strip())))
        meta[key] = items
    return meta, body


def collect_known_targets(kb_dir: Path) -> dict[str, str]:
    """Build a target map for resolving wikilinks.

    Keys include wiki-relative ids, raw ids, and unique basenames. Values are
    canonical ids. Ambiguous basenames are deliberately omitted.
    """
    kb_dir = Path(kb_dir)
    wiki_dir = kb_dir / "wiki"
    targets: set[str] = set()

    if wiki_dir.is_dir():
        for path in wiki_dir.rglob("*.md"):
            rel = path.relative_to(wiki_dir)
            if rel.parts and rel.parts[0] == ".pending":
                continue
            targets.add(rel.with_suffix("").as_posix())

    raw_dir = kb_dir / "raw"
    if raw_dir.is_dir():
        for path in raw_dir.iterdir():
            if path.is_file() and path.suffix == ".md":
                targets.add(f"raw/{path.stem}")
            elif path.is_dir() and (path / "clean.md").exists():
                targets.add(f"raw/{path.name}")
                targets.add(f"raw/{path.name}/clean")

    mapping = {target: target for target in targets}
    basename_to_targets: dict[str, list[str]] = {}
    for target in targets:
        basename_to_targets.setdefault(target.rsplit("/", 1)[-1], []).append(target)
    for basename, matches in basename_to_targets.items():
        if len(matches) == 1:
            mapping.setdefault(basename, matches[0])
    return mapping


def check_frontmatter(candidate: ArticleCandidate) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    meta = candidate.metadata

    if not candidate.is_article:
        return issues

    if not meta:
        return [ReviewIssue(code="frontmatter_missing", message="missing frontmatter")]

    expected_type = _expected_type_for_rel_path(candidate.rel_path)
    article_type = str(meta.get("type", "")).strip()
    required = REQUIRED_FIELDS.get(article_type, REQUIRED_FIELDS["default"])
    for field_name in required:
        if _is_empty(meta.get(field_name)):
            issues.append(
                ReviewIssue(
                    code="frontmatter_required",
                    message=f"missing required frontmatter field: {field_name}",
                )
            )

    if expected_type and article_type and article_type != expected_type:
        issues.append(
            ReviewIssue(
                code="frontmatter_type_mismatch",
                message=(
                    f"type '{article_type}' does not match {candidate.rel_path}; "
                    f"expected '{expected_type}'"
                ),
            )
        )

    last_compiled = str(meta.get("last_compiled", "")).strip()
    if last_compiled and not ISO_DATE_RE.match(last_compiled):
        issues.append(
            ReviewIssue(
                code="frontmatter_date",
                message="last_compiled must use YYYY-MM-DD",
            )
        )

    return issues


def check_min_length(candidate: ArticleCandidate) -> list[ReviewIssue]:
    if not candidate.is_article:
        return []

    min_words = MIN_WORDS_BY_TYPE.get(
        candidate.article_type,
        MIN_WORDS_BY_TYPE["default"],
    )
    words = count_words(candidate.body)
    if words >= min_words:
        return []
    return [
        ReviewIssue(
            code="min_length",
            message=(
                f"{candidate.article_type} body has {words} words; "
                f"minimum is {min_words}"
            ),
        )
    ]


def check_wikilinks(
    candidate: ArticleCandidate,
    known_targets: dict[str, str],
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for line_no, target in extract_wikilinks_with_lines(candidate.text):
        normalized = normalize_wikilink_target(target)
        if not normalized:
            continue
        if normalized not in known_targets:
            issues.append(
                ReviewIssue(
                    code="wikilink_unresolved",
                    message=f"wikilink does not resolve: [[{normalized}]]",
                    line=line_no,
                    token=f"[[{normalized}]]",
                )
            )
    return issues


def check_template_placeholders(text: str) -> list[ReviewIssue]:
    """Find template placeholders outside markdown code spans/blocks."""
    issues: list[ReviewIssue] = []
    in_fence = False
    fence_char: Optional[str] = None
    fence_length = 0
    in_indented_code = False
    prev_blank = True

    for line_no, line in enumerate(text.splitlines(), start=1):
        fence = _get_fence_delimiter(line)
        if in_fence:
            if fence and fence[0] == fence_char and fence[1] >= fence_length:
                in_fence = False
                fence_char = None
                fence_length = 0
            prev_blank = False
            continue

        if fence:
            in_fence = True
            fence_char, fence_length = fence
            in_indented_code = False
            prev_blank = False
            continue

        is_blank = not line.strip()
        if in_indented_code:
            if is_blank:
                prev_blank = True
                continue
            if _is_indented_code_line(line):
                prev_blank = False
                continue
            in_indented_code = False

        if prev_blank and _is_indented_code_line(line):
            in_indented_code = True
            prev_blank = False
            continue

        prev_blank = is_blank
        if is_blank:
            continue

        scan_line = _strip_inline_code(line)
        for match in WIKILINK_RE.finditer(scan_line):
            target = normalize_wikilink_target(match.group(1))
            if target in PLACEHOLDER_WIKILINKS:
                issues.append(
                    ReviewIssue(
                        code="template_placeholder",
                        message=f"template placeholder wikilink leaked: [[{target}]]",
                        line=line_no,
                        token=f"[[{target}]]",
                    )
                )

        for match in MUSTACHE_PLACEHOLDER_RE.finditer(scan_line):
            issues.append(
                ReviewIssue(
                    code="template_placeholder",
                    message=f"template placeholder leaked: {match.group(0)}",
                    line=line_no,
                    token=match.group(0),
                )
            )

    return issues


def quarantine_invalid_articles(
    *,
    wiki_dir: Path,
    reviews: list[ArticleReview],
    before_snapshot: dict[str, str],
) -> str:
    """Move rejected drafts under ``wiki/.pending/`` and restore old content."""
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    pending_root = wiki_dir / ".pending" / timestamp
    pending_root.mkdir(parents=True, exist_ok=False)

    for review in reviews:
        source = wiki_dir / review.rel_path
        if not source.exists():
            continue

        draft_text = source.read_text(encoding="utf-8", errors="replace")
        pending_article = pending_root / review.rel_path
        pending_article.parent.mkdir(parents=True, exist_ok=True)
        pending_article.write_text(draft_text, encoding="utf-8")

        notes_path = pending_article.with_name(
            f"{pending_article.stem}.review.md"
        )
        notes_path.write_text(_render_review_notes(review), encoding="utf-8")
        review.quarantined_to = pending_article.relative_to(wiki_dir).as_posix()

        if review.rel_path in before_snapshot:
            source.write_text(before_snapshot[review.rel_path], encoding="utf-8")
        else:
            source.unlink()

    return pending_root.relative_to(wiki_dir).as_posix()


def append_review_log(kb_dir: Path, outcome: ReviewOutcome) -> str:
    """Append a structured compile review event and return its relative path."""
    meta_dir = Path(kb_dir) / "wiki" / "_meta"
    meta_dir.mkdir(parents=True, exist_ok=True)
    log_path = meta_dir / "compile-review.jsonl"
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": "compile_review",
        "ok": outcome.ok,
        "candidates": outcome.candidates,
        "accepted": len(outcome.accepted),
        "rejected": len(outcome.rejected),
        "quarantine_batch": outcome.quarantine_batch,
        "llm": {
            "enabled": outcome.llm_enabled,
            "model": outcome.llm_model,
            "cost": outcome.llm_cost,
        },
        "articles": [review.as_dict() for review in outcome.accepted + outcome.rejected],
    }
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, sort_keys=True) + "\n")
    return log_path.relative_to(kb_dir).as_posix()


def default_llm_reviewer(
    candidate: ArticleCandidate,
    context: str,
    config: ReviewerConfig,
) -> LLMReviewDecision:
    """Run the optional LLM reviewer. Disabled unless ``KB_REVIEW_LLM=1``."""
    from tools.kb.budget import BudgetTracker
    from tools.kb.runner import invoke_llm

    article_text = candidate.text
    if len(article_text) > config.max_article_chars_for_llm:
        article_text = article_text[: config.max_article_chars_for_llm] + "\n[truncated]"

    prompt = f"""Review this LLM knowledge-base article.

Return JSON only with this schema:
{{"ok": true|false, "issues": ["short issue descriptions"]}}

Checks:
- The article shape matches type {candidate.article_type}.
- The article is internally consistent.
- It does not contradict the supplied existing wiki summaries.
- It is not a template stub and does not contain unresolved instructions.

Existing wiki summaries:
{context}

Article path: {candidate.rel_path}

Article:
{article_text}
"""
    budget = BudgetTracker(limit=None)
    result = invoke_llm(
        prompt,
        model=config.llm_model,
        budget=budget,
        dry_run=False,
        permission_mode="default",
        verbose=False,
    )
    usage = {
        "input_tokens": result.usage.input_tokens,
        "output_tokens": result.usage.output_tokens,
        "cache_creation_input_tokens": result.usage.cache_creation_input_tokens,
        "cache_read_input_tokens": result.usage.cache_read_input_tokens,
        "total_tokens": result.usage.total,
    }
    if result.returncode != 0:
        return LLMReviewDecision(
            ok=False,
            notes=[result.text or "LLM reviewer failed"],
            usage=usage,
        )

    try:
        payload = _extract_json_object(result.text)
    except ValueError as exc:
        return LLMReviewDecision(
            ok=False,
            notes=[f"LLM reviewer returned non-JSON output: {exc}"],
            usage=usage,
        )

    notes = payload.get("issues") or []
    if isinstance(notes, str):
        notes = [notes]
    if not isinstance(notes, list):
        notes = ["LLM reviewer returned malformed issues"]

    return LLMReviewDecision(
        ok=bool(payload.get("ok")),
        notes=[str(note) for note in notes],
        usage=usage,
    )


def extract_wikilinks_with_lines(text: str) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    for line_no, line in enumerate(text.splitlines(), start=1):
        for match in WIKILINK_RE.finditer(line):
            out.append((line_no, match.group(1)))
    return out


def normalize_wikilink_target(payload: str) -> str:
    target = _split_wikilink_payload(payload).strip()
    if "#" in target:
        target = target.split("#", 1)[0].strip()
    if target.endswith(".md"):
        target = target[:-3]
    if target.startswith("wiki/"):
        target = target[5:]
    return target


def count_words(body: str) -> int:
    text = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    text = re.sub(r"`[^`]*`", "", text)
    text = re.sub(
        r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]",
        lambda match: match.group(2) or match.group(1),
        text,
    )
    text = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", text)
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    return len(re.findall(r"\b\w+\b", text))


def _load_candidate(path: Path, wiki_dir: Path) -> ArticleCandidate:
    text = path.read_text(encoding="utf-8", errors="replace")
    meta, body = parse_frontmatter(text)
    rel = path.relative_to(wiki_dir).as_posix()
    expected_type = _expected_type_for_rel_path(rel)
    article_type = str(meta.get("type") or expected_type or "wiki-page")
    return ArticleCandidate(
        path=path,
        rel_path=rel,
        text=text,
        metadata=meta,
        body=body,
        article_type=article_type,
        is_article=expected_type is not None,
    )


def _expected_type_for_rel_path(rel_path: str) -> Optional[str]:
    first = rel_path.split("/", 1)[0]
    return DIR_TYPE_MAP.get(first)


def _reject_links_to_rejected_candidates(
    reviews: dict[str, ArticleReview],
    candidates: list[ArticleCandidate],
) -> None:
    candidate_by_rel = {candidate.rel_path: candidate for candidate in candidates}
    changed = True
    while changed:
        changed = False
        rejected_ids = {
            Path(rel).with_suffix("").as_posix()
            for rel, review in reviews.items()
            if not review.accepted
        }
        rejected_basenames = {target.rsplit("/", 1)[-1] for target in rejected_ids}
        for rel, review in reviews.items():
            if not review.accepted:
                continue
            candidate = candidate_by_rel[rel]
            for _line_no, payload in extract_wikilinks_with_lines(candidate.text):
                target = normalize_wikilink_target(payload)
                if target in rejected_ids or target in rejected_basenames:
                    review.reject(
                        ReviewIssue(
                            code="wikilink_rejected_target",
                            message=f"wikilink points to rejected article: [[{target}]]",
                            token=f"[[{target}]]",
                        )
                    )
                    changed = True
                    break


def _parse_yamlish_value(value: str) -> object:
    value = value.strip()
    if value.startswith("["):
        try:
            parsed = json.loads(value)
            return parsed
        except json.JSONDecodeError:
            matches = re.findall(r'"([^"]*)"|\'([^\']*)\'', value)
            quoted = [first or second for first, second in matches]
            if quoted:
                return quoted
            return [
                item.strip()
                for item in value[1:-1].split(",")
                if item.strip()
            ]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _is_empty(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip()
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    return False


def _split_wikilink_payload(payload: str) -> str:
    chars: list[str] = []
    index = 0
    while index < len(payload):
        ch = payload[index]
        if ch == "\\" and index + 1 < len(payload) and payload[index + 1] == "|":
            break
        if ch == "|":
            break
        chars.append(ch)
        index += 1
    return "".join(chars).strip()


def _get_fence_delimiter(line: str) -> Optional[tuple[str, int]]:
    match = FENCE_RE.match(line.lstrip())
    if not match:
        return None
    marker = match.group(1)
    return marker[0], len(marker)


def _strip_inline_code(line: str) -> str:
    cleaned: list[str] = []
    index = 0
    while index < len(line):
        if line[index] != "`":
            cleaned.append(line[index])
            index += 1
            continue
        tick_start = index
        while index < len(line) and line[index] == "`":
            index += 1
        tick_count = index - tick_start
        closing = line.find("`" * tick_count, index)
        if closing == -1:
            cleaned.append(line[tick_start:])
            break
        index = closing + tick_count
    return "".join(cleaned)


def _is_indented_code_line(line: str) -> bool:
    return bool(line.strip()) and (line.startswith("    ") or line.startswith("\t"))


def _render_review_notes(review: ArticleReview) -> str:
    lines = [
        "---",
        f'title: "Review notes: {review.rel_path}"',
        "type: compile-review-note",
        f"created_at: {datetime.now(timezone.utc).isoformat()}",
        "---",
        "",
        f"# Review notes: `{review.rel_path}`",
        "",
        "This draft was quarantined because the compile review gate rejected it.",
        "",
        "## Issues",
        "",
    ]
    for issue in review.issues:
        loc = f" line {issue.line}" if issue.line is not None else ""
        token = f" `{issue.token}`" if issue.token else ""
        lines.append(f"- `{issue.code}`{loc}{token}: {issue.message}")
    lines.append("")
    return "\n".join(lines)


def _load_review_context(wiki_dir: Path, config: ReviewerConfig) -> str:
    summaries = wiki_dir / "_meta" / "summaries.md"
    if not summaries.exists():
        return "(no summaries available)"
    text = summaries.read_text(encoding="utf-8", errors="replace")
    if len(text) > config.max_context_chars_for_llm:
        return text[: config.max_context_chars_for_llm] + "\n[truncated]"
    return text


def _extract_json_object(text: str) -> dict[str, object]:
    stripped = (text or "").strip()
    if not stripped:
        raise ValueError("empty response")
    try:
        payload = json.loads(stripped)
    except json.JSONDecodeError:
        start = stripped.find("{")
        end = stripped.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise ValueError(stripped[:120])
        payload = json.loads(stripped[start : end + 1])
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value is not an object")
    return payload


def _empty_cost() -> dict[str, int]:
    return {
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "total_tokens": 0,
    }


def _add_cost(total: dict[str, int], usage: dict[str, int]) -> None:
    for key in (
        "input_tokens",
        "output_tokens",
        "cache_creation_input_tokens",
        "cache_read_input_tokens",
    ):
        total[key] = int(total.get(key, 0)) + int(usage.get(key, 0) or 0)
    total["total_tokens"] = (
        total["input_tokens"]
        + total["output_tokens"]
        + total["cache_creation_input_tokens"]
        + total["cache_read_input_tokens"]
    )


def _json_default(value: object) -> object:
    if isinstance(value, Path):
        return str(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Review wiki article writes")
    parser.add_argument(
        "--kb-dir",
        default=str(Path(__file__).resolve().parents[2]),
        help="Knowledge-base root containing wiki/ and raw/",
    )
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Reserved for integration use; standalone mode validates all articles.",
    )
    parser.add_argument(
        "--llm",
        action="store_true",
        help="Enable optional LLM reviewer for this run.",
    )
    parser.add_argument(
        "--quarantine",
        action="store_true",
        help="Quarantine rejected articles. Default standalone mode only reports.",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args(argv)

    cfg = ReviewerConfig.from_env()
    if args.llm:
        cfg.enable_llm = True
    cfg.quarantine_invalid = args.quarantine

    outcome = review_wiki_writes(
        Path(args.kb_dir),
        before_snapshot=None,
        config=cfg,
    )
    if args.json:
        print(json.dumps(outcome.as_dict(), indent=2, default=_json_default))
    elif outcome.ok:
        print(f"Review passed ({outcome.candidates} article candidate(s)).")
    else:
        print("Review rejected article writes:")
        print(outcome.rejection_summary())
    return 0 if outcome.ok else 1


if __name__ == "__main__":
    sys.exit(main())
