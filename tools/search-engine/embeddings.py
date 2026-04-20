#!/usr/bin/env python3
"""
Dense embedding index for the wiki.

Design goals:
- **Offline**: uses a local sentence-transformer model (BGE-small-en-v1.5 by
  default). First run downloads weights to ~/.cache/huggingface; subsequent
  runs are fully offline.
- **Incremental**: only re-embeds chunks whose content hash changed. Existing
  vectors are reused.
- **Graceful degradation**: this module imports cleanly even when numpy or
  sentence-transformers is missing. Callers use `is_available()` to check.

Storage layout under `tools/search-engine/.index/`:
    vectors.npy    -- float32 array of shape (N, D)
    chunks.json    -- parallel array of chunk metadata, same length as vectors

Both files are regenerated together so they are always aligned by row index.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

try:
    import numpy as np
    _HAS_NUMPY = True
except ImportError:
    np = None  # type: ignore
    _HAS_NUMPY = False

# We DO NOT import sentence_transformers at module load time -- that's slow and
# pulls in torch. We import it lazily inside the encoder the first time it's
# used, so this module stays cheap to import for everyone else.

# -----------------------------------------------------------------------------
# Paths and defaults
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
INDEX_DIR = BASE_DIR / ".index"
VECTORS_FILE = INDEX_DIR / "vectors.npy"
CHUNKS_FILE = INDEX_DIR / "chunks.json"

DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
# Allow override via env var so users with air-gapped environments can point
# at a pre-downloaded local path.
MODEL_NAME = os.environ.get("KB_EMBED_MODEL", DEFAULT_MODEL)

BATCH_SIZE = 32


# -----------------------------------------------------------------------------
# Availability gate
# -----------------------------------------------------------------------------

def is_available() -> tuple[bool, str]:
    """
    Check whether the embedding pipeline can run.

    Returns (ok, message). When ok is False, `message` is a user-facing hint
    explaining what's missing and how to install it.
    """
    if not _HAS_NUMPY:
        return False, (
            "numpy is not installed. Install optional ML deps:\n"
            "  pip install -r tools/search-engine/requirements-ml.txt"
        )
    try:
        import sentence_transformers  # noqa: F401
    except ImportError:
        return False, (
            "sentence-transformers is not installed. Install optional ML deps:\n"
            "  pip install -r tools/search-engine/requirements-ml.txt\n"
            "First run will download the model (~130MB) to ~/.cache/huggingface."
        )
    return True, "ok"


# -----------------------------------------------------------------------------
# Encoder wrapper (lazy)
# -----------------------------------------------------------------------------

class Encoder:
    """
    Wrapper around sentence-transformers that loads the model lazily on first
    `.encode()` call. The instance is safe to construct even if weights aren't
    downloaded yet -- the actual load happens on demand.
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
        # Silence sentence_transformers info logs unless the user opts in.
        if not os.environ.get("KB_EMBED_VERBOSE"):
            import logging
            logging.getLogger("sentence_transformers").setLevel(logging.WARNING)
        from sentence_transformers import SentenceTransformer
        self._model = SentenceTransformer(self.model_name)

    def dim(self) -> int:
        self._ensure_loaded()
        return int(self._model.get_sentence_embedding_dimension())

    def encode(self, texts, batch_size: int = BATCH_SIZE, show_progress: bool = False):
        """
        Encode a list of strings into a (N, D) float32 numpy array.
        Results are L2-normalized so that dot product == cosine similarity.
        """
        self._ensure_loaded()
        import numpy as np  # safe: is_available() passed
        vecs = self._model.encode(
            list(texts),
            batch_size=batch_size,
            show_progress_bar=show_progress,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )
        return vecs.astype(np.float32, copy=False)


# -----------------------------------------------------------------------------
# Incremental vector index
# -----------------------------------------------------------------------------

