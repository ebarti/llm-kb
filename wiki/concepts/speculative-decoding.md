---
title: "Speculative Decoding"
type: concept
sources: ["[[sources/speculative-decoding-bentoml]]", "[[sources/bentoml-speculative-decoding]]", "[[sources/on-device-llms-2026]]"]
related: ["[[concepts/transformer-architecture]]", "[[concepts/causal-attention]]", "[[concepts/llm-inference-optimization]]", "[[concepts/kv-cache]]", "[[concepts/edge-inference]]"]
last_compiled: 2026-04-05
summary: "A latency optimization pairing a small draft model with a large target model: the draft proposes tokens, the target verifies in parallel, achieving 2-3x speedup with mathematically guaranteed output equivalence."
---

## Overview

Speculative decoding is a technique for accelerating LLM inference without sacrificing output quality. A small, fast "draft" model proposes multiple tokens ahead, and the larger "target" model verifies them in a single parallel forward pass. Because the target model has final say, the output is mathematically identical to what the target would produce alone — this is a lossless speedup.

The technique exploits a key insight: most of the time, a small model predicts the same tokens as a large model (especially for "easy" tokens like common phrases, function words, and predictable continuations). Only when the draft model diverges does the target need to regenerate, and even then it advances by at least one token.

## How It Works

1. The draft model predicts K tokens following the current sequence
2. The target model verifies all K tokens in a single parallel forward pass
3. The target accepts the longest matching prefix (h tokens)
4. The target generates the (h+1)th token (guaranteed progress)
5. Process repeats from the new position

## Key Metrics

- **Acceptance Rate (alpha)**: Probability that draft tokens match target. Higher alpha = more speedup. At alpha >= 0.6, benefits become significant.
- **Speculative Token Count (gamma)**: How many tokens the draft proposes per step. Increasing gamma helps only when acceptance rate is high.
- **Acceptance Length (tau)**: Average tokens accepted per round. Determines actual speedup.

## Performance

- Sweet spot: alpha >= 0.6, gamma >= 5 delivers **2-3x speedups**
- ICML 2025 (Intel/Weizmann): universal vocabulary support enables **up to 2.8x speedup** regardless of vocabulary differences between draft and target
- On-device: Medusa achieves **2.2-3.6x acceleration** without retraining

## Deployment Considerations

- **Memory overhead**: Both models must fit in GPU memory simultaneously. On single-GPU setups, this constrains batch size.
- **Draft model selection**: The closer the draft's distribution matches the target, the higher the acceptance rate. Domain-specific fine-tuning of the draft model improves alignment.
- **When it doesn't help**: Low acceptance rates waste GPU cycles on rejected drafts. If the domain is highly specialized or the draft model is poorly matched, benefits diminish.

## Variants

| Variant | Innovation | Source |
|---------|-----------|--------|
| Mirror-SD (Apple) | Parallel rollouts across GPU+NPU, breaks latency-acceptance tradeoff | Apple ML Research |
| Online Speculative Decoding | Continuously adapts draft model to evolving query distribution | Berkeley |
| EAGLE | Self-speculative using early exit layers | Research |
| Medusa | Multiple draft heads on the same model, no separate draft model needed | Research |

## Sources
- [[sources/bentoml-speculative-decoding]] — comprehensive technical walkthrough
- [[sources/on-device-llms-2026]] — speculative decoding for mobile inference

## Related Concepts
- [[concepts/llm-inference-optimization]] — speculative decoding as a latency technique
- [[concepts/kv-cache]] — draft and target models share KV cache infrastructure
- [[concepts/edge-inference]] — critical technique for on-device acceleration
