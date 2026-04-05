---
title: "Sentence Transformers"
type: entity
entity_type: tool
sources: ["[[sources/huggingface-matryoshka-embeddings]]"]
related: ["[[concepts/text-embeddings]]", "[[concepts/matryoshka-representation-learning]]", "[[concepts/bi-encoder-vs-cross-encoder]]"]
last_compiled: 2026-04-05
summary: "The leading open-source Python library for text embeddings (Hugging Face): provides pretrained models (all-MiniLM-L6-v2, mpnet), training utilities (MatryoshkaLoss, contrastive losses), and a simple encode() API."
---

## Overview

Sentence Transformers (sbert.net) is the most widely used open-source library for computing [[concepts/text-embeddings]]. Maintained by Hugging Face, it provides pretrained models, training utilities, and a simple API for generating embeddings.

## Key Features

- **Simple API**: `model.encode(["text"])` returns dense vectors
- **Pretrained models**: Hundreds of models on Hugging Face Hub
- **Training framework**: Fine-tune models with various loss functions
- **MatryoshkaLoss**: Train [[concepts/matryoshka-representation-learning]] models with `truncate_dim` support
- **Cross-encoder support**: Train and use reranking models
- **Similarity computation**: Built-in `model.similarity()` method

## Popular Pretrained Models

| Model | Dimensions | Size | Speed | Quality |
|-------|-----------|------|-------|---------|
| all-MiniLM-L6-v2 | 384 | 22MB | 5x faster | Good |
| all-mpnet-base-v2 | 768 | ~400MB | Baseline | Better |
| all-MiniLM-L12-v2 | 384 | 33MB | 3x faster | Good+ |

The all-MiniLM-L6-v2 model is the most popular for resource-constrained deployments: trained on 1B+ pairs, it maps text to 384-dimensional vectors with good quality at 5x the speed of larger models.

## Training Capabilities

Supports multiple loss functions:
- **CoSENTLoss**: For semantic similarity
- **ContrastiveLoss**: For contrastive learning
- **TripletLoss**: For triplet-based training
- **MatryoshkaLoss**: Wrapper that applies any loss at multiple dimensions
- **MultipleNegativesRankingLoss**: For retrieval training with in-batch negatives

## Mentioned In

- [[sources/huggingface-matryoshka-embeddings]] — training and inference with MatryoshkaLoss
