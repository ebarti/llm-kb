---
title: "Source: Let's Verify Step by Step"
type: source-summary
source: "[[raw/lightman-lets-verify-step-by-step]]"
related: ["[[concepts/process-reward-models]]", "[[concepts/llm-reasoning]]", "[[concepts/test-time-compute]]", "[[entities/openai]]"]
last_compiled: 2026-04-05
summary: "OpenAI 2023 paper establishing that process supervision (step-level feedback) significantly outperforms outcome supervision (answer-only feedback) for mathematical reasoning, with alignment benefits. Released PRM800K dataset."
---

## Key Points

- Process supervision (feedback per reasoning step) significantly outperforms outcome supervision (feedback on final answer only).
- Process-supervised model achieved 78% on representative MATH test subset.
- Released PRM800K: 800,000 step-level human feedback labels.
- Process supervision aligns better with human reasoning -- specifies exact error locations.

## Detailed Summary

Lightman et al. (2023) at OpenAI compared two approaches to training reward models for mathematical reasoning:

**Outcome Reward Models (ORMs)**: Trained on (problem, solution, correct/incorrect) triples. Can only judge the final answer. A model that gets the right answer via flawed reasoning is rewarded.

**Process Reward Models (PRMs)**: Trained on step-level labels. Each reasoning step is marked as helpful (+) or unhelpful (-). The PRM can identify exactly where reasoning goes wrong.

The PRM approach won convincingly on the MATH benchmark, establishing that granular feedback on reasoning quality produces better reasoners than simply rewarding correct answers. The paper makes an explicit connection to AI alignment: process supervision rewards endorsed reasoning chains, not just correct outputs, making the model's reasoning more interpretable and trustworthy.

The PRM800K dataset (800K step-level labels) became a crucial resource for subsequent research on [[concepts/test-time-compute|test-time compute scaling]] and [[concepts/reasoning-models|reasoning model]] training.

## Related Concepts

- [[concepts/process-reward-models]] -- the core contribution
- [[concepts/test-time-compute]] -- PRMs are central to compute-optimal test-time scaling
- [[concepts/reasoning-models]] -- PRMs are believed to be a key component of o1/o3
- [[concepts/mathematical-reasoning-llm]] -- the domain of evaluation
