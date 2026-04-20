---
title: "Process Reward Models That Think (ThinkPRM)"
source: "https://arxiv.org/abs/2504.16828"
author: "Muhammad Khalifa, Rishabh Agarwal, Lajanugen Logeswaran, Jaekyeom Kim, Hao Peng, Moontae Lee, Honglak Lee, Lu Wang"
date_published: 2025-04-23
date_ingested: 2026-04-05
tags: [process-reward-models, test-time-compute, verification, reasoning, data-efficiency]
type: paper
status: raw
discovered_via: search
---

# ThinkPRM: Process Reward Models That Think

## Core Innovation
ThinkPRM is a generative approach to process reward modeling. Instead of discriminative classifiers that score steps, it generates verification chains-of-thought (CoT) to evaluate solution steps. It is a long CoT verifier fine-tuned on orders of magnitude fewer process labels than discriminative PRMs.

## Method
1. Train a model to generate verification reasoning chains that examine each step.
2. Leverages inherent reasoning capabilities of extended reasoning models.
3. Requires only 1% of process labels in PRM800K for training.

## Performance Results
- Outperforms LLM-as-a-Judge and discriminative verifiers using only 1% of PRM800K labels.
- Surpasses discriminative verifiers trained on full PRM800K by 8% on GPQA-Diamond.
- Improves LiveCodeBench performance by 4.5%.
- Outperforms LLM-as-a-Judge by 7.2% under equivalent token budgets on ProcessBench.
- Strong out-of-domain generalization.

## Implications for Test-Time Scaling
- Generative long-CoT PRMs can scale test-time compute for verification while requiring minimal supervision for training.
- More practical pathway for deploying advanced verification systems.
- Verification compute itself can be scaled (spending more tokens on verification improves results).

## Significance
Demonstrates that the "thinking" paradigm extends to verification models, not just generation models. Opens a path to highly data-efficient process supervision.
