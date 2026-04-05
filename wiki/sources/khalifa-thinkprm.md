---
title: "Source: Process Reward Models That Think (ThinkPRM)"
type: source-summary
source: "[[raw/khalifa-thinkprm-process-reward-models-that-think]]"
related: ["[[concepts/process-reward-models]]", "[[concepts/test-time-compute]]", "[[concepts/reasoning-models]]"]
tags: [process-reward-models, verification, data-efficiency, test-time-compute]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "ThinkPRM: generative process verifier that generates verification CoT, requiring only 1% of PRM800K labels while outperforming discriminative PRMs by 8% -- extending the 'thinking' paradigm to verification itself."
---

## Key Points

- Generative approach: PRMs that generate verification chain-of-thought instead of discriminative scoring.
- Requires only 1% of process labels in PRM800K.
- Outperforms discriminative verifiers trained on full PRM800K by 8% on GPQA-Diamond.
- Outperforms LLM-as-a-Judge by 7.2% under equivalent token budgets.
- Verification compute itself scales: spending more tokens on verification improves results.
- Strong out-of-domain generalization.

## Detailed Summary

Khalifa et al. (2025) show that the "thinking" paradigm transforming generation models also transforms verification models. ThinkPRM is a [[concepts/process-reward-models|process reward model]] that verifies reasoning by generating its own chain-of-thought about each step's correctness, rather than outputting a simple score.

This approach is dramatically more data-efficient: 1% of PRM800K labels suffice, because the model's reasoning capabilities do the heavy lifting. The verification itself benefits from [[concepts/test-time-compute]] scaling -- spending more tokens on the verification CoT yields better verification quality.

This creates an interesting recursive structure: reasoning models benefit from verification, and verification benefits from reasoning. Both can scale independently at test time.

## Metadata

- **Author**: Muhammad Khalifa, Rishabh Agarwal et al.
- **Date Published**: 2025-04-23
- **Format**: paper
- **URL**: https://arxiv.org/abs/2504.16828
