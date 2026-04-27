"""Schema-driven wiki compilation.

The compiler turns immutable ``raw/`` sources into deterministic wiki pages by
asking the LLM for small JSON objects, validating those objects with Pydantic,
and rendering markdown locally. The LLM extracts facts; this module owns file
layout, wikilinks, frontmatter, and idempotency.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional, TypeVar

from tools.compile.review import (
    ReviewerConfig,
    review_wiki_writes,
    snapshot_articles,
)

from .budget import BudgetExceeded
from .git_util import auto_commit
from .models import (
    BaseModel,
    EXIT_BUDGET,
    EXIT_ERROR,
    EXIT_SUCCESS,
    Field,
    LLMInvocationResult,
    TokenUsage,
)
from .runner import LLMResult, invoke_llm


COMPILER_VERSION = "typed-compile-v1"
CACHE_REL_PATH = "wiki/_meta/typed-compile-cache.json"
MAX_SOURCE_CHARS = 48_000


class SourceSummary(BaseModel):
    title: str
    key_points: list[str]
    detailed_summary: str
    notable_quotes: list[str] = Field(default_factory=list)
    related_concepts: list[str] = Field(default_factory=list)
    entities_mentioned: list[str] = Field(default_factory=list)


class ConceptUpdate(BaseModel):
    concept_id: str
    new_key_ideas: list[str]
    source_citation: str
    related_concepts: list[str] = Field(default_factory=list)


class ConceptUpdateBatch(BaseModel):
    updates: list[ConceptUpdate] = Field(default_factory=list)


class EntityRef(BaseModel):
    name: str
    entity_type: str
    role_in_source: str
    aliases: list[str] = Field(default_factory=list)


class EntityRefBatch(BaseModel):
    entities: list[EntityRef] = Field(default_factory=list)


class ComparisonDimension(BaseModel):
    dimension: str
    subject_a: str
    subject_b: str


class Comparison(BaseModel):
    subject_a: str
    subject_b: str
    dimensions: list[ComparisonDimension] = Field(default_factory=list)
    tradeoffs: list[str] = Field(default_factory=list)


class ComparisonBatch(BaseModel):
    comparisons: list[Comparison] = Field(default_factory=list)


@dataclass(frozen=True)
class RawSource:
    key: str
    slug: str
    path: Path
    rel_path: str
    clean_text: str
    sha256: str
    meta: dict[str, Any]


@dataclass
class CompileBundle:
    raw_key: str
    raw_slug: str
    source_rel_path: str
    sha256: str
    compiled_at: str
    source_summary: SourceSummary
    concept_updates: list[ConceptUpdate]
    entity_refs: list[EntityRef]
    comparisons: list[Comparison]


InvokeLLM = Callable[..., LLMResult]
ModelT = TypeVar("ModelT", bound=BaseModel)


def compile_workspace(
    ctx,
    *,
    invoke_model: InvokeLLM = invoke_llm,
    now: Optional[datetime] = None,
) -> LLMInvocationResult:
    """Compile ``raw/`` into ``wiki/`` through typed, validated LLM calls."""
    if ctx.dry_run:
        return LLMInvocationResult(
            command="compile",
            topic=None,
            dry_run=True,
            budget_limit=ctx.budget_limit,
            model=ctx.model,
            message="[dry-run] compile: would run schema-driven typed LLM calls",
            details={"compiler_version": COMPILER_VERSION},
        )

    missing = _missing_required_scripts(ctx.workspace.kb_dir)
    if missing is not None:
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=False,
            exit_code=EXIT_ERROR,
            budget_limit=ctx.budget_limit,
            model=ctx.model,
            message=missing,
            details={"compiler_version": COMPILER_VERSION},
        )

    ctx.workspace.ensure_dirs()
    article_snapshot = snapshot_articles(ctx.workspace.wiki_dir)
    budget = ctx.new_budget()
    compiled_at = (now or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")

    sources = discover_raw_sources(ctx.workspace.kb_dir)
    cache = load_cache(ctx.workspace.kb_dir)
    bundles: list[CompileBundle] = []
    refreshed_sources: list[str] = []
    llm_calls = 0

    try:
        for source in sources:
            cached = _cached_bundle(cache, source)
            if cached is not None:
                bundles.append(cached)
                continue

            bundle, calls = compile_source(
                ctx,
                source,
                budget=budget,
                invoke_model=invoke_model,
                compiled_at=compiled_at,
            )
            bundles.append(bundle)
            refreshed_sources.append(source.key)
            llm_calls += calls
    except BudgetExceeded as exc:
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=False,
            exit_code=EXIT_BUDGET,
            budget_limit=ctx.budget_limit,
            usage=_copy_usage(exc.usage),
            model=ctx.model,
            message=str(exc),
            details={"compiler_version": COMPILER_VERSION},
        )
    except TypedCompileError as exc:
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=False,
            exit_code=EXIT_ERROR,
            budget_limit=ctx.budget_limit,
            usage=_copy_usage(budget.usage),
            model=ctx.model,
            message=str(exc),
            details={
                "compiler_version": COMPILER_VERSION,
                "object": exc.object_name,
                "source": exc.raw_key,
            },
        )

    planned_cache = build_cache(bundles)
    changed_outputs = render_bundles(ctx.workspace.kb_dir, bundles)
    cache_changed = cache_needs_update(ctx.workspace.kb_dir, planned_cache)

    if not changed_outputs and not cache_changed and not refreshed_sources:
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=True,
            exit_code=EXIT_SUCCESS,
            budget_limit=ctx.budget_limit,
            usage=_copy_usage(budget.usage),
            model=ctx.model,
            message="compile: typed cache is current; LLM skipped",
            details={
                "compiler_version": COMPILER_VERSION,
                "sources": [source.key for source in sources],
                "llm_calls": 0,
                "outputs": [],
                "cache_hit": True,
            },
        )

    review_outcome = review_wiki_writes(
        ctx.workspace.kb_dir,
        before_snapshot=article_snapshot,
        config=ReviewerConfig.from_env(),
    )
    details: dict[str, Any] = {
        "compiler_version": COMPILER_VERSION,
        "sources": [source.key for source in sources],
        "refreshed_sources": refreshed_sources,
        "llm_calls": llm_calls,
        "outputs": changed_outputs,
        "cache_changed": cache_changed,
    }
    if review_outcome.candidates:
        details["compile_review"] = review_outcome.as_dict()

    if not review_outcome.ok:
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=False,
            exit_code=EXIT_ERROR,
            budget_limit=ctx.budget_limit,
            usage=_copy_usage(budget.usage),
            model=ctx.model,
            message=(
                "compile review rejected wiki writes:\n"
                + review_outcome.rejection_summary()
            ),
            details=details,
        )

    cache_changed = save_cache_if_changed(ctx.workspace.kb_dir, planned_cache)
    details["cache_changed"] = cache_changed

    decoration_snapshot = snapshot_articles(ctx.workspace.wiki_dir)
    meta_result = run_metadata_generators(ctx.workspace.kb_dir)
    post_review = review_wiki_writes(
        ctx.workspace.kb_dir,
        before_snapshot=decoration_snapshot,
        config=ReviewerConfig.from_env(),
    )
    if post_review.candidates:
        details["post_decoration_review"] = post_review.as_dict()

    if meta_result is not None or not post_review.ok:
        message_parts: list[str] = []
        if meta_result is not None:
            message_parts.append(meta_result)
        if not post_review.ok:
            message_parts.append(
                "post-decoration compile review rejected wiki writes:\n"
                + post_review.rejection_summary()
            )
        return LLMInvocationResult(
            command="compile",
            topic=None,
            ok=False,
            exit_code=EXIT_ERROR,
            budget_limit=ctx.budget_limit,
            usage=_copy_usage(budget.usage),
            model=ctx.model,
            message="\n\n".join(message_parts),
            details=details,
        )

    append_compile_log(ctx.workspace.kb_dir, refreshed_sources, changed_outputs)

    result = LLMInvocationResult(
        command="compile",
        topic=None,
        ok=True,
        exit_code=EXIT_SUCCESS,
        budget_limit=ctx.budget_limit,
        usage=_copy_usage(budget.usage),
        model=ctx.model,
        message=(
            "compile: schema-driven typed compile completed "
            f"({len(refreshed_sources)} source(s), {llm_calls} LLM call(s))"
        ),
        details=details,
    )
    if not ctx.no_commit:
        committed = auto_commit(ctx.workspace.kb_dir, "compile wiki", dry_run=False)
        result.committed = committed
        result.commit_label = "compile wiki" if committed else None
    return result


def compile_source(
    ctx,
    source: RawSource,
    *,
    budget,
    invoke_model: InvokeLLM,
    compiled_at: str,
) -> tuple[CompileBundle, int]:
    """Run the four typed LLM extraction calls for one raw source."""
    calls = 0
    summary = _call_typed_object(
        ctx,
        source,
        object_name="SourceSummary",
        model_cls=SourceSummary,
        task=(
            "Summarize this source for a knowledge-base source page. "
            "Keep key_points factual and make detailed_summary complete enough "
            "to stand alone without the original page."
        ),
        budget=budget,
        invoke_model=invoke_model,
    )
    calls += 1
    concepts = _call_typed_object(
        ctx,
        source,
        object_name="ConceptUpdateBatch",
        model_cls=ConceptUpdateBatch,
        task=(
            "Extract concept updates from this source. Use lowercase, hyphenated "
            "concept_id values. Return an empty updates list if the source adds "
            "no durable concepts."
        ),
        budget=budget,
        invoke_model=invoke_model,
    )
    calls += 1
    entities = _call_typed_object(
        ctx,
        source,
        object_name="EntityRefBatch",
        model_cls=EntityRefBatch,
        task=(
            "Extract notable named entities mentioned in this source. Entity "
            "types should be person, tool, org, paper, dataset, framework, or "
            "other. Return an empty entities list if none are notable."
        ),
        budget=budget,
        invoke_model=invoke_model,
    )
    calls += 1
    comparisons = _call_typed_object(
        ctx,
        source,
        object_name="ComparisonBatch",
        model_cls=ComparisonBatch,
        task=(
            "Extract explicit comparisons or trade-offs from this source. Use "
            "plain subject names. Return an empty comparisons list if the source "
            "does not compare alternatives."
        ),
        budget=budget,
        invoke_model=invoke_model,
    )
    calls += 1

    return (
        CompileBundle(
            raw_key=source.key,
            raw_slug=source.slug,
            source_rel_path=f"sources/{source.slug}.md",
            sha256=source.sha256,
            compiled_at=compiled_at,
            source_summary=summary,
            concept_updates=[
                _ensure_model(ConceptUpdate, item) for item in concepts.updates
            ],
            entity_refs=[_ensure_model(EntityRef, item) for item in entities.entities],
            comparisons=[
                _normalize_comparison(item) for item in comparisons.comparisons
            ],
        ),
        calls,
    )


class TypedCompileError(Exception):
    def __init__(self, raw_key: str, object_name: str, message: str) -> None:
        self.raw_key = raw_key
        self.object_name = object_name
        super().__init__(
            f"{raw_key}: validation failed for {object_name}: {message}"
        )


def _call_typed_object(
    ctx,
    source: RawSource,
    *,
    object_name: str,
    model_cls: type[ModelT],
    task: str,
    budget,
    invoke_model: InvokeLLM,
) -> ModelT:
    prompt = build_schema_prompt(source, object_name=object_name, model_cls=model_cls, task=task)
    result = invoke_model(
        prompt=prompt,
        model=ctx.model,
        budget=budget,
        dry_run=False,
        permission_mode=ctx.permission_mode,
        verbose=ctx.verbose,
        cwd=str(ctx.workspace.kb_dir),
    )
    if result.returncode != 0 or result.budget_exceeded:
        raise TypedCompileError(
            source.key,
            object_name,
            result.text or f"LLM call failed with rc={result.returncode}",
        )
    return parse_typed_object(source.key, object_name, model_cls, result.text)


def build_schema_prompt(
    source: RawSource,
    *,
    object_name: str,
    model_cls: type[BaseModel],
    task: str,
) -> str:
    schema = _schema_for_prompt(model_cls)
    body = source.clean_text[:MAX_SOURCE_CHARS]
    truncated = len(source.clean_text) > MAX_SOURCE_CHARS
    return (
        f"You are compiling raw source `{source.key}` into an Obsidian wiki.\n"
        f"{task}\n\n"
        f"Return ONLY one JSON object matching this Pydantic model: {object_name}.\n"
        f"Do not write files. Do not include markdown fences or commentary.\n\n"
        f"JSON schema:\n{json.dumps(schema, indent=2, sort_keys=True)}\n\n"
        f"Source metadata:\n{json.dumps(source.meta, indent=2, sort_keys=True)}\n\n"
        f"Source content{' (truncated)' if truncated else ''}:\n{body}\n"
    )


def parse_typed_object(
    raw_key: str,
    object_name: str,
    model_cls: type[ModelT],
    text: str,
) -> ModelT:
    try:
        payload = json.loads(_extract_json_object(text))
    except Exception as exc:  # noqa: BLE001
        raise TypedCompileError(raw_key, object_name, f"invalid JSON: {exc}") from exc
    try:
        if hasattr(model_cls, "model_validate"):
            return model_cls.model_validate(payload)  # type: ignore[attr-defined]
        if hasattr(model_cls, "parse_obj"):
            return model_cls.parse_obj(payload)  # type: ignore[attr-defined]
        return model_cls(**payload)
    except Exception as exc:  # noqa: BLE001
        raise TypedCompileError(raw_key, object_name, str(exc)) from exc


def discover_raw_sources(kb_dir: Path) -> list[RawSource]:
    raw_dir = Path(kb_dir) / "raw"
    if not raw_dir.is_dir():
        return []

    sources: list[RawSource] = []
    for path in sorted(raw_dir.iterdir(), key=lambda p: p.name):
        if path.is_dir() and (path / "clean.md").exists():
            clean_path = path / "clean.md"
            meta = _read_json(path / "meta.json")
            slug = path.name
            rel_path = f"raw/{slug}/clean.md"
        elif path.is_file() and path.suffix == ".md":
            clean_path = path
            meta = {}
            slug = path.stem
            rel_path = f"raw/{path.name}"
        else:
            continue
        clean_text = clean_path.read_text(encoding="utf-8", errors="replace")
        sources.append(
            RawSource(
                key=f"raw/{slug}",
                slug=_slugify(slug),
                path=clean_path,
                rel_path=rel_path,
                clean_text=clean_text,
                sha256=hashlib.sha256(clean_text.encode("utf-8")).hexdigest(),
                meta=meta,
            )
        )
    return sources


def load_cache(kb_dir: Path) -> dict[str, Any]:
    cache_path = Path(kb_dir) / CACHE_REL_PATH
    if not cache_path.exists():
        return {"version": COMPILER_VERSION, "sources": {}}
    try:
        payload = json.loads(cache_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"version": COMPILER_VERSION, "sources": {}}
    if payload.get("version") != COMPILER_VERSION:
        return {"version": COMPILER_VERSION, "sources": {}}
    if not isinstance(payload.get("sources"), dict):
        payload["sources"] = {}
    return payload


def build_cache(bundles: list[CompileBundle]) -> dict[str, Any]:
    return {
        "version": COMPILER_VERSION,
        "sources": {
            bundle.raw_key: {
                "sha256": bundle.sha256,
                "compiled_at": bundle.compiled_at,
                "source_rel_path": bundle.source_rel_path,
                "outputs": bundle_outputs(bundle),
                "objects": {
                    "source_summary": _model_dump(bundle.source_summary),
                    "concept_updates": [_model_dump(item) for item in bundle.concept_updates],
                    "entity_refs": [_model_dump(item) for item in bundle.entity_refs],
                    "comparisons": [_model_dump(item) for item in bundle.comparisons],
                },
            }
            for bundle in sorted(bundles, key=lambda item: item.raw_key)
        },
    }


def save_cache_if_changed(kb_dir: Path, payload: dict[str, Any]) -> bool:
    cache_path = Path(kb_dir) / CACHE_REL_PATH
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    return _write_if_changed(cache_path, _cache_text(payload))


def cache_needs_update(kb_dir: Path, payload: dict[str, Any]) -> bool:
    cache_path = Path(kb_dir) / CACHE_REL_PATH
    try:
        return (
            not cache_path.exists()
            or cache_path.read_text(encoding="utf-8") != _cache_text(payload)
        )
    except OSError:
        return True


def _cache_text(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"


def _cached_bundle(cache: dict[str, Any], source: RawSource) -> Optional[CompileBundle]:
    entry = (cache.get("sources") or {}).get(source.key)
    if not isinstance(entry, dict) or entry.get("sha256") != source.sha256:
        return None
    objects = entry.get("objects")
    if not isinstance(objects, dict):
        return None
    try:
        summary = _model_from_dict(SourceSummary, objects.get("source_summary") or {})
        concepts = [
            _model_from_dict(ConceptUpdate, item)
            for item in objects.get("concept_updates") or []
        ]
        entities = [
            _model_from_dict(EntityRef, item)
            for item in objects.get("entity_refs") or []
        ]
        comparisons = [
            _normalize_comparison(item)
            for item in objects.get("comparisons") or []
        ]
    except Exception:
        return None
    return CompileBundle(
        raw_key=source.key,
        raw_slug=source.slug,
        source_rel_path=entry.get("source_rel_path") or f"sources/{source.slug}.md",
        sha256=source.sha256,
        compiled_at=entry.get("compiled_at") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        source_summary=summary,
        concept_updates=concepts,
        entity_refs=entities,
        comparisons=comparisons,
    )


def render_bundles(kb_dir: Path, bundles: list[CompileBundle]) -> list[str]:
    wiki_dir = Path(kb_dir) / "wiki"
    changed: list[str] = []

    for subdir in ("sources", "concepts", "entities", "comparisons", "_meta"):
        (wiki_dir / subdir).mkdir(parents=True, exist_ok=True)

    for bundle in sorted(bundles, key=lambda item: item.raw_key):
        path = wiki_dir / bundle.source_rel_path
        if _write_if_changed(path, render_source_page(bundle)):
            changed.append(f"wiki/{bundle.source_rel_path}")

    for rel_path, text in render_concept_pages(bundles).items():
        if _write_if_changed(wiki_dir / rel_path, text):
            changed.append(f"wiki/{rel_path}")

    for rel_path, text in render_entity_pages(bundles).items():
        if _write_if_changed(wiki_dir / rel_path, text):
            changed.append(f"wiki/{rel_path}")

    for rel_path, text in render_comparison_pages(bundles).items():
        if _write_if_changed(wiki_dir / rel_path, text):
            changed.append(f"wiki/{rel_path}")

    index = render_index(wiki_dir)
    if _write_if_changed(wiki_dir / "_index.md", index):
        changed.append("wiki/_index.md")

    return sorted(changed)


def render_source_page(bundle: CompileBundle) -> str:
    summary = bundle.source_summary
    concepts = [_normalize_concept_id(c) for c in summary.related_concepts]
    concept_links = [f"[[concepts/{c}]]" for c in concepts if c]
    entity_links = [f"[[entities/{_slugify(e.name)}]]" for e in bundle.entity_refs]
    related = sorted(set(concept_links + entity_links))
    source_link = f"[[{bundle.raw_key}]]"
    frontmatter = _frontmatter(
        {
            "title": f"Source: {summary.title}",
            "type": "source-summary",
            "source": source_link,
            "related": related,
            "last_compiled": _date_part(bundle.compiled_at),
            "summary": _one_line(summary.detailed_summary, fallback=summary.title),
        }
    )

    lines = [frontmatter, "## Key Points", ""]
    lines.extend(_bullet_lines(summary.key_points or [summary.detailed_summary]))
    lines.extend(["", "## Detailed Summary", "", summary.detailed_summary.strip(), ""])

    lines.extend(["## Notable Quotes", ""])
    if summary.notable_quotes:
        for quote in summary.notable_quotes:
            lines.append(f"> {quote.strip()}")
            lines.append("")
    else:
        lines.append("_No notable quotes extracted._")
        lines.append("")

    lines.extend(["## Related Concepts", ""])
    if concepts:
        for concept in concepts:
            lines.append(f"- [[concepts/{concept}]] -- discussed in this source")
    else:
        lines.append("- No durable concepts extracted from this source.")
    lines.append("")

    lines.extend(["## Entities Mentioned", ""])
    if bundle.entity_refs:
        for entity in sorted(bundle.entity_refs, key=lambda item: item.name.lower()):
            role = entity.role_in_source.strip() or "mentioned in the source"
            lines.append(f"- [[entities/{_slugify(entity.name)}]] -- {role}")
    else:
        lines.append("- No notable entities extracted from this source.")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_concept_pages(bundles: list[CompileBundle]) -> dict[str, str]:
    by_id: dict[str, list[tuple[CompileBundle, ConceptUpdate]]] = {}
    generated_ids: set[str] = set()
    for bundle in bundles:
        for update in bundle.concept_updates:
            cid = _normalize_concept_id(update.concept_id)
            if not cid:
                continue
            generated_ids.add(cid)
            by_id.setdefault(cid, []).append((bundle, update))
        for comparison in bundle.comparisons:
            generated_ids.add(_normalize_concept_id(comparison.subject_a))
            generated_ids.add(_normalize_concept_id(comparison.subject_b))

    pages: dict[str, str] = {}
    for concept_id in sorted(generated_ids):
        entries = by_id.get(concept_id, [])
        source_links = sorted({f"[[{entry[0].source_rel_path[:-3]}]]" for entry in entries})
        related_ids = sorted(
            {
                _normalize_concept_id(rel)
                for _, update in entries
                for rel in update.related_concepts
                if _normalize_concept_id(rel) in generated_ids
            }
        )
        title = _titleize(concept_id)
        compiled_at = _first_compiled_at(entries, bundles)
        frontmatter = _frontmatter(
            {
                "title": title,
                "type": "concept",
                "sources": source_links,
                "related": [f"[[concepts/{rel}]]" for rel in related_ids],
                "last_compiled": _date_part(compiled_at),
                "summary": f"Compiled concept notes for {title}.",
            }
        )
        lines = [
            frontmatter,
            "## Overview",
            "",
            (
                f"{title} is a concept extracted by the typed compiler from "
                f"{len(source_links) or 1} source-backed compilation record(s). "
                "The page is rebuilt deterministically from validated concept "
                "updates, so repeated compiles with unchanged raw content keep "
                "the same body and frontmatter."
            ),
            "",
            "## Key Ideas",
            "",
        ]
        if entries:
            for bundle, update in sorted(entries, key=lambda item: item[0].raw_key):
                lines.append(f"### [[{bundle.source_rel_path[:-3]}]]")
                lines.append("")
                lines.extend(_bullet_lines(update.new_key_ideas))
                lines.append("")
        else:
            lines.append(
                "- This subject is present in a typed comparison but no standalone "
                "concept update was extracted yet."
            )
            lines.append(
                "- The comparison evidence below keeps the concept resolvable for "
                "Obsidian links and later compile passes can enrich it."
            )
            lines.append("")

        lines.extend(["## Sources", ""])
        if entries:
            for bundle, update in sorted(entries, key=lambda item: item[0].raw_key):
                citation = update.source_citation.strip() or "source-backed update"
                lines.append(f"- [[{bundle.source_rel_path[:-3]}]] -- {citation}")
        else:
            for bundle in bundles:
                if any(
                    concept_id
                    in {
                        _normalize_concept_id(c.subject_a),
                        _normalize_concept_id(c.subject_b),
                    }
                    for c in bundle.comparisons
                ):
                    lines.append(
                        f"- [[{bundle.source_rel_path[:-3]}]] -- comparison subject context"
                    )
        lines.append("")
        pages[f"concepts/{concept_id}.md"] = "\n".join(lines).rstrip() + "\n"
    return pages


def render_entity_pages(bundles: list[CompileBundle]) -> dict[str, str]:
    by_slug: dict[str, list[tuple[CompileBundle, EntityRef]]] = {}
    for bundle in bundles:
        for entity in bundle.entity_refs:
            slug = _slugify(entity.name)
            if slug:
                by_slug.setdefault(slug, []).append((bundle, entity))

    pages: dict[str, str] = {}
    for slug, entries in sorted(by_slug.items()):
        primary = entries[0][1]
        title = primary.name.strip()
        entity_type = primary.entity_type.strip() or "other"
        sources = sorted({f"[[{bundle.source_rel_path[:-3]}]]" for bundle, _ in entries})
        aliases = sorted(
            {
                alias.strip()
                for _, entity in entries
                for alias in entity.aliases
                if alias.strip() and alias.strip().lower() != title.lower()
            }
        )
        frontmatter = _frontmatter(
            {
                "title": title,
                "type": "entity",
                "entity_type": entity_type,
                "sources": sources,
                "related": [],
                "last_compiled": _date_part(entries[0][0].compiled_at),
                "summary": f"{title} is a {entity_type} extracted from typed source compilation.",
            }
        )
        lines = [
            frontmatter,
            "## Overview",
            "",
            (
                f"{title} is tracked as a {entity_type} because validated source "
                "extractions mention it by name. This generated page records "
                "the role supplied by each source and keeps aliases available "
                "for future canonicalization work."
            ),
            "",
            "## Key Contributions / Features",
            "",
        ]
        for bundle, entity in sorted(entries, key=lambda item: item[0].raw_key):
            role = entity.role_in_source.strip() or "mentioned in this source"
            lines.append(f"- [[{bundle.source_rel_path[:-3]}]] -- {role}")
        lines.extend(["", "## Aliases", ""])
        if aliases:
            lines.extend(_bullet_lines(aliases))
        else:
            lines.append("- No aliases extracted.")
        lines.extend(["", "## Mentioned In", ""])
        for source in sources:
            lines.append(f"- {source} -- typed entity extraction")
        lines.append("")
        pages[f"entities/{slug}.md"] = "\n".join(lines).rstrip() + "\n"
    return pages


def render_comparison_pages(bundles: list[CompileBundle]) -> dict[str, str]:
    grouped: dict[str, list[tuple[CompileBundle, Comparison]]] = {}
    for bundle in bundles:
        for comparison in bundle.comparisons:
            a = _normalize_concept_id(comparison.subject_a)
            b = _normalize_concept_id(comparison.subject_b)
            if not a or not b or a == b:
                continue
            key = f"{a}-vs-{b}"
            grouped.setdefault(key, []).append((bundle, comparison))

    pages: dict[str, str] = {}
    for key, entries in sorted(grouped.items()):
        first = entries[0][1]
        a_slug = _normalize_concept_id(first.subject_a)
        b_slug = _normalize_concept_id(first.subject_b)
        a_title = _titleize(a_slug)
        b_title = _titleize(b_slug)
        sources = sorted({f"[[{bundle.source_rel_path[:-3]}]]" for bundle, _ in entries})
        frontmatter = _frontmatter(
            {
                "title": f"{a_title} vs {b_title}",
                "type": "comparison",
                "subjects": [f"[[concepts/{a_slug}]]", f"[[concepts/{b_slug}]]"],
                "sources": sources,
                "last_compiled": _date_part(entries[0][0].compiled_at),
                "summary": f"Typed comparison of {a_title} and {b_title}.",
            }
        )
        lines = [
            frontmatter,
            "## Overview",
            "",
            (
                f"This comparison is rebuilt from validated typed extractions "
                f"where sources contrast {a_title} and {b_title}. The rendered "
                "table, trade-offs, and source links are deterministic so the "
                "page remains byte-identical when raw inputs and typed objects "
                "are unchanged."
            ),
            "",
            "## Comparison Table",
            "",
            f"| Dimension | {a_title} | {b_title} |",
            "|-----------|---|---|",
        ]
        dimensions = [
            dim
            for _, comparison in entries
            for dim in comparison.dimensions
        ]
        if dimensions:
            for dim in sorted(dimensions, key=lambda item: item.dimension.lower()):
                lines.append(
                    f"| {_escape_table(dim.dimension)} | "
                    f"{_escape_table(dim.subject_a)} | "
                    f"{_escape_table(dim.subject_b)} |"
                )
        else:
            lines.append("| Source framing | Mentioned as one side of the comparison | Mentioned as the alternative |")
        lines.extend(["", "## Trade-offs", ""])
        tradeoffs = [
            tradeoff
            for _, comparison in entries
            for tradeoff in comparison.tradeoffs
            if tradeoff.strip()
        ]
        if tradeoffs:
            lines.extend(_bullet_lines(sorted(set(tradeoffs))))
        else:
            lines.append("- No explicit trade-offs extracted beyond the comparison table.")
        lines.extend(["", "## Sources", ""])
        for source in sources:
            lines.append(f"- {source} -- comparison evidence")
        lines.append("")
        pages[f"comparisons/{key}.md"] = "\n".join(lines).rstrip() + "\n"
    return pages


def render_index(wiki_dir: Path) -> str:
    sections = [
        ("Sources", "sources"),
        ("Concepts", "concepts"),
        ("Entities", "entities"),
        ("Comparisons", "comparisons"),
    ]
    lines = [
        "---",
        'title: "Knowledge Base Index"',
        "type: index",
        f'last_updated: "{datetime.now(timezone.utc).date().isoformat()}"',
        "---",
        "",
        "# Knowledge Base Index",
        "",
    ]
    for title, dirname in sections:
        lines.extend([f"## {title}", ""])
        paths = sorted((wiki_dir / dirname).glob("*.md")) if (wiki_dir / dirname).is_dir() else []
        if paths:
            for path in paths:
                rel = path.relative_to(wiki_dir).with_suffix("").as_posix()
                meta_title = _read_title(path) or _titleize(path.stem)
                lines.append(f"- [[{rel}]] -- {meta_title}")
        else:
            lines.append(f"_No {title.lower()} yet._")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def run_metadata_generators(kb_dir: Path) -> Optional[str]:
    regen = Path(kb_dir) / "tools" / "compile" / "regen_meta.py"
    generate_all = Path(kb_dir) / "tools" / "compile" / "pages" / "generate_all.py"

    for script, label in ((regen, "regen_meta.py"), (generate_all, "generate_all.py")):
        proc = subprocess.run(
            [sys.executable, str(script)],
            cwd=str(kb_dir),
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            diag = (proc.stderr or proc.stdout or "").strip()
            return f"{label} failed" + (f":\n{diag}" if diag else "")
    return None


def append_compile_log(kb_dir: Path, refreshed_sources: list[str], outputs: list[str]) -> None:
    log_path = Path(kb_dir) / "wiki" / "log.md"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).date().isoformat()
    lines = [
        "",
        f"## [{today}] compile | schema-driven typed compile",
        f"- Refreshed sources: {len(refreshed_sources)}",
        f"- Changed outputs: {len(outputs)}",
    ]
    if refreshed_sources:
        lines.append("- Sources: " + ", ".join(sorted(refreshed_sources)))
    text = "\n".join(lines).rstrip() + "\n"
    with log_path.open("a", encoding="utf-8") as fh:
        fh.write(text)


def bundle_outputs(bundle: CompileBundle) -> list[str]:
    outputs = [f"wiki/{bundle.source_rel_path}"]
    outputs.extend(f"wiki/concepts/{_normalize_concept_id(c.concept_id)}.md" for c in bundle.concept_updates)
    outputs.extend(f"wiki/entities/{_slugify(e.name)}.md" for e in bundle.entity_refs)
    for comparison in bundle.comparisons:
        a = _normalize_concept_id(comparison.subject_a)
        b = _normalize_concept_id(comparison.subject_b)
        if a and b and a != b:
            outputs.extend([f"wiki/concepts/{a}.md", f"wiki/concepts/{b}.md"])
            outputs.append(f"wiki/comparisons/{a}-vs-{b}.md")
    outputs.append("wiki/_index.md")
    return sorted(set(outputs))


def _missing_required_scripts(kb_dir: Path) -> Optional[str]:
    regen = Path(kb_dir) / "tools" / "compile" / "regen_meta.py"
    if not regen.exists():
        return f"Missing regen_meta script: {regen}"
    generate_all = Path(kb_dir) / "tools" / "compile" / "pages" / "generate_all.py"
    if not generate_all.exists():
        return f"Missing generate_all script: {generate_all}"
    return None


def _model_from_dict(model_cls: type[ModelT], payload: dict[str, Any]) -> ModelT:
    if hasattr(model_cls, "model_validate"):
        return model_cls.model_validate(payload)  # type: ignore[attr-defined]
    if hasattr(model_cls, "parse_obj"):
        return model_cls.parse_obj(payload)  # type: ignore[attr-defined]
    return model_cls(**payload)


def _ensure_model(model_cls: type[ModelT], item: Any) -> ModelT:
    if isinstance(item, model_cls):
        return item
    if isinstance(item, dict):
        return _model_from_dict(model_cls, item)
    return model_cls(**getattr(item, "__dict__", {}))


def _normalize_comparison(item: Any) -> Comparison:
    comparison = _ensure_model(Comparison, item)
    comparison.dimensions = [
        _ensure_model(ComparisonDimension, dim)
        for dim in (comparison.dimensions or [])
    ]
    return comparison


def _model_dump(model: BaseModel) -> dict[str, Any]:
    if hasattr(model, "model_dump"):
        return model.model_dump()  # type: ignore[attr-defined]
    if hasattr(model, "dict"):
        return model.dict()  # type: ignore[attr-defined]
    return dict(model.__dict__)


def _copy_usage(usage: TokenUsage) -> TokenUsage:
    return TokenUsage(
        input_tokens=usage.input_tokens,
        output_tokens=usage.output_tokens,
        cache_creation_input_tokens=usage.cache_creation_input_tokens,
        cache_read_input_tokens=usage.cache_read_input_tokens,
    )


def _extract_json_object(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError("no JSON object found")
    return stripped[start : end + 1]


def _schema_for_prompt(model_cls: type[BaseModel]) -> dict[str, Any]:
    if hasattr(model_cls, "model_json_schema"):
        return model_cls.model_json_schema()  # type: ignore[attr-defined]
    if hasattr(model_cls, "schema"):
        return model_cls.schema()  # type: ignore[attr-defined]
    return {"type": "object", "required": list(getattr(model_cls, "__annotations__", {}))}


def _read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}
    return payload if isinstance(payload, dict) else {}


def _write_if_changed(path: Path, text: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        if path.exists() and path.read_text(encoding="utf-8") == text:
            return False
    except OSError:
        pass
    path.write_text(text, encoding="utf-8")
    return True


def _frontmatter(fields: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        if isinstance(value, list):
            lines.append(f"{key}: {json.dumps(value, ensure_ascii=True)}")
        else:
            lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=True)}")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def _bullet_lines(items: list[str]) -> list[str]:
    cleaned = [item.strip() for item in items if str(item).strip()]
    return [f"- {item}" for item in cleaned] if cleaned else ["- No details extracted."]


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "untitled"


def _normalize_concept_id(value: str) -> str:
    value = value.strip()
    if value.startswith("[[") and value.endswith("]]"):
        value = value[2:-2].split("|", 1)[0]
    value = value.removeprefix("concepts/").removesuffix(".md")
    return _slugify(value)


def _titleize(slug: str) -> str:
    return " ".join(part.capitalize() for part in _slugify(slug).split("-"))


def _date_part(timestamp: str) -> str:
    if re.match(r"^\d{4}-\d{2}-\d{2}", timestamp):
        return timestamp[:10]
    return datetime.now(timezone.utc).date().isoformat()


def _one_line(text: str, *, fallback: str) -> str:
    stripped = " ".join((text or fallback).split())
    if len(stripped) <= 180:
        return stripped
    return stripped[:177].rstrip() + "..."


def _escape_table(value: str) -> str:
    return " ".join(value.split()).replace("|", "\\|")


def _read_title(path: Path) -> Optional[str]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
    return match.group(1) if match else None


def _first_compiled_at(
    entries: list[tuple[CompileBundle, ConceptUpdate]],
    bundles: list[CompileBundle],
) -> str:
    if entries:
        return entries[0][0].compiled_at
    if bundles:
        return bundles[0].compiled_at
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
