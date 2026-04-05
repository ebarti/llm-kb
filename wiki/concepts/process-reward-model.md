---
title: "Process Reward Model (PRM)"
type: concept
sources: ["[[sources/wolfe-reward-models-llm]]"]
related: ["[[concepts/reward-model]]", "[[concepts/reward-hacking]]", "[[concepts/rlhf]]", "[[concepts/scalable-oversight]]"]
last_compiled: 2026-04-05
summary: "A reward model variant that scores each reasoning step individually rather than only the final output -- providing finer-grained feedback that is harder to hack but requires expensive step-level supervision data."
---

## Overview

Process Reward Models (PRMs) extend the standard [[concepts/reward-model]] by providing scores **after each reasoning step** rather than only evaluating the final output. This is particularly important for mathematical reasoning and code generation, where a model might arrive at the correct answer via flawed reasoning (or vice versa).

## How They Differ

| Aspect | Outcome RM (ORM) | Process RM (PRM) |
|--------|------------------|------------------|
| Granularity | Scores final output | Scores each step |
| Supervision | Outcome-level labels | Step-level labels |
| Data cost | Lower | Much higher |
| Hack resistance | Lower (can game the final answer) | Higher (must be correct at every step) |
| Best for | General alignment | Reasoning, math, code |

## Advantages

- **Harder to hack**: The model cannot take shortcuts or fabricate intermediate steps
- **Better debugging**: Errors can be localized to specific reasoning steps
- **Training signal density**: More reward signal per example (one score per step vs. one per sequence)

## Challenges

- **Expensive supervision**: Step-level annotations require expert annotators who can evaluate intermediate reasoning
- **Ambiguous step boundaries**: Deciding where one "step" ends and another begins is non-trivial
- **Limited applicability**: Most useful for structured reasoning tasks, less clear benefit for open-ended generation

## Sources
- [[sources/wolfe-reward-models-llm]] -- PRM as a reward model variant

## Related Concepts
- [[concepts/reward-model]] -- the broader category PRMs belong to
- [[concepts/reward-hacking]] -- PRMs are more resistant to hacking
- [[concepts/scalable-oversight]] -- PRMs as finer-grained oversight
