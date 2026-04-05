---
title: "CLIP"
type: entity
entity_type: tool
sources: ["[[sources/pinecone-clip-multimodal-embeddings]]", "[[sources/nvidia-multimodal-rag-intro]]", "[[sources/multimodal-rag-images-text-guide]]"]
related: ["[[concepts/multimodal-embeddings]]", "[[concepts/multimodal-rag]]", "[[concepts/multimodal-ai]]", "[[concepts/vision-language-models]]"]
last_compiled: 2026-04-05
summary: "OpenAI's Contrastive Language-Image Pretraining model (2021): dual text/image encoders producing 512-dim shared embeddings via contrastive learning; foundational for multimodal search, RAG, and image generation."
---

## Overview

CLIP (Contrastive Language-Image Pretraining) is a multimodal embedding model developed by OpenAI and released in January 2021. It maps images and text into a shared 512-dimensional vector space using contrastive learning, enabling cross-modal similarity search. CLIP is arguably the single most influential model in the multimodal AI field — it underpins text-to-image search, guides diffusion models (DALL-E, Stable Diffusion), and serves as the embedding backbone for [[concepts/multimodal-rag]] systems.

## Architecture

- **Text Encoder**: 12-layer transformer (similar to GPT-2 small)
- **Image Encoder**: Vision Transformer (ViT) or ResNet variants
- **Output**: Both encoders produce 512-dimensional normalized vectors
- **Training**: Contrastive loss on 400 million image-text pairs from the web
- **Input**: Text tokenized to max 77 tokens; images resized to 224x224 pixels

## Key Capabilities

- **Zero-shot image classification**: Compare image embedding to text label embeddings without task-specific training
- **Cross-modal search**: Find images from text queries or text from image queries
- **Image generation guidance**: Provides the text-to-image alignment signal for DALL-E and Stable Diffusion
- **Object detection**: Patch-based comparisons create relevance maps matching language descriptions

## Successors and Alternatives

| Model | Developer | Dimensions | Key Improvement |
|-------|-----------|-----------|-----------------|
| CLIP | OpenAI | 512 | Original (2021) |
| ALIGN | Google | 640 | Larger-scale noisy training |
| SigLIP | Google | 512-1024 | Sigmoid loss for efficiency |
| Jina CLIP v2 | Jina AI | 1024 | 89 languages, 512x512 images |
| Voyage multimodal-3 | Voyage AI | 1024 | 32K token limit |
| ImageBind | Meta | 1024 | 6 modalities (audio, depth, thermal) |
| ColPali | Research | Varies | Late interaction for documents |

## Mentioned In

- [[sources/pinecone-clip-multimodal-embeddings]] — detailed architecture and contrastive learning explanation
- [[sources/nvidia-multimodal-rag-intro]] — CLIP as unified vector space approach for multimodal RAG
- [[sources/multimodal-rag-images-text-guide]] — CLIP compared to newer embedding models
