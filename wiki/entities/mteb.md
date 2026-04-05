---
title: "MTEB (Massive Text Embedding Benchmark)"
type: entity
entity_type: dataset
sources: ["[[sources/modal-mteb-leaderboard]]", "[[sources/pinecone-embedding-models-rundown]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/matryoshka-representation-learning]]"]
last_compiled: 2026-04-05
summary: "The standard benchmark for evaluating text embedding models: 8 task categories across 56+ English datasets (MMTEB: 131 tasks, 250+ languages), hosted on Hugging Face with a continuously updated leaderboard."
---

## Overview

The Massive Text Embedding Benchmark (MTEB) is the primary evaluation framework for [[concepts/text-embeddings]] models. Created by the embeddings-benchmark project and hosted on Hugging Face, it provides standardized evaluation across diverse tasks and a public leaderboard for model comparison.

## Task Categories

MTEB evaluates models across **8 task categories**:

1. **Classification**: Text classification accuracy
2. **Clustering**: Grouping similar texts
3. **Pair Classification**: Determining if text pairs are related
4. **Reranking**: Re-ordering search results by relevance
5. **Retrieval**: Finding relevant documents for queries
6. **Semantic Textual Similarity (STS)**: Measuring meaning similarity between sentences
7. **Summarization**: Evaluating summary quality
8. **Bitext Mining**: Finding parallel sentences across languages

## Scale

- **English MTEB**: 56 datasets across 8 categories
- **Multilingual MTEB (MMTEB)**: 131 tasks across 250+ languages

## Current Top Models (March 2026)

### English Leaderboard

| Model | Score | Notes |
|-------|-------|-------|
| Gemini Embedding 001 | 68.32 | Proprietary (Google) |
| NV-Embed-v2 | 72.31 | Open-weight (NVIDIA) |
| Qwen3-Embedding-8B | — | Apache-2.0 (Alibaba) |

### Multilingual Leaderboard

| Model | Score | Notes |
|-------|-------|-------|
| Qwen3-Embedding-8B | 70.58 | Top multilingual, Apache-2.0 |
| llama-embed-nemotron-8b | — | Non-commercial (NVIDIA) |

## Interpretation Guidance

- **Overall score is a headline number but not the whole story**: Task-specific performance often matters more
- **For RAG**: Retrieval and STS scores are most predictive of production performance
- **Self-reported results**: Scores are submitted by model authors; some may be optimized for the benchmark
- **Domain-specific models**: PubMedBERT (medicine), Voyage Finance, CodeBERT consistently outperform general models in their domains
- **Size matters less than training**: EmbeddingGemma-300M (300M params) competes with much larger models

## Key Trends (2025-2026)

1. Open-source models have caught up with and surpassed commercial APIs on benchmarks
2. Dimension flexibility ([[concepts/matryoshka-representation-learning]]) is increasingly standard
3. Multimodal embeddings are emerging (Gemini Embedding 2 Preview: text, image, video, audio, PDF)
4. The gap between largest and smallest models is narrowing

## Mentioned In

- [[sources/modal-mteb-leaderboard]] — comprehensive leaderboard analysis
- [[sources/pinecone-embedding-models-rundown]] — practical MTEB interpretation guidance
