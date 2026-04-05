---
title: "Cosmos World Foundation Model Platform for Physical AI"
source: "https://arxiv.org/abs/2501.03575"
author: "NVIDIA"
date_published: 2025-01-06
date_ingested: 2026-04-05
tags: [NVIDIA, Cosmos, world-foundation-model, physical-AI, tokenizer, diffusion]
type: paper
status: raw
discovered_via: search
---

# NVIDIA Cosmos: World Foundation Model Platform

## Tokenizer Architecture
- Encoder-decoder with temporal causality
- 2-level wavelet transform for initial downsampling
- Spatio-temporal factorized 3D convolution (2D spatial + temporal)
- Compression: spatial (8x, 16x), temporal (4x, 8x)
- Continuous tokens (16-dim embeddings) and discrete tokens (64,000 vocab via Finite-Scalar-Quantization)
- +4 dB PSNR improvement on DAVIS videos; 12x faster than competitors

## Diffusion-Based WFM
- 7B and 14B parameters (Text2World and Video2World variants)
- 3D patchification with FPS-aware 3D RoPE positional embeddings
- Cross-attention for text conditioning; AdaLN-LoRA (36% parameter reduction)
- Progressive training: 512p/57 frames → 720p/121 frames
- Joint image-video training with domain-specific normalization

## Autoregressive-Based WFM
- 4B, 5B, 12B, 13B variants (Llama3-style GPT, no language understanding)
- T5-embedded text conditioning
- Paired with diffusion decoder for quality enhancement
- Inference optimizations toward real-time generation

## Training Data
- 20M hours raw video → ~100M clips extracted
- Nine categories: driving (11%), manipulation (16%), human motion (10%), navigation (16%), POV (8%), nature dynamics (20%), camera movement (8%), synthetic (4%), other (7%)
- Curated with NVIDIA NeMo Curator: 20M hours in 14 days on Blackwell (vs 3 years CPU)

## Benchmarks
- TokenBench: 500 videos across robotic, driving, egocentric domains
- PSNR, SSIM, rFVD metrics

## Applications
- Camera control: navigable virtual worlds with pose conditioning
- Robotic manipulation: video-action sequence prediction
- Autonomous driving: multi-camera prediction
- Industrial: 1X, Agility, Figure AI, Waabi, XPENG, Uber adoption

## Availability
- Open Model License; 2M+ downloads by Jan 2026
