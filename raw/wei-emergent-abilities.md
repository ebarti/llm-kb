---
title: "Emergent Abilities of Large Language Models"
source: "https://arxiv.org/abs/2206.07682"
author: "Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, Ed H. Chi, Tatsunori Hashimoto, Oriol Vinyals, Percy Liang, Jeff Dean, William Fedus"
date_published: 2022-06-15
date_ingested: 2026-04-05
tags: [emergent-abilities, scaling, capabilities, unpredictability]
type: paper
status: raw
discovered_via: search
---

# Emergent Abilities of Large Language Models

TMLR, 2022

## Definition

An ability is emergent if it is not present in smaller models but is present in larger models. Emergent abilities cannot be predicted simply by extrapolating the performance of smaller models.

## Key Characteristics

- Performance is near-random until a certain critical threshold of scale is reached.
- After the threshold, performance increases to substantially above random -- often dramatically.
- The threshold scale varies by task and is not predictable in advance.
- As models continue to scale, additional emergent abilities may appear.

## Examples

- **Chain-of-thought prompting**: Performs worse than direct answering until ~10^22 FLOPs, then substantially better.
- **In-context learning**: The ability to learn from examples in the prompt.
- **Multi-step arithmetic**: Appears at scale.
- **Word unscrambling, code generation, etc.**: Various tasks show phase transitions.

## The "Mirage" Debate

Schaeffer et al. (2023) argued that emergent abilities may be a measurement artifact:
- Nonlinear metrics (like exact-match accuracy) produce apparent emergence.
- Linear metrics (like token-level accuracy) show smooth, predictable improvements.
- The implication: emergence may be about how we measure, not what the model can do.

Counter-argument: Even if the metric explanation is partially correct, the practical reality remains that certain capabilities only become useful above a certain scale threshold, regardless of whether the underlying improvement is smooth or discontinuous.

## Policy Implications

- Emergence has attracted congressional attention and shaped AI governance debates.
- Unpredictable capabilities raise safety concerns: "we are better able to make models safe when we know what capabilities they possess."
- The difficulty of predicting what abilities will emerge makes it harder to proactively address risks.

## Significance

This paper crystallized one of the most important phenomena in LLM research -- the idea that scale doesn't just make models better at existing tasks but can unlock qualitatively new capabilities. Whether or not "emergence" is the right framing, the practical reality of phase transitions in capability remains a central concern for AI safety and development.
