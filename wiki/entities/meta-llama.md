---
title: "Meta Llama"
type: entity
entity_type: tool
sources: ["[[sources/meta-llama-4-multimodal]]", "[[sources/bentoml-open-source-llms-2026]]"]
related: ["[[concepts/open-source-llms]]", "[[concepts/mixture-of-experts]]"]
last_compiled: 2026-04-05
summary: "Meta's open-weight LLM family — Llama 4 introduced MoE architecture with Scout (10M token context), Maverick (multimodal), and Behemoth (2T params, teacher model)."
---

## Overview

Llama is Meta's family of open-weight large language models, among the most widely used open models in the world. Llama 4, released April 2025, marked the family's transition to [[concepts/mixture-of-experts]] architecture and native multimodality.

## Key Models

### Llama 4 Scout
- 17B active / 109B total, 16 experts
- 10 million token context window (industry-leading for open models)
- Fits on single NVIDIA H100 with Int4 [[concepts/quantization]]
- iRoPE architecture for length generalization

### Llama 4 Maverick
- 17B active / 400B total, 128 experts
- Natively multimodal (image + text understanding)
- ELO 1417 on LMArena
- Runs on single H100 DGX host

### Llama 4 Behemoth
- 288B active / ~2T total, 16 experts
- Teacher model for distilling Scout and Maverick
- Outperforms GPT-4.5, Claude Sonnet 3.7 on STEM benchmarks

### Llama 3.2 (2024)
- 1B and 3B variants for mobile/edge deployment
- 3B: 63.4% MMLU, best tool-use capability (67% BFCL V2)
- Key [[concepts/small-language-models]] option

## Training
- 30T+ tokens (2x Llama 3), 200 languages
- Post-training: lightweight SFT → online RL → lightweight DPO
- FP8 precision: 390 TFLOPs/GPU utilization

## Licensing
Meta community license — free for most uses with some restrictions for very large deployments.

## Mentioned In
- [[sources/meta-llama-4-multimodal]] — official Llama 4 announcement
- [[sources/bentoml-open-source-llms-2026]] — placement in 2026 model landscape
