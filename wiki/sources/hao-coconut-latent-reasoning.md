---
title: "Source: COCONUT - Training LLMs to Reason in Continuous Latent Space"
type: source-summary
source: "[[raw/hao-coconut-latent-reasoning]]"
related: ["[[concepts/latent-reasoning]]", "[[concepts/test-time-compute]]", "[[concepts/chain-of-thought]]"]
tags: [latent-reasoning, efficiency, chain-of-thought, inference-scaling]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Introduces Chain of Continuous Thought (COCONUT), replacing token-level CoT with reasoning in hidden state space, enabling breadth-first search and more efficient inference -- a frontier in test-time compute efficiency."
---

## Key Points

- Replaces explicit CoT token generation with reasoning in continuous latent space.
- Uses last hidden state as "continuous thought" fed directly back as next input.
- Enables breadth-first search: continuous thoughts encode multiple alternative next steps simultaneously.
- Most word tokens in CoT ensure textual coherence, not reasoning -- COCONUT eliminates this overhead.
- Superior on logical reasoning tasks requiring backtracking.
- Current limitation: some performance degradation vs. explicit reasoning on certain tasks.

## Detailed Summary

Hao et al. (2024) from Meta challenge the fundamental assumption that reasoning must happen in language space. COCONUT operates by feeding the last hidden state of the LLM directly back as the next input embedding, bypassing token decoding entirely. This "continuous thought" carries richer information than a single discrete token.

The most striking capability is implicit breadth-first search: because continuous representations can superpose multiple reasoning paths, the model explores alternatives without explicitly generating them as separate token sequences. This is fundamentally different from standard [[concepts/chain-of-thought]] which commits to a single path at each step.

However, [[concepts/latent-reasoning]] approaches face challenges: hidden state distributions differ significantly from token embedding distributions, causing training instability. Performance can degrade on tasks where the verbalized reasoning of standard CoT provides important self-correction signals.

COCONUT represents a frontier direction for making [[concepts/test-time-compute]] more efficient -- achieving reasoning gains without the token generation overhead.

## Metadata

- **Author**: Shibo Hao et al. (Meta)
- **Date Published**: 2024-12-09
- **Format**: paper
- **URL**: https://arxiv.org/abs/2412.06769
