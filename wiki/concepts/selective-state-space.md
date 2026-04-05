---
title: "Selective State Space (S6)"
type: concept
sources: ["[[sources/mamba-state-space-models-visual-guide]]"]
related: ["[[concepts/mamba]]", "[[concepts/state-space-models]]"]
last_compiled: 2026-04-05
summary: "Mamba's core innovation: making SSM state transition matrices B, C and step size delta input-dependent, enabling content-aware selective information compression into the hidden state."
---

## Overview

Selective State Space (S6) is the key mechanism in [[concepts/mamba]] that overcomes the fundamental limitation of traditional [[concepts/state-space-models]]: time-invariance. Standard SSMs process every input identically regardless of content. S6 makes the state transition matrices B, C, and the discretization step size delta all functions of the current input.

## How It Works

For each input token x(t):
- **B(t) = f_B(x(t))**: Input-dependent state update matrix — controls what gets written to the hidden state
- **C(t) = f_C(x(t))**: Input-dependent output mapping — controls what gets read from the hidden state
- **delta(t) = f_delta(x(t))**: Input-dependent step size — acts as a gate:
  - Large delta: emphasize current input (high information value)
  - Small delta: rely on accumulated state (current input is less important)

This selectivity enables Mamba to solve tasks that time-invariant SSMs cannot, such as selective copying (filtering relevant information from noise) and induction heads (reproducing patterns from context).

## Sources

- [[sources/mamba-state-space-models-visual-guide]] — visual explanation of the selective mechanism

## Related Concepts

- [[concepts/mamba]] — the architecture built on S6
- [[concepts/state-space-models]] — the broader family
- [[concepts/self-attention]] — analogous content-aware weighting in transformers
