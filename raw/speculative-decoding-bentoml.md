---
title: "Speculative Decoding for LLM Inference"
source: "https://bentoml.com/llm/inference-optimization/speculative-decoding"
author: "BentoML"
date_published: 2024-09-01
date_ingested: 2026-04-05
tags: [speculative-decoding, inference-optimization, draft-model, EAGLE, LLM-serving]
type: article
status: raw
discovered_via: search
---

# Speculative Decoding for LLM Inference

## Core Algorithm

Speculative decoding operates through a draft-then-verify loop:

1. A smaller draft model proposes K tokens following the input sequence
2. The target (larger) model verifies these K tokens in parallel
3. The target accepts the longest prefix matching its predictions
4. If h tokens are accepted, the target generates token (h+1) independently
5. The process repeats with the extended sequence

This mechanism guarantees output quality matches the target model alone, with no degradation. The algorithm exploits the asymmetry between autoregressive generation (sequential, slow) and verification (parallel, fast).

## Key Performance Metrics

**Acceptance Rate (alpha)**: Probability the target accepts draft tokens. Higher alpha directly correlates with speedup.

**Speculative Token Count (gamma)**: Configurable number of tokens drafted per step.

**Acceptance Length (tau)**: Average tokens accepted per round: tau = (1 - alpha^(gamma+1)) / (1 - alpha)

## Performance Characteristics

- At alpha >= 0.6 and gamma >= 5: 2-3x speedups over baseline decoding
- TPOT (Time Per Output Token) improved roughly 2x
- Performance plateaus under high concurrency (coordination overhead)
- Multi-GPU setups (TP > 1) show better scaling than single-GPU

## Notable Variants

### EAGLE (Extrapolation Algorithm for Greater Language-Model Efficiency)
Trains a lightweight draft head (1-2 transformer layers) that plugs directly into the target model, reusing internal feature maps. Under 5% parameter overhead for 70B models.

### P-EAGLE (Parallel EAGLE)
Removes sequential bottleneck from standard EAGLE by generating all K draft tokens in a single forward pass. Up to 1.69x speedup over vanilla EAGLE-3 on real workloads.

### Medusa
Adds multiple prediction heads to the target model itself, generating multiple candidate tokens in parallel without a separate draft model.

## Practical Considerations

- Memory overhead: Both models must load into GPU memory
- Wasted computation: Low acceptance rates waste GPU cycles on rejected tokens
- Draft model tuning: Domain-specific fine-tuning improves acceptance rates
- Implementation frameworks: vLLM and SGLang provide built-in support
