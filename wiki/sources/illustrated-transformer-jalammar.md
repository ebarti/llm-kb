---
title: "Source: The Illustrated Transformer"
type: source-summary
source: "[[raw/illustrated-transformer-jalammar]]"
related: ["[[concepts/transformer-architecture]]", "[[concepts/self-attention]]", "[[concepts/multi-head-attention]]", "[[concepts/positional-encoding]]", "[[entities/attention-is-all-you-need]]"]
last_compiled: 2026-04-05
summary: "Jay Alammar's visual walkthrough of the original Transformer: encoder-decoder stacks, Q/K/V self-attention, multi-head attention, positional encoding, residual connections, and beam search decoding."
---

## Key Points

- The Transformer architecture consists of stacked encoders (6) and decoders (6), each with self-attention and feed-forward sub-layers
- [[concepts/self-attention]] works by computing Query, Key, Value vectors from input embeddings, then using scaled dot-product attention: Attention(Q,K,V) = softmax(QK^T / sqrt(d_k)) V
- [[concepts/multi-head-attention]] runs 8 parallel attention heads with separate Q/K/V matrices, concatenating and projecting results
- [[concepts/positional-encoding]] uses sinusoidal functions to inject sequence order information
- Residual connections and layer normalization stabilize training of deep networks
- Decoder uses masked self-attention (future positions set to -inf) plus encoder-decoder cross-attention

## Detailed Summary

Alammar's tutorial is the canonical visual introduction to the [[concepts/transformer-architecture]]. He walks through the full encoder-decoder pipeline: input embeddings receive [[concepts/positional-encoding]] vectors, then pass through 6 stacked encoder layers. Each encoder has two sub-layers: a [[concepts/self-attention]] layer where each word attends to all other words in the sequence, and a position-wise feed-forward network applied identically to each position.

The self-attention mechanism creates three vectors per input — Query (what am I looking for?), Key (what do I contain?), and Value (what do I give?) — by multiplying input embeddings by learned weight matrices. Attention scores come from dot products of queries against keys, scaled by sqrt(d_k)=8 for numerical stability, softmaxed, then used to weight value vectors. This produces a context-aware representation for each position.

[[concepts/multi-head-attention]] extends this by maintaining 8 separate sets of Q/K/V weight matrices, allowing the model to attend to different representation subspaces simultaneously. The 8 output matrices are concatenated and projected through W_O.

The decoder adds a third sub-layer: encoder-decoder attention using queries from the decoder and keys/values from the encoder output. Its self-attention is masked to prevent attending to future positions.

## Notable Quotes

> "The encoding component is a stack of encoders... the feed-forward layer does not have those dependencies"

> "With multi-headed attention, we maintain separate Q/K/V weight matrices for each head resulting in different Q/K/V matrices"

## Related Concepts

- [[concepts/transformer-architecture]] — the complete architecture this article explains
- [[concepts/self-attention]] — the core mechanism described in detail
- [[concepts/multi-head-attention]] — the parallel attention heads mechanism
- [[concepts/positional-encoding]] — sinusoidal position injection
- [[entities/attention-is-all-you-need]] — the paper this article illustrates
