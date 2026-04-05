---
title: "Causal Attention"
type: concept
sources: ["[[sources/raschka-self-attention-coding]]", "[[sources/illustrated-transformer-jalammar]]"]
related: ["[[concepts/self-attention]]", "[[concepts/transformer-architecture]]", "[[entities/gpt]]"]
last_compiled: 2026-04-05
summary: "Masked self-attention that restricts each position to attend only to previous positions, enabling autoregressive generation in decoder-only models like GPT and Llama."
---

## Overview

Causal attention (also called masked self-attention or autoregressive attention) is the variant of [[concepts/self-attention]] used in decoder-only transformers. It prevents each position from attending to future positions, enforcing the autoregressive property: token t can only depend on tokens 1 through t-1. This is essential for both training (teacher forcing) and inference (sequential generation) in models like [[entities/gpt]], Llama, and Claude.

## Implementation

The most efficient approach applies a triangular mask **before** softmax:

1. Compute attention scores normally: scores = QK^T / sqrt(d_k)
2. Set above-diagonal entries to -infinity
3. Apply softmax: since e^(-inf) = 0, future positions get zero attention weight

```python
mask = torch.triu(torch.ones(N, N), diagonal=1)
scores = scores.masked_fill(mask.bool(), -torch.inf)
weights = torch.softmax(scores, dim=-1)
```

This is more efficient than masking after softmax because it avoids computing attention weights that will be zeroed out and requires no renormalization.

## Role in Modern LLMs

Virtually all frontier LLMs (GPT-4, Claude, Gemini, Llama, Mistral) use decoder-only architectures with causal attention. The encoder-only (BERT) and encoder-decoder (T5) variants have been largely superseded for general-purpose language modeling, though they remain useful for specific tasks like classification and translation.

## Sources

- [[sources/raschka-self-attention-coding]] — two implementation approaches compared
- [[sources/illustrated-transformer-jalammar]] — masking in the decoder context

## Related Concepts

- [[concepts/self-attention]] — the unmasked base mechanism
- [[concepts/cross-attention]] — complementary mechanism in encoder-decoder models
- [[concepts/speculative-decoding]] — optimizing the sequential generation bottleneck causal attention creates
