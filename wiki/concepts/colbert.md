---
title: "ColBERT (Contextualized Late Interaction over BERT)"
type: concept
sources: ["[[sources/colbert-late-interaction]]"]
related: ["[[concepts/late-interaction-retrieval]]", "[[concepts/hybrid-search]]", "[[concepts/retrieval-augmented-generation]]", "[[concepts/reranking]]"]
last_compiled: 2026-04-05
summary: "A retrieval model that keeps per-token embeddings and uses MaxSim scoring — 100x faster than cross-encoders with comparable accuracy, strong zero-shot generalization, and multimodal extensions (ColPali, ColQwen)."
---

## Overview

ColBERT (Contextualized Late Interaction over BERT) is a neural retrieval model that occupies a unique position in the retrieval accuracy/efficiency tradeoff. It independently encodes queries and documents into per-token embeddings (like a bi-encoder for efficiency), but then computes fine-grained token-level similarity at query time (like a cross-encoder for accuracy). This [[concepts/late-interaction-retrieval]] approach achieves effectiveness competitive with full cross-encoders while executing **two orders of magnitude faster** and requiring **four orders of magnitude fewer FLOPs per query**.

First introduced in SIGIR 2020, ColBERT has since evolved through ColBERTv2 (improved compression), and spawned multimodal variants ColPali and ColQwen for visual document retrieval.

## Technical Architecture

### Encoding
ColBERT builds on BERT's 110M-parameter foundation but modifies the output:
- Each token in a query or document gets its own embedding vector
- Dimensionality is reduced from BERT's native 768 to **128 dimensions** per token
- Queries and documents are encoded independently and can be pre-computed

### MaxSim Scoring
The core innovation is the **MaxSim** (Maximum Similarity) operator:
1. For each query token, compute cosine similarity against **all** document tokens
2. Keep only the **maximum** similarity score for each query token
3. **Sum** all maximum scores to produce the final document relevance score

This allows each query term to find its best match anywhere in the document, capturing semantic alignment at the token level without the quadratic cost of full cross-attention.

### Storage and Compression
The per-token representation creates a storage tradeoff:
- ColBERTv1: 256 bytes per token vector (768-dim float32)
- ColBERTv2: ~20 bytes per token via **residual compression** (centroid + residual quantization)
- Still roughly **6-10x more storage** than single-vector approaches like sentence-transformers

## Performance Characteristics

| Dimension | Bi-Encoder | ColBERT | Cross-Encoder |
|---|---|---|---|
| Speed | Fastest | ~100x faster than cross | Slowest |
| Accuracy | Lower | Near cross-encoder | Highest |
| Storage | Lowest (1 vector/doc) | 6-10x more | N/A (no index) |
| Zero-shot | Variable | Strong | Strong |
| FLOPs/query | Low | ~10,000x fewer than cross | Highest |

ColBERTv2 has been repeatedly shown to be **extremely strong at zero-shot retrieval in new domains**, making it valuable for RAG systems that need to handle diverse, unfamiliar content without domain-specific fine-tuning.

## Multimodal Extensions

**ColPali** (~3B parameters, PaliGemma vision model): Treats PDF pages as images, processes them into uniform patches, and generates per-patch embeddings. This eliminates the need for complex OCR pipelines and naturally handles mixed content (text, tables, charts, diagrams).

**ColQwen** (~2B parameters, Qwen2-VL, Apache 2.0 license): Same late interaction approach with a different vision backbone. The Apache 2.0 license makes it more commercially accessible.

Both maintain the 128-dimensional embedding standard, processing document patches rather than text tokens.

## RAGatouille

The [RAGatouille](https://github.com/AnswerDotAI/RAGatouille) library provides a simple interface for integrating ColBERT into any RAG pipeline. It handles index creation, querying, and model management, making state-of-the-art late interaction retrieval accessible without deep infrastructure expertise.

## Sources

- [[sources/colbert-late-interaction]] — Weaviate overview of late interaction models

## Related Concepts

- [[concepts/late-interaction-retrieval]] — the paradigm ColBERT instantiates
- [[concepts/hybrid-search]] — ColBERT can complement sparse retrieval
- [[concepts/reranking]] — ColBERT can also serve as a reranker
- [[concepts/multimodal-rag]] — ColPali/ColQwen enable visual document retrieval
