---
title: "Diffusion Models"
type: concept
sources: ["[[sources/bentoml-open-source-image-generation-2026]]", "[[sources/dit-diffusion-transformer-architecture]]", "[[sources/flow-matching-iclr-2025]]", "[[sources/consistency-models-fast-generation]]", "[[sources/flux-vs-stable-diffusion-2026]]"]
related: ["[[concepts/flow-matching]]", "[[concepts/diffusion-transformer]]", "[[concepts/consistency-models]]", "[[concepts/image-generation]]", "[[concepts/video-generation]]", "[[concepts/latent-diffusion]]", "[[concepts/autoregressive-image-generation]]"]
tags: [generative-ai, diffusion, denoising, deep-learning]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The dominant generative framework (2020-2026) that produces data by learning to reverse a gradual noise-addition process, surpassing GANs and VAEs across image, video, audio, and 3D generation -- now evolving toward flow matching and transformer backbones."
---

## Overview

Diffusion models are a family of generative models that produce data by learning to reverse a gradual noise-corruption process. Given a clean data sample, the forward process progressively adds Gaussian noise over T timesteps until the sample becomes indistinguishable from pure noise. The model then learns the reverse process -- predicting and removing noise at each step to recover the original data.

Since their breakthrough in 2020-2021, diffusion models have surpassed GANs and VAEs as the dominant paradigm for generative AI across images, video, audio, 3D content, and molecular design. They power systems ranging from [[entities/stable-diffusion]] and [[entities/flux]] for images, to [[entities/sora]] and [[entities/veo]] for video, to [[entities/suno]] and [[entities/udio]] for music.

## Key Ideas

### The Forward and Reverse Process

The forward process is fixed (non-learned): it adds small amounts of Gaussian noise at each timestep according to a variance schedule. After enough steps, the data distribution converges to an isotropic Gaussian. The reverse process is learned: a neural network (historically a U-Net, now increasingly a [[concepts/diffusion-transformer]]) predicts the noise added at each step, enabling iterative denoising from pure noise to clean data.

### Latent Diffusion

A critical efficiency innovation is [[concepts/latent-diffusion]]: rather than operating in pixel space, a pretrained VAE encoder compresses images into a lower-dimensional latent representation. The diffusion process operates in this compressed space, dramatically reducing computational cost. All modern image generation systems ([[entities/stable-diffusion]], [[entities/flux]]) use latent diffusion.

### Conditioning Mechanisms

Diffusion models accept various conditioning signals:
- **Text conditioning**: Text encoders (CLIP, T5) produce embeddings that guide generation via cross-attention or [[concepts/adaptive-layer-normalization]]
- **Classifier-free guidance**: Trains the model both conditionally and unconditionally, then interpolates at inference to strengthen adherence to the condition
- **Image conditioning**: ControlNet, IP-Adapter, and reference image approaches provide structural or stylistic guidance

### The Backbone Evolution

The model architecture has undergone a major transition:
1. **U-Net era (2020-2023)**: Convolutional encoder-decoder with skip connections and attention layers at bottleneck resolutions. Used in SD 1.x, 2.x, SDXL.
2. **[[concepts/diffusion-transformer]] era (2023-present)**: Transformer backbone with patchification, replacing convolutions with self-attention for global context. Used in SD 3, [[entities/flux]], [[entities/sora]]. Demonstrates superior scaling properties.

### Training Objectives

Three main training objectives:
- **Noise prediction (epsilon)**: Predict the noise added at timestep t. Used in DDPM, Stable Diffusion 1-2.
- **Velocity prediction**: Predict the velocity vector from noise to data. Used in [[concepts/flow-matching]] models like [[entities/flux]].
- **Score prediction**: Predict the score function (gradient of log-probability). Theoretically equivalent to noise prediction.

## The Sampling Speed Problem

Standard diffusion requires 20-1000 denoising steps at inference, making it slow. Major acceleration approaches include:
- **[[concepts/consistency-models]]**: Learn direct noise-to-data mapping in 1-2 steps (FID 2.82 on CIFAR-10 in one step)
- **[[concepts/flow-matching]] / [[concepts/rectified-flow]]**: Straight-line transport paths requiring fewer integration steps
- **Progressive distillation**: Train student models on fewer steps from teacher
- **DDIM / DPM-Solver**: Deterministic samplers enabling larger step sizes
- **SDXL-Lightning / LCM**: Distilled models achieving quality in 1-8 steps
- **SANA-Sprint**: 0.1s latency for 1024x1024 on H100 via continuous-time consistency distillation

## Current State (2026)

The field is in architectural transition. [[concepts/flow-matching]] has largely replaced DDPM training objectives in leading models. The [[concepts/diffusion-transformer]] has replaced U-Net as the standard backbone. Key metrics:

| Model | Architecture | Parameters | Training Objective | FID (ImageNet 256) |
|-------|-------------|-----------|-------------------|-------------------|
| ADM-U (2021) | U-Net | Large | Epsilon | 3.60 |
| DiT-XL/2 (2023) | DiT | 675M | Epsilon | 2.27 |
| FLUX.1 (2024) | MMDiT | 12B | Flow matching | State-of-art |
| SD 3.5 (2024) | MMDiT | 8B | Flow matching | Competitive |
| HunyuanImage-3.0 | MoE DiT | 80B (13B active) | AR + diffusion | State-of-art |

Meanwhile, [[concepts/autoregressive-image-generation]] has re-emerged as a serious competitor, with models like LlamaGen and NextStep-1 matching diffusion quality while offering superior inference-time scaling.

## How It Connects

Diffusion models form the generative backbone for the entire multimodal creation frontier:
- **Images**: [[concepts/image-generation]] via [[entities/stable-diffusion]], [[entities/flux]], Midjourney
- **Video**: [[concepts/video-generation]] via [[entities/sora]], [[entities/veo]], [[entities/kling]], [[entities/runway]]
- **Audio**: [[concepts/audio-generation]] via [[entities/suno]], [[entities/udio]]
- **3D**: [[concepts/3d-generation]] via score distillation, [[concepts/gaussian-splatting]] guided by diffusion priors
- **Code**: Emerging diffusion-based code generation (d-LLMs) that model edits bidirectionally

## Open Questions

- Will [[concepts/flow-matching]] fully replace traditional diffusion training, or will both coexist?
- Can [[concepts/autoregressive-image-generation]] overtake diffusion, especially as unified multimodal models scale?
- How will [[concepts/consistency-models]] and distillation methods evolve to make real-time high-res generation ubiquitous?
- What are the limits of scaling [[concepts/diffusion-transformer]] architectures?

## Sources

- [[sources/bentoml-open-source-image-generation-2026]] -- 2026 model landscape
- [[sources/dit-diffusion-transformer-architecture]] -- DiT architecture details
- [[sources/flow-matching-iclr-2025]] -- flow matching vs diffusion
- [[sources/consistency-models-fast-generation]] -- fast generation alternatives
- [[sources/flux-vs-stable-diffusion-2026]] -- FLUX vs SD comparison
- [[sources/flux-architecture-demystified]] -- FLUX.1 architecture deep-dive
- [[sources/autoregressive-vision-models-survey]] -- AR competition
