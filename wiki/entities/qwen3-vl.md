---
title: "Qwen3-VL"
type: entity
entity_type: tool
sources: ["[[sources/bentoml-vision-language-models-2026]]"]
related: ["[[concepts/vision-language-models]]", "[[concepts/multimodal-ai]]", "[[concepts/image-understanding]]"]
last_compiled: 2026-04-05
summary: "Alibaba's flagship open-source VLM (235B params, 22B active MoE): rivals GPT-5 and Gemini-2.5-Pro with 256K-1M context, multilingual OCR (32 languages), and visual agent capabilities."
---

## Overview

Qwen3-VL is a family of vision-language models developed by Alibaba Cloud. The flagship model, Qwen3-VL-235B-A22B, uses a Mixture-of-Experts (MoE) architecture with 235B total parameters and 22B active, rivaling proprietary models like GPT-5 and Gemini-2.5-Pro on key benchmarks.

## Key Specifications

- **Parameters**: 235B total / 22B active (flagship); 30B variant also available
- **Context Window**: 256K tokens native, expandable to 1M
- **Architecture**: Mixture-of-Experts
- **Editions**: Instruct and Thinking variants for the 30B model
- **License**: Open-source

## Capabilities

- Visual agent abilities for UI operation and automation
- Multilingual OCR covering 32 languages
- Frame-by-frame video analysis across hour-long content
- Matches frontier proprietary models on MMLU, AIME25, and LiveBench benchmarks

## Significance

Qwen3-VL represents the most capable open-source [[concepts/vision-language-models]] as of early 2026, demonstrating that the gap between open-source and proprietary multimodal models has effectively closed for many practical applications.

## Mentioned In

- [[sources/bentoml-vision-language-models-2026]] — profiled as a top open-source VLM
