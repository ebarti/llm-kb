---
title: "Top Embedding Models on the MTEB Leaderboard"
source: "https://modal.com/blog/mteb-leaderboard-article"
author: "Modal"
date_published: 2025-11-15
date_ingested: 2026-04-05
tags: [MTEB, benchmark, embeddings, leaderboard, evaluation]
type: article
status: raw
discovered_via: search
---

# Top Embedding Models on the MTEB Leaderboard — Modal

## What MTEB Measures

The Massive Text Embedding Benchmark evaluates models across 8 task categories:
1. Classification
2. Clustering
3. Pair classification
4. Reranking
5. Retrieval
6. Semantic textual similarity (STS)
7. Summarization
8. Bitext Mining

English MTEB: 56 datasets. Multilingual MTEB (MMTEB): 131 tasks across 250+ languages.

## Top Open-Weight Models (2025)

1. Qwen3-Embedding-8B — Apache-2.0, strong multilingual, also 4B and 0.6B variants
2. llama-embed-nemotron-8b (NVIDIA) — multilingual, non-commercial license
3. bge-m3 (BAAI) — MIT, supports dense + sparse + multi-vector
4. stella_en_1.5B_v5 — compact English, Matryoshka dimensions
5. embeddinggemma-300m (Google) — 300M params, 100+ languages, Apache-2.0
6. BGE Base Financial Matryoshka — domain-specific finance

## Key Insights

- Overall score is a headline number but not the whole story
- Retrieval and STS correlate most with production RAG/search performance
- Domain-specific models (PubMedBERT, Voyage Finance, CodeBERT) significantly outperform general-purpose in their domains
- Self-reported benchmarks can be gamed

## Market Shifts

Gemini Embedding 001: top English MTEB (68.32). Qwen3-Embedding-8B: top multilingual (70.58). Open-source has caught up with and surpassed commercial APIs on benchmarks. Dimension flexibility and reduced latency define the top tier as of March 2026.

## New Models (2025-2026)

- Gemini Embedding 2 Preview (March 2026): 5 modalities, 100+ languages, native MRL, 3072 dims
- EmbeddingGemma-300M: lightweight, on-device deployment
