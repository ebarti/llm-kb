---
title: "Balancing Vocabulary Size in Modern LLMs (GPT-4, LLaMA, Mistral)"
source: "https://www.rohan-paul.com/p/tutorial-balancing-vocabulary-size"
author: "Rohan Paul"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [tokenization, vocabulary-size, tradeoffs, llm-training]
type: article
status: raw
discovered_via: search
---

# Balancing Vocabulary Size in Modern LLMs

## Core Trade-off

The fundamental tension involves sequence length versus computational efficiency. Smaller vocabularies break text into more (but smaller) tokens, whereas larger vocabularies break text into fewer (but larger) tokens.

**Fixed Token Budget:** With a predetermined token allocation (e.g., 1 trillion tokens), larger vocabularies enable more passes over training data since fewer tokens represent the same text.

**Fixed Epoch Budget:** With a set number of training passes, smaller vocabularies generate more total tokens, increasing compute requirements but potentially improving performance through greater token exposure.

## Modern LLM Vocabulary Choices

- **GPT-4:** ~100,000 tokens (improved from GPT-3's 50,000)
- **LLaMA 3:** ~128,000 tokens (upgraded from earlier 32,000)
- **Mistral:** ~131,000 tokens in recent models (expanded from 32,000)

## Key Trade-offs

### Coverage vs. Computation
- Small vocabularies eliminate out-of-vocabulary issues but create lengthy sequences, exhausting context windows
- Large vocabularies reduce sequence length but increase embedding layer parameters and per-token computation

### Perplexity Gains
Performance improvements show diminishing returns beyond ~100,000 tokens. Expanding from 8k to 32k tokens yields substantial gains; going beyond 100k provides minimal improvements relative to increased costs.

### Training Impact
- A 32k vocabulary requires ~130 million embedding parameters (with 4,096 dimensions)
- 128k requires over 500 million — significant memory overhead

### Inference Trade-offs
Larger vocabularies reduce generation steps for long outputs but increase per-step softmax computation. The net benefit typically favors reduced token count when handling extended contexts.

### Multilingual Efficiency
Models targeting multiple languages benefit from expanded vocabularies. Character fertility (tokens per word) improves significantly with larger vocabularies for non-Latin scripts.

## Emerging Approaches

Research explores vocabulary curriculum learning, which dynamically merges predictable tokens during training — adapting vocabulary alongside model capabilities rather than using fixed tokenization throughout.
