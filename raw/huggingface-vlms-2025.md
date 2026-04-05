---
title: "Vision Language Models: Better, Faster, Stronger (2025)"
source: "https://huggingface.co/blog/vlms-2025"
author: "Hugging Face"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [vision-language-models, multimodal, ocr, document-understanding, vlm]
type: article
status: raw
discovered_via: search
---

# Vision Language Models: Better, Faster, Stronger (2025)

Comprehensive overview of VLM landscape from Hugging Face.

## Model Architectures

### Any-to-Any Models
Multiple encoders (one per modality) → shared representation space → multiple decoders.
- Qwen 2.5 Omni: "Thinker-Talker" architecture
- MiniCPM-o 2.6 (8B): Vision, speech, language
- Janus-Pro-7B: Unified with decoupled visual encoding

### Mixture-of-Experts (MoE) as Decoders
Selective activation reduces inference time vs. dense models. Higher memory cost.
- Kimi-VL-A3B-Thinking: 16B total, 2.8B active
- DeepSeek-VL2: Broad multimodal capabilities

### Vision-Language-Action (VLA) Models
Extensions with action tokens, state tokens, time information.
- π0 (Physical Intelligence): 7 robotics platforms, 68 tasks
- GR00T N1 (NVIDIA): 2B parameters

## Key Models

| Model | Size | Strengths |
|-------|------|-----------|
| Qwen2.5-VL | 3B-72B | Agentic tasks, math, localization |
| RolmOCR | 7B | OCR performance |
| Kimi-VL-Thinking | 16B MoE (3B active) | Best reasoning |
| SmolVLM2 | 256M-2.2B | Video on devices |
| Gemma 3-4B-IT | 4B | 128k context, 140+ languages |
| Molmo | 1B-72B | Open, localization |

## Document Understanding & Multimodal RAG

### Document Screenshot Embedding (DSE)
Single vector per passage. Text encoder + image encoder. Softmax over dot products.

### ColBERT-like Models (Recommended for docs)
ColPali, ColQwen2, ColSmolVLM. Vision LM as image encoder, LLM as text encoder. Multiple vectors per token (MaxSim). Better performance but higher compute.

### ViDoRe Benchmark
English/French documents: financial reports, scientific figures, administrative docs.

## 2025 Trends
1. Smaller, more capable models (256M-3B)
2. Any-to-any multimodal processing
3. Reasoning capabilities in VLMs
4. MoE efficiency for inference
5. Agentic VLMs for UI/web automation
6. Multimodal RAG for complex documents
7. Extended context windows (up to 128k tokens)
