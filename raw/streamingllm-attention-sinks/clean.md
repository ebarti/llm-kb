---
title: "Efficient Streaming Language Models with Attention Sinks"
source: "https://arxiv.org/html/2309.17453v3"
author: "Xiao et al. (MIT HAN Lab)"
date_published: 2023-09-29
date_ingested: 2026-04-05
tags: [attention-sinks, streaming, window-attention, infinite-context, KV-cache]
type: paper
status: raw
discovered_via: search
---

# Efficient Streaming Language Models with Attention Sinks

## The Attention Sink Phenomenon

Initial tokens in a sequence receive disproportionately high attention scores regardless of semantic relevance. These "attention sinks" collect unnecessary attention values due to softmax's constraint that scores sum to one.

When a query lacks strong matches, the model allocates unneeded attention values to initial tokens because they are visible to all subsequent tokens in autoregressive generation, making them "more readily trained to serve as attention sinks."

## Window Attention Failure

Standard window attention (caching only recent tokens) fails catastrophically when sequences exceed cache size. For Llama-2-13B, window attention achieves 5,158 perplexity compared to normal 5.40 when initial tokens are removed.

Substituting original initial tokens with linebreak tokens achieves comparable perplexity restoration, indicating positional bias rather than content importance.

## The StreamingLLM Algorithm

Preserve a small number of initial tokens' KV cache alongside recent tokens:

1. Attention sinks: Four initial tokens providing stable attention anchors
2. Rolling KV cache: Recent tokens crucial for language modeling

Positional embeddings are recalculated within the cache rather than using original text positions.

## Performance Across Models

Validated across Llama-2 (7B-70B), MPT (7B-30B), Falcon (7B-40B), Pythia (2.9B-12B).

All achieve stable performance modeling 4+ million tokens with up to 22.2x speedup in decoding latency.

## Pre-Training with Dedicated Sink Tokens

Adding a learnable placeholder token during pre-training concentrates attention sinks to a single token. Sink-token-trained models maintain 18.01-18.02 perplexity with just the dedicated sink, vs vanilla models needing four initial tokens for 18.05 perplexity.

## Limitations

Does not extend context window or enhance long-term memory. Excels where recent context dominates (chat, short QA) but cannot replace fine-tuning for long document tasks. The phenomenon appears universal across transformer architectures including BERT and Vision Transformers.
