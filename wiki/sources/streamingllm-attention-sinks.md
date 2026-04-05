---
title: "Source: Efficient Streaming Language Models with Attention Sinks"
type: source-summary
source: "[[raw/streamingllm-attention-sinks]]"
related: ["[[concepts/attention-sinks]]", "[[concepts/kv-cache]]", "[[concepts/self-attention]]", "[[concepts/infinite-context]]", "[[entities/streamingllm]]"]
tags: [attention-sinks, streaming, window-attention, KV-cache, infinite-context]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "MIT HAN Lab paper discovering attention sinks — initial tokens receiving disproportionate attention regardless of content — and StreamingLLM framework enabling infinite-length generation by preserving 4 sink tokens plus a rolling KV window, with 22.2x decoding speedup."
---

## Key Points

- Initial tokens act as "attention sinks" collecting excess attention due to softmax's sum-to-one constraint
- Removing initial tokens from window attention causes catastrophic perplexity spike (5.40 to 5,158 for Llama-2-13B)
- Replacing initial tokens with linebreak tokens restores performance — position, not content, matters
- StreamingLLM: preserve 4 initial tokens + rolling recent window = stable infinite-length generation
- Validated across Llama-2, MPT, Falcon, Pythia families up to 4M+ tokens
- Up to 22.2x speedup in decoding latency vs recomputation baselines
- Pre-training with a dedicated sink token concentrates sinks to a single position
- Phenomenon is universal across transformer architectures including BERT and ViTs

## Detailed Summary

This ICLR 2024 paper from MIT's HAN Lab addresses a fundamental challenge in deploying LLMs for streaming applications like multi-round dialogue: the [[concepts/kv-cache]] grows without bound, consuming increasing memory.

The naive solution — window attention caching only recent tokens — fails catastrophically. The paper traces this failure to a previously undocumented phenomenon: **attention sinks**. Due to the softmax normalization in [[concepts/self-attention]], attention scores must sum to one. When queries lack strong matches, the model dumps excess attention weight onto initial tokens, which are visible to all subsequent tokens and thus "more readily trained to serve as attention sinks."

The key experiment proves this is positional, not semantic: substituting the first four tokens with arbitrary linebreak characters recovers full performance. This implies the model learns to use specific positions as attention garbage collectors during training.

[[entities/streamingllm]]'s solution is elegant: maintain a two-part KV cache with (1) the first four tokens as attention sinks and (2) a rolling window of recent tokens. Positional embeddings are recalculated relative to the cache contents rather than absolute text positions.

The paper validates this across all major open-source model families and proposes a training improvement: adding a dedicated learnable sink token during pre-training concentrates all sink behavior into a single token, reducing the overhead from four tokens to one.

## Concepts Introduced or Discussed

- [[concepts/attention-sinks]] — the newly discovered phenomenon
- [[concepts/kv-cache]] — the memory challenge being addressed
- [[concepts/self-attention]] — the mechanism exhibiting sink behavior
- [[concepts/infinite-context]] — the architectural goal

## Metadata

- **Author**: Xiao et al. (MIT HAN Lab)
- **Date Published**: 2023-09-29
- **Format**: paper (ICLR 2024)
- **URL**: https://arxiv.org/abs/2309.17453
