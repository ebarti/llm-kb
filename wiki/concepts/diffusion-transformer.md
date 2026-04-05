---
title: "Diffusion Transformer (DiT)"
type: concept
sources: ["[[sources/dit-diffusion-transformer-architecture]]", "[[sources/flux-architecture-demystified]]", "[[sources/bentoml-open-source-image-generation-2026]]"]
related: ["[[concepts/diffusion-models]]", "[[concepts/flow-matching]]", "[[concepts/image-generation]]", "[[concepts/vision-transformer]]", "[[concepts/adaptive-layer-normalization]]", "[[entities/flux]]", "[[entities/stable-diffusion]]", "[[entities/sora]]"]
tags: [dit, transformer, diffusion, architecture, scalability]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Architecture replacing U-Net with transformer backbone for diffusion models -- using patchification, self-attention, and adaLN conditioning to achieve predictable scaling: DiT-XL/2 achieves FID 2.27 on ImageNet 256x256, and the design underpins FLUX, SD3, and Sora."
---

## Overview

The Diffusion Transformer (DiT) replaces the convolutional U-Net that was the standard backbone for [[concepts/diffusion-models]] with a Vision Transformer (ViT) architecture. Introduced by Peebles & Xie (ICCV 2023), DiT demonstrated that the U-Net's spatial inductive bias is not necessary for high-quality image generation, and that transformer-based diffusion models exhibit the same predictable scaling properties that made transformers dominant in language modeling.

DiT is now the foundation for the most capable generation systems: [[entities/flux]] FLUX.1, [[entities/stable-diffusion]] 3, [[entities/sora]], and PixArt-alpha.

## Key Ideas

### Architecture Pipeline

1. **VAE Encoding**: A pretrained variational autoencoder compresses images from pixel space (e.g., 256x256x3) into latent space (e.g., 32x32x4), reducing computational cost by 64x or more
2. **Patchification**: The latent representation is divided into non-overlapping patches (typically 2x2), each flattened into a vector. This creates a token sequence identical in structure to ViT
3. **Transformer Blocks**: Standard blocks with multi-head self-attention and feedforward networks process the token sequence, capturing global relationships across the entire image
4. **Conditioning**: Timestep t and optional class/text embeddings are injected via one of several mechanisms (see below)
5. **VAE Decoding**: The transformer output is reshaped and decoded back to pixel space

### Conditioning Mechanisms

DiT explored four conditioning approaches:

| Method | Mechanism | Performance |
|--------|-----------|-------------|
| In-context tokens | Append condition tokens to sequence | Baseline |
| Cross-attention | Condition tokens attended separately | Good |
| adaLN (Adaptive LayerNorm) | Condition generates scale/shift for LN | Best |
| adaLN-Zero | adaLN initialized to identity function | Best (used in practice) |

The adaLN-Zero approach -- where timestep and class label are processed through MLPs to generate per-layer scale (gamma) and shift (beta) parameters for layer normalization -- proved most effective. It provides "dynamic influence to the entire network's computations at every layer."

### Scalability

The defining property of DiT is predictable scaling. Four configurations (S/B/L/XL) with 33M to 675M parameters demonstrated a clear correlation between computational cost (GFlops) and generation quality (FID):

- **DiT-S/2**: 33M params, 0.4 GFlops
- **DiT-B/2**: 130M params, ~10 GFlops
- **DiT-L/2**: 458M params, ~80 GFlops
- **DiT-XL/2**: 675M params, 119 GFlops, FID 2.27 (ImageNet 256x256)

This scaling law -- analogous to the language model scaling laws that drove GPT-3 and beyond -- made DiT the architecture of choice for large-scale systems.

### Multimodal DiT (MMDiT)

[[entities/stable-diffusion]] 3 and [[entities/flux]] extend DiT into the Multimodal DiT (MMDiT) design, where text and image tokens are processed jointly:

- **Dual-stream blocks**: Separate weight matrices for text and image tokens, with joint self-attention over concatenated sequences. This allows modality-specific specialization while sharing cross-modal information.
- **Single-stream blocks** (FLUX only): After dual-stream processing, tokens are merged and processed with shared weights for deeper fusion.
- **Dual text encoding**: T5 (dense per-token) + CLIP (pooled semantic) encoders provide both fine-grained and high-level text understanding.

### Comparison with U-Net

| Dimension | U-Net | DiT |
|-----------|-------|-----|
| Inductive bias | Spatial/convolutional | None (learned) |
| Context | Local (conv kernels) | Global (self-attention) |
| Scaling | Diminishing returns | Predictable improvement |
| Architecture | Encoder-decoder with skip connections | Flat transformer stack |
| Conditioning | Cross-attention at select layers | adaLN at every layer |
| Compute (comparable quality) | 742 GFlops (ADM-U) | 119 GFlops (DiT-XL/2) |

## How It Connects

DiT represents the convergence of two dominant paradigms: the transformer architecture from language modeling and the diffusion framework from generative modeling. This connection is why models like [[entities/sora]] can treat video as sequences of spatiotemporal patches -- the same architecture scales from images to video to 3D.

The shift to DiT also enabled [[concepts/flow-matching]] training objectives, as transformer architectures handle the velocity prediction formulation naturally.

## Open Questions

- How far can MMDiT architectures scale? HunyuanImage-3.0 at 80B MoE suggests substantial headroom
- Will hybrid AR+diffusion designs (GLM-Image, TransDiff) prove more capable than pure diffusion?
- Can DiT efficiency be improved for on-device deployment?

## Sources

- [[sources/dit-diffusion-transformer-architecture]] -- core architecture walkthrough
- [[sources/flux-architecture-demystified]] -- FLUX.1 MMDiT design
- [[sources/bentoml-open-source-image-generation-2026]] -- DiT models in production
