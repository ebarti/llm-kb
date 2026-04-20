---
title: "Test-Time Learning for Large Language Models (TLM)"
source: "https://arxiv.org/abs/2505.20633"
author: "Jinwu Hu, Zhitian Zhang, Guohao Chen, Xutao Wen, Chao Shuai, Wei Luo, Bin Xiao, Yuanqing Li, Mingkui Tan"
date_published: 2025-05-27
date_ingested: 2026-04-05
tags: [test-time-training, domain-adaptation, inference, self-supervised, LoRA]
type: paper
status: raw
discovered_via: search
---

# Test-Time Learning for Large Language Models (TLM)

ICML 2025 paper on domain adaptation at test time without labeled data.

## Core Method
TLM dynamically adapts LLMs to target domains using only unlabeled test data during testing. Three components:

1. **Input Perplexity Minimization**: More accurate predictions from LLMs can be achieved by minimizing the input perplexity of unlabeled test data. Self-supervised enhancement.

2. **Sample Efficiency Strategy**: Identifies high-perplexity samples as particularly valuable for optimization, selectively emphasizing them during adaptation.

3. **LoRA-Based Stability**: Uses Low-Rank Adaptation instead of full-parameter optimization to prevent catastrophic forgetting while preserving original knowledge.

## Results
- At least 20% improvement compared to original LLMs on domain knowledge adaptation (AdaptEval benchmark).
- Works with only unlabeled test data.
- Maintains stability through LoRA-based updates.

## Significance
Addresses critical limitation in LLMs: handling distribution shifts and domain-specific generalization. Test-time training (TTT) is distinct from test-time scaling (TTS) -- it modifies model weights rather than just spending more inference compute. TLM bridges these approaches by showing that lightweight weight updates at test time can substantially improve domain performance.
