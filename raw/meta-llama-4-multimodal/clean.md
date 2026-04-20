---
title: "The Llama 4 Herd: The Beginning of a New Era of Natively Multimodal AI Innovation"
source: "https://ai.meta.com/blog/llama-4-multimodal-intelligence/"
author: "Meta AI"
date_published: 2025-04-05
date_ingested: 2026-04-05
tags: [llama, meta, open-source-llm, multimodal, moe, architecture]
type: article
status: raw
discovered_via: search
---

# Llama 4: Natively Multimodal AI

## Model Variants

### Llama 4 Scout
- 17 billion active parameters with 16 experts
- 109 billion total parameters
- Fits on single NVIDIA H100 GPU (Int4 quantization)
- Industry-leading 10 million token context window
- Pre-trained and post-trained with 256K context length

### Llama 4 Maverick
- 17 billion active parameters with 128 experts
- 400 billion total parameters
- Runs on single H100 DGX host
- Natively multimodal with image/text understanding
- ELO score of 1417 on LMArena

### Llama 4 Behemoth (still training at time of announcement)
- 288 billion active parameters with 16 experts
- Nearly 2 trillion total parameters
- Teacher model for smaller variants
- Outperforms GPT-4.5, Claude Sonnet 3.7 on STEM benchmarks

## Architecture

### Mixture of Experts (MoE)
First Llama family to use MoE — a single token activates only a fraction of the total parameters, improving compute efficiency.

### Multimodal Design
Early fusion: seamlessly integrates text and vision tokens into a unified model backbone, enabling joint pre-training on unlabeled multimodal data.

### iRoPE Architecture
Scout uses interleaved attention layers without positional embeddings, with inference time temperature scaling for length generalization.

## Training
- Over 30 trillion tokens (2x Llama 3)
- 200 languages supported (100+ with 1B+ tokens each)
- FP8 precision achieved 390 TFLOPs/GPU utilization
- Post-training: lightweight SFT → online RL → lightweight DPO
- Removed 50%+ of easy training data; continuous online RL with adaptive filtering

## Availability
Both Scout and Maverick available on llama.com and Hugging Face. Integrated into Meta AI across WhatsApp, Messenger, Instagram Direct, and web.
