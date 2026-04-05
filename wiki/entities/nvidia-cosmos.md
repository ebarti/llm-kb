---
title: "NVIDIA Cosmos"
type: entity
entity_type: framework
url: "https://www.nvidia.com/en-us/ai/cosmos/"
related: ["[[concepts/world-models]]", "[[concepts/physical-ai]]", "[[concepts/embodied-ai]]"]
tags: [NVIDIA, Cosmos, world-foundation-model, physical-AI, autonomous-driving, robotics]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "NVIDIA's world foundation model platform: wavelet-based tokenizer (12x faster), 7B-14B diffusion and 4B-13B autoregressive models trained on 20M hours of video, targeting autonomous driving and robotics; open model license, 2M+ downloads."
---

## Overview

NVIDIA Cosmos is a platform of world foundation models (WFMs) designed to accelerate [[concepts/physical-ai]] development. Launched at CES 2025, it provides the full infrastructure stack: advanced tokenizers, diffusion and autoregressive world models at multiple scales, and a CUDA-accelerated data processing pipeline. By January 2026, Cosmos had surpassed 2 million downloads.

## Key Facts

- **Type**: framework/platform
- **Developer**: NVIDIA
- **Launch**: CES 2025
- **License**: NVIDIA Open Model License
- **Downloads**: 2M+ by January 2026
- **Training data**: 20M hours → 100M clips across 9 physical domains

## Model Architecture

| Model Type | Sizes | Architecture | Approach |
|-----------|-------|-------------|---------|
| Diffusion WFM | 7B, 14B | DiT + 3D RoPE + AdaLN-LoRA | Text2World, Video2World |
| Autoregressive WFM | 4B, 5B, 12B, 13B | Llama3-style GPT | Discrete token prediction |
| Tokenizer | - | Wavelet + 3D conv | 12x faster, +4dB PSNR |
| Prompt Upsampler | 12B | Mistral-NeMo-based | Text prompt enhancement |

## Model Types

- **Cosmos-Predict**: Future state simulation via video prediction
- **Cosmos-Transfer**: High-quality generation with spatial control
- **Cosmos-Reason**: Open, customizable reasoning model

## Industrial Adoption

Robotics: 1X, Agility, Figure AI | Autonomous driving: Waabi, XPENG, Uber | Edge: Cosmos Nano

## Mentions

- [[sources/nvidia-cosmos-world-foundation]] — full technical details
- [[sources/world-models-race-2026]] — competitive positioning
