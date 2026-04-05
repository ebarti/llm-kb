---
title: "Chinchilla Scaling Laws"
type: concept
sources: ["[[sources/chinchilla-scaling-laws-explained]]", "[[sources/mlops-pretraining-pipeline]]"]
related: ["[[concepts/compute-optimal-training]]", "[[concepts/llm-pretraining]]", "[[concepts/llm-training-costs]]"]
last_compiled: 2026-04-05
summary: "DeepMind's 2022 finding that compute-optimal LLM training requires ~20 tokens per parameter — overturning GPT-3-era wisdom of scaling parameters over data. Post-Chinchilla, the industry shifted further to overtrained small models (Llama 3: 1,875:1) for inference efficiency."
---

## Overview

The Chinchilla scaling laws, published by DeepMind (Hoffmann et al., 2022) in the paper "Training Compute-Optimal Large Language Models," established that for a given compute budget, model size and training data should be scaled equally. The key finding: **~20 tokens per parameter** is the compute-optimal ratio.

This overturned the earlier Kaplan scaling laws (OpenAI, 2020) which suggested ~1.7 tokens per parameter — meaning most existing models were massively undertrained on data relative to their size.

## The Core Result

For compute-optimal training:
- Both parameters (N) and training tokens (D) scale with the cube root of the compute budget (C)
- N ~ C^0.5 and D ~ C^0.5 (approximately)
- For every doubling of model size, training tokens should also double
- Optimal ratio: **D/N ~ 20**

## Impact: Chinchilla vs. the Field

The 70B-parameter Chinchilla model, trained on 1.4T tokens, matched or outperformed:
- Gopher (280B parameters) — 4x larger
- GPT-3 (175B parameters) — 2.5x larger
- Megatron-Turing NLG (530B parameters) — 7.5x larger

All using the same compute budget. The conclusion: the field had been spending compute on parameters when it should have been spending it on data.

## Evolution of Scaling Ratios

| Model/Study | Year | Ratio (tokens/param) | Notes |
|------------|------|---------------------|-------|
| GPT-3 (Kaplan) | 2020 | 1.7:1 | Original scaling law |
| Chinchilla | 2022 | 20:1 | Compute-optimal |
| DeepSeek | 2024 | 30:1 | Quality-adjusted |
| Mosaic | 2023 | 190:1 | Inference-cost-aware |
| Tsinghua | 2024 | 192:1 | Small model regime |
| Llama 3 | 2024 | 1,875:1 | Inference-optimized |
| Qwen3-0.6B | 2025 | 60,000:1 | Extreme overtraining |

## Beyond Compute-Optimal: Inference-Optimal

The industry quickly moved beyond Chinchilla's compute-optimal point. The insight: training is a one-time cost, but inference runs continuously. Training a smaller model on far more data than Chinchilla prescribes ("overtraining") produces a model that is:
- Cheaper to serve (fewer parameters = less inference compute)
- Competitive with larger models (compensated by more training data)
- More practical for deployment at scale

This explains why Llama 3 (8B) trains on 15T tokens despite Chinchilla prescribing only 160B.

## Sources

- [[sources/chinchilla-scaling-laws-explained]] — plain-English explanation with evolution of ratios
- [[sources/mlops-pretraining-pipeline]] — Chinchilla's impact on the field

## Related Concepts

- [[concepts/compute-optimal-training]] — the broader principle
- [[concepts/llm-pretraining]] — the process these laws govern
- [[concepts/llm-training-costs]] — economic implications of scaling choices
