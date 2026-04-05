---
title: "Source: Test-Time Learning for Large Language Models (TLM)"
type: source-summary
source: "[[raw/hu-test-time-learning-llm]]"
related: ["[[concepts/test-time-training]]", "[[concepts/test-time-compute]]", "[[entities/lora]]"]
tags: [test-time-training, domain-adaptation, self-supervised]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "ICML 2025 paper on TLM: domain adaptation at test time via input perplexity minimization on unlabeled data with LoRA, achieving 20%+ improvement without ground-truth labels."
---

## Key Points

- Dynamically adapts LLMs to target domains using only unlabeled test data.
- Formulates adaptation as input perplexity minimization (self-supervised).
- Uses LoRA for stability, preventing catastrophic forgetting.
- At least 20% improvement on domain knowledge adaptation.
- Distinct from test-time scaling: modifies model weights, not just inference procedure.

## Detailed Summary

Hu et al. (ICML 2025) introduce TLM, a [[concepts/test-time-training]] method that adapts LLMs at deployment time. The key insight: minimizing input perplexity on unlabeled test data serves as an effective self-supervised objective for domain adaptation.

The method identifies high-perplexity samples as most valuable for optimization, focuses adaptation on them, and uses LoRA to prevent catastrophic forgetting. This achieves 20%+ improvement on the AdaptEval benchmark without any labeled data.

TLM occupies a distinct position in the test-time landscape: [[concepts/test-time-compute]] spends more compute without changing the model, while [[concepts/test-time-training]] actually modifies model weights. TLM shows these approaches are complementary -- you can both adapt the model and scale its inference compute.

## Metadata

- **Author**: Jinwu Hu et al.
- **Date Published**: 2025-05-27 (ICML 2025)
- **Format**: paper
- **URL**: https://arxiv.org/abs/2505.20633
