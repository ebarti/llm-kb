#!/usr/bin/env python3
"""
Build (or rebuild) the search indexes for the wiki.

Two indexes are maintained:
  - BM25 index (always built; pure stdlib, fast)
  - Vector index (optional; requires sentence-transformers + numpy)

Usage:
    python build-index.py                     # BM25 only (default, stdlib-only)
    python build-index.py --vectors           # BM25 + incremental vector index
    python build-index.py --vectors --force   # BM25 + full vector rebuild
    python build-index.py --vectors-only      # skip BM25, vectors only
"""

import argparse
import sys
import time
from pathlib import Path

# Import from search module (sibling file)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from search import scan_documents, build_index, save_index, INDEX_FILE


def _build_bm25(force):
    print("Scanning wiki documents...")
    t0 = time.time()
    docs = scan_documents()
    print(f"  Found {len(docs)} documents")

    print("Building BM25 index...")
    index = build_index(docs)

    print("Saving BM25 index...")
    save_index(index)

    elapsed = time.time() - t0
    print(f"BM25 index built in {elapsed:.2f}s")
    print(f"  Documents: {index['num_docs']}")
    print(f"  Vocabulary: {len(index['vocab'])} terms")
    print(f"  Avg doc length: {index['avg_dl']:.0f} tokens")
    print(f"  Saved to: {INDEX_FILE}")
    return docs


def _build_vectors(docs, force):
    try:
        import embeddings
        from chunker import chunk_document
    except ImportError as e:
        print(f"\nVector index build skipped: {e}", file=sys.stderr)
        return 1

    ok, msg = embeddings.is_available()
    if not ok:
        print(f"\nVector index build skipped: {msg}", file=sys.stderr)
        return 1

    print("\nChunking documents...")
    t0 = time.time()
    all_chunks = []
    for doc in docs:
        chunks = chunk_document(doc["id"], doc["body"])
        all_chunks.extend(chunks)
    print(f"  Produced {len(all_chunks)} chunks from {len(docs)} documents")
    if all_chunks:
        avg = sum(c.tokens for c in all_chunks) / len(all_chunks)
        print(f"  Avg chunk tokens: {avg:.0f}")

    existing = None if force else embeddings.VectorIndex.load()
    if existing is not None and force:
        print("  --force: ignoring existing vector cache")

    print("Encoding (first run downloads model to ~/.cache/huggingface)...")
    encoder = embeddings.Encoder()
    vec_index = embeddings.build_or_update_index(
        all_chunks, encoder=encoder, existing=existing, verbose=True,
    )
    vec_index.save()
    elapsed = time.time() - t0
    print(f"Vector index built in {elapsed:.2f}s")
    print(f"  Chunks: {len(vec_index.chunks)}")
    print(f"  Dim: {vec_index.dim}")
    print(f"  Model: {vec_index.model_name}")
    print(f"  Saved to: {embeddings.VECTORS_FILE} + {embeddings.CHUNKS_FILE}")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Build the wiki search index(es)")
    parser.add_argument("--force", action="store_true", help="Force full rebuild (ignore cache)")
    parser.add_argument("--vectors", action="store_true",
                        help="Also build the dense-vector index (requires optional ML deps)")
    parser.add_argument("--vectors-only", action="store_true",
                        help="Build only the vector index (assume BM25 already current)")
    args = parser.parse_args()

    docs = None
    if not args.vectors_only:
        docs = _build_bm25(args.force)

    if args.vectors or args.vectors_only:
        if docs is None:
            # --vectors-only path: we still need the docs list for chunking
            print("Scanning wiki documents for chunking...")
            docs = scan_documents()
            print(f"  Found {len(docs)} documents")
        rc = _build_vectors(docs, args.force)
        if rc != 0:
            sys.exit(rc)


if __name__ == "__main__":
    main()
