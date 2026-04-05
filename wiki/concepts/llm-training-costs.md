---
title: "LLM Training Costs"
type: concept
sources: ["[[sources/training-costs-2026-analysis]]", "[[sources/chinchilla-scaling-laws-explained]]"]
related: ["[[concepts/llm-pretraining]]", "[[concepts/training-infrastructure]]", "[[concepts/distributed-training]]", "[[concepts/compute-optimal-training]]"]
last_compiled: 2026-04-05
summary: "Frontier LLM training costs $5M-$200M, dominated by GPU compute (70-80%). GPT-4 ~$100-150M, Gemini Ultra ~$191M, Llama 3.1 405B ~$170M. DeepSeek V3's $5.6M challenged the assumption that frontier requires $100M+."
---

## Overview

Training a frontier LLM from scratch is one of the most expensive activities in the tech industry, with costs ranging from $5M to $200M+ for a single training run. GPU compute accounts for 70-80% of total costs, making hardware selection and efficiency the primary economic lever.

## Cost by Model

| Model | Estimated Cost | Parameters | Notes |
|-------|---------------|-----------|-------|
| GPT-4 (2023) | $100-150M | ~1.8T MoE* | Stanford AI Index: ~$78M compute alone |
| Gemini Ultra (2024) | ~$191M | — | Most expensive confirmed training run |
| Llama 3.1 405B (2024) | ~$170M | 405B | Including infrastructure and personnel |
| Llama 3.1 405B (compute) | ~$25M | 405B | Compute alone on rented H100s |
| DeepSeek V3 (2025) | $5.6M | 671B MoE | Excluded infrastructure/failed runs |
| GPT-3 (2020) | ~$5-10M | 175B | Historical baseline |

*GPT-4 architecture unconfirmed.

## Cost Breakdown

| Component | Share | Example ($150M run) |
|-----------|-------|-------------------|
| GPU compute | 70-80% | $105-120M |
| Data operations | 10-15% | $15-22M |
| Engineering personnel | 15-20% | $22-30M |
| Software/tools | 5-10% | $7-15M |

## Cost by Model Size

| Parameters | GPU Requirement | Cost Range |
|-----------|----------------|-----------|
| 1B | Small cluster | $2K-$15K |
| 7B | ~16-32 GPUs | $50K-$500K |
| 70B | 256x H200 | $1.2M-$6M |
| 175B+ | 2,000+ H200 | $50M-$200M |
| 405B+ | 5,000+ B200 | $80M-$400M |

## Trends

- Hardware efficiency improvements reduced costs ~45% since 2023 (H200/B200 vs A100)
- Fine-tuning costs only 1-5% of pretraining from scratch
- The industry is bifurcating: massive frontier runs ($100M+) vs efficient approaches (DeepSeek's $5.6M)
- Inference-optimal overtraining (see [[concepts/chinchilla-scaling-laws]]) increases training cost but reduces lifetime inference cost

## The DeepSeek Challenge

DeepSeek V3's reported $5.6M cost was a watershed moment, though context matters:
- Excluded infrastructure, experimentation, and failed runs
- Used novel architectural innovations (MoE, multi-head latent attention)
- Leveraged extensive prior research (not truly "from scratch")
- Still demonstrated that algorithmic innovation can dramatically reduce costs

## Sources

- [[sources/training-costs-2026-analysis]] — comprehensive cost analysis with breakdowns
- [[sources/chinchilla-scaling-laws-explained]] — economic implications of scaling choices

## Related Concepts

- [[concepts/training-infrastructure]] — the hardware driving costs
- [[concepts/compute-optimal-training]] — how to allocate the budget
- [[concepts/distributed-training]] — infrastructure utilization
