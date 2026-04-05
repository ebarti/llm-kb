---
title: "Switch Transformer"
type: entity
entity_type: paper
sources: ["[[sources/huggingface-mixture-of-experts]]"]
related: ["[[concepts/mixture-of-experts]]", "[[entities/t5]]", "[[concepts/transformer-architecture]]"]
last_compiled: 2026-04-05
summary: "Google's 2021 MoE model scaling to 1.6T parameters with 2048 experts using simplified single-expert routing — 4x pretraining speedup over T5-XXL, demonstrating MoE scaling viability."
---

## Overview

The Switch Transformer (Fedus et al., Google, 2021) demonstrated that [[concepts/mixture-of-experts]] could scale to 1.6 trillion parameters with 2,048 experts. Built on the [[entities/t5]] encoder-decoder architecture, it replaced dense FFN layers with MoE layers using a key simplification: **single-expert routing** instead of top-2.

## Key Innovations

- **Single-expert routing**: Each token goes to exactly one expert (simpler, faster than top-2)
- **Halved expert batch sizes**: Reduces memory per device
- **Selective precision**: Experts in bfloat16, router in full precision for stability
- **4x pretraining speedup** over T5-XXL at equivalent quality

## Scale

1.6T total parameters across 2,048 experts, with each token activating ~1B parameters.

## Impact

Proved MoE could achieve enormous scale while maintaining training stability, directly inspiring [[entities/mixtral]], DeepSeek, and the 2025 generation of frontier MoE models.

## Mentioned In

- [[sources/huggingface-mixture-of-experts]] — detailed architecture and training analysis
