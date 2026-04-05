---
title: "Stable Diffusion"
type: entity
entity_type: tool
url: "https://stability.ai/"
related: ["[[concepts/diffusion-models]]", "[[concepts/latent-diffusion]]", "[[concepts/diffusion-transformer]]", "[[concepts/image-generation]]", "[[entities/flux]]", "[[entities/black-forest-labs]]", "[[entities/comfyui]]"]
tags: [stable-diffusion, image-generation, stability-ai, open-source, latent-diffusion]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The model family that democratized AI image generation from 2022 -- evolving from U-Net + DDPM (SD 1.x/2.x/XL) to MMDiT + flow matching (SD 3.5), retaining the largest fine-tuning ecosystem (thousands of LoRAs) despite being surpassed by FLUX in raw quality."
---

## Overview

Stable Diffusion is a family of open-source [[concepts/image-generation]] models developed by Stability AI, based on the [[concepts/latent-diffusion]] architecture pioneered by the CompVis group at LMU Munich (whose key researchers later founded [[entities/black-forest-labs]] to create [[entities/flux]]). Released in August 2022, Stable Diffusion was the first high-quality text-to-image model available as open weights, sparking a massive ecosystem of fine-tuned models, LoRAs, tools, and creative communities.

## Key Facts

- **Type**: tool / model family
- **Developer**: Stability AI (based on CompVis/LMU Munich research)
- **Notable for**: Democratizing AI image generation; largest ecosystem of fine-tuned models and LoRAs
- **License**: Various (open-weight, some restrictions on commercial use)

## Model Versions

| Version | Year | Architecture | Parameters | Key Change |
|---------|------|-------------|-----------|------------|
| SD 1.4/1.5 | 2022 | U-Net + DDPM | ~1B | First open release; 512x512 |
| SD 2.0/2.1 | 2022 | U-Net + DDPM | ~1B | Improved quality; OpenCLIP |
| SDXL | 2023 | U-Net + DDPM | ~3.5B | 1024x1024; two-stage refiner |
| SDXL Turbo | 2023 | Distilled U-Net | ~3.5B | Real-time generation |
| SD 3.0/3.5 | 2024 | MMDiT + flow matching | ~8B | DiT backbone; improved text |
| SVD | 2024 | U-Net temporal | - | Video from images |

## Architecture Evolution

The progression from SD 1.x to SD 3.5 mirrors the broader field's architectural transition:

1. **SD 1.x-2.x**: Latent diffusion with U-Net backbone, CLIP text encoding, DDPM noise prediction
2. **SDXL**: Larger U-Net, dual CLIP encoders, two-stage generation with refiner
3. **SD 3.5**: Complete architecture change to [[concepts/diffusion-transformer]] (MMDiT), dual text encoders (T5 + CLIP), [[concepts/flow-matching]] training -- the same architectural paradigm as [[entities/flux]]

## Ecosystem Advantages

Despite being surpassed by FLUX in raw quality metrics, Stable Diffusion retains:
- **Thousands of LoRAs**: Specialized fine-tuned adapters for every conceivable style and subject
- **Low hardware requirements**: SD 1.5 runs on 4GB VRAM
- **Mature tooling**: Deep integration with [[entities/comfyui]], A1111, and production pipelines
- **Fine-tuning ecosystem**: LoRA, Textual Inversion, DreamBooth all well-established
- **SDXL-Lightning**: High-quality output in 1-8 steps for near-real-time use

## Mentioned In

- [[sources/bentoml-open-source-image-generation-2026]] -- 2026 model landscape
- [[sources/flux-vs-stable-diffusion-2026]] -- comparison with FLUX
- [[sources/flux-architecture-demystified]] -- SD3 MMDiT design compared with FLUX

## External References

- https://stability.ai/
- https://github.com/Stability-AI/generative-models
