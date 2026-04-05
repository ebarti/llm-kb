---
title: "BERT (Bidirectional Encoder Representations from Transformers)"
type: entity
entity_type: paper
sources: ["[[sources/unite-ai-bert-gpt-t5-comparison]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/self-attention]]", "[[entities/gpt]]", "[[entities/t5]]"]
last_compiled: 2026-04-05
summary: "Google's 2018 encoder-only transformer using bidirectional Masked Language Modeling — revolutionized NLP understanding tasks but cannot generate text. 110M (base) to 340M (large) parameters."
---

## Overview

BERT (Bidirectional Encoder Representations from Transformers), introduced by Devlin et al. at Google in 2018, is an encoder-only [[concepts/transformer-architecture]] variant. Its key innovation is **bidirectional pre-training**: each token attends to all surrounding tokens (both left and right), unlike autoregressive models that process left-to-right.

## Architecture

- **Encoder-only**: No decoder component
- **Bidirectional attention**: All positions attend to all other positions
- **Parameters**: BERT-base (110M, 12 layers, 768 dim, 12 heads), BERT-large (340M, 24 layers, 1024 dim, 16 heads)
- **Tokenization**: WordPiece (~30,000 tokens)
- **Position encoding**: Learned absolute

## Pre-training Objectives

1. **Masked Language Modeling (MLM)**: Randomly mask 15% of tokens; model predicts the originals
2. **Next Sentence Prediction (NSP)**: Binary classification of whether sentence B follows sentence A

## Strengths and Limitations

**Strengths**: Rich bidirectional context makes BERT excellent for understanding tasks — classification, named entity recognition, question answering, semantic similarity.

**Limitations**: Cannot generate free-form text. The bidirectional attention that makes it powerful for understanding prevents autoregressive generation.

## Legacy

While BERT-style encoder-only models have been largely superseded by decoder-only models ([[entities/gpt]]) for general purposes, they remain the standard for embedding models (sentence-transformers, E5, BGE) and classification tasks.

## Mentioned In

- [[sources/unite-ai-bert-gpt-t5-comparison]] — architecture comparison with GPT and T5
