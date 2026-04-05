---
title: "Vision Language Models: Better, Faster, Stronger (2025)"
source: "https://huggingface.co/blog/vlms-2025"
author: "Hugging Face"
date_published: 2025-06-15
date_ingested: 2026-04-05
tags: [VLM, multimodal, vision-language, architecture, MoE, video-LM]
type: article
status: raw
discovered_via: search
---

# Vision Language Models: Better, Faster, Stronger (2025)

## Architectural Approaches

### Any-to-Any Models
Models accepting multiple input modalities and producing multiple output modalities. Architecture: multiple encoders (one per modality), fused embeddings into shared representation space, multiple/single decoders.

Notable models:
- Qwen 2.5 Omni: "Thinker-Talker" architecture
- MiniCPM-o 2.6 (8B): Vision, speech, language
- Janus-Pro-7B: Unified with decoupled visual encoding

### MoE as Decoders
Selective expert activation for efficiency:
- Kimi-VL-A3B-Thinking: 16B params, 2.8B active (most advanced open reasoning)
- DeepSeek-VL2: Broad multimodal capabilities
- Llama 4: Full MoE with vision
- MoE-LLaVA: Efficiency and hallucination reduction

### Dense Vision Encoders in Small Models
SmolVLM2 (256M, 500M, 2.2B), Gemma-3-4B-IT (128k context), Qwen2.5-VL-3B.

## Specialized Capabilities

### Object Detection and Segmentation
Token-based localization: models output bounding box coordinates as tokens. PaliGemma 2 for detection/segmentation, Molmo for pointing and counting.

### Multimodal RAG
Two retriever types:
1. Document Screenshot Embedding (DSE): single vector per query/passage
2. ColBERT-like (ColPali, ColQwen2): multiple vectors per token/patch with MaxSim scoring

### Video Language Models
- LongVU (Meta): DINOv2 downsampling + text-query refinement
- Qwen2.5-VL: Extended multimodal RoPE for temporal positions
- Gemma 3: Interleaved timestamps with frames

### Vision-Language-Action Models (VLAs)
VLM outputs extended with action/state/time tokens for robotics:
- pi-0/pi-0-FAST (Physical Intelligence): 7 platforms, 68 tasks
- GR00T N1 (NVIDIA): 2B humanoid robot foundation model

## Training: DPO for VLMs
Direct Preference Optimization adapted for visual models using preference datasets with chosen/rejected image-answer pairs.

## Top Models (2025)

| Model | Sizes | Key Strength |
|-------|-------|--------------|
| Qwen2.5-VL | 3B-72B | Versatile, agentic, math |
| Kimi-VL-Thinking | 16B (2.8B active) | Best reasoning |
| SmolVLM2 | 256M-2.2B | Smallest video LM |
| Gemma-3-4B | 4B | Long context (128k) |
| Llama 4 | 109B-400B MoE | Extreme long context |
