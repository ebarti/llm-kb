---
title: "Source: RLHF and Alternatives - Comprehensive Overview"
type: source-summary
source: "[[raw/argilla-rlhf-alternatives-overview]]"
related: ["[[concepts/rlhf]]", "[[concepts/dpo]]", "[[concepts/kto]]", "[[concepts/ipo]]", "[[concepts/orpo]]", "[[comparisons/rlhf-alternatives]]"]
last_compiled: 2026-04-05
summary: "Argilla/MantisNLP's systematic comparison of 9+ preference alignment methods (RLHF, DPO, IPO, KTO, ORPO, SPIN, CoH, RLAIF, SimPO) with data requirements, compute costs, and practical guidance on when to use each."
---

## Key Points
- Covers 9+ methods: RLHF, DPO, IPO, KTO, ORPO, SPIN, CoH, RLAIF, SimPO
- Data requirements vary wildly: RLHF needs 10K, KTO uses 600K, but SPIN works with just 1.8K
- No single method addresses all aspects effectively; each has trade-offs
- Well-curated data allows dramatic dataset size reduction without performance loss
- AI-generated preference datasets are now widely accepted practice
- ORPO combines instruction tuning and preference alignment in a single step

## Detailed Summary

This comprehensive survey maps the landscape of LLM alignment methods beyond traditional [[concepts/rlhf]]. The methods range from reward-based (RLHF) to reward-free ([[concepts/dpo]], [[concepts/kto]], [[concepts/ipo]]) to self-supervised ([[concepts/spin]]).

Key distinctions emerge around data format: RLHF and DPO require pairwise preferences, [[concepts/kto]] accepts binary signals, and SPIN auto-generates rejected responses. Compute requirements similarly vary: RLHF and SPIN are high, DPO/IPO are medium, and [[concepts/orpo]]/SimPO are low.

The most striking finding is data efficiency: SPIN achieved comparable results with 1.8K prompts versus 50K, and ORPO succeeded with just 7K instances. This suggests that data quality dominates data quantity for alignment.

## Related Concepts
- [[concepts/rlhf]] -- the baseline method all alternatives compare against
- [[concepts/dpo]] -- the most popular alternative
- [[concepts/kto]] -- binary-signal alternative based on prospect theory
- [[concepts/orpo]] -- single-step instruction tuning + alignment
- [[comparisons/rlhf-alternatives]] -- detailed comparison page