@dataclass
class VectorIndex:
    """
    Thin wrapper over parallel (vectors.npy, chunks.json) storage.

    Invariants:
      - `vectors` is a (N, D) float32 array, L2-normalized.
      - `chunks` is a list of length N holding dicts with at least
        'chunk_id', 'doc_id', 'heading_path', 'text', 'tokens', 'content_hash'.
      - Row i in `vectors` corresponds to entry i in `chunks`.
    """
    vectors: "np.ndarray"        # type: ignore[name-defined]
    chunks: list
    dim: int
    model_name: str

    @classmethod
    def empty(cls, dim: int, model_name: str) -> "VectorIndex":
        if not _HAS_NUMPY:
            raise RuntimeError("numpy required for VectorIndex")
        return cls(
            vectors=np.zeros((0, dim), dtype=np.float32),
            chunks=[],
            dim=dim,
            model_name=model_name,
        )

    def save(self, vectors_file: Path = VECTORS_FILE, chunks_file: Path = CHUNKS_FILE):
        if not _HAS_NUMPY:
            raise RuntimeError("numpy required to save VectorIndex")
        INDEX_DIR.mkdir(parents=True, exist_ok=True)
        np.save(vectors_file, self.vectors)
        meta = {
            "model_name": self.model_name,
            "dim": self.dim,
            "chunks": self.chunks,
        }
        chunks_file.write_text(json.dumps(meta, indent=2), encoding="utf-8")

    @classmethod
    def load(cls, vectors_file: Path = VECTORS_FILE, chunks_file: Path = CHUNKS_FILE) -> Optional["VectorIndex"]:
        if not _HAS_NUMPY:
            return None
        if not vectors_file.exists() or not chunks_file.exists():
            return None
        try:
            vectors = np.load(vectors_file)
            meta = json.loads(chunks_file.read_text(encoding="utf-8"))
        except Exception:
            return None
        return cls(
            vectors=vectors.astype(np.float32, copy=False),
            chunks=meta.get("chunks", []),
            dim=int(meta.get("dim", vectors.shape[1] if vectors.ndim == 2 else 0)),
            model_name=meta.get("model_name", MODEL_NAME),
        )

    def search(self, query_vec, top_k: int = 20) -> list:
        """
        Cosine-similarity search. Since vectors are L2-normalized, dot product
        is cosine. Returns list of (chunk_dict, score) sorted by score desc.
        """
        if not _HAS_NUMPY or self.vectors.shape[0] == 0:
            return []
        # Support both 1-D (D,) and 2-D (1, D) query vectors.
        q = query_vec.reshape(-1) if query_vec.ndim > 1 else query_vec
        scores = self.vectors @ q  # (N,)
        k = min(top_k, scores.shape[0])
        # argpartition is O(N) vs argsort's O(N log N)
        idx = np.argpartition(-scores, k - 1)[:k]
        idx = idx[np.argsort(-scores[idx])]
        return [(self.chunks[i], float(scores[i])) for i in idx]


def build_or_update_index(
    chunks: list,
    encoder: Optional[Encoder] = None,
    existing: Optional[VectorIndex] = None,
    verbose: bool = False,
) -> VectorIndex:
    """
    Build or incrementally update a vector index from a list of Chunks (or chunk
    dicts). Only chunks whose content_hash is not already present are re-encoded.

    Args:
        chunks: list of chunker.Chunk objects OR dicts with the same shape.
        encoder: Encoder instance; if None a default one is created.
        existing: prior VectorIndex to reuse; if None we try to load from disk.
        verbose: print progress.

    Returns:
        A fresh VectorIndex ordered to match the incoming `chunks` list.
        Stale entries (chunks that disappeared) are dropped automatically.
    """
    ok, msg = is_available()
    if not ok:
        raise RuntimeError(msg)
    import numpy as np  # safe past is_available()

    if encoder is None:
        encoder = Encoder()

    # Normalize input to dicts
    norm: list = []
    for c in chunks:
        if hasattr(c, "to_dict"):
            norm.append(c.to_dict())
        elif hasattr(c, "embed_text"):
            # Plain object with the right duck type
            norm.append({
                "chunk_id": c.chunk_id,
                "doc_id": c.doc_id,
                "heading_path": list(getattr(c, "heading_path", [])),
                "text": c.text,
                "tokens": int(getattr(c, "tokens", 0)),
                "content_hash": c.content_hash,
            })
        else:
            norm.append(dict(c))

    if existing is None:
        existing = VectorIndex.load()

    # Build a hash -> vector lookup from the prior index so we can reuse rows.
    hash_to_vec: dict = {}
    if existing is not None and existing.vectors.shape[0] == len(existing.chunks):
        # Only trust the cache if the model name matches -- changing models
        # invalidates all prior vectors.
        if existing.model_name == encoder.model_name:
            for i, c in enumerate(existing.chunks):
                h = c.get("content_hash")
                if h:
                    hash_to_vec[h] = existing.vectors[i]

    # Partition: which chunks need fresh encoding vs. can be copied.
    to_encode_idx: list = []
    to_encode_text: list = []
    for i, c in enumerate(norm):
        if c["content_hash"] not in hash_to_vec:
            to_encode_idx.append(i)
            bc = " > ".join(c.get("heading_path") or [])
            text = f"{bc}\n\n{c['text']}" if bc else c["text"]
            to_encode_text.append(text)

    if verbose:
        reused = len(norm) - len(to_encode_idx)
        print(f"  Embedding {len(to_encode_idx)} new chunks (reused {reused})")

    # Encode the deltas
    new_vecs = None
    if to_encode_text:
        new_vecs = encoder.encode(to_encode_text, show_progress=verbose)

    # Assemble the fresh vectors array in the order of `norm`.
    dim = encoder.dim()
    vectors = np.zeros((len(norm), dim), dtype=np.float32)
    new_cursor = 0
    for i, c in enumerate(norm):
        cached = hash_to_vec.get(c["content_hash"])
        if cached is not None:
            vectors[i] = cached
        else:
            vectors[i] = new_vecs[new_cursor]
            new_cursor += 1

    return VectorIndex(
        vectors=vectors,
        chunks=norm,
        dim=dim,
        model_name=encoder.model_name,
    )


__all__ = [
    "Encoder",
    "VectorIndex",
    "build_or_update_index",
    "is_available",
    "VECTORS_FILE",
    "CHUNKS_FILE",
    "MODEL_NAME",
    "DEFAULT_MODEL",
]
