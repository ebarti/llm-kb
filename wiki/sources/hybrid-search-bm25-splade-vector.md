---
title: "Source: Hybrid Search for RAG — BM25, SPLADE, and Vector Search Combined"
type: source-summary
source: "[[raw/hybrid-search-bm25-splade-vector]]"
related: ["[[concepts/hybrid-search]]", "[[concepts/bm25]]", "[[concepts/splade]]", "[[concepts/reranking]]"]
last_compiled: 2026-04-05
summary: "PremAI technical guide comparing BM25, SPLADE, and dense vector search with three fusion strategies (RRF, convex combination, DBSF) — showing +26-31% NDCG improvement on BEIR with hybrid approaches."
reading_time: "2 min"
---

## Key Points

- BM25: exact match, no training required, no vocabulary expansion
- SPLADE: transformer-based sparse vectors with vocabulary expansion, outperforms BM25 on BEIR
- Three fusion strategies: RRF (rank-based), convex combination (score-based), DBSF (distribution-based)
- Benchmark improvements: +26-31% NDCG on BEIR, +24% recall on BRIGHT Biology
- Recommended pipeline: hybrid top-20 → cross-encoder rerank → top-5 to LLM
- Convex combination outperforms RRF when tuned on just 50-100 labeled pairs
- Warning: poorly tuned hybrid can underperform dense-only baselines

## Detailed Summary

This technical guide from PremAI provides the most detailed comparison of sparse retrieval methods for [[concepts/hybrid-search]]. The key addition beyond BM25 is [[concepts/splade]], which uses transformer encoding to expand vocabulary — so "car" in a query can match documents about "automobile." SPLADE outperforms BM25 on most BEIR benchmarks while maintaining inverted index compatibility, at the cost of GPU inference during indexing.

The three fusion strategies represent increasing sophistication: RRF requires no tuning, convex combination needs 50-100 labeled examples, and DBSF adapts to score distribution variance. The production recommendation of hybrid retrieval → cross-encoder reranking is a key architectural pattern.

## Related Concepts

- [[concepts/hybrid-search]] — the combined approach
- [[concepts/bm25]] — traditional sparse retrieval
- [[concepts/splade]] — learned sparse retrieval
- [[concepts/reranking]] — post-retrieval quality improvement
