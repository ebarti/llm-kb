---
title: "Introduction to Matryoshka Embedding Models"
source: "https://huggingface.co/blog/matryoshka"
author: "Tom Aarsen"
date_published: 2024-03-27
date_ingested: 2026-04-05
tags: [matryoshka, embeddings, dimension-reduction, sentence-transformers, MRL]
type: article
status: raw
discovered_via: search
---

# Introduction to Matryoshka Embedding Models — Hugging Face

## Core Concept

Matryoshka Embedding Models produce useful embeddings at multiple dimensions by storing more important information in earlier dimensions and less important information in later dimensions — like Russian nesting dolls.

## Training Approach

Rather than optimizing embeddings at a single dimensionality, Matryoshka models apply the same loss function on truncated portions of the embeddings at multiple sizes (e.g., 768, 512, 256, 128, 64). The combined loss sums losses across all dimensions, optionally with weights. Training with MatryoshkaLoss incurs no notable overhead in training time.

## Performance Metrics (mpnet-base-nli-matryoshka vs standard model)

Tested on STSBenchmark across dimensions:
- At 768 dimensions: Matryoshka model achieves higher Spearman similarity
- At 64 dimensions (8.3% of original size):
  - Matryoshka model preserves 98.37% of full-size performance
  - Standard model preserves 96.46% of full-size performance

## Practical Usage

Sentence Transformers supports `truncate_dim` parameter. After truncation, re-normalize embeddings. Normalization should happen after truncation, not before.

Inference speed for embedding generation is the same regardless of target dimension. Downstream tasks (retrieval, clustering) are significantly faster with truncated embeddings.

## Use Cases

1. Shortlisting and Reranking: Use truncated embeddings to efficiently shortlist candidates, rerank with full-dimension embeddings
2. Trade-off Optimization: Balance storage cost, processing speed, and performance

## Key Models

- nomic-ai/nomic-embed-text-v1.5: Production-ready Matryoshka model (10.5M downloads)
- tomaarsen/mpnet-base-nli-matryoshka: Trained on AllNLI

## Comparison to PCA

MRL almost always outperforms post-hoc dimensionality reduction like PCA at equivalent compression ratios, as MRL trains the model to produce high-quality representations at small sizes as a primary objective.

## Reference

Original Paper: Kusupati et al. (2022), "Matryoshka Representation Learning" (arxiv:2205.13147)
