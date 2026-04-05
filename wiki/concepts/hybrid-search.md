---
title: "Hybrid Search"
type: concept
sources: ["[[sources/weaviate-hybrid-search-explained]]", "[[sources/superlinked-hybrid-search-reranking]]", "[[sources/redis-semantic-vs-keyword-search]]", "[[sources/hybrid-search-rag-optimization]]", "[[sources/hybrid-search-bm25-splade-vector]]", "[[sources/ragflow-rag-review-2025]]"]
related: ["[[concepts/bm25]]", "[[concepts/vector-search]]", "[[concepts/semantic-search]]", "[[concepts/keyword-search]]", "[[concepts/reranking]]", "[[concepts/two-stage-retrieval]]", "[[concepts/splade]]", "[[concepts/colbert]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "Combining BM25/SPLADE keyword search with dense vector search in parallel, merging via RRF or convex combination — yielding +26-31% NDCG improvement on BEIR benchmarks over single-method retrieval."
---

## Overview

Hybrid search combines two complementary retrieval methods — [[concepts/keyword-search]] (via [[concepts/bm25]]) and [[concepts/vector-search]] (via [[concepts/text-embeddings]]) — into a single ranked result list. This addresses the fundamental limitation that each approach fails where the other succeeds: keyword search misses synonyms and conceptual matches, while vector search misses exact identifiers and string-literal patterns.

## Architecture

```
Query
  ├── BM25 Search (Inverted Index) → Ranked List A
  ├── Vector Search (HNSW Index)    → Ranked List B
  └── Fusion (RRF or Weighted)      → Merged Ranked List
                                        └── Optional: Reranking
```

Both indexes reference the same document collection — no data duplication required. Searches execute in parallel.

## Result Fusion Methods

### Reciprocal Rank Fusion (RRF)

```
RRF(d) = Σ 1/(k + r(d))
```

Where r(d) is the rank of document d in each list and k is a constant (typically 60). RRF penalizes lower-ranked documents and does not require score normalization between the two methods.

Example: Document ranked 1st in BM25 and 3rd in vector search:
- Score = 1/(0+1) + 1/(0+3) = 1.33

### Weighted Alpha Fusion

```
H = (1-α)K + αV
```

Where K is the keyword score, V is the vector score, and alpha controls the balance:
- alpha = 0: pure keyword search
- alpha = 0.5: equal weighting
- alpha = 0.75: default in [[entities/weaviate]] (favors vector)
- alpha = 1: pure vector search

### Relative Score Fusion

Normalizes scores from each method to [0,1] before combining. Available in Weaviate as an alternative to ranked fusion.

## Where Hybrid Excels

Testing shows hybrid search significantly outperforms either method alone for:

- **Abbreviations**: GAN, LLaMA, BERT (keyword catches the exact acronym; vector catches the concept)
- **Named entities**: Biden, Salvador Dali (exact name + contextual information)
- **Geographic locations**: Strait of Hormuz (exact place name + related content)
- **Code snippets**: Exact syntax + semantic understanding of purpose
- **Domain-specific queries**: Technical terms with conceptual context

## Implementation Support

| Database | Hybrid Support | Notes |
|----------|---------------|-------|
| [[entities/weaviate]] | Native | Alpha parameter, BM25F, two fusion algorithms |
| [[entities/qdrant]] | Native | Sparse + dense vectors |
| Elasticsearch | Native | kNN + full-text in single query |
| Redis | Native | HNSW + full-text, unified API |
| [[entities/pinecone]] | Limited | No native BM25/full-text |
| ChromaDB | Manual | Requires EnsembleRetriever wrapper |

## SPLADE: Learned Sparse Retrieval

Beyond BM25, [[concepts/splade]] (Sparse Lexical and Expansion model) offers a learned alternative for the sparse component. SPLADE uses transformer encoding to generate sparse vectors with **vocabulary expansion** — so "car" in a query can match documents about "automobile." It outperforms BM25 on most BEIR benchmarks while maintaining inverted index compatibility, at the cost of GPU-accelerated inference during indexing.

**Selection guide**: Use BM25 for exact-match-heavy domains (legal identifiers, financial codes). Deploy SPLADE when vocabulary mismatch between queries and documents is high.

## Distribution-Based Score Fusion (DBSF)

In addition to RRF and alpha-weighted fusion, DBSF normalizes scores using each retriever's mean and standard deviation (clipping at +/-3 sigma). This adapts to varying score distributions across queries. Research shows convex combination outperforms RRF when tuned on as few as 50-100 labeled query pairs.

## Benchmark Results

Hybrid search improvements vary by domain, reflecting vocabulary mismatch severity:
- **BEIR aggregate**: +26-31% NDCG improvement
- **BRIGHT Biology**: +24% recall gain
- **WANDS e-commerce**: +1.7-1.9% Mean NDCG
- **OpenSearch real-world**: +9% MAP, +19% NDCG

## Production Pipeline

The recommended architecture separates recall optimization from precision optimization:
1. **Hybrid retrieval** → top-20 candidates via RRF or convex combination
2. **Cross-encoder [[concepts/reranking]]** → score query-document pairs jointly
3. **Top-5 reranked results** → pass to the LLM

Reranking cannot recover documents missed during initial retrieval, making hybrid search's expanded candidate set essential.

## Limitations

- **Higher latency**: Running two search algorithms is slower than either alone
- **Tuning complexity**: Alpha/fusion parameters need domain-specific calibration
- **Infrastructure**: Not all vector databases support hybrid natively
- **Score normalization**: BM25 and cosine similarity scores are on different scales; fusion must account for this

## Sources

- [[sources/weaviate-hybrid-search-explained]] — RRF, alpha parameter, Weaviate implementation
- [[sources/superlinked-hybrid-search-reranking]] — full pipeline with fusion and reranking
- [[sources/redis-semantic-vs-keyword-search]] — parallel index architecture

## Related Concepts

- [[concepts/bm25]] — the keyword ranking algorithm
- [[concepts/vector-search]] — the semantic retrieval component
- [[concepts/semantic-search]] — meaning-based search
- [[concepts/keyword-search]] — term-based search
- [[concepts/reranking]] — often applied after hybrid retrieval
- [[concepts/two-stage-retrieval]] — the broader pipeline hybrid fits into
