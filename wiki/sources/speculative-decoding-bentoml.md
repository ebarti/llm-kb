---
title: "Source: Speculative Decoding for LLM Inference"
type: source-summary
source: "[[raw/speculative-decoding-bentoml]]"
related: ["[[concepts/speculative-decoding]]", "[[concepts/kv-cache]]", "[[concepts/transformer-architecture]]"]
last_compiled: 2026-04-05
summary: "Technical overview of speculative decoding: draft-then-verify algorithm, acceptance rate metrics, EAGLE/P-EAGLE/Medusa variants, 2-3x speedups at alpha >= 0.6, vLLM/SGLang implementation support."
---

## Key Points

- Draft model proposes K tokens; target model verifies in parallel — output quality guaranteed identical
- Acceptance rate (alpha) is the critical metric; at alpha >= 0.6 and gamma >= 5: 2-3x speedup
- EAGLE: lightweight draft head (1-2 transformer layers) reusing target model features; <5% param overhead for 70B
- P-EAGLE: parallel draft token generation in single forward pass; 1.69x over EAGLE-3
- Medusa: multiple prediction heads on target model itself (no separate draft model)
- Memory overhead: both draft and target must fit in GPU memory
- vLLM and SGLang provide built-in support

## Detailed Summary

[[concepts/speculative-decoding]] exploits a key asymmetry in autoregressive LLMs: generating one token requires a full forward pass, but verifying K tokens can happen in a single forward pass. A small, fast draft model proposes candidate token sequences, then the large target model verifies them all at once.

The algorithm is mathematically guaranteed to produce identical output to the target model alone. If the target rejects a draft token at position h, it generates its own token for that position and the draft restarts from there. The expected speedup depends on the acceptance rate alpha: higher alignment between draft and target means more tokens accepted per verification pass.

EAGLE represents the state of the art: instead of a separate draft model, it trains a small head (1-2 transformer layers) that plugs into the target model and reuses its internal feature maps. This minimizes both memory overhead and prediction mismatch. P-EAGLE further optimizes by generating all K draft tokens in parallel rather than autoregressively.

## Related Concepts

- [[concepts/speculative-decoding]] — the optimization technique detailed here
- [[concepts/kv-cache]] — both techniques address inference bottlenecks
- [[concepts/transformer-architecture]] — the architecture being optimized
