---
title: "Source: Vision Language Models 2025"
type: source-summary
source: "[[raw/vlms-2025-huggingface]]"
related: ["[[concepts/multimodal-transformers]]", "[[concepts/mixture-of-experts]]", "[[concepts/vision-language-models]]"]
last_compiled: 2026-04-05
summary: "Hugging Face's 2025 VLM survey: any-to-any models, MoE decoders (Kimi-VL 2.8B active of 16B), dense small models (SmolVLM2), multimodal RAG (ColPali), video understanding, VLAs for robotics, and agentic capabilities."
---

## Key Points

- Any-to-any models: multiple encoders, fused embeddings, multiple decoders (Qwen 2.5 Omni, Janus-Pro)
- MoE decoders dominate: Kimi-VL (16B, 2.8B active), DeepSeek-VL2, Llama 4
- Small efficient VLMs: SmolVLM2 (256M-2.2B), Gemma-3-4B (128k context)
- Multimodal RAG: ColBERT-like (ColPali, ColQwen2) vs DSE approaches for document retrieval
- Video LMs: dynamic frame selection (LongVU), multimodal RoPE for temporal encoding (Qwen2.5-VL)
- VLAs extend VLMs with action/state tokens for robotics (pi-0, GR00T N1)
- DPO alignment adapted for visual preference learning

## Detailed Summary

The [[concepts/multimodal-transformers]] landscape in 2025 has converged around several architectural families. The dominant approach combines a pre-trained vision encoder (often SigLIP or DINOv2) with an LLM decoder, connected via an MLP adapter or cross-attention bridge. [[concepts/mixture-of-experts]] architectures are particularly prevalent for balancing quality and efficiency.

The most striking trend is the emergence of very small yet capable VLMs (SmolVLM2 at 256M parameters handles video understanding) and the extension of VLMs into agentic domains — UI navigation, document analysis, and even robot control through Vision-Language-Action models.

Multimodal RAG has evolved two main approaches: single-vector DSE for efficiency and multi-vector ColBERT-style methods (ColPali, ColQwen2) for accuracy, both operating directly on document screenshots without OCR.

## Related Concepts

- [[concepts/multimodal-transformers]] — the broad category
- [[concepts/vision-language-models]] — specific architecture family
- [[concepts/mixture-of-experts]] — dominant decoder architecture for VLMs
- [[concepts/rotary-position-embeddings]] — multimodal RoPE for video temporal encoding
