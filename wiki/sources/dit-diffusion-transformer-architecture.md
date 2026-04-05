---
title: "Source: Diffusion Transformer (DiT) Architecture Guide"
type: source-summary
source: "[[raw/dit-diffusion-transformer-architecture]]"
related: ["[[concepts/diffusion-transformer]]", "[[concepts/diffusion-models]]", "[[entities/sora]]", "[[entities/stable-diffusion]]"]
tags: [dit, transformer, diffusion, architecture]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Technical guide to DiT architecture: replaces U-Net with transformer backbone using patchification, adaLN conditioning, and VAE latent space -- achieving FID 2.27 on ImageNet 256x256, with scalable performance proven through depth/width/token increases."
---

## Key Points

- [[concepts/diffusion-transformer]] replaces the U-Net backbone with a pure Vision Transformer, proving that convolutional spatial inductive bias is not necessary for high-quality generation
- The architecture processes latent representations as patch token sequences, identical to how [[concepts/vision-transformer]] handles image classification
- Conditioning uses adaptive layer normalization (adaLN-Zero): timestep and class labels generate scale/shift parameters via MLPs that modulate every transformer layer
- Scalability is the primary advantage: increasing model depth, width, or input tokens consistently improves generation quality (measured by Gflops vs. FID correlation)
- DiT-XL/2 achieves state-of-the-art FID 2.27 on ImageNet 256x256, beating all prior diffusion models including the much larger ADM-U (742 GFlops vs. 119 GFlops)
- Foundational paper by Peebles & Xie (ICCV 2023) spawned downstream models including [[entities/sora]], [[entities/stable-diffusion]] 3, PixArt-alpha, and Lumina-Video

## Detailed Summary

The Lightly AI guide provides a step-by-step walkthrough of the DiT architecture. The process begins with a pretrained VAE encoder compressing images into latent space, followed by patchification that divides the latent into non-overlapping patches forming a token sequence. Standard Vision Transformer blocks with multi-head self-attention capture global image relationships -- a critical advantage over U-Net's local convolutional receptive fields.

The training objective is straightforward noise prediction at random timesteps, with MSE loss between predicted and actual noise. The frozen VAE encoder/decoder handles the latent-to-pixel conversion.

Four model configurations (S/B/L/XL) range from 33M to 675M parameters. The paper demonstrates a clear scaling law: computational cost (Gflops) directly correlates with improved FID scores, suggesting that DiTs will continue improving with scale -- a property that made them attractive for large-scale systems like [[entities/sora]].

## Concepts Introduced or Discussed

- [[concepts/diffusion-transformer]] -- the core subject
- [[concepts/diffusion-models]] -- the broader framework
- [[concepts/latent-diffusion]] -- operating in compressed latent space
- [[concepts/adaptive-layer-normalization]] -- adaLN conditioning mechanism

## Metadata

- **Author**: Lightly AI
- **Date Published**: 2025-06-01
- **Format**: article
- **URL**: https://www.lightly.ai/blog/diffusion-transformers-dit
