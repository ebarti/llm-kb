---
title: "FLUX"
type: entity
entity_type: tool
url: "https://blackforestlabs.ai/"
related: ["[[concepts/diffusion-transformer]]", "[[concepts/flow-matching]]", "[[concepts/image-generation]]", "[[entities/stable-diffusion]]", "[[entities/black-forest-labs]]", "[[entities/comfyui]]"]
tags: [flux, image-generation, flow-matching, dit, open-source]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Leading open-source text-to-image model family from Black Forest Labs using MMDiT architecture with flow matching -- FLUX.2 [dev] at 32B parameters, FLUX.2 [klein] at 4-9B for consumer GPUs, featuring dual-stream/single-stream transformer blocks and T5+CLIP text encoding."
---

## Overview

FLUX is a family of text-to-image generation models developed by [[entities/black-forest-labs]], the company founded by the original Stable Diffusion creators. FLUX represents the state of the art in open-weight [[concepts/image-generation]], using a Multimodal [[concepts/diffusion-transformer]] (MMDiT) architecture with [[concepts/flow-matching]] training.

## Key Facts

- **Type**: tool / model family
- **Developer**: [[entities/black-forest-labs]]
- **Notable for**: State-of-the-art open-weight image generation; superior typography and prompt adherence
- **Architecture**: MMDiT (19 dual-stream + single-stream transformer blocks)
- **Training**: [[concepts/rectified-flow]] velocity prediction
- **Text encoding**: Dual T5 + CLIP encoders

## Model Variants

| Variant | Parameters | Access | Use Case |
|---------|-----------|--------|----------|
| FLUX.2 [pro] | Undisclosed | API only | Highest quality commercial |
| FLUX.2 [flex] | Undisclosed | Developer API | Parameter control |
| FLUX.2 [dev] | 32B | Open-weight | Research, production |
| FLUX.2 [klein] | 9B / 4B | Open-weight | Sub-second on consumer GPUs (~13GB VRAM) |
| FLUX.1 [schnell] | 12B | Open-weight | Fast prototyping (8GB VRAM) |

## Architecture Details

FLUX.1 uses a fully transformer-based architecture in latent space:
- **19 dual-stream blocks**: Separate weights for text and image tokens with joint self-attention over concatenated sequences (MMDiT design from SD3)
- **Single-stream blocks**: Shared weights with parallel attention and feedforward computation
- **AdaLN modulation**: Dynamic scaling/shifting per layer based on conditioning
- **RoPE**: Rotary Positional Embeddings for resolution flexibility
- **Dual text encoders**: T5 (dense per-token) + CLIP (pooled semantic) for comprehensive text understanding

## Performance Advantages

- Near-perfect typography and text rendering
- Realistic hand generation with correct finger counts
- Multi-reference consistency (up to 10 reference images in FLUX.2)
- Quality results in 4-20 steps (vs. 20-50 for DDPM-trained models)
- ~4x faster than torch.compile via MAX optimization

## Mentioned In

- [[sources/bentoml-open-source-image-generation-2026]] -- 2026 open-source landscape
- [[sources/flux-vs-stable-diffusion-2026]] -- comparison with SD
- [[sources/flux-architecture-demystified]] -- architecture deep-dive

## External References

- https://blackforestlabs.ai/
- https://github.com/black-forest-labs/flux
