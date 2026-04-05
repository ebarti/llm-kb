---
title: "Latent Reasoning"
type: concept
sources: ["[[sources/hao-coconut-latent-reasoning]]", "[[sources/raschka-state-of-reasoning-inference]]"]
related: ["[[concepts/test-time-compute]]", "[[concepts/chain-of-thought]]", "[[concepts/reasoning-models]]", "[[concepts/reasoning-tokens]]"]
last_compiled: 2026-04-05
summary: "Reasoning in continuous hidden state space rather than through explicit token generation -- potentially more efficient than chain-of-thought by enabling breadth-first search, but currently suffering performance degradation on some tasks."
---

## Overview

Latent reasoning is an emerging frontier in [[concepts/test-time-compute]] research that performs computation in the model's hidden state space rather than generating explicit language tokens. The key insight: most tokens in [[concepts/chain-of-thought]] sequences primarily ensure textual coherence and are not essential for the reasoning itself.

## COCONUT: Chain of Continuous Thought

[[sources/hao-coconut-latent-reasoning|Hao et al. (2024)]] introduce the most prominent latent reasoning approach:

1. Instead of decoding hidden states into word tokens, feed them directly back as input embeddings.
2. These "continuous thoughts" carry richer information than discrete tokens.
3. Enable implicit **breadth-first search**: continuous representations can superpose multiple alternative reasoning paths simultaneously.
4. Standard CoT commits to a single path at each step; COCONUT explores alternatives without generating them explicitly.

## Advantages Over Explicit Reasoning

| Dimension | Explicit CoT | Latent Reasoning |
|-----------|-------------|-----------------|
| Bandwidth | One token at a time | Full hidden state vector |
| Search strategy | Depth-first (sequential) | Breadth-first (parallel paths in one representation) |
| Token overhead | High (all reasoning verbalized) | Low (no token generation) |
| Interpretability | High (readable reasoning) | Low (opaque) |
| Self-correction | Via explicit backtracking text | Via implicit state revision |

## Current Limitations

- **Performance degradation**: Latent methods frequently underperform explicit CoT on some tasks.
- **Distribution mismatch**: Hidden state distributions differ significantly from token embedding distributions, causing training instability.
- **No interpretability**: Cannot inspect what the model is "thinking" -- a significant concern for [[concepts/ai-safety]] and [[concepts/scalable-oversight]].
- **Training complexity**: Requires curriculum training to gradually replace language tokens with continuous thoughts.

## Latent Reasoning as Vocabulary-Space Superposition

Recent work (2025) reveals that LLM reasoning in hidden states can be understood as superposition of multiple vocabulary-space concepts. This theoretical framework helps explain both the power (parallel exploration) and the limitations (distribution mismatch) of latent reasoning.

## Relationship to Recurrent Depth Approaches

A related line of research uses recurrent transformer blocks that can be iterated to arbitrary depth at test time, reasoning "in latent space through iterating a recurrent block." This provides a different mechanism for scaling [[concepts/test-time-compute]] without explicit token generation.

## Safety and Alignment Concerns

Latent reasoning raises concerns for the [[concepts/ai-alignment]] community:
- Hidden reasoning makes it impossible to verify that a model is reasoning faithfully.
- "Steganographic" reasoning could hide deceptive chains of thought.
- Alignment Forum discussion (2025) identifies latent reasoning as a potential vector for undetectable deceptive behavior.

This creates a tension: latent reasoning is more efficient, but explicit reasoning is more auditable.

## Open Questions

- Can latent reasoning match or exceed explicit CoT performance on all tasks?
- How can we make latent reasoning interpretable (probing, sparse autoencoders)?
- Will hybrid approaches (latent for exploration, explicit for final answer) dominate?
- Does latent reasoning fundamentally change the alignment verification problem?

## Sources

- [[sources/hao-coconut-latent-reasoning]] -- COCONUT (Chain of Continuous Thought)
- [[sources/raschka-state-of-reasoning-inference]] -- survey covering latent reasoning as frontier

## Related Concepts

- [[concepts/test-time-compute]] -- the paradigm latent reasoning optimizes
- [[concepts/chain-of-thought]] -- the explicit alternative
- [[concepts/reasoning-models]] -- may eventually incorporate latent reasoning
- [[concepts/reasoning-tokens]] -- the tokens latent reasoning seeks to eliminate
- [[concepts/ai-safety]] -- safety concerns from opaque reasoning
