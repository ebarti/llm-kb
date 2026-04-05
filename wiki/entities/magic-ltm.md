---
title: "Magic / LTM-2-Mini"
type: entity
entity_type: tool
sources: ["[[sources/magic-ltm-100m-context]]"]
related: ["[[concepts/long-context-models]]", "[[concepts/context-windows]]", "[[concepts/needle-in-a-haystack]]"]
last_compiled: 2026-04-05
summary: "Magic's LTM-2-Mini: 100M token context model using a novel sequence-dimension algorithm 1,000x cheaper than standard attention, requiring a fraction of one H100 vs 638 for Llama 405B."
---

## Overview

Magic is an AI company focused on building models with extremely long context windows for software development. Their flagship model, **LTM-2-Mini**, was the first to achieve a 100 million token context window — equivalent to 10 million lines of code or 750 novels.

## Key Innovation: Sequence-Dimension Algorithm

Magic replaced standard transformer attention with a novel "sequence-dimension algorithm" that achieves:
- **1,000x cheaper** inference than Llama 3.1 405B attention at 100M tokens
- **Memory**: Fraction of one H100 GPU vs **638 H100s** for Llama 405B's KV cache at 100M tokens
- Required building an entire training and inference stack from scratch (no torch autograd, custom CUDA kernels)

## HashHop Benchmark

Magic introduced HashHop as a harder alternative to [[concepts/needle-in-a-haystack]]:
- Uses incompressible random hash pairs (no pattern exploitation)
- Tests: single-step induction, multi-hop chains, position-invariant retrieval, direct jumps
- Addresses criticism that standard NIAH is too easy for modern models

## Applications

- Primary focus: software development with full codebase in context
- Successfully created custom GUI frameworks and implemented features in complex codebases
- General capability still below frontier models

## Significance

LTM-2-Mini demonstrates that fundamentally different architectures — not just engineering around attention's O(n^2) — can enable orders-of-magnitude more context. It suggests a possible future where entire codebases, documentation, and project histories are permanently available during inference.

## Mentioned In

- [[sources/magic-ltm-100m-context]] — detailed architecture and benchmark analysis
