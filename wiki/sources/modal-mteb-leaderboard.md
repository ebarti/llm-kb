---
title: "Source: Top Embedding Models on the MTEB Leaderboard"
type: source-summary
source: "[[raw/modal-mteb-leaderboard]]"
related: ["[[entities/mteb]]", "[[concepts/text-embeddings]]", "[[concepts/matryoshka-representation-learning]]"]
last_compiled: 2026-04-05
summary: "Modal's analysis of the MTEB leaderboard: 8 task categories, top open-weight models (Qwen3-Embedding-8B, NVIDIA Nemotron, bge-m3), domain-specific outperformance, and the open-source catch-up to proprietary APIs."
reading_time: "2 min"
---

## Key Points

- MTEB evaluates 8 task categories: classification, clustering, pair classification, reranking, retrieval, STS, summarization, bitext mining
- English MTEB: 56 datasets; Multilingual MMTEB: 131 tasks, 250+ languages
- Top open-weight (2025): Qwen3-Embedding-8B (Apache-2.0), llama-embed-nemotron-8b (NVIDIA), bge-m3 (MIT)
- Domain-specific models significantly outperform general-purpose (PubMedBERT, Voyage Finance, CodeBERT)
- Retrieval and STS scores correlate most with production RAG/search performance
- Open-source has caught up with and surpassed commercial APIs on benchmarks
- Gemini Embedding 2 Preview (March 2026): 5 modalities, native MRL, 3072 dims
- EmbeddingGemma-300M: 300M params, 100+ languages, on-device deployment

## Detailed Summary

The article provides essential context for interpreting [[entities/mteb]] scores. The key insight is that the overall average score hides task-specific variation — a model leading in classification may underperform in retrieval. For RAG applications, retrieval and semantic textual similarity scores matter most. The landscape has shifted dramatically: open-weight models like Qwen3-Embedding-8B now rival or exceed commercial offerings, and domain-specific fine-tuning (finance, medicine, code) consistently outperforms general models. The newest generation (Gemini Embedding 2, March 2026) adds multimodal support and native [[concepts/matryoshka-representation-learning]].

## Related Concepts

- [[entities/mteb]] — the benchmark itself
- [[concepts/text-embeddings]] — what's being benchmarked
- [[concepts/matryoshka-representation-learning]] — increasingly standard in top models
