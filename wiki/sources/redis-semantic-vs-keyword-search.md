---
title: "Source: Semantic Search vs. Keyword Search"
type: source-summary
source: "[[raw/redis-semantic-vs-keyword-search]]"
related: ["[[concepts/semantic-search]]", "[[concepts/keyword-search]]", "[[concepts/hybrid-search]]", "[[comparisons/semantic-vs-keyword-search]]"]
last_compiled: 2026-04-05
summary: "Redis's comprehensive comparison of semantic vs keyword search: complementary failure modes, when to use each, and why production systems need hybrid approaches combining both."
reading_time: "1 min"
---

## Key Points

- Semantic search uses transformer models (BERT) for dense vector embeddings with cosine similarity
- Keyword search uses inverted indexes with BM25 probabilistic ranking
- Complementary failure modes: semantic fails on exact codes ("SKU-2847-B"); keyword fails on synonyms ("car repairs" vs "automotive maintenance")
- Keyword search is deterministic (critical for compliance); semantic results vary with retraining
- Keyword search: minimal memory, fast; semantic: significant memory, higher latency (especially CPU)
- GPU acceleration substantially improves semantic search performance
- Hybrid architecture: parallel HNSW + BM25 indexes, same document collection, merge via RRF

## Detailed Summary

The article provides the clearest articulation of why [[concepts/semantic-search]] and [[concepts/keyword-search]] are complementary rather than competing approaches. The failure mode analysis is particularly valuable: semantic search cannot reliably match product codes, error identifiers, or other string-literal patterns, while keyword search misses conceptually related content when different terminology is used. This complementarity is exactly why [[concepts/hybrid-search]] has become the production standard — combining HNSW vector indexes with BM25 inverted indexes over the same document collection.

## Related Concepts

- [[concepts/semantic-search]] — vector-based meaning matching
- [[concepts/keyword-search]] — lexical term matching
- [[concepts/hybrid-search]] — the combined approach
- [[comparisons/semantic-vs-keyword-search]] — the full comparison article
