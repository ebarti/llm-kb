---
title: "Source: Speculative Decoding — LLM Inference Handbook"
type: source-summary
source: "[[raw/bentoml-speculative-decoding]]"
related: ["[[concepts/speculative-decoding]]", "[[concepts/llm-inference-optimization]]", "[[entities/bentoml]]"]
last_compiled: 2026-04-05
summary: "BentoML handbook chapter: speculative decoding achieves 2-3x speedup by pairing a fast draft model with a target verifier, with practical guidance on acceptance rates, memory tradeoffs, and deployment."
---

## Key Points
- Draft-then-verify pattern guarantees output matches target model exactly — no quality loss
- At acceptance rate ≥ 0.6 and γ ≥ 5 speculative tokens, achieves 2-3x speedups
- Both models must fit in GPU memory simultaneously — constrains batch size on single-GPU
- Fine-tuning draft models on domain-specific data improves acceptance rates
- Variants: Mirror-SD (Apple, heterogeneous accelerators), OSD (adaptive draft models), EAGLE, Medusa

## Detailed Summary

BentoML's inference handbook provides a practical deep-dive into [[concepts/speculative-decoding|speculative decoding]], the technique of pairing a small fast "draft" model with a large "target" model. The draft model proposes K tokens ahead, and the target model verifies them in a single parallel forward pass. Accepted tokens bypass the slow autoregressive loop; rejected tokens trigger regeneration from the target.

Three metrics govern effectiveness: acceptance rate (α, how often draft tokens are accepted), speculative token count (γ, how many tokens the draft proposes), and acceptance length (τ, average tokens accepted per round). The sweet spot is α ≥ 0.6 with γ ≥ 5, delivering 2-3x speedups. With tensor parallelism across multiple GPUs, performance improves further.

Key deployment considerations include memory overhead (both models must load simultaneously), acceptance rate sensitivity (low α wastes GPU cycles on rejected drafts), and draft model selection (distribution alignment with target is critical).

## Related Concepts
- [[concepts/speculative-decoding]] — the core technique
- [[concepts/llm-inference-optimization]] — broader optimization landscape
- [[concepts/kv-cache]] — speculative decoding interacts with KV cache management
