---
title: "RAG vs. Index-Based Retrieval"
type: concept
sources: ["[[sources/karpathy-llm-knowledge-bases]]"]
related: ["[[concepts/llm-qa-over-documents]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "At small-to-medium scale (~100 articles, ~400K words), LLM-maintained index files and one-line summaries can replace vector database RAG for document Q&A."
---

## Overview

Retrieval-Augmented Generation (RAG) uses vector embeddings and similarity search to retrieve relevant document chunks for LLM Q&A. However, at small-to-medium scale, a simpler approach — LLM-maintained index files and concise summaries — can be equally or more effective.

## Key Ideas

- **RAG**: Chunks documents, embeds them into a vector database, retrieves top-k chunks by semantic similarity at query time. Scales to very large corpora but adds infrastructure complexity.
- **Index-based retrieval**: The LLM maintains a `summaries.md` file with one-line descriptions of every article. At query time, the LLM reads this index to identify relevant full articles, then reads those articles directly.
- **Scale threshold**: Karpathy found index-based retrieval sufficient at ~100 articles and ~400K words. Above this scale, RAG or finetuning may become necessary.
- **LLM finetuning as alternative**: At large scale, synthetic data generation + finetuning could encode the corpus into model weights, eliminating context window retrieval entirely.

## Trade-offs

| | Index-Based | RAG | Finetuning |
|---|---|---|---|
| Infrastructure | Minimal | Vector DB required | Training pipeline |
| Scale | Small-medium | Large | Very large |
| Freshness | Immediate (recompile) | Re-embed on update | Retrain to update |
| Accuracy | High (LLM reads full articles) | Depends on chunk quality | Baked into weights |

## Sources

- [[sources/karpathy-llm-knowledge-bases]] — Karpathy's observation that RAG was not needed at small scale

## Related Concepts

- [[concepts/llm-qa-over-documents]] — the Q&A system that uses this retrieval approach
- [[concepts/llm-knowledge-base]] — the broader system
