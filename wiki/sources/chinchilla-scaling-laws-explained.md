---
title: "Source: Chinchilla Data-Optimal Scaling Laws in Plain English"
type: source-summary
source: "[[raw/chinchilla-scaling-laws-explained]]"
related: ["[[concepts/chinchilla-scaling-laws]]", "[[concepts/compute-optimal-training]]", "[[concepts/llm-pretraining]]"]
last_compiled: 2026-04-05
summary: "Plain-English explanation of Chinchilla scaling laws: 20 tokens per parameter optimal ratio (vs GPT-3's 1.7:1), subsequent evolution to extreme ratios (Llama 3 at 1,875:1, Qwen3 at 60,000:1), and implications for compute-optimal vs inference-optimal training."
---

## Key Points

- Chinchilla (2022) established 20 tokens per parameter as compute-optimal ratio
- GPT-3 used only 1.7 tokens per parameter — 11x undertrained by Chinchilla standards
- A 175B model should optimally train on 3.5T tokens (GPT-3 used only 300B)
- Both parameters and tokens scale with cube root of compute budget
- Post-Chinchilla: industry shifted to massively overtrained small models for inference efficiency

## Detailed Summary

The [[concepts/chinchilla-scaling-laws]] fundamentally changed how the industry thinks about scaling. Before Chinchilla, the prevailing wisdom (from Kaplan/OpenAI, 2020) was to scale model size aggressively with relatively little data. Chinchilla showed this was wrong: for every doubling of model size, training tokens should also double.

**The key ratio**: 20 tokens per parameter. A 70B model should train on 1.4T tokens. This was validated by the Chinchilla model itself — 70B parameters matching or beating Gopher (280B), GPT-3 (175B), and Megatron-Turing NLG (530B) using the same compute budget.

**Post-Chinchilla evolution** moved beyond compute-optimal to inference-optimal:
- Mosaic (2023): 190:1 ratio, factoring in inference costs
- DeepSeek (2024): 30:1, emphasizing data quality
- Llama 3 (2024): 1,875:1 — massively overtrained for inference efficiency
- Qwen3-0.6B (2025): 60,000:1 — extreme overtraining for compact models

The shift reflects economic reality: training is a one-time cost, but inference runs continuously. Overtraining smaller models relative to Chinchilla optimum can be more cost-effective over the model's lifetime.

## Related Concepts

- [[concepts/chinchilla-scaling-laws]] — the core scaling law
- [[concepts/compute-optimal-training]] — balancing parameters and data
- [[concepts/llm-pretraining]] — the training process these laws govern
