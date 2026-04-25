#!/usr/bin/env python3
"""
Optional cross-encoder reranker.

Cross-encoders (like bge-reranker-v2-m3) score (query, document) pairs jointly,
which is much more accurate than separately-encoded dense retrieval but far
slower. The standard pattern is: retrieve top-K with a fast hybrid (BM25 + dense),
then rerank the top-K with a cross-encoder before returning the final top-N.

Gated behind the --rerank flag on the CLI. Lazy-loads the model on first use.
Falls back gracefully when sentence-transformers is missing.
"""

from __future__ import annotations

import os
from typing import Optional

DEFAULT_MODEL = "BAAI/bge-reranker-v2-m3"
MODEL_NAME = os.environ.get("KB_RERANK_MODEL", DEFAULT_MODEL)

# Cap how many candidates we send to the cross-encoder -- each forward pass is
# expensive and returns diminishing gains past ~50.
DEFAULT_RERANK_POOL = 50


def is_available() -> tuple[bool, str]:
    """Whether the cross-encoder stack can run."""
    try:
        import sentence_transformers  # noqa: F401
    except ImportError:
        return False, (
            "sentence-transformers is not installed. Install optional ML deps:\n"
            "  pip install -r tools/search-engine/requirements-ml.txt\n"
            "Reranker will download on first run (~1GB)."
        )
    return True, "ok"


class CrossEncoderReranker:
    """
    Lazy wrapper around sentence_transformers.CrossEncoder. The model is loaded
    on first .score_pairs() call so importing this module is free.
    """
    def __init__(self, model_name: str = MODEL_NAME):
        self.model_name = model_name
        self._model = None

    def _ensure_loaded(self):
        if self._model is not None:
            return
        ok, msg = is_available()
        if not ok:
            raise RuntimeError(msg)
        if not os.environ.get("KB_EMBED_VERBOSE"):
            import logging
            logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
        from sentence_transformers import CrossEncoder
        self._model = CrossEncoder(self.model_name)

    def score_pairs(self, pairs: list) -> list:
        """
        Score a list of (query, document) pairs. Returns parallel list of
        floats; higher is more relevant.
        """
        self._ensure_loaded()
        if not pairs:
            return []
        # CrossEncoder.predict returns a numpy array; convert to plain floats.
        scores = self._model.predict(pairs, show_progress_bar=False)
        return [float(s) for s in scores]


def rerank_results(
    query: str,
    results: list,
    reranker: Optional[CrossEncoderReranker] = None,
    pool: int = DEFAULT_RERANK_POOL,
    text_keys: tuple = ("chunk_snippet", "summary", "title"),
) -> list:
    """
    Rerank a list of candidate result dicts using a cross-encoder.

    Args:
        query: the original query.
        results: list of result dicts (as produced by hybrid_search). Only the
            first `pool` are reranked; the rest keep their existing order.
        reranker: CrossEncoderReranker instance; one is created if omitted.
        pool: how many top results to consider for reranking.
        text_keys: ordered list of keys to try when extracting the doc text to
            pair with the query. The first non-empty match wins. We prefer the
            chunk snippet (most specific) then summary then title.

    Returns:
        A new list with the top `pool` reordered by cross-encoder score (desc),
        followed by any remaining results untouched. Each reranked entry gains
        a `rerank_score` field.
    """
    if not results:
        return results

    pool = max(int(pool), 0)
    if pool == 0:
        return list(results)

    if reranker is None:
        reranker = CrossEncoderReranker()

    head = results[:pool]
    tail = results[pool:]

    pairs = []
    for r in head:
        doc_text = _extract_text(r, text_keys)
        pairs.append((query, doc_text))

    scores = reranker.score_pairs(pairs)

    for r, s in zip(head, scores):
        r["rerank_score"] = round(float(s), 6)

    head.sort(key=lambda r: r.get("rerank_score", 0.0), reverse=True)
    return head + tail


def _extract_text(result: dict, keys: tuple) -> str:
    """Pull the best available text for reranking from a result dict."""
    for k in keys:
        v = result.get(k)
        if isinstance(v, dict):
            # chunk_snippet is a nested dict with a 'text' field.
            t = v.get("text") or v.get("content") or ""
            if t:
                return t
        elif isinstance(v, str) and v:
            return v
    # Fallback to title
    return result.get("title", "")


__all__ = [
    "CrossEncoderReranker",
    "rerank_results",
    "is_available",
    "DEFAULT_MODEL",
    "DEFAULT_RERANK_POOL",
]
