---
title: "Text Embeddings"
type: concept
sources: ["[[sources/pinecone-embedding-models-rundown]]", "[[sources/modal-mteb-leaderboard]]", "[[sources/huggingface-matryoshka-embeddings]]", "[[sources/jina-colbert-late-interaction]]"]
related: ["[[concepts/vector-search]]", "[[concepts/semantic-search]]", "[[concepts/bi-encoder-vs-cross-encoder]]", "[[concepts/matryoshka-representation-learning]]", "[[concepts/chunking-strategies]]", "[[entities/mteb]]", "[[entities/sentence-transformers]]"]
last_compiled: 2026-04-05
summary: "Dense vector representations of text that capture semantic meaning, enabling similarity-based retrieval; the foundation of modern semantic search, RAG, and vector database infrastructure."
reading_time: "4 min"
---

## Overview

Text embeddings are dense numerical vectors that represent the semantic meaning of text in a high-dimensional space. Two pieces of text with similar meaning will have vectors close together (measured by cosine similarity or dot product), even if they share no common words. This property makes embeddings the foundation of [[concepts/semantic-search]], [[concepts/vector-search]], and Retrieval-Augmented Generation (RAG).

## How Embeddings Are Created

Modern text embeddings are produced by transformer-based neural networks. The process involves:

1. **Tokenization**: Convert text into integer sequences (e.g., `[0, 531, 81, 944, ...]`). Most models support up to 512 tokens; some newer models handle 8192+.
2. **Transformer encoding**: Pass tokens through a pretrained transformer (BERT, RoBERTa, MPNet, etc.) to produce contextualized token-level representations.
3. **Pooling**: Aggregate token-level embeddings into a single vector. **Mean pooling** (averaging non-padding token embeddings) is the most common approach, though some models use CLS token pooling.
4. **Normalization**: L2-normalize the output vector so cosine similarity reduces to a dot product.

The resulting vector typically has 384 to 3072 dimensions, depending on the model.

## Key Model Architectures

### Bi-Encoders (Single-Vector Models)

The dominant architecture for embedding models. Encode queries and documents independently into single vectors. Fast at inference (pre-compute document embeddings offline) but lossy — all document meaning must be compressed into one vector. See [[concepts/bi-encoder-vs-cross-encoder]] for details.

### Multi-Vector Models (Late Interaction)

[[concepts/colbert-late-interaction]] produces per-token embeddings (128 dims each) rather than a single vector. More expressive but requires more storage. Scoring uses the MaxSim operation across token pairs.

### Cross-Encoders

Not embedding models per se — they take a query-document pair as joint input and output a relevance score. Used for [[concepts/reranking]] rather than retrieval. See [[concepts/bi-encoder-vs-cross-encoder]].

## Asymmetric Search

Many embedding models distinguish between query and document embeddings:

- **Cohere**: Uses `input_type` parameter ("search_document" vs "search_query")
- **E5**: Prefixes text with "passage:" or "query:"
- **Nomic**: Prefixes with "search_document:" or "search_query:"

This asymmetry reflects that queries are typically short and documents long — the model learns different encoding strategies for each.

## Dimensions and Storage

| Model | Dimensions | Size |
|-------|-----------|------|
| all-MiniLM-L6-v2 | 384 | 22MB |
| E5-base-v2 | 768 | ~400MB |
| Cohere embed-english-v3.0 | 1024 | API-only |
| OpenAI text-embedding-ada-002 | 1536 | API-only |
| OpenAI text-embedding-3-large | 3072 | API-only |
| Gemini Embedding 2 Preview | 3072 | API-only |

Higher dimensions capture more nuance but increase storage cost, memory usage, and retrieval latency. [[concepts/matryoshka-representation-learning]] addresses this by training models whose embeddings can be truncated to any smaller dimension with graceful quality degradation.

## The Embedding Landscape (2025-2026)

The market has shifted dramatically. Key trends:

1. **Open-source parity**: Models like Qwen3-Embedding-8B (Apache-2.0) and bge-m3 (MIT) match or exceed proprietary APIs on [[entities/mteb]] benchmarks
2. **Multimodal embeddings**: Gemini Embedding 2 Preview (March 2026) handles text, image, video, audio, and PDF natively
3. **Dimension flexibility**: Most new models include [[concepts/matryoshka-representation-learning]] for flexible truncation
4. **Domain specialization**: Fine-tuned models (PubMedBERT, Voyage Finance, CodeBERT) significantly outperform general-purpose models in their domains
5. **Lightweight models**: EmbeddingGemma-300M enables on-device embedding generation

## Evaluation

The primary benchmark is [[entities/mteb]] (Massive Text Embedding Benchmark), which evaluates 8 task categories across 56+ datasets. For RAG applications, the **retrieval** and **semantic textual similarity** scores are most predictive of production performance. Caution: MTEB scores are self-reported and can be gamed through benchmark-specific fine-tuning.

## Practical Considerations

- **Speed vs quality**: E5-base-v2 on GPU (3:53 for 42K chunks) was 2.5x faster than OpenAI ada-002 via API (9:07)
- **Cost at scale**: Open-source models eliminate per-API-call costs that compound at high volume
- **Privacy**: Local models avoid sending data to third-party APIs
- **Fine-tuning**: Open-source models can be adapted to domain-specific data; API models cannot

## Sources

- [[sources/pinecone-embedding-models-rundown]] — practical comparison of OpenAI, Cohere, and E5
- [[sources/modal-mteb-leaderboard]] — MTEB benchmark analysis and top models
- [[sources/huggingface-matryoshka-embeddings]] — dimension-flexible embeddings
- [[sources/jina-colbert-late-interaction]] — multi-vector alternative to single-vector embeddings

## Related Concepts

- [[concepts/vector-search]] — using embeddings for retrieval
- [[concepts/semantic-search]] — the search paradigm embeddings enable
- [[concepts/bi-encoder-vs-cross-encoder]] — the two main architectures
- [[concepts/matryoshka-representation-learning]] — dimension flexibility
- [[concepts/chunking-strategies]] — how text is prepared for embedding
- [[concepts/colbert-late-interaction]] — multi-vector alternative
- [[concepts/reranking]] — cross-encoder refinement after embedding retrieval
