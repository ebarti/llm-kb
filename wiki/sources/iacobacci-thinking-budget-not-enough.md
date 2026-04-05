---
title: "Source: Increasing the Thinking Budget is Not All You Need"
type: source-summary
source: "[[raw/iacobacci-thinking-budget-not-enough]]"
related: ["[[concepts/test-time-compute]]", "[[concepts/adaptive-compute-allocation]]", "[[concepts/reasoning-tokens]]", "[[concepts/best-of-n-sampling]]"]
tags: [thinking-budget, overthinking, efficiency, test-time-compute]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Shows that simply increasing thinking budgets hits plateaus; summary-of-multiple-outputs and self-consistency (parallel strategies) outperform naive sequential budget increases, especially for weaker models."
---

## Key Points

- Simply increasing thinking budget is not the most effective use of compute.
- Performance fluctuates across budgets and shows plateau signs.
- Weaker models struggle to benefit from extended reasoning.
- Summary approach (generate multiple, consolidate) outperforms naive budget increases.
- Self-consistency (majority voting) shows competitive results.
- Ensemble methods without thinking outperform single-run with thinking.

## Detailed Summary

Iacobacci et al. (2025) provide an important corrective to the "more thinking = better" narrative in [[concepts/test-time-compute]]. Testing across model sizes, they find that the relationship between thinking budget and performance is not monotonically positive -- it plateaus and can even fluctuate.

The practical recommendation: invest in parallel strategies (generating multiple diverse outputs and consolidating) rather than simply extending sequential reasoning length. This aligns with findings from [[sources/chen-deep-thinking-tokens]] that token count is an unreliable proxy for reasoning quality, and with the broader [[concepts/adaptive-compute-allocation]] literature suggesting that how compute is distributed matters more than total amount.

The distinction between weaker and stronger models is important: larger models (Qwen3-8B) show some ability to leverage extended thinking, while smaller models struggle. This suggests thinking budget scaling requires a minimum model capability threshold.

## Metadata

- **Author**: Ignacio Iacobacci et al. (Elm Company)
- **Date Published**: 2025-12-30
- **Format**: paper
- **URL**: https://arxiv.org/abs/2512.19585
