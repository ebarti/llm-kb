---
title: "On-Device LLMs: State of the Union, 2026"
source: "https://v-chandra.github.io/on-device-llms/"
author: "Vikas Chandra (Meta AI Research)"
date_published: 2026-01-01
date_ingested: 2026-04-05
tags: [edge-ai, on-device, mobile-inference, quantization, executorch]
type: article
status: raw
discovered_via: search
---

# On-Device LLMs: State of the Union, 2026

## Model Sizes & Architecture
Dominant range: Sub-1B to 3B parameters for practical mobile deployment.
- Llama 3.2 (1B, 3B): 128K context, Qualcomm/MediaTek optimized
- Gemma 3 (270M-27B): Extreme efficiency at small scales
- Phi-4 (3.8B mini, 14B): High-quality synthetic data training
- SmolLM2 (135M-1.7B): 11T training tokens, outperforms Llama 3.2 1B

Architecture insight: Deep-thin designs (more layers, smaller dimensions) outperform wide-shallow architectures at small scales. Reasoning via distillation from larger models.

## Hardware Capabilities
Mobile neural processing units:
- Apple A19 Pro: ~35 TOPS
- Qualcomm Snapdragon 8 Elite Gen 5: ~60 TOPS
- MediaTek Dimensity 9400+: ~50 TOPS

Critical constraint: Memory bandwidth (50-90 GB/s on mobile vs. 2-3 TB/s in datacenters) creates 30-50x gap, making decode memory-bound.

## Quantization Strategies
- 4-bit standard: AWQ and GPTQ enable 4x memory reduction with minimal quality loss
- SmoothQuant: Migrates quantization difficulty from activations to weights
- SpinQuant: Rotation matrices reshape activation distributions for 4-bit weights/activations/KV-cache
- Sub-4-bit: BitNet demonstrates native 1.58-bit training

## Inference Optimization
- Speculative decoding: Draft models accelerate generation 2.2-3.6x (Medusa) without retraining
- KV cache compression: 3-bit quantization with negligible quality degradation
- Grouped query attention and local-global attention mechanisms now standard for mobile

## Deployment Frameworks
- ExecuTorch 1.0 (Meta, Oct 2025): 50KB footprint, 12+ hardware backends, serves billions of users
- llama.cpp: Standard CPU inference with GGUF format
- MLX (Apple): Optimized for Apple Silicon with unified memory
- MLC-LLM: Cross-platform compilation support

## Key Constraints
- Memory: Available RAM typically <4GB on high-end devices
- Power: Models must fit sustained inference within battery/thermal budgets
- Latency: On-device generates tokens in under 20ms vs cloud's 200-500ms roundtrip

## Emerging Directions
- MoE on Edge: Expert partitioning targeting sub-10W, <8GB
- Test-Time Compute: Small models with intensive inference-time reasoning matching larger models
- On-Device Personalization: Self-supervised test-time training without cloud transmission
- Multimodal: Native architectures consolidating vision and language
