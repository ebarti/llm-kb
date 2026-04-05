---
title: "Attention Sinks"
type: concept
sources: ["[[sources/streamingllm-attention-sinks]]"]
related: ["[[concepts/self-attention]]", "[[concepts/kv-cache]]", "[[concepts/attention-mechanisms]]", "[[concepts/infinite-context]]", "[[entities/streamingllm]]"]
tags: [attention-sinks, streaming, window-attention, softmax]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The phenomenon where initial tokens in a sequence receive disproportionately high attention scores regardless of semantic content — caused by softmax's sum-to-one constraint forcing excess attention weight onto positionally-biased anchors."
---

## Overview

Attention sinks are a surprising emergent property of transformer [[concepts/self-attention]]: the first few tokens in a sequence consistently receive far more attention than their semantic importance warrants. Discovered by Xiao et al. at MIT's HAN Lab (ICLR 2024), this phenomenon explains why naive window attention (caching only recent tokens) fails catastrophically when initial tokens are evicted.

The root cause is the softmax normalization constraint: attention weights must sum to one. When a query has no strong match among available keys, the model must distribute its attention somewhere. Initial tokens — visible to all subsequent positions in autoregressive generation — become natural "sinks" for this excess attention. They are trained into this role during pretraining.

## The Evidence

The evidence for attention sinks is dramatic:

- **Catastrophic failure**: Removing initial tokens from Llama-2-13B's KV cache causes perplexity to spike from 5.40 to 5,158 — a 955x degradation
- **Content independence**: Replacing the first four tokens with arbitrary linebreak characters achieves comparable perplexity restoration, proving the effect is positional, not semantic
- **Universality**: The phenomenon appears across all tested architectures: Llama-2, MPT, Falcon, Pythia, and even in BERT and Vision Transformers

## Why This Happens

In standard [[concepts/self-attention]] with softmax normalization:

1. Softmax forces attention weights to sum to 1.0 across all keys
2. When a query genuinely does not need information from most positions, the model still must allocate probability mass somewhere
3. Initial tokens are visible to every subsequent token (no causal mask blocks them)
4. Through training, initial positions learn to serve as attention "dumping grounds"
5. The actual content at these positions becomes irrelevant — it is their position that matters

This is analogous to a "default" case in a switch statement: attention has nowhere else to go, so it goes to the sink.

## Practical Impact: StreamingLLM

The discovery of attention sinks directly enables [[entities/streamingllm]], a framework for infinite-length generation:

1. Maintain a two-part KV cache: **4 initial sink tokens** + **rolling recent window**
2. Discard all intermediate tokens to maintain constant memory
3. Recalculate positional embeddings relative to cache contents (not absolute position)

This achieves stable generation over 4M+ tokens with up to 22.2x speedup in decoding latency, with no fine-tuning required.

## Training Optimization

Models can be pre-trained with a dedicated learnable **sink token** appended at position 0. This concentrates all attention sink behavior into a single token, reducing the overhead from four to one. Sink-token-trained models maintain 18.01 perplexity with just the dedicated sink, while vanilla models need four initial tokens for 18.05 perplexity.

## Implications for Understanding Attention

Attention sinks reveal that not all attention scores are semantically meaningful. Some attention is structural — a byproduct of the softmax normalization rather than genuine information retrieval. This has implications for:
- **Attention interpretability**: High attention weight does not always mean semantic relevance
- **Context window design**: The first few positions have special structural significance
- **KV cache optimization**: Intelligent eviction policies must preserve sink tokens
- **Architecture design**: Future attention mechanisms might benefit from explicit "no-op" targets

## Open Questions

- Can attention sinks be eliminated entirely with alternative normalization (e.g., sigmoid attention)?
- Do attention sinks carry any useful information, or are they purely structural?
- How do attention sinks interact with [[concepts/flash-attention]] and [[concepts/sparse-attention]]?
- What is the relationship between attention sinks and the [[concepts/lost-in-the-middle]] phenomenon?

## Sources

- [[sources/streamingllm-attention-sinks]] — the original discovery paper (ICLR 2024)

## Related Concepts

- [[concepts/self-attention]] — the mechanism exhibiting sink behavior
- [[concepts/kv-cache]] — the inference structure affected by sinks
- [[concepts/infinite-context]] — the goal StreamingLLM enables
- [[concepts/lost-in-the-middle]] — potentially related attention degradation pattern
- [[concepts/attention-mechanisms]] — the umbrella family
