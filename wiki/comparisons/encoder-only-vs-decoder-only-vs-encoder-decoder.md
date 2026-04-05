---
title: "Encoder-Only vs Decoder-Only vs Encoder-Decoder Transformers"
type: comparison
subjects: ["[[entities/bert]]", "[[entities/gpt]]", "[[entities/t5]]"]
sources: ["[[sources/unite-ai-bert-gpt-t5-comparison]]", "[[sources/illustrated-transformer-jalammar]]"]
last_compiled: 2026-04-05
summary: "Three transformer variant families: BERT (encoder-only, bidirectional understanding), GPT (decoder-only, autoregressive generation — now dominant), T5 (encoder-decoder, flexible text-to-text) — with architecture, training, and use case differences."
---

## Overview

The original [[concepts/transformer-architecture]] is an encoder-decoder model. Three major variants emerged by dropping or keeping components, each optimized for different tasks. By 2025, the decoder-only ([[entities/gpt]]-style) architecture dominates for general-purpose LLMs.

## Comparison Table

| Dimension | Encoder-Only (BERT) | Decoder-Only (GPT) | Encoder-Decoder (T5) |
|-----------|-------------------|-------------------|---------------------|
| **Attention** | Bidirectional | Causal (left-to-right) | Bi in encoder, causal in decoder |
| **Pre-training** | Masked LM + NSP | Causal LM (next token) | Span denoising |
| **Tokenization** | WordPiece (30K) | BPE (50K-175K) | SentencePiece |
| **Position encoding** | Learned absolute | Learned / RoPE | Relative position biases |
| **Generation** | Cannot generate | Native | Native |
| **Understanding** | Excellent | Good | Good |
| **Parameters (base)** | 110M | 117M-175B+ | 220M-11B |
| **Training data** | BookCorpus + Wiki | Common Crawl | C4 |
| **Current status** | Embeddings/classification | Dominant for LLMs | Translation/summarization |

## Architecture Details

### Encoder-Only (BERT)

Each layer has [[concepts/self-attention]] + FFN. All positions attend to all others (bidirectional). Pre-trained by masking 15% of tokens and predicting them. Cannot generate text because there is no autoregressive mechanism.

**Best for**: Text classification, named entity recognition, semantic similarity, embeddings

### Decoder-Only (GPT)

Each layer has [[concepts/causal-attention]] + FFN. Each position attends only to previous positions. Pre-trained by predicting the next token. The simplest architecture that scales.

**Best for**: Text generation, dialogue, coding, reasoning — virtually all general-purpose LLM tasks

### Encoder-Decoder (T5)

Encoder uses bidirectional attention; decoder uses causal attention + [[concepts/cross-attention]] to encoder. Pre-trained by replacing spans with sentinels. Treats every task as text-to-text.

**Best for**: Translation, summarization, structured generation, tasks with clear input-output separation

## Why Decoder-Only Won

1. **Simplicity**: Fewer architectural decisions, easier to scale
2. **Scaling**: Causal LM pre-training scales smoothly with parameters and data
3. **Emergent abilities**: In-context learning, chain-of-thought reasoning emerged at scale
4. **Unification**: Generation subsumes understanding (a model that can generate can also classify)
5. **Data efficiency**: Causal LM uses every token as a training signal (no masking waste)

## Remaining Niches

- **Encoder-only**: Embedding models (sentence-transformers, E5), BERT-based classifiers
- **Encoder-decoder**: Machine translation, audio transcription (Whisper), certain seq2seq tasks

## Sources

- [[sources/unite-ai-bert-gpt-t5-comparison]] — detailed three-way architecture comparison
- [[sources/illustrated-transformer-jalammar]] — original encoder-decoder architecture
