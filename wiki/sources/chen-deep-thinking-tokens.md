---
title: "Source: Think Deep, Not Just Long -- Measuring LLM Reasoning via Deep-Thinking Tokens"
type: source-summary
source: "[[raw/chen-deep-thinking-tokens]]"
related: ["[[concepts/test-time-compute]]", "[[concepts/reasoning-tokens]]", "[[concepts/adaptive-compute-allocation]]"]
tags: [reasoning-tokens, overthinking, evaluation, test-time-compute]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Introduces 'deep-thinking tokens' (where predictions undergo significant revisions in deeper layers) as a superior measure of reasoning effort, showing token count is an unreliable proxy for reasoning quality."
---

## Key Points

- Deep-thinking tokens: tokens where internal predictions undergo significant revisions in deeper model layers.
- Raw token count is unreliable -- longer responses may signal overthinking, not better reasoning.
- Deep-thinking ratio correlates robustly with accuracy, outperforming length-based and confidence-based alternatives.
- Think@n: test-time scaling strategy prioritizing high deep-thinking ratio samples for cost-efficient inference.
- Tested across AIME 24/25, HMMT 25, GPQA-diamond on GPT-OSS, DeepSeek-R1, Qwen3.

## Detailed Summary

Chen et al. (2026) challenge the "more tokens = better reasoning" assumption underpinning much of [[concepts/test-time-compute]] research. They discover that what matters is not how many tokens a model generates, but how deeply it "thinks" on each token -- measured by the magnitude of prediction revisions across transformer layers.

This has immediate practical value: the Think@n strategy achieves comparable accuracy to standard self-consistency while reducing compute by rejecting samples with low deep-thinking ratios early. This represents a more principled form of [[concepts/adaptive-compute-allocation]] -- allocating compute based on reasoning quality signals rather than just problem difficulty.

The finding that more tokens can hurt (via "overthinking") connects to [[sources/iacobacci-thinking-budget-not-enough]], which independently found that increasing thinking budgets shows diminishing returns.

## Metadata

- **Author**: Wei-Lin Chen et al.
- **Date Published**: 2026-02-19
- **Format**: paper
- **URL**: https://arxiv.org/abs/2602.13517
