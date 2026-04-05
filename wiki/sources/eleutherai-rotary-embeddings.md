---
title: "Source: Rotary Embeddings: A Relative Revolution"
type: source-summary
source: "[[raw/eleutherai-rotary-embeddings]]"
related: ["[[concepts/positional-encoding]]", "[[concepts/rotary-position-embeddings]]", "[[concepts/self-attention]]"]
last_compiled: 2026-04-05
summary: "EleutherAI's technical deep-dive into RoPE: position as rotation in complex-number embedding space, mathematical proof of relative position preservation, comparison with sinusoidal/learned/T5 alternatives, and GPT-NeoX implementation."
---

## Key Points

- RoPE encodes position by rotating embedding pairs as complex numbers: f(x, l) = x * e^(i*l*theta)
- Inner product depends only on relative position (m-n), not absolute — unifying absolute and relative approaches
- Outperforms learned absolute (2.809 vs 2.759 loss at 125M) and T5 RPE (2.801 vs 2.759)
- At 1.4B scale: 30% faster convergence than learned absolute embeddings
- Parameter-free: no learnable positional weights needed
- Compatible with efficient attention variants (unlike T5 RPE which requires full N x N matrix)
- Runtime overhead: 1-3% overall transformer overhead with fused implementation
- Now the standard for all major LLMs (Llama, Mistral, etc.)

## Detailed Summary

This EleutherAI blog post provides the canonical explanation of [[concepts/rotary-position-embeddings]] (RoPE). The core insight: consecutive pairs of embedding dimensions are treated as complex numbers, and position is encoded by rotating these complex numbers by position-dependent angles. The dot product between rotated query and key vectors then naturally depends only on the relative position difference (m-n), achieving relative positional encoding through an absolute encoding mechanism.

The mathematical elegance is that rotation preserves vector magnitudes while the angle difference between rotated Q and K vectors encodes relative distance. This works because the 2D rotation matrix M_j applied at position m creates a phase difference with position n that depends only on (m-n).

Compared to alternatives: sinusoidal embeddings from the original Transformer are additive and element-wise, while RoPE is multiplicative and mixes coordinate pairs. T5's relative position embeddings require the full N x N attention matrix, making them incompatible with efficient attention methods like FAVOR+. RoPE works with all attention variants.

## Related Concepts

- [[concepts/rotary-position-embeddings]] — the technique this article defines
- [[concepts/positional-encoding]] — the broader category
- [[concepts/self-attention]] — where position encoding is applied
- [[concepts/transformer-architecture]] — the architecture using these encodings
