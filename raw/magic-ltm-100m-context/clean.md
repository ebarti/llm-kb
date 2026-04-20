---
title: "100M Token Context Windows — Magic LTM-2-Mini"
source: "https://magic.dev/blog/100m-token-context-windows"
author: "Magic"
date_published: 2024-08-28
date_ingested: 2026-04-05
tags: [long-context, magic, ltm, 100m-tokens, architecture, efficiency]
type: article
status: raw
discovered_via: search
---

# Magic LTM-2-Mini: 100M Token Context Windows

## Overview

LTM-2-Mini is Magic's first model with a 100 million token context window — equivalent to 10 million lines of code or 750 novels.

## Architecture: Sequence-Dimension Algorithm

Magic developed a novel "sequence-dimension algorithm" that replaces traditional attention mechanisms:

- **Efficiency**: Roughly **1,000x cheaper** than Llama 3.1 405B's attention mechanism for 100M token contexts.
- **Memory**: Running Llama 3.1 405B with 100M tokens requires **638 H100s per user** just for the KV cache. LTM requires only a fraction of a single H100's memory.
- Required writing an entire training and inference stack from scratch (no torch autograd, custom CUDA kernels).

## HashHop Benchmark

Magic introduced HashHop to address flaws in existing long-context benchmarks like Needle-in-a-Haystack (NIAH):

- Uses **incompressible hash pairs** requiring maximum information storage.
- Tests: single-step induction heads (A→B completion), multi-hop chains (1→2→3), position-invariant retrieval (shuffled pairs), advanced direct jumps across context.
- NIAH criticism: too easy, can be solved without truly processing the full context.

## Performance

- Strong performance on 2-hop tasks without chain-of-thought reasoning, suggesting development of complex circuits beyond single induction heads.
- Successfully created custom GUI frameworks and implemented features in complex codebases with full codebase in context.
- Performance still below frontier models on general tasks.

## Implications

- Demonstrates that fundamentally different architectures can handle orders-of-magnitude more context than standard transformers.
- Focus on software development: having all code, documentation, and libraries in context enables better code synthesis.
- Suggests a future where entire codebases are contextually available during inference.
