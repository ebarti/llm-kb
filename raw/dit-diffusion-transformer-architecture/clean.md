---
title: "Diffusion Transformer (DiT) Architecture: A Beginner's Guide"
source: "https://www.lightly.ai/blog/diffusion-transformers-dit"
author: "Lightly AI"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [diffusion-models, dit, transformer, architecture, image-generation]
type: article
status: raw
discovered_via: search
---

# Diffusion Transformer (DiT) Architecture

## Core Architecture
DiTs replace the traditional U-Net backbone with a pure Transformer architecture. Unlike U-Nets that rely on convolutional local structure, DiTs leverage self-attention for capturing global context during the image diffusion process. This proves the U-Net's spatial inductive bias is not strictly necessary.

## How DiTs Work Step-by-Step
1. Latent Space Encoding: Input images processed through pre-trained VAE encoder into compressed latent representations.
2. Patchification: Latent image divided into non-overlapping patches, flattened into token sequences.
3. Positional Embeddings: Spatial structure preserved via positional embeddings.
4. DiT Blocks: Stacked Vision Transformer blocks with Layer Norm, Multi-Head Self-Attention, and Feedforward Networks.
5. Conditioning via adaLN: Timestep and class information processed through MLPs generating scale (gamma) and shift (beta) parameters for adaptive layer normalization.
6. VAE Decoding: Final latent outputs upscaled back to full resolution.

## Training Process
Model predicts added noise at random timesteps. Training: sample clean image, encode through frozen VAE, apply noise at random timestep t, predict noise using transformer, compute MSE loss, backpropagate.

## Scalability Properties
Increasing model depth/width or input tokens consistently improves generation quality. DiT-XL/2: 675M parameters, ~119 GFlops. ImageNet 256x256: FID 2.27 (vs. previous best 3.60). ImageNet 512x512: FID 3.04 (vs. previous best 3.85).

## Model Configurations
DiT-S, DiT-B, DiT-L, DiT-XL: 33M to 675M parameters, 0.4 to 119 GFlops. Patch size 2 maximizes tokens and performance.

## Key Paper
Peebles & Xie (2023), "Scalable Diffusion Models with Transformers," ICCV 2023.

## Downstream Applications
- Sora (OpenAI): Video generation
- Stable Diffusion 3 (Stability AI): Text-to-image with flow matching
- PixArt-alpha: Fast training text-to-image
- Lumina-Video: Spatiotemporal multi-scale patches
- TransDiff: Hybrid AR + diffusion, FID 1.42
