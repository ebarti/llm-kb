---
title: "Speculative Decoding — LLM Inference Handbook"
source: "https://bentoml.com/llm/inference-optimization/speculative-decoding"
author: "BentoML"
date_published: 2025-06-01
date_ingested: 2026-04-05
tags: [speculative-decoding, inference-optimization, draft-model, latency]
type: article
status: raw
discovered_via: search
---

# Speculative Decoding — LLM Inference Handbook

## Core Mechanism
Speculative decoding pairs two models in a draft-then-verify pattern:
- Draft model: A smaller, faster model proposes multiple tokens ahead
- Target model: A larger model verifies proposed tokens in parallel

This draft-then-verify pattern guarantees the final output matches exactly what the original target model would have produced without sacrificing quality. The process can achieve up to 3x faster LLM inference.

## How It Works
The algorithm operates iteratively:
1. Draft model predicts K tokens following the input
2. Target model verifies these K tokens in parallel
3. Target model accepts the longest matching prefix
4. If h tokens are accepted, the target generates the (h+1)th token
5. Process repeats with extended sequence

## Key Performance Metrics

### Acceptance Rate (α)
The probability of accepting draft tokens by the target model. Higher α means fewer target model forward passes, reducing latency and improving GPU utilization.

### Speculative Token Count (γ)
Configurable number of tokens the draft model proposes per step.

### Acceptance Length (τ)
Average tokens accepted per decoding round.

## Performance Results
- At α ≥ 0.6 and γ ≥ 5, speculative decoding achieved 2-3x speedups
- With tensor parallelism (TP=2), performance improved significantly over TP=1
- Universal vocabulary support (ICML 2025): up to 2.8x speedup over standard autoregressive decoding

## Deployment Considerations
- Memory Overhead: Both models must load into GPU memory simultaneously, potentially constraining batch sizes on single-GPU setups
- Acceptance Rate Sensitivity: When target model rejects too many draft tokens, GPU still spends time generating and verifying without performance gains
- Draft Model Selection: How closely draft model distribution matches target determines acceptance rate. Fine-tuning draft models on domain-specific data improves alignment

## Variants
- Mirror Speculative Decoding (Apple): breaks latency-acceptance tradeoff with parallel rollouts across heterogeneous accelerators (GPU and NPU)
- Online Speculative Decoding (OSD): continuously adapts draft models to evolving query distribution during serving
- EAGLE and Medusa: advanced approaches for self-speculative decoding
