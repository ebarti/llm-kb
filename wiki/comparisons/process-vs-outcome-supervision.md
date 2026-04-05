---
title: "Process Supervision vs Outcome Supervision"
type: comparison
subjects: ["[[concepts/process-reward-models]]", "[[concepts/llm-reasoning]]"]
sources: ["[[sources/lightman-lets-verify-step-by-step]]"]
last_compiled: 2026-04-05
summary: "Comparison of two approaches to training reasoning verifiers: process supervision (step-level feedback, 78% on MATH, better alignment) vs. outcome supervision (answer-only feedback, cheaper to label but weaker performance and less interpretable)."
---

## Overview

When training models to solve reasoning problems, there are two fundamental approaches to providing feedback: evaluating only the final answer (outcome supervision) or evaluating each intermediate reasoning step (process supervision). [[sources/lightman-lets-verify-step-by-step|Lightman et al. (2023)]] at OpenAI demonstrated that process supervision significantly outperforms outcome supervision.

## Comparison Table

| Dimension | Outcome Supervision (ORM) | Process Supervision (PRM) |
|-----------|--------------------------|--------------------------|
| **Feedback level** | Final answer only | Each reasoning step |
| **Label format** | (problem, answer) -> correct/incorrect | (problem, step_1, step_2, ...) -> +/- per step |
| **Error localization** | Cannot identify where reasoning failed | Pinpoints exact error step |
| **MATH benchmark** | Lower | **78%** (significantly better) |
| **Labeling cost** | Cheap (just check final answer) | Expensive (annotate each step) |
| **Dataset** | -- | PRM800K (800K step-level labels) |
| **Interpretability** | Low | High |
| **Alignment benefit** | Rewards any path to correct answer | Rewards endorsed reasoning chains |
| **Failure mode** | Rewards correct answers from flawed reasoning | Penalizes flawed reasoning even with correct answers |
| **Scalability** | Easier to scale (automated checking) | Harder to scale (requires human annotation) |

## Why Process Supervision Wins

1. **Precision**: Step-level feedback tells the model exactly where it went wrong, enabling targeted improvement.
2. **Alignment**: A model that gets the right answer via incorrect reasoning is dangerous. Process supervision catches this.
3. **Composability**: Step-level verification enables [[concepts/test-time-compute|test-time search]] -- evaluate partial solutions and prune bad branches.
4. **Generalization**: Models trained with process supervision learn better reasoning strategies, not just answer shortcuts.

## The Alignment Argument

Process supervision is particularly important for AI safety:
- **Outcome-supervised models** learn to reach correct answers by any means, including shortcuts and flawed reasoning that happen to work.
- **Process-supervised models** learn to reason correctly step by step, making their behavior more predictable and auditable.
- As reasoning tasks get harder and human verification of final answers becomes difficult, the reasoning process itself becomes the only auditable signal.

## Recent Developments

- **Automated process labels**: Math-Shepherd (2023) generates step-level labels without human annotators.
- **PRMs That Think** (2025): Verbalized PRMs that generate verification CoTs, needing orders of magnitude fewer labels.
- **Formally verified data**: Using proof assistants to generate provably correct process labels.

## Sources

- [[sources/lightman-lets-verify-step-by-step]] -- foundational comparison of process vs. outcome supervision
