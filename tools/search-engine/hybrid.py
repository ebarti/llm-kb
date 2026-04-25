#!/usr/bin/env python3
"""
Hybrid retrieval: Reciprocal Rank Fusion (RRF) over BM25 and dense-vector
result lists.

RRF formula (Cormack et al. 2009):

    score(d) = sum over rankers r of  1 / (k + rank_r(d))

where rank is 1-indexed and k is a smoothing constant (60 is the standard
choice from the literature). Documents absent from a ranker contribute 0 for
that ranker. RRF is robust because it ignores score magnitudes -- it fuses
purely on ordinal rank, which is what we want when combining BM25 log-scores
with cosine similarities.

Chunk vs. document handling: dense search works on chunks; BM25 works on whole
documents. To fuse them we roll up chunk results to the parent doc, keeping
the best-ranking chunk as the representative.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Iterable

# Conventional RRF smoothing constant.
DEFAULT_K = 60


def rrf_fuse(
    ranked_lists: Iterable[list],
    k: int = DEFAULT_K,
    id_key: str = "id",
) -> list:
    """
    Fuse multiple ranked result lists using Reciprocal Rank Fusion.

    Args:
        ranked_lists: iterable of result lists. Each result list is a list of
            dicts, each holding at least `id_key`. Order within each list is
            assumed to be descending relevance (rank 1 = best).
        k: RRF smoothing constant. 60 is standard; higher flattens the curve.
        id_key: which dict key identifies a result.

    Returns:
        A single fused list, sorted by RRF score descending. Each entry is a
        dict carrying:
          - id (from id_key)
          - rrf_score     (the fused score)
          - contributions (per-ranker ranks, 1-indexed; missing entries absent)
          - payload       (the first-seen original result dict for convenience)
    """
    if k <= 0:
        raise ValueError(f"RRF k must be positive, got {k}")

    scores: dict = defaultdict(float)
    contributions: dict = defaultdict(dict)
    payloads: dict = {}

    for r_idx, ranked in enumerate(ranked_lists):
        for rank, item in enumerate(ranked, start=1):
            if not isinstance(item, dict) or id_key not in item:
                # Skip malformed entries rather than crashing.
                continue
            rid = item[id_key]
            scores[rid] += 1.0 / (k + rank)
            contributions[rid][f"ranker_{r_idx}"] = rank
            payloads.setdefault(rid, item)

    fused = [
        {
            "id": rid,
            "rrf_score": scores[rid],
            "contributions": contributions[rid],
            "payload": payloads[rid],
        }
        for rid in scores
    ]
    fused.sort(key=lambda r: r["rrf_score"], reverse=True)
    return fused


def chunks_to_doc_ranking(chunk_results: list) -> list:
    """
    Roll up chunk-level hits into a doc-level ranking, keeping each doc's best
    chunk as the representative.

    Args:
        chunk_results: list of (chunk_dict, score) tuples as produced by
            VectorIndex.search. Each chunk_dict must carry 'doc_id' and
            'chunk_id'.

    Returns:
        A list of dicts suitable for passing to rrf_fuse(), with keys:
            id         -- doc_id
            score      -- best chunk score for that doc
            chunk_id   -- id of the best chunk
            chunk_text -- text of the best chunk (for snippet display)
            heading_path
    """
    best: dict = {}
    for chunk, score in chunk_results:
        doc_id = chunk.get("doc_id")
        if not doc_id:
            continue
        prior = best.get(doc_id)
        if prior is None or score > prior["score"]:
            best[doc_id] = {
                "id": doc_id,
                "score": float(score),
                "chunk_id": chunk.get("chunk_id"),
                "chunk_text": chunk.get("text", ""),
                "heading_path": list(chunk.get("heading_path") or []),
            }

    ranked = sorted(best.values(), key=lambda r: r["score"], reverse=True)
    return ranked


def bm25_results_to_ranking(bm25_results: list) -> list:
    """
    Adapt BM25 output from search.py (dicts with 'id', 'score', ...) into the
    shape expected by rrf_fuse. The input is already sorted by score desc so
    we just pass it through unchanged.
    """
    # The BM25 path already uses 'id' as the identifier -- no-op.
    return [dict(r) for r in bm25_results]


def hybrid_search(
    query: str,
    index,
    vector_index=None,
    encoder=None,
    top_n: int = 10,
    rrf_k: int = DEFAULT_K,
    bm25_k: int = 50,
    vector_k: int = 50,
    bm25_search=None,
    **bm25_kwargs,
) -> list:
    """
    Run BM25 retrieval and, when configured, dense retrieval, fuse the result
    lists with RRF, and return the top-N fused results decorated with BM25
    metadata.

    Args:
        query: raw query string.
        index: the BM25 index dict produced by search.build_index().
        vector_index: an embeddings.VectorIndex, or None to skip dense retrieval.
        encoder: an embeddings.Encoder for encoding the query; required if
            vector_index is provided.
        top_n: final result count.
        rrf_k: RRF smoothing constant.
        bm25_k: how deep into BM25 to consider.
        vector_k: how many chunks to pull from the vector index.
        bm25_search: callable matching search.search's signature. Injected by
            the caller to avoid a circular import at module load.
        bm25_kwargs: extra filters passed through to bm25_search
            (doc_type, tags, date_from, date_to, fuzzy).

    Returns:
        A list of result dicts, shaped like BM25 results for compatibility with
        format_llm / format_pretty, but augmented with 'rrf_score' and
        'chunk_snippet' fields.
    """
    if bm25_search is None:
        raise TypeError(
            "hybrid_search requires a bm25_search callable; pass "
            "search.search from the caller."
        )

    bm25_hits = bm25_search(query, index, top_n=bm25_k, **bm25_kwargs)

    vector_hits: list = []
    chunk_snippets: dict = {}
    if vector_index is not None and encoder is not None and vector_index.vectors.shape[0] > 0:
        q_vec = encoder.encode([query])[0]
        raw_chunks = vector_index.search(q_vec, top_k=vector_k)
        # Apply the same filters BM25 applied: since vector index doesn't know
        # about types/tags/dates, we filter against the BM25 doc metadata here.
        vector_hits_rolled = chunks_to_doc_ranking(raw_chunks)
        # Only run the doc-id filter scan when at least one filter value is
        # actually truthy. The caller in search._run_hybrid always forwards
        # doc_type/tags/date_from/date_to as kwargs (often None), so a bare
        # `if bm25_kwargs:` check would force a full index scan on every
        # hybrid query even when no filter was supplied.
        doc_type = bm25_kwargs.get("doc_type")
        tags = bm25_kwargs.get("tags")
        date_from = bm25_kwargs.get("date_from")
        date_to = bm25_kwargs.get("date_to")
        if doc_type or tags or date_from or date_to:
            allowed = _filter_doc_ids(
                index,
                doc_type=doc_type,
                tags=tags,
                date_from=date_from,
                date_to=date_to,
            )
            vector_hits_rolled = [r for r in vector_hits_rolled if r["id"] in allowed]
        vector_hits = vector_hits_rolled
        chunk_snippets = {
            r["id"]: {
                "chunk_id": r["chunk_id"],
                "text": r["chunk_text"],
                "heading_path": r["heading_path"],
            }
            for r in vector_hits
        }

    # Fuse.
    fused = rrf_fuse(
        [bm25_results_to_ranking(bm25_hits), vector_hits],
        k=rrf_k,
        id_key="id",
    )

    # Decorate: preserve BM25 metadata where available, then supplement with
    # chunk snippet when we have one. BM25 payloads are richer so prefer them.
    bm25_by_id = {r["id"]: r for r in bm25_hits}
    out: list = []
    for entry in fused[:top_n]:
        rid = entry["id"]
        base = bm25_by_id.get(rid)
        if base is None:
            # Vector-only hit -- pull doc metadata from the BM25 index.
            doc_info = index["docs"].get(rid, {})
            base = {
                "id": rid,
                "title": doc_info.get("title", rid),
                "type": doc_info.get("type", "unknown"),
                "tags": doc_info.get("tags", []),
                "date": doc_info.get("date", ""),
                "summary": doc_info.get("summary", ""),
                "path": doc_info.get("path", ""),
                "score": 0.0,
                "bm25": 0.0,
                "tfidf": 0.0,
                "links": doc_info.get("links", []),
                "related": doc_info.get("related", []),
                "sources": doc_info.get("sources", []),
                "backlinks": index["backlinks"].get(rid, []),
            }
        merged = dict(base)
        merged["rrf_score"] = round(entry["rrf_score"], 6)
        merged["rrf_contributions"] = entry["contributions"]
        if rid in chunk_snippets:
            merged["chunk_snippet"] = chunk_snippets[rid]
        out.append(merged)

    return out


def _filter_doc_ids(
    index,
    doc_type=None,
    tags=None,
    date_from=None,
    date_to=None,
    **_,
) -> set:
    """
    Recreate the filtering logic from search.search so vector-only hits respect
    the same constraints the user supplied.
    """
    allowed: set = set()
    tag_set = set(tags) if tags else None
    for doc_id, info in index["docs"].items():
        if doc_type and info.get("type") != doc_type:
            continue
        if tag_set:
            if not tag_set.intersection(set(info.get("tags", []))):
                continue
        doc_date = info.get("date", "")
        if date_from and doc_date and doc_date < date_from:
            continue
        if date_to and doc_date and doc_date > date_to:
            continue
        allowed.add(doc_id)
    return allowed


__all__ = [
    "rrf_fuse",
    "chunks_to_doc_ranking",
    "bm25_results_to_ranking",
    "hybrid_search",
    "DEFAULT_K",
]
