---
title: "Source: Demystifying Flux Architecture"
type: source-summary
source: "[[raw/flux-architecture-demystified]]"
related: ["[[entities/flux]]", "[[concepts/diffusion-transformer]]", "[[concepts/flow-matching]]", "[[concepts/multimodal-attention]]"]
tags: [flux, architecture, mmdit, transformer, flow-matching]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "arXiv paper reverse-engineering FLUX.1 architecture: 19 dual-stream MMDiT blocks (separate text/image weights with joint attention) followed by single-stream blocks (shared weights), dual T5+CLIP text encoding, RoPE positional embeddings, and rectified flow velocity prediction training."
---

## Key Points

- [[entities/flux]] uses a fully transformer-based architecture in latent space with two block types
- 19 dual-stream blocks maintain separate weights for text and image tokens but perform joint attention over concatenated sequences
- Single-stream blocks follow, using shared weights and parallel attention+feedforward computation
- Dual text encoders: T5 (dense per-token embeddings) and CLIP (pooled semantic embeddings) for superior prompt adherence
- Rotary Positional Embeddings (RoPE) applied to Q/K vectors, supporting extrapolation beyond training lengths
- [[concepts/flow-matching]] training: predicts velocity vectors (not noise), minimizing difference between predicted velocity and the vector from noise to data along straight interpolation paths
- Extends [[entities/stable-diffusion]] 3's MMDiT design by adding single-stream blocks for enhanced capacity

## Detailed Summary

Greenberg's arXiv paper provides a detailed reverse-engineering of the [[entities/flux]] FLUX.1 architecture. The key insight is the two-phase block design. The first 19 dual-stream (double) blocks process text and image tokens with separate weight matrices, allowing each modality to specialize while still sharing information through joint self-attention over the concatenated token sequences. This is the Multimodal DiT (MMDiT) design pioneered by [[entities/stable-diffusion]] 3.

The subsequent single-stream blocks merge both modalities into a shared representation, processing them with identical weights. This shift from specialization to integration mirrors how the model progressively fuses textual and visual information.

Adaptive Layer Normalization (adaLN) in each stream dynamically generates scaling and shifting parameters from conditioning vectors, providing fine-grained control over the generation process. The use of RoPE rather than absolute positional embeddings enables the model to handle varying resolutions.

The [[concepts/flow-matching]] training paradigm predicts velocity vectors rather than noise, enabling faster and more stable synthesis compared to traditional [[concepts/diffusion-models]] epsilon-prediction.

## Concepts Introduced or Discussed

- [[concepts/diffusion-transformer]] -- the DiT/MMDiT backbone
- [[concepts/flow-matching]] -- rectified flow velocity prediction
- [[concepts/multimodal-attention]] -- joint text-image self-attention
- [[concepts/adaptive-layer-normalization]] -- adaLN conditioning

## Metadata

- **Author**: Or Greenberg
- **Date Published**: 2025-07-12
- **Format**: paper (arXiv)
- **URL**: https://arxiv.org/html/2507.09595v1
