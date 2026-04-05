---
title: "Source: Late Interaction Retrieval Models — ColBERT, ColPali, ColQwen"
type: source-summary
source: "[[raw/colbert-late-interaction]]"
related: ["[[concepts/colbert]]", "[[concepts/late-interaction-retrieval]]", "[[concepts/multimodal-rag]]"]
last_compiled: 2026-04-05
summary: "Weaviate overview of late interaction models: ColBERT keeps token-level embeddings with MaxSim scoring, achieving 100x speedup over cross-encoders; ColPali/ColQwen extend this to visual documents."
reading_time: "2 min"
---

## Key Points

- Late interaction sits between bi-encoders (fast, less accurate) and cross-encoders (accurate, slow)
- MaxSim operator: for each query token, find max similarity against all doc tokens, then sum
- ColBERT reduces BERT embeddings from 768 to 128 dimensions per token
- ColBERTv2 residual compression: 256 bytes → 20 bytes per vector, still 6-10x more storage than single-vector
- 100x faster than cross-encoders, 10,000x fewer FLOPs per query
- Strong zero-shot generalization to new domains
- ColPali (3B params, PaliGemma) and ColQwen (2B params, Qwen2-VL) extend to visual documents
- RAGatouille library simplifies ColBERT integration into RAG pipelines

## Detailed Summary

[[concepts/colbert]] represents a key innovation in retrieval architecture. Traditional bi-encoders compress documents into single vectors, losing token-level detail. Cross-encoders preserve this detail but require processing every query-document pair at query time. [[concepts/late-interaction-retrieval]] threads the needle: encode queries and documents independently (like bi-encoders) but keep per-token embeddings and compute fine-grained similarity at query time (like cross-encoders).

The multimodal extensions ([[entities/colpali]], [[entities/colqwen]]) are particularly notable for eliminating OCR pipelines by treating PDF pages as images and processing them into patch embeddings.

## Related Concepts

- [[concepts/colbert]] — the foundational model
- [[concepts/late-interaction-retrieval]] — the paradigm
- [[concepts/multimodal-rag]] — visual document retrieval
