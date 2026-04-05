---
title: "Edge Inference (On-Device LLMs)"
type: concept
sources: ["[[sources/on-device-llms-2026]]"]
related: ["[[concepts/quantization]]", "[[concepts/speculative-decoding]]", "[[concepts/llm-inference-optimization]]", "[[entities/executorch]]", "[[entities/llama-cpp]]"]
last_compiled: 2026-04-05
summary: "Running LLMs directly on mobile devices and edge hardware: sub-1B to 3B models with 4-bit quantization achieve <20ms/token latency — 10-25x faster than cloud roundtrips — with zero data transmission and zero API cost."
---

## Overview

Edge inference (on-device LLM inference) runs language models directly on end-user hardware — smartphones, laptops, IoT devices — rather than routing requests to cloud servers. In 2026, this has moved from research novelty to practical engineering, with models serving billions of users across Meta's apps via [[entities/executorch|ExecuTorch]].

Four drivers make on-device inference compelling:
1. **Latency**: <20ms per token vs cloud's 200-500ms roundtrip (10-25x faster)
2. **Privacy**: Data never leaves the device
3. **Cost**: Zero API costs; inference runs on user's own hardware
4. **Availability**: Works without network connectivity

## The Hardware Landscape (2026)

Mobile neural processing units now deliver substantial compute:

| Chip | TOPS | Target |
|------|------|--------|
| Apple A19 Pro | ~35 | iPhone |
| Qualcomm Snapdragon 8 Elite Gen 5 | ~60 | Android flagship |
| MediaTek Dimensity 9400+ | ~50 | Android mid-high |

**Critical constraint**: Memory bandwidth. Mobile devices offer 50-90 GB/s vs datacenter's 2-3 TB/s — a **30-50x gap**. Since the decode phase is memory-bandwidth-bound, this makes aggressive model compression essential.

**Available RAM**: Typically <4GB for inference on high-end devices (after OS and app overhead), limiting practical model sizes.

## Model Landscape

The practical range has settled at sub-1B to 3B parameters:

| Model | Params | Notable |
|-------|--------|---------|
| SmolLM2 | 135M-1.7B | 11T training tokens, outperforms Llama 3.2 1B |
| Gemma 3 | 270M-27B | Extreme efficiency at small scales |
| Llama 3.2 | 1B, 3B | 128K context, Qualcomm/MediaTek optimized |
| Phi-4 mini | 3.8B | High-quality synthetic data training |

Architecture insight: **deep-thin designs** (more layers, smaller dimensions) outperform wide-shallow architectures at small scales. Reasoning capabilities achieved through distillation from larger models.

## Enabling Technologies

- **[[concepts/quantization]]**: 4-bit AWQ/GPTQ is standard; sub-4-bit techniques (BitNet 1.58-bit, SpinQuant) emerging
- **[[concepts/speculative-decoding]]**: Medusa achieves 2.2-3.6x acceleration without retraining
- **KV Cache Compression**: 3-bit quantization with negligible quality degradation
- **Grouped Query Attention**: Standard for mobile, reducing cache requirements

## Deployment Frameworks

| Framework | Focus | Key Feature |
|-----------|-------|-------------|
| [[entities/executorch|ExecuTorch]] 1.0 | Production mobile | 50KB footprint, 12+ backends |
| [[entities/llama-cpp|llama.cpp]] | CPU inference | GGUF format standard |
| MLX | Apple Silicon | Unified memory optimization |
| MLC-LLM | Cross-platform | Compilation to multiple targets |

## Use Case Guidance

**Best for on-device**: Latency-sensitive interactions, privacy-critical data, high-volume simple tasks, offline scenarios

**Best left to cloud**: Frontier reasoning, long conversations (>128K context), broad knowledge retrieval, tasks requiring latest model capabilities

## Emerging Directions

- **MoE on Edge**: Expert partitioning targeting sub-10W, <8GB constraints
- **Test-Time Compute**: Small models with intensive inference-time reasoning matching larger models
- **On-Device Personalization**: Self-supervised test-time training for domain adaptation
- **Multimodal**: Unified vision-language architectures (Qwen3 Omni, Gemini 3)

## Sources
- [[sources/on-device-llms-2026]] — Meta AI Research survey of the 2026 on-device landscape

## Related Concepts
- [[concepts/quantization]] — enabling technology for fitting models on mobile hardware
- [[concepts/speculative-decoding]] — acceleration technique for on-device inference
- [[concepts/llm-inference-optimization]] — edge inference as the extreme optimization case
- [[concepts/llm-cost-optimization]] — eliminating API costs entirely
