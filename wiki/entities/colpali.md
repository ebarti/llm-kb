---
title: "ColPali"
type: entity
entity_type: tool
sources: ["[[sources/huggingface-vlms-2025]]"]
related: ["[[concepts/vision-language-models]]", "[[concepts/document-processing-pipeline]]", "[[concepts/ocr-document-extraction]]"]
last_compiled: 2026-04-05
summary: "ColBERT-like multimodal retrieval model using VLMs as image encoders: produces multiple vectors per token with MaxSim similarity for direct visual document retrieval without OCR, evaluated on ViDoRe benchmark."
---

## Overview

ColPali is a multimodal document retrieval model that applies the ColBERT late-interaction architecture to visual documents. Instead of extracting text via OCR and then embedding it, ColPali directly embeds document images using a Vision Language Model as the image encoder and an LLM as the text encoder.

## How It Works

1. **Document images** are encoded into multiple vectors per token by a VLM
2. **Text queries** are encoded into multiple vectors by an LLM
3. **MaxSim similarity** computes relevance by finding maximum similarity between each query token and all document tokens
4. This produces **better performance** than single-vector approaches but at **higher compute cost**

## Variants

- **ColPali**: Original model
- **ColQwen2**: Uses Qwen2-VL as the vision encoder
- **ColSmolVLM**: Uses SmolVLM for smaller, faster deployment

## Evaluation

Evaluated on the **ViDoRe** benchmark: English/French financial reports, scientific figures, administrative documents. Outperforms traditional OCR + text embedding pipelines.

## Significance

ColPali represents a paradigm shift for [[concepts/document-processing-pipeline]] systems: it eliminates OCR as a prerequisite for document retrieval, though extraction of specific fields still requires text-capable models.

## Mentioned In
- [[sources/huggingface-vlms-2025]] — recommended approach for multimodal document retrieval
