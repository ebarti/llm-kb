---
title: "Source: Comparing 2025's Leading MoE Models"
type: source-summary
source: "[[raw/moe-models-comparison-2025]]"
related: ["[[concepts/mixture-of-experts]]", "[[entities/deepseek]]", "[[entities/llama]]", "[[entities/qwen]]"]
last_compiled: 2026-04-05
summary: "Comparison of 7 frontier MoE models (2025): DeepSeek-R1 (671B/37B), Llama 4 Maverick (400B/17B), Qwen3-235B (235B/22B), GPT-OSS (117B/5.1B) — routing strategies, quantization, and the shared vs. routed expert divide."
---

## Key Points

- All frontier models in 2025 use MoE; trend accelerated after DeepSeek R1 (Jan 2025)
- DeepSeek-R1: 671B total / 37B active, 256 experts, 9 active (1 shared)
- Llama 4 Maverick: 400B / 17B active, 128 experts, 1M context
- Llama 4 Scout: 109B / 17B active, 16 experts, 10M context
- Qwen3-235B: 235B / 22B active, 128 experts, top-8 routing
- Two routing strategies: shared+routed experts (DeepSeek, Llama) vs top-k only (GPT-OSS, Qwen)
- Quantization enables deployment: FP4, FP8, MXFP4, even 1.78-bit for DeepSeek

## Detailed Summary

This Friendli AI comparison demonstrates that [[concepts/mixture-of-experts]] has become the default architecture for frontier LLMs by 2025. The key design choice is between shared and routed expert strategies: DeepSeek and Llama 4 use a shared expert that processes every token (providing stable generalization) plus routed experts for specialization, while GPT-OSS and Qwen3 use pure top-k routing for maximum expert specialization.

The activation ratios vary widely: GPT-OSS-120B activates only 4.3% of parameters per token (5.1B of 117B), while Qwen3-235B activates 9.4% (22B of 235B). This flexibility in the capacity-vs-compute tradeoff is MoE's primary advantage.

Aggressive quantization (down to 1.78-bit for DeepSeek) makes these massive models deployable on standard hardware, trading minimal accuracy for dramatic memory savings.

## Related Concepts

- [[concepts/mixture-of-experts]] — the architecture all models use
- [[concepts/scaling-laws]] — MoE as a path to scale beyond Chinchilla
- [[concepts/transformer-architecture]] — the base architecture
