---
title: "Source: Claude's Extended Thinking"
type: source-summary
source: "[[raw/anthropic-extended-thinking]]"
related: ["[[concepts/test-time-compute]]", "[[concepts/reasoning-models]]", "[[entities/anthropic]]", "[[entities/claude]]"]
last_compiled: 2026-04-05
summary: "Anthropic's 2025 announcement of Claude 3.7 Sonnet's extended thinking: a configurable 'thinking budget' that enables serial test-time compute, achieving 96.5% on physics and scaling math accuracy logarithmically with token allocation."
---

## Key Points

- Claude 3.7 Sonnet operates as both a standard LLM and a reasoning model -- toggle extended thinking on/off.
- Configurable thinking budget lets developers control compute allocation per query.
- Performance: 96.5% on GPQA physics, predictable scaling on AIME with more thinking tokens.
- Visible thinking process: raw thought chain shown to users for transparency.
- Math accuracy improves logarithmically with token budget; model self-regulates (often stops before budget limit).

## Detailed Summary

Anthropic's extended thinking feature represents a distinctive approach to [[concepts/reasoning-models|reasoning models]]: rather than creating a separate reasoning model, they enabled the same model to optionally engage in extended deliberation. This hybrid approach lets users choose between fast System 1 responses and deeper System 2 reasoning based on task needs.

The "thinking budget" concept is technically interesting -- rather than all-or-nothing reasoning, developers can fine-tune the compute-quality tradeoff. The logarithmic scaling of accuracy with tokens suggests diminishing returns, but the model's self-regulation (stopping before the budget is exhausted) indicates it can assess when further thinking won't help.

Anthropic chose to make the thinking process visible, prioritizing transparency. This enables trust-building and alignment research but creates concerns about faithfulness (do displayed thoughts reflect actual computation?) and jailbreak vectors (attackers may manipulate the visible reasoning chain).

## Related Concepts

- [[concepts/test-time-compute]] -- extended thinking is serial test-time compute
- [[concepts/reasoning-models]] -- Claude's approach to the reasoning model paradigm
- [[concepts/system-1-system-2-thinking]] -- toggle between System 1 (standard) and System 2 (extended thinking)
- [[entities/anthropic]] -- the organization behind Claude
