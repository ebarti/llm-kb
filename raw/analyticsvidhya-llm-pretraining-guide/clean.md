---
title: "A Comprehensive Guide to LLM Pretraining"
source: "https://www.analyticsvidhya.com/blog/2025/02/llm-pre-training/"
author: "Analytics Vidhya"
date_published: 2025-02-01
date_ingested: 2026-04-05
tags: [llm-pretraining, tokenization, bpe, neural-network, next-token-prediction, base-model]
type: article
status: raw
discovered_via: search
---

# A Comprehensive Guide to LLM Pretraining

## Overview

LLM pretraining is the foundational phase where models learn to understand and generate text by processing billions of words and predicting the next token in sequences.

## Data Collection and Preprocessing

FineWeb: 15 trillion tokens, 44TB disk space, constructed from CommonCrawl.

Preprocessing Pipeline:
1. URL Filtering: Blocks undesirable domains (adult content, spam)
2. Text Extraction: Removes HTML, JavaScript
3. Language Filtering: fastText classifiers, confidence >= 0.65
4. Quality Filtering: Gopher filters for low-quality/repetitive text
5. Deduplication: MinHash techniques for near-duplicate detection
6. C4 Filtering: Removes boilerplate and excessive repetition
7. PII Removal: Scrubs sensitive information

Result: 36 trillion tokens from original web data after filtering.

## Tokenization

Byte Pair Encoding (BPE): Iteratively merges frequently occurring symbol pairs into new tokens.
- Initial vocabulary: 256 symbols (bytes)
- GPT-4 vocabulary: 100,277 tokens
- Balances shorter sequences with sufficient token granularity

## Neural Network Architecture

- Embedding layers: convert token IDs to numerical representations
- Transformer blocks with attention mechanisms
- Multiple stacked layers progressively refine representations
- Output: probability distribution over vocabulary of possible next tokens

## Training Process

- Loss: cross-entropy loss between predicted and correct probabilities
- Optimization: gradient descent, Adam
- Iterative: repeated exposure to data with continuous parameter updates

## Base Model Characteristics

GPT-2 (2019): 1.6B parameters, 100B tokens, 1,024-token context
Llama 3 (2024): 405B parameters, 15T tokens

Base models function as "statistical pattern recognizers" — they lack explicit understanding of user intent. They serve as intermediate steps before fine-tuning.
