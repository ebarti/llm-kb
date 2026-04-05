---
title: "Source: Large Language Model Reasoning Failures Survey"
type: source-summary
source: "[[raw/song-llm-reasoning-failures-survey]]"
related: ["[[concepts/llm-reasoning-limitations]]", "[[concepts/llm-reasoning]]", "[[concepts/stochastic-parrot-debate]]"]
last_compiled: 2026-04-05
summary: "TMLR 2026 survey providing the first comprehensive taxonomy of LLM reasoning failures: fundamental architectural limitations, application-specific weaknesses, and robustness issues, with mitigation strategies for each."
---

## Key Points

- First comprehensive taxonomy of LLM reasoning failures.
- Three failure types: fundamental (architectural), application-specific, and robustness (inconsistency across variations).
- Root cause: next-token optimization biases toward locally coherent continuation rather than constraint satisfaction.
- Self-attention disperses working memory; tokenization artifacts destabilize reasoning.

## Detailed Summary

Song, Han, and Goodman (2026) systematized the growing literature on LLM reasoning failures into a rigorous taxonomy. Their framework first distinguishes embodied reasoning (physical/spatial) from non-embodied reasoning (further split into informal/intuitive and formal/logical).

**Fundamental failures** are intrinsic to transformer architecture:
- Next-token prediction optimizes for local coherence, not global logical consistency.
- Self-attention patterns enable surface pattern matching but not compositional reasoning.
- Working memory limitations emerge from attention dispersion over long sequences.

**Application-specific failures** manifest in particular domains:
- Compositional reasoning: models fail when problems require combining multiple logical operations.
- Disjunctive reasoning: multi-path problems (OR logic) are systematically weak.
- Graph-based reasoning: models hallucinate non-existent features, causing cascading errors.

**Robustness failures** show inconsistency:
- Minor input variations produce drastically different outputs.
- Models use frequency heuristics rather than algebraic closure.

For each failure type, the survey provides definitions, existing research analysis, root cause exploration, and mitigation strategies.

## Related Concepts

- [[concepts/llm-reasoning-limitations]] -- the comprehensive picture of limitations
- [[concepts/llm-reasoning]] -- what failures tell us about the nature of LLM reasoning
- [[concepts/stochastic-parrot-debate]] -- failures as evidence in the debate
- [[concepts/chain-of-thought]] -- how CoT can fail in specific ways
