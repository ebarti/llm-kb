---
title: "GPT (Generative Pre-trained Transformer)"
type: entity
entity_type: paper
sources: ["[[sources/unite-ai-bert-gpt-t5-comparison]]", "[[sources/chinchilla-scaling-laws]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/causal-attention]]", "[[concepts/scaling-laws]]", "[[entities/bert]]", "[[entities/t5]]"]
last_compiled: 2026-04-05
summary: "OpenAI's decoder-only transformer family using causal language modeling — from GPT-1 (117M, 2018) to GPT-3 (175B, 2020) to GPT-4, establishing the decoder-only paradigm as the dominant LLM architecture."
---

## Overview

GPT (Generative Pre-trained Transformer) is OpenAI's family of decoder-only [[concepts/transformer-architecture]] models. Starting with GPT-1 in 2018, the series established that scaling decoder-only transformers with [[concepts/causal-attention]] and causal language modeling (CLM) pre-training produces increasingly capable general-purpose language models.

## Architecture

- **Decoder-only**: No encoder; pure autoregressive generation
- **[[concepts/causal-attention]]**: Each token attends only to previous tokens (unidirectional)
- **Pre-training**: Causal Language Modeling — predict the next token given all previous tokens
- **Tokenization**: Byte Pair Encoding (BPE)

## Evolution

| Model | Year | Parameters | Training Data | Key Innovation |
|-------|------|-----------|---------------|---------------|
| GPT-1 | 2018 | 117M | BookCorpus | Pre-training + fine-tuning |
| GPT-2 | 2019 | 1.5B | WebText | Zero-shot task performance |
| GPT-3 | 2020 | 175B | Common Crawl | In-context learning, few-shot |
| GPT-4 | 2023 | Undisclosed (rumored MoE) | Diverse | Multimodal, reasoning |

## Impact

GPT-3 demonstrated that [[concepts/scaling-laws]] applied dramatically: a 100x parameter increase from GPT-2 to GPT-3 unlocked qualitatively new capabilities like in-context learning. The decoder-only architecture with CLM pre-training has become the dominant paradigm, adopted by Llama, Mistral, Claude, Gemini, and virtually all frontier LLMs.

[[entities/chinchilla]] later showed GPT-3 was significantly undertrained: at 175B parameters, Chinchilla-optimal training would require ~3.5T tokens versus GPT-3's ~300B.

## Mentioned In

- [[sources/unite-ai-bert-gpt-t5-comparison]] — comparison with encoder-only and encoder-decoder variants
- [[sources/chinchilla-scaling-laws]] — GPT-3 as an example of undertrained models
