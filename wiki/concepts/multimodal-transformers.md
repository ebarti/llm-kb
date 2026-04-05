---
title: "Multimodal Transformers"
type: concept
sources: ["[[sources/vlms-2025-huggingface]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/cross-attention]]", "[[concepts/mixture-of-experts]]", "[[concepts/vision-language-models]]", "[[concepts/rotary-position-embeddings]]"]
last_compiled: 2026-04-05
summary: "Transformer architectures processing multiple modalities (text, image, video, audio, actions) — evolving from encoder-bridge-decoder to native multimodal fusion, with MoE decoders dominating by 2025."
---

## Overview

Multimodal transformers extend the [[concepts/transformer-architecture]] to process inputs beyond text — images, video, audio, and even robotic actions. The core challenge is combining representations from different modalities into a shared space where the model can reason across them.

## Architectural Families

### Encoder-Bridge-Decoder (Dominant 2023-2024)

A pre-trained vision encoder (ViT, SigLIP, DINOv2) processes images into patch embeddings. An MLP adapter or cross-attention bridge maps these into the LLM's token space. The LLM decoder processes interleaved text and visual tokens.

Examples: LLaVA, Qwen-VL, InternVL

### Native Multimodal (Emerging 2025)

No distinction between vision and language modules — a unified architecture processes all modalities from the start. LLaMA 4 uses early fusion MLP adapters; the NEO architecture eliminates separate visual/language modules entirely.

### Any-to-Any Models

Accept multiple input modalities and produce multiple output modalities:
- Qwen 2.5 Omni: "Thinker-Talker" for text + streaming speech
- Janus-Pro-7B: Decoupled visual encoding for understanding vs generation

### MoE Multimodal Decoders

[[concepts/mixture-of-experts]] dominates multimodal decoders in 2025:
- Kimi-VL-A3B-Thinking: 16B params, 2.8B active (best open reasoning VLM)
- DeepSeek-VL2, Llama 4, MoE-LLaVA

## Video Understanding

Key innovations for temporal modeling:
- **Extended Multimodal RoPE** (Qwen2.5-VL): [[concepts/rotary-position-embeddings]] extended for absolute time positions and adaptive FPS
- **DINOv2 downsampling** (LongVU): Remove redundant frames via visual similarity
- **Interleaved timestamps** (Gemma 3): Frame-timestamp pairs for temporal grounding

## Vision-Language-Action Models (VLAs)

VLMs extended with action/state/time tokens for robotics:
- pi-0 / pi-0-FAST (Physical Intelligence): 7 platforms, 68 tasks
- GR00T N1 (NVIDIA): 2B humanoid robot foundation model

## Multimodal RAG

Two retrieval approaches for visual documents:
- **DSE** (Document Screenshot Embedding): Single-vector per page, efficient
- **ColBERT-like** (ColPali, ColQwen2): Multi-vector per token/patch, higher accuracy

## Sources

- [[sources/vlms-2025-huggingface]] — comprehensive 2025 VLM survey

## Related Concepts

- [[concepts/transformer-architecture]] — the base architecture
- [[concepts/cross-attention]] — mechanism for fusing modalities
- [[concepts/mixture-of-experts]] — dominant decoder architecture for VLMs
- [[concepts/rotary-position-embeddings]] — extended for multimodal temporal encoding
