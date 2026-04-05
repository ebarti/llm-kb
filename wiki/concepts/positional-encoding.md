---
title: "Positional Encoding"
type: concept
sources: ["[[sources/illustrated-transformer-jalammar]]", "[[sources/eleutherai-rotary-embeddings]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/rotary-position-embeddings]]", "[[concepts/self-attention]]"]
last_compiled: 2026-04-05
summary: "Methods for injecting sequence order information into transformers, which are inherently position-agnostic — evolved from sinusoidal (2017) to learned absolute to relative (T5) to rotary (RoPE, now standard)."
---

## Overview

The [[concepts/self-attention]] mechanism is inherently permutation-invariant: it produces identical outputs regardless of input ordering. Positional encoding solves this by injecting position information into the input representations, enabling the [[concepts/transformer-architecture]] to distinguish between "the cat sat on the mat" and "the mat sat on the cat."

## Evolution of Position Encoding

### 1. Sinusoidal (Original Transformer, 2017)

The original approach adds fixed sinusoidal signals to input embeddings:
- PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
- PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

Different dimensions oscillate at different frequencies, creating a unique position fingerprint. The design enables theoretical extrapolation to longer sequences.

### 2. Learned Absolute (BERT, GPT-2)

Replace the fixed sinusoidal pattern with a learnable embedding matrix. Simple but doesn't generalize to unseen positions and lacks relative distance information.

### 3. Relative Position Biases (T5, 2019)

Add a learned bias based on relative distance (i-j) to attention scores. Captures that "distance-3" relationships should be treated similarly regardless of absolute position. Limitation: requires constructing the full N x N attention matrix.

### 4. ALiBi (Attention with Linear Biases)

Subtract a linear penalty proportional to distance from attention scores. Simple, no parameters, enables zero-shot length extrapolation.

### 5. [[concepts/rotary-position-embeddings]] (RoPE, 2021)

Rotate embedding pairs as complex numbers. Achieves relative position encoding through an absolute mechanism. Now the standard for virtually all modern LLMs.

## Comparison

| Method | Parameters | Relative | Efficient Attention Compatible | Length Extrapolation |
|--------|-----------|----------|-------------------------------|---------------------|
| Sinusoidal | 0 | No | Yes | Theoretical |
| Learned | O(L * d) | No | Yes | No |
| T5 RPE | O(bins) | Yes | No | Limited |
| ALiBi | 0 | Yes | Yes | Good |
| RoPE | 0 | Yes | Yes | Good (with NTK scaling) |

## Sources

- [[sources/illustrated-transformer-jalammar]] — sinusoidal encoding in original Transformer
- [[sources/eleutherai-rotary-embeddings]] — comprehensive comparison and RoPE details

## Related Concepts

- [[concepts/rotary-position-embeddings]] — the current standard approach
- [[concepts/self-attention]] — the mechanism requiring position information
- [[concepts/transformer-architecture]] — the architecture using positional encoding
