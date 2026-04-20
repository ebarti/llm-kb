---
title: "The Rise of MoE: Comparing 2025's Leading Mixture-of-Experts AI Models"
source: "https://friendli.ai/blog/moe-models-comparison"
author: "Friendli AI"
date_published: 2025-07-01
date_ingested: 2026-04-05
tags: [MoE, mixture-of-experts, DeepSeek, Llama-4, Qwen3, model-comparison]
type: article
status: raw
discovered_via: search
---

# Comparing 2025's Leading MoE Models

## Model Specifications

| Model | Total Params | Active Params | Experts | Routing | Context |
|-------|-------------|---------------|---------|---------|---------|
| GPT-OSS-120B | 117B | 5.1B | 128 | Top-4 | - |
| GPT-OSS-20B | 21B | 3.6B | 32 | Top-4 | - |
| DeepSeek-R1-0528 | 671B | 37B | 256 | 9 active (1 shared) | - |
| Llama 4 Maverick | 400B | 17B | 128 | 2 active (1 shared) | 1M |
| Llama 4 Scout | 109B | 17B | 16 | 2 active (1 shared) | 10M |
| Qwen3-235B-A22B | 235B | 22B | 128 | Top-8 | - |
| Qwen3-30B-A3B | 30.5B | 3.3B | 128 | Top-8 | - |

## Routing Strategies

**Without Shared Experts (GPT-OSS, Qwen3):** Top-k routing where tokens route exclusively through selected experts, maximizing specialization.

**With Shared Experts (DeepSeek, Llama-4):** Combine a shared expert for all tokens plus routed experts, balancing stable generalization with token-level specialization.

## Quantization for Deployment

- GPT-OSS: MXFP4
- DeepSeek: FP4 and 1.78-bit compressed
- Llama-4: BF16 and FP8
- Qwen3: FP8

Reducing numerical precision cuts memory use and speeds up inference without major accuracy loss, making massive models deployable on standard hardware clusters.

## Key Trend

Nearly all frontier models in 2025-2026 use MoE architecture. The trend accelerated after DeepSeek R1's success in January 2025, building on DeepSeek V2.
