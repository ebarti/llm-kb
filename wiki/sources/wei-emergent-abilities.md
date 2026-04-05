---
title: "Source: Emergent Abilities of Large Language Models"
type: source-summary
source: "[[raw/wei-emergent-abilities]]"
related: ["[[concepts/emergent-abilities]]", "[[concepts/llm-reasoning]]", "[[concepts/chain-of-thought]]"]
last_compiled: 2026-04-05
summary: "Influential 2022 paper defining emergent abilities as capabilities absent in smaller models that appear at scale, with near-random-to-high performance phase transitions -- subject to the 'mirage' debate about measurement artifacts."
---

## Key Points

- Emergent ability: not present in smaller models, present in larger models, not predictable by extrapolating smaller model performance.
- Performance shows phase transitions: near-random until a critical scale threshold, then rapid improvement.
- Chain-of-thought prompting is an example: useless below ~10^22 FLOPs, transformative above.
- Schaeffer et al. (2023) counter-argued that emergence may be a measurement artifact of nonlinear metrics.

## Detailed Summary

Wei et al. (2022) catalogued a striking phenomenon in LLM scaling: certain capabilities appear to emerge suddenly and unpredictably at specific scale thresholds. Unlike predictable improvements in perplexity (which scale smoothly with model size), some task-level capabilities show phase transitions from near-random to high performance.

Examples include [[concepts/chain-of-thought|chain-of-thought reasoning]], in-context learning, multi-step arithmetic, word unscrambling, and code generation. The threshold scale varies by task and cannot be predicted in advance, which has significant implications for AI safety -- if we cannot predict when dangerous capabilities will emerge, we cannot proactively mitigate them.

The subsequent debate sparked by Schaeffer et al. (2023) questioned whether emergence is real or an artifact of metric choice. Their argument: metrics like exact-match accuracy (nonlinear, threshold-dependent) produce apparent phase transitions, while linear metrics like per-token accuracy show smooth improvement. This reframing is important but doesn't fully resolve the practical concern -- even if improvement is smooth in some metric, the practical utility of a capability can still be threshold-dependent.

## Related Concepts

- [[concepts/emergent-abilities]] -- the core phenomenon
- [[concepts/chain-of-thought]] -- a key example of an emergent ability
- [[concepts/llm-reasoning]] -- emergence relates to the nature of reasoning capabilities
- [[concepts/stochastic-parrot-debate]] -- emergence is evidence against the "mere pattern matching" view
