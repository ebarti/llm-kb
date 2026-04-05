---
title: "Source: GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in LLMs"
type: source-summary
source: "[[raw/mirzadeh-gsm-symbolic]]"
related: ["[[concepts/mathematical-reasoning-llm]]", "[[concepts/llm-reasoning-limitations]]", "[[concepts/llm-reasoning]]"]
last_compiled: 2026-04-05
summary: "ICLR 2025 paper demonstrating LLM mathematical reasoning is fragile: performance drops up to 65% with irrelevant information, varies with number changes, and degrades with complexity -- evidence for pattern matching over genuine reasoning."
---

## Key Points

- LLMs show noticeable variance on different numerical instantiations of the same math problem.
- Adding a single irrelevant-but-plausible clause drops performance up to 65% across all state-of-the-art models.
- Performance degrades sharply as problem complexity (number of clauses) increases.
- Central finding: LLMs "replicate reasoning steps from training data" rather than performing genuine logical reasoning.

## Detailed Summary

Mirzadeh et al. (2024) created the GSM-Symbolic benchmark as a more rigorous alternative to GSM8K. By generating problems from symbolic templates, they could systematically vary numbers, add irrelevant information, and increase complexity while preserving the underlying reasoning structure.

Three key experiments revealed fragility:

1. **Numerical sensitivity**: Changing only the numbers in a problem (keeping the reasoning structure identical) caused significant performance variance across all models tested. A true reasoner should be invariant to such changes.

2. **Complexity scaling**: As the number of reasoning steps increased, accuracy degraded sharply -- far more than expected from a model that understood the underlying logic.

3. **Distractor susceptibility (GSM-NoOp)**: Adding a single sentence that was contextually relevant but mathematically unnecessary caused up to 65% performance drops. Models incorporated the irrelevant information into their calculations rather than ignoring it.

This paper is central to the debate about whether [[concepts/llm-reasoning|LLM reasoning]] is genuine understanding or [[concepts/llm-reasoning-limitations|sophisticated pattern matching]].

## Related Concepts

- [[concepts/mathematical-reasoning-llm]] -- the specific capability tested
- [[concepts/llm-reasoning-limitations]] -- evidence for fundamental limitations
- [[concepts/chain-of-thought]] -- the reasoning technique that fails under these variations
- [[concepts/stochastic-parrot-debate]] -- this evidence supports the "pattern matching" side
