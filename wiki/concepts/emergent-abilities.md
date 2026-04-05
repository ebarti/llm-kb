---
title: "Emergent Abilities of Large Language Models"
type: concept
sources: ["[[sources/wei-emergent-abilities]]", "[[sources/wei-chain-of-thought-prompting]]"]
related: ["[[concepts/llm-reasoning]]", "[[concepts/chain-of-thought]]", "[[concepts/stochastic-parrot-debate]]"]
last_compiled: 2026-04-05
summary: "Capabilities absent in smaller LLMs that appear suddenly at scale -- including chain-of-thought reasoning, in-context learning, and multi-step arithmetic -- subject to debate about whether the phase transitions are genuine or measurement artifacts."
---

## Overview

Emergent abilities are capabilities that are not present in smaller language models but appear in larger ones, seemingly suddenly and unpredictably. The concept was formalized by [[entities/jason-wei|Wei et al. (2022)]] and has become central to discussions about AI scaling, safety, and governance.

## Definition

An ability is **emergent** if:
1. It is absent in smaller models (near-random performance).
2. It appears in larger models (substantially above random).
3. It cannot be predicted by extrapolating smaller model performance.

When plotted on a scaling curve, emergent abilities show a characteristic "hockey stick" shape: flat performance followed by a sharp uptick at a critical threshold.

## Examples of Emergent Abilities

| Ability | Approximate Threshold | Significance |
|---------|----------------------|-------------|
| [[concepts/chain-of-thought]] reasoning | ~10^22 FLOPs (~100B params) | Foundational for all reasoning techniques |
| In-context learning | ~10^21 FLOPs | Enables few-shot learning without fine-tuning |
| Multi-step arithmetic | Variable | Precise calculation from text |
| Word unscrambling | Variable | Character-level manipulation |
| Code generation | Variable | Complex structured output |

## The "Mirage" Debate

Schaeffer et al. (2023) challenged the emergence narrative:

**Claim**: Apparent emergence is an artifact of metric choice.
- **Nonlinear metrics** (e.g., exact-match accuracy): Create phase transitions because they are threshold-dependent. Below a certain capability level, accuracy is 0%; above it, accuracy jumps.
- **Linear metrics** (e.g., per-token accuracy): Show smooth, predictable improvements across all scales.

**Implication**: The underlying capability may improve gradually, but our measurement makes it look sudden.

**Counter-arguments**:
- Even if improvement is smooth in some metrics, the practical utility of a capability can be threshold-dependent (a 40% accurate calculator is useless; a 95% accurate one is useful).
- Some tasks genuinely require compositional capabilities that only work above a minimum threshold.
- The safety concern remains regardless: if we cannot predict when useful capabilities appear, we cannot predict when dangerous ones will.

## Policy Implications

Emergence has entered policy discussions:
- Congressional members have referenced emergence research in AI governance debates.
- The unpredictability of emergent capabilities complicates risk assessment.
- If dangerous capabilities (e.g., autonomous hacking, bioweapon synthesis) could emerge unpredictably, preemptive safety measures are harder to design.

## Relationship to Reasoning

[[concepts/chain-of-thought|Chain-of-thought reasoning]] is the canonical example of an emergent ability. Below ~100B parameters, CoT prompting hurts performance (models generate illogical chains). Above that threshold, CoT dramatically improves reasoning. This has profound implications: reasoning capabilities may continue to emerge unpredictably as models scale further.

## Sources

- [[sources/wei-emergent-abilities]] -- the foundational paper defining emergence
- [[sources/wei-chain-of-thought-prompting]] -- CoT as a key example of emergence

## Related Concepts

- [[concepts/llm-reasoning]] -- reasoning as an emergent capability
- [[concepts/chain-of-thought]] -- the most prominent emergent reasoning technique
- [[concepts/stochastic-parrot-debate]] -- emergence as evidence against the "mere imitation" view
