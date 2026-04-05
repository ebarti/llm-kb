---
title: "Source: NVIDIA Cosmos — World Foundation Model Platform for Physical AI"
type: source-summary
source: "[[raw/nvidia-cosmos-world-foundation-model]]"
related: ["[[concepts/world-models]]", "[[entities/nvidia-cosmos]]", "[[concepts/physical-ai]]", "[[concepts/diffusion-models]]"]
tags: [NVIDIA, Cosmos, world-foundation-model, physical-AI, tokenizer, autonomous-driving, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "NVIDIA Cosmos platform: wavelet-based tokenizer (12x faster, +4dB PSNR), 7B-14B diffusion and 4B-13B autoregressive world models trained on 20M hours of video across 9 categories, targeting autonomous driving and robotics with open model license."
---

## Key Points

- Tokenizer: 2-level wavelet transform + spatiotemporal factorized 3D convolution; 12x faster, +4dB PSNR vs competitors
- Diffusion models: 7B and 14B params with 3D patchification, FPS-aware 3D RoPE, AdaLN-LoRA (36% parameter reduction)
- Autoregressive models: 4B-13B params (Llama3-style GPT), T5 text conditioning, no language understanding
- Training data: 20M hours → 100M clips across 9 categories; curated in 14 days on Blackwell (vs 3 years CPU)
- Applications: autonomous driving (XPENG, Uber, Waabi), robotics (1X, Agility, Figure AI), camera control
- Open Model License; 2M+ downloads by January 2026

## Detailed Summary

NVIDIA Cosmos takes a distinctly infrastructure-oriented approach to [[concepts/world-models]], positioning itself as the platform layer for [[concepts/physical-ai]] development. Rather than building a single model, Cosmos provides a full stack: advanced tokenizers, diffusion and autoregressive world foundation models at multiple scales, and a CUDA-accelerated data processing pipeline.

The tokenizer architecture is particularly innovative — using wavelet transforms for initial downsampling before spatiotemporal factorized 3D convolutions. This achieves state-of-the-art compression-quality tradeoffs with both continuous (16-dim) and discrete (64K vocabulary) token outputs.

The model lineup spans diffusion-based (7B/14B for Text2World and Video2World) and autoregressive (4B-13B Llama3-style) architectures, with progressive training from 512p/57 frames to 720p/121 frames. Training data covers nine physical domains with emphasis on manipulation (16%), navigation (16%), and nature dynamics (20%).

## Metadata

- **Author**: NVIDIA Research
- **Date Published**: 2025-01-06
- **Format**: paper + platform launch
- **URL**: https://arxiv.org/abs/2501.03575
