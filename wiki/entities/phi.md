---
title: "Phi (Microsoft)"
type: entity
entity_type: tool
sources: ["[[sources/small-language-models-guide-2026]]"]
related: ["[[concepts/small-language-models]]", "[[concepts/local-llm-inference]]"]
last_compiled: 2026-04-05
summary: "Microsoft's SLM family — Phi-4 (14B) beats GPT-4o on MATH/GPQA with 84.8% MMLU; Phi-4-mini (3.8B) runs on 3GB VRAM with 128K context."
---

## Overview

Phi is Microsoft's family of [[concepts/small-language-models]], designed to achieve high reasoning performance in compute-constrained settings. The Phi series demonstrates that carefully curated training data can produce small models that outperform much larger ones on specific benchmarks.

## Key Models

### Phi-4 (14B parameters)
- 84.8% MMLU
- Beats GPT-4o on MATH and GPQA benchmarks
- ~10GB VRAM required
- Strong reasoning despite compact size

### Phi-4-mini (3.8B parameters)
- 67.3% MMLU
- ~3GB VRAM (runs on 8GB machines with [[concepts/quantization]])
- 128K token context window
- Outperforms Llama 3.2 3B
- Trained on 3.4T tokens of high-quality, reasoning-rich data

## Design Philosophy

Phi models prioritize data quality over parameter count. Training on curated, reasoning-rich data produces models that punch well above their weight class on mathematical and logical reasoning tasks.

## Mentioned In
- [[sources/small-language-models-guide-2026]] — benchmarks and VRAM requirements
