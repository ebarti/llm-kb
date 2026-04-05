---
title: "BM25 vs Vector Search"
type: comparison
subjects: ["[[concepts/bm25]]", "[[concepts/vector-databases]]"]
sources: ["[[sources/hybrid-search-rag-optimization]]", "[[sources/hybrid-search-bm25-splade-vector]]"]
last_compiled: 2026-04-05
summary: "BM25 excels at exact matches (codes, names, identifiers) while vector search captures semantic meaning — production RAG systems should use both via hybrid search for +26-31% NDCG improvement."
---

## Overview

[[concepts/bm25]] (keyword-based sparse retrieval) and vector search (embedding-based dense retrieval) represent fundamentally different approaches to document retrieval in [[concepts/retrieval-augmented-generation]]. Each excels where the other fails, which is why [[concepts/hybrid-search]] combining both has become the production standard.

## Comparison Table

| Dimension | BM25 | Vector Search |
|---|---|---|
| **Matching type** | Exact keyword matching | Semantic similarity |
| **Strengths** | SKUs, codes, names, legal clauses | Synonyms, paraphrases, conceptual queries |
| **Weaknesses** | No vocabulary expansion | Dilutes exact identifiers |
| **Infrastructure** | Inverted index (CPU) | Vector DB + embeddings (GPU for indexing) |
| **Training required** | None | Embedding model (pretrained or fine-tuned) |
| **Query speed** | Very fast | Fast (ANN search) |
| **Interpretability** | High (term matching is visible) | Low (embedding similarity is opaque) |
| **Example success** | "error code ERR-4521" | "how to improve performance" |
| **Example failure** | "car" won't find "automobile" | "Bank of America" may match "river bank" |

## When Each Wins

**BM25 is better for**:
- Technical documentation with specific identifiers
- Legal and regulatory text with precise terminology
- Code search with exact syntax matching
- Any domain where exact term matching is critical

**Vector search is better for**:
- Conversational, natural language queries
- Cross-lingual or multilingual retrieval
- Domains with high synonym density
- Exploratory, open-ended questions

## The Hybrid Answer

For production RAG, the answer is almost always "both":
1. Run BM25 and vector search in parallel
2. Fuse results via RRF (parameter-free) or convex combination (tunable)
3. Optionally rerank with a cross-encoder

Benchmark data: hybrid approaches yield **+26-31% NDCG improvement** on the BEIR aggregate benchmark versus either method alone.

## Also Consider: SPLADE

[[concepts/splade]] offers a middle ground — learned sparse retrieval with vocabulary expansion. It captures some semantic matching (like vector search) while maintaining inverted index efficiency (like BM25). See [[concepts/splade]] for details.

## Sources

- [[sources/hybrid-search-rag-optimization]] — practical comparison and implementation
- [[sources/hybrid-search-bm25-splade-vector]] — benchmarks and fusion strategies
