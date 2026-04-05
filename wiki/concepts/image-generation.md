---
title: "Image Generation"
type: concept
sources: ["[[sources/bentoml-open-source-image-generation-2026]]", "[[sources/flux-vs-stable-diffusion-2026]]", "[[sources/dit-diffusion-transformer-architecture]]", "[[sources/autoregressive-vision-models-survey]]"]
related: ["[[concepts/diffusion-models]]", "[[concepts/diffusion-transformer]]", "[[concepts/flow-matching]]", "[[concepts/autoregressive-image-generation]]", "[[concepts/visual-tokenization]]", "[[concepts/video-generation]]", "[[concepts/3d-generation]]", "[[entities/flux]]", "[[entities/stable-diffusion]]"]
tags: [image-generation, text-to-image, generative-ai, creative-tools]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "The field of AI-driven image synthesis from text, image, or other inputs -- dominated in 2026 by diffusion-based models (FLUX, SD3, Midjourney) using DiT architectures and flow matching, with autoregressive approaches (LlamaGen, NextStep-1) emerging as serious competitors."
---

## Overview

Image generation encompasses AI systems that synthesize novel images from various inputs: text prompts (text-to-image), reference images (image-to-image), sketches, depth maps, or combinations thereof. It is the most mature domain within generative AI beyond text, with commercial systems like Midjourney, [[entities/flux]], and [[entities/stable-diffusion]] producing photorealistic outputs indistinguishable from photographs.

The field has undergone three architectural generations: GANs (2014-2021), U-Net-based [[concepts/diffusion-models]] (2020-2024), and [[concepts/diffusion-transformer]]-based systems with [[concepts/flow-matching]] (2023-present). A fourth paradigm -- [[concepts/autoregressive-image-generation]] -- is re-emerging as a serious competitor.

## Key Ideas

### Architectural Generations

**Generation 1: GANs (2014-2021)**
Generative Adversarial Networks pitted a generator against a discriminator in adversarial training. StyleGAN produced remarkable quality but suffered from mode collapse, training instability, and limited text conditioning. Largely superseded by diffusion models.

**Generation 2: U-Net Diffusion (2020-2024)**
Latent diffusion models with U-Net backbones democratized image generation. DALL-E 2 (OpenAI, 2022) used diffusion conditioned on CLIP embeddings. Imagen (Google, 2022) showed that scaling the text encoder (T5) matters more than scaling the image model. [[entities/stable-diffusion]] (Stability AI, 2022) open-sourced the technology, creating an massive ecosystem of fine-tuned models, LoRAs, and tools.

**Generation 3: DiT + Flow Matching (2023-present)**
[[concepts/diffusion-transformer]] architectures replaced U-Net with transformers for predictable scaling. [[entities/flux]] FLUX.1 (Black Forest Labs, 2024) and [[entities/stable-diffusion]] 3 (Stability AI, 2024) both adopted MMDiT designs with [[concepts/flow-matching]] training. Key improvements: superior text rendering, consistent hand generation, better prompt adherence.

**Generation 4 (emerging): Autoregressive**
[[concepts/autoregressive-image-generation]] models like LlamaGen, VAR (NeurIPS 2024 Best Paper), and NextStep-1 (ICLR 2026 Oral) treat image generation as next-token prediction, matching diffusion quality while offering superior inference-time scaling.

### The Open-Source Landscape (2026)

| Model | Developer | Parameters | Architecture | Specialty |
|-------|-----------|-----------|--------------|-----------|
| FLUX.2 [dev] | Black Forest Labs | 32B | MMDiT + flow matching | Multi-reference consistency |
| FLUX.2 [klein] | Black Forest Labs | 4-9B | Distilled MMDiT | Sub-second consumer GPU |
| SD 3.5 Large | Stability AI | 8B | MMDiT + flow matching | LoRA ecosystem |
| HunyuanImage-3.0 | Tencent | 80B MoE (13B active) | AR + DiT | Long-prompt comprehension |
| Qwen-Image | Alibaba | 20B | DiT | Text rendering, editing |
| GLM-Image | Zhipu AI | 16B (9B AR + 7B DiT) | Hybrid AR+diffusion | Dense text, UI layouts |
| Z-Image-Turbo | Alibaba | 6B | DiT | Ultra-fast, bilingual |

### Key Quality Dimensions

Modern image generation is evaluated across:
- **Prompt adherence**: Does the image match all elements of the text prompt?
- **Typography**: Can the model render readable text within images?
- **Anatomical correctness**: Hands, fingers, faces, body proportions
- **Photorealism**: Lighting, materials, depth of field, texture fidelity
- **Artistic style control**: Ability to adopt specific styles via prompting or fine-tuning
- **Resolution**: SD 1.5 (512x512) to FLUX.2 (4MP/4K-class)

### Deployment Tooling

- [[entities/comfyui]]: Node-based visual workflow builder for complex generation pipelines
- Automatic1111 (A1111): Gradio-based UI for simpler workflows
- [[concepts/lora-fine-tuning]]: Low-Rank Adaptation for specializing models with minimal data (5+ images)

## How It Connects

Image generation is the foundation technology that extends into [[concepts/video-generation]] (temporal sequences of images), [[concepts/3d-generation]] (via score distillation from 2D models), and [[concepts/audio-generation]] (shared architectural principles). The [[concepts/diffusion-transformer]] architecture scales across all these modalities.

## Open Questions

- Will autoregressive approaches overtake diffusion for image generation?
- How will real-time generation (sub-100ms) change interactive creative workflows?
- What is the role of specialized fine-tuning vs. general-purpose foundation models?

## Sources

- [[sources/bentoml-open-source-image-generation-2026]] -- 2026 open-source landscape
- [[sources/flux-vs-stable-diffusion-2026]] -- FLUX vs SD comparison
- [[sources/dit-diffusion-transformer-architecture]] -- DiT architecture
- [[sources/autoregressive-vision-models-survey]] -- AR competition
