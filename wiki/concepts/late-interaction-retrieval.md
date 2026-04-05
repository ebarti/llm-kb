---
title: "Late Interaction Retrieval"
type: concept
sources: ["[[sources/colbert-late-interaction]]"]
related: ["[[concepts/colbert]]", "[[concepts/hybrid-search]]", "[[concepts/reranking]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "A retrieval paradigm between bi-encoders and cross-encoders: independently encode queries and documents into per-token embeddings, then compute fine-grained MaxSim scoring at query time — balancing accuracy and speed."
---

## Overview

Late interaction retrieval is a neural retrieval paradigm that sits between two extremes:

- **Bi-encoders**: Encode queries and documents into single vectors independently. Fast (pre-computed document vectors) but lose token-level detail.
- **Cross-encoders**: Process query and document together through full attention. Accurate but too slow for corpus-scale search.

Late interaction models like [[concepts/colbert]] independently encode queries and documents (like bi-encoders for efficiency) but keep **per-token embeddings** and compute token-level similarity at query time (like cross-encoders for accuracy). The MaxSim operator scores each query token against its best-matching document token, then sums the scores.

## The Tradeoff

| Property | Bi-Encoder | Late Interaction | Cross-Encoder |
|---|---|---|---|
| Encoding | Independent, single vector | Independent, per-token vectors | Joint, full attention |
| Pre-computation | Full | Full | None |
| Query-time cost | Low | Medium | High |
| Accuracy | Lower | Near cross-encoder | Highest |
| Storage | 1 vector/doc | Many vectors/doc | N/A |

## Key Models

- [[concepts/colbert]] (ColBERTv2): Text retrieval, 128-dim per-token embeddings
- **ColPali**: Visual document retrieval using PaliGemma (~3B params)
- **ColQwen**: Visual document retrieval using Qwen2-VL (~2B params, Apache 2.0)

## Sources

- [[sources/colbert-late-interaction]] — comprehensive overview of late interaction models

## Related Concepts

- [[concepts/colbert]] — the primary late interaction model
- [[concepts/reranking]] — late interaction can also serve reranking purposes
- [[concepts/hybrid-search]] — late interaction can complement sparse retrieval
