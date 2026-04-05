---
title: "Rotary Position Embeddings (RoPE)"
type: concept
sources: ["[[sources/eleutherai-rotary-embeddings]]"]
related: ["[[concepts/positional-encoding]]", "[[concepts/self-attention]]", "[[concepts/transformer-architecture]]"]
last_compiled: 2026-04-05
summary: "Position encoding via complex-number rotation of embedding pairs — parameter-free, inherently relative, compatible with efficient attention, and the standard for all modern LLMs (Llama, Mistral, Qwen, etc.)."
---

## Overview

Rotary Position Embedding (RoPE) is the dominant [[concepts/positional-encoding]] method in modern [[concepts/transformer-architecture]] models. Introduced by Su et al. (2021) in the RoFormer paper, it encodes position by rotating pairs of embedding dimensions as complex numbers. The key property: the dot product between any two rotated vectors depends only on their relative position difference, not their absolute positions.

## Mathematical Foundation

### Core Formula

For input vector x at position l:

f(x, l) = x * e^(i * l * theta)

This rotates each consecutive pair of embedding dimensions by an angle proportional to the position index l.

### Key Property

For query at position m and key at position n:

<f(q, m), f(k, n)> = g(q, k, m - n)

The inner product (and thus the attention score) depends only on the relative distance (m - n). This achieves relative position encoding through absolute rotations.

### Block-Diagonal Rotation Matrix

For each pair j of embedding dimensions at position m:

M_j = [[cos(m * theta_j), -sin(m * theta_j)],
       [sin(m * theta_j),  cos(m * theta_j)]]

Different dimension pairs use different rotation frequencies (controlled by theta_j), creating position fingerprints at multiple scales.

## Implementation

```python
def rotate_half(x):
    x1, x2 = x[..., :x.shape[-1]//2], x[..., x.shape[-1]//2:]
    return torch.cat((-x2, x1), dim=-1)

def apply_rotary_pos_emb(q, k, cos, sin):
    return (q * cos) + (rotate_half(q) * sin), \
           (k * cos) + (rotate_half(k) * sin)
```

Runtime overhead: 1-3% overall with fused implementation. No learnable parameters.

## Advantages Over Alternatives

1. **Parameter-free**: No learnable positional weights (unlike learned absolute)
2. **Inherently relative**: Dot products encode relative distance automatically
3. **Compatible with efficient attention**: Works with FlashAttention, FAVOR+, etc. (unlike T5 RPE)
4. **Scalable**: Extends to sequences much longer than training length
5. **Multi-dimensional**: Generalizes to 2D/3D for vision and multimodal applications

## Context Length Extension

Several techniques extend RoPE beyond training context:

- **NTK-Aware Scaling**: Adjust base frequency to interpolate rather than extrapolate
- **YaRN**: Combines NTK scaling with attention temperature adjustment
- **Multimodal RoPE**: Extended by Qwen2.5-VL for temporal video encoding

## Experimental Results

At 125M parameters on OpenWebText2:
- Learned Absolute: 2.809 loss
- T5 RPE: 2.801 loss
- **RoPE: 2.759 loss** (best, fastest convergence)

At 1.4B on the Pile:
- 30% faster convergence than learned absolute embeddings

## Adoption

RoPE is used by virtually all modern LLMs: Llama 2/3, Mistral, Qwen, DeepSeek, Falcon, GPT-NeoX. It has become the unquestioned default for position encoding.

## Sources

- [[sources/eleutherai-rotary-embeddings]] — definitive technical explanation with experiments

## Related Concepts

- [[concepts/positional-encoding]] — the broader category of position methods
- [[concepts/self-attention]] — where RoPE is applied (to Q and K before dot product)
- [[concepts/kv-cache]] — RoPE rotations are applied before caching
- [[concepts/multimodal-transformers]] — multimodal RoPE extensions
