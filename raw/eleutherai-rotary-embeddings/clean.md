---
title: "Rotary Embeddings: A Relative Revolution"
source: "https://blog.eleuther.ai/rotary-embeddings/"
author: "EleutherAI"
date_published: 2021-04-20
date_ingested: 2026-04-05
tags: [RoPE, positional-encoding, rotary-embeddings, transformer, position-encoding]
type: article
status: raw
discovered_via: search
---

# Rotary Embeddings: A Relative Revolution

## Core Concept

RoPE (Rotary Position Embedding) unifies absolute and relative positional encoding approaches. The method treats token embeddings as complex numbers and applies pure rotations based on position, enabling relative positional information to be preserved through attention operations.

## Mathematical Formulation

Basic formula: f(x, l) = x * e^(i*l*theta)

Key property: For query and key vectors at positions m and n, the inner product <f(q, m), f(k, n)> = g(q, k, m-n). This ensures the inner product depends only on relative position (m-n), not absolute positions.

Matrix implementation uses block-diagonal rotation matrices:
M_j = [[cos(m*theta_j), -sin(m*theta_j)], [sin(m*theta_j), cos(m*theta_j)]]

## Position Encoding Mechanism

The approach leverages the geometric property that the dot product between two vectors is a function of the magnitude of individual vectors and the angle between them. By rotating embeddings, the relative angle between query and key vectors remains invariant under simultaneous position shifts.

Consecutive pairs of embedding dimensions are treated as single complex numbers: q = (q1+iq2, q3+iq4, ...)

## Comparison with Alternatives

### vs. Sinusoidal Embeddings (Original Transformer)
- RoPE mixes pairs of coordinates; sinusoidal operates element-wise
- RoPE uses multiplicative factor; sinusoidal is additive

### vs. T5 Relative Position Embeddings
- T5 RPE requires constructing the full N x N attention matrix, incompatible with efficient attention variants like FAVOR+
- RoPE works with both standard and efficient mechanisms

### vs. Learned Absolute Embeddings
- RoPE demonstrated empirical advantages on OpenWebText2 validation

## Experimental Results

**125M Parameter Models (OpenWebText2):**
- Learned Absolute: 2.809 loss
- T5 RPE: 2.801 loss
- RoPE: 2.759 loss (fastest convergence)

**1.4B Parameter Models (Pile Dataset):**
- Learned Absolute: 2.240 loss
- T5 RPE: 2.223 loss
- RoPE: 2.173 loss (30% faster convergence than learned absolute)

## PyTorch Implementation (GPT-NeoX)

```python
def rotate_half(x):
    x1, x2 = x[..., : x.shape[-1] // 2], x[..., x.shape[-1] // 2 :]
    return torch.cat((-x2, x1), dim=x1.ndim - 1)

@torch.jit.script
def apply_rotary_pos_emb(q, k, cos, sin):
    return (q * cos) + (rotate_half(q) * sin),
           (k * cos) + (rotate_half(k) * sin)
```

Runtime overhead: 4-5x cost of additive positional embeddings naively; reduced to 2-2.5x with fusion. Overall transformer overhead: 1-3% across model sizes.

## Key Advantages

- Parameter-free (no learnable positional weights)
- Inherently relative while encoding absolute position
- Scales gracefully from sub-word n-grams to book-length contexts
- Compatible with efficient attention mechanisms
- Now the standard for modern LLMs (Llama, Mistral, etc.)
