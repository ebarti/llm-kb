---
title: "Source: KTO - Kahneman-Tversky Optimization"
type: source-summary
source: "[[raw/argilla-kto-kahneman-tversky]]"
related: ["[[concepts/kto]]", "[[concepts/dpo]]", "[[concepts/preference-data]]", "[[entities/kahneman-tversky]]"]
last_compiled: 2026-04-05
summary: "Argilla's overview of KTO: a prospect-theory-based alignment method using binary (desirable/undesirable) signals instead of pairwise preferences, outperforming DPO on noisy real-world data and matching SFT+DPO combined on Llama models."
---

## Key Points
- KTO requires only binary feedback (desirable/undesirable), not pairwise preferences
- Based on Kahneman-Tversky prospect theory: loss aversion makes humans weight losses more than equivalent gains
- KTO alone matches SFT + DPO combined on Llama models
- Outperforms DPO on noisy, real-world datasets
- Without prior SFT, DPO models ramble and hallucinate while KTO remains stable
- Works well with imbalanced data (90% of desirable examples can be discarded)

## Detailed Summary

[[concepts/kto]] represents a fundamentally different approach to preference optimization by grounding the loss function in prospect theory rather than the Bradley-Terry model. The HALO (Human-Aware Loss functions) framework classifies alignment methods by whether they model human cognitive biases. KTO, as a HALO, matched or outperformed non-HALOs at 13B+ parameter scales.

The practical advantage is data efficiency: binary signals (thumbs up/down) are far cheaper and more abundant than pairwise preference comparisons. Even with 90% of desirable examples discarded, KTO-aligned Llama-7B outperformed DPO.

A critical finding is robustness: without prior SFT, DPO models degenerated into rambling and hallucination, while KTO maintained coherent outputs. This suggests KTO is better suited for real-world scenarios where data is noisy and prior fine-tuning may be limited.

## Related Concepts
- [[concepts/kto]] -- the central concept
- [[concepts/dpo]] -- the primary comparison point
- [[concepts/preference-data]] -- KTO's relaxed data requirements
- [[concepts/prospect-theory-in-alignment]] -- the theoretical foundation
