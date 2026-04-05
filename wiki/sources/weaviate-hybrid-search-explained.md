---
title: "Source: Hybrid Search Explained"
type: source-summary
source: "[[raw/weaviate-hybrid-search-explained]]"
related: ["[[concepts/hybrid-search]]", "[[concepts/bm25]]", "[[concepts/vector-search]]", "[[entities/weaviate]]"]
last_compiled: 2026-04-05
summary: "Weaviate's technical explanation of hybrid search combining BM25 keyword scoring with dense vector search via Reciprocal Rank Fusion, including the alpha parameter for tuning the balance."
reading_time: "1 min"
---

## Key Points

- Hybrid search merges sparse (BM25) and dense (vector) results into a single ranked list
- BM25 builds on TF-IDF with Binary Independence Model and document-length normalization
- BM25F variant (Weaviate v1.17+) allows per-field weighting (e.g., title vs body)
- Reciprocal Rank Fusion: score = sum(1/(k + r(d))) across both ranked lists
- Alpha parameter: 0 = pure keyword, 0.5 = equal, 1 = pure vector; default 0.75
- Two fusion algorithms available: rankedFusion (default) and relativeScoreFusion

## Detailed Summary

The article explains how [[entities/weaviate]] implements [[concepts/hybrid-search]] by running BM25 keyword search and dense vector search in parallel, then merging results. The [[concepts/bm25]] component handles exact-term matching while [[concepts/vector-search]] captures semantic meaning. The key tunable is the alpha parameter — defaulting to 0.75 (favoring vector search) — which lets users balance precision of keyword matching against the recall of semantic understanding depending on their use case.

## Related Concepts

- [[concepts/hybrid-search]] — the retrieval strategy
- [[concepts/bm25]] — the keyword scoring algorithm
- [[concepts/vector-search]] — the semantic component
- [[entities/weaviate]] — the implementing database
