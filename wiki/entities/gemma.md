---
title: "Gemma (Google)"
type: entity
entity_type: tool
sources: ["[[sources/small-language-models-guide-2026]]"]
related: ["[[concepts/small-language-models]]", "[[concepts/local-llm-inference]]"]
last_compiled: 2026-04-05
summary: "Google's open-weight SLM family — Gemma 3 4B offers 128K context and multimodal vision in 3GB VRAM; Gemma 270M runs 25 conversations on 0.75% phone battery."
---

## Overview

Gemma is Google's family of open-weight [[concepts/small-language-models]], spanning from the ultra-tiny 270M parameter model (suitable for mobile phones) to the capable 4B and 9B variants. Gemma is notable for its strong multilingual support (140+ languages) and multimodal vision capabilities across model sizes.

## Key Models

### Gemma 3 4B
- 59.6% MMLU
- ~3GB VRAM with [[concepts/quantization]]
- 128K token context window
- 140+ languages
- Multimodal vision support

### Gemma 270M
- Ultra-efficient mobile model
- 0.75% battery consumption for 25 conversations on Pixel 9 Pro
- Proves SLMs are viable for on-device deployment

### Gemma 4 (April 2026)
- Four variants including E2B and E4B for on-device use
- Runs on 5GB RAM with 4-bit quantization on modern smartphones

## Design Philosophy

Gemma emphasizes efficiency and breadth: multilingual support, multimodal capabilities, and extreme efficiency at the smallest sizes. The 270M model demonstrates that useful AI can run within a phone's power budget.

## Mentioned In
- [[sources/small-language-models-guide-2026]] — benchmarks and edge deployment
