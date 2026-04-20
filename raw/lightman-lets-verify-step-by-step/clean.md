---
title: "Let's Verify Step by Step"
source: "https://arxiv.org/abs/2305.20050"
author: "Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe"
date_published: 2023-05-31
date_ingested: 2026-04-05
tags: [process-reward-models, verification, math, alignment, supervision]
type: paper
status: raw
discovered_via: search
---

# Let's Verify Step by Step

OpenAI, 2023

## Key Findings

1. **Process supervision significantly outperforms outcome supervision** for training models to solve problems from the challenging MATH dataset.
2. A process-supervised model solves 78% of problems from a representative subset of the MATH test set.
3. Process supervision is more aligned with human reasoning -- it specifies the exact location of errors.
4. Active learning enhances the effectiveness of process supervision.

## Process vs. Outcome Supervision

- **Outcome supervision (ORM)**: Reward model receives feedback only on the final answer (correct/incorrect).
- **Process supervision (PRM)**: Reward model receives feedback for each step in the chain-of-thought. Each step is labeled as helpful (+) or unhelpful (-).

Process supervision provides more precise feedback by specifying exactly where errors occur. It also more directly rewards models for following human-endorsed reasoning chains.

## PRM800K Dataset

- Released a dataset containing 800,000 step-level human feedback labels.
- Labels cover reasoning steps in mathematical problem-solving.
- Enables training and evaluation of process reward models.

## AI Alignment Implications

The paper explicitly connects process supervision to AI alignment:
- Process supervision is easier for humans to interpret and audit.
- It rewards models for following endorsed reasoning processes, not just reaching correct answers.
- A model that gets the right answer via flawed reasoning is penalized under process supervision but rewarded under outcome supervision.
- This makes process supervision a stronger foundation for building trustworthy AI systems.

## Significance

This paper established process reward models (PRMs) as a key building block for reasoning systems. PRMs became central to later test-time compute scaling methods (Snell et al., 2024) and are believed to be a core component of OpenAI's o1 and o3 reasoning models.
