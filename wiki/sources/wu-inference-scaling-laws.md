---
title: "Source: Inference Scaling Laws -- Compute-Optimal Inference for LLM Problem-Solving"
type: source-summary
source: "[[raw/wu-inference-scaling-laws]]"
related: ["[[concepts/inference-scaling-laws]]", "[[concepts/test-time-compute]]", "[[concepts/best-of-n-sampling]]", "[[concepts/scaling-laws]]"]
tags: [inference-scaling, scaling-laws, compute-optimal, test-time-compute]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "ICLR 2025 paper establishing inference scaling laws: log10(C) = 1.19*log10(N) + 2.03, showing Llemma-7B with tree search outperforms Llemma-34B -- inference compute is an independent optimizable axis."
---

## Key Points

- Published at ICLR 2025 -- the inference counterpart to Chinchilla training scaling laws.
- Establishes concrete equation: log10(C) = 1.19 * log10(N) + 2.03.
- Llemma-7B with tree search outperforms Llemma-34B across all inference strategies on MATH.
- Compute-optimal allocation is adaptive: 4x efficiency improvement over uniform best-of-N.
- Scaling solution generation matters more than scaling verification count.

## Detailed Summary

Wu et al. (ICLR 2025) provide the first rigorous formalization of [[concepts/inference-scaling-laws]]. They evaluate six inference strategies (greedy search, majority voting, [[concepts/best-of-n-sampling]], weighted voting, two tree search variants) across model sizes from 7B to 34B.

The headline result: Llemma-7B with a novel tree search consistently outperforms Llemma-34B at the same compute budget. This validates the core thesis of [[concepts/test-time-compute]] -- that inference compute is a separately optimizable dimension, not merely a consequence of model size.

The compute-optimal strategy allocates test-time compute adaptively per prompt based on difficulty, achieving 4x efficiency over uniform allocation. Interestingly, the optimal allocation favors scaling solution generation more aggressively than scaling the number of verifications -- suggesting the bottleneck is diversity of solutions, not verification quality.

## Metadata

- **Author**: Yangzhen Wu et al.
- **Date Published**: 2024-08-01 (ICLR 2025)
- **Format**: paper
- **URL**: https://arxiv.org/abs/2408.00724
