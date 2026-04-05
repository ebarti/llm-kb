---
title: "Extended Thinking"
type: concept
sources: ["[[sources/anthropic-extended-thinking-docs]]", "[[sources/anthropic-claude-4-announcement]]", "[[sources/anthropic-extended-thinking]]"]
related: ["[[entities/claude]]", "[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]", "[[concepts/chain-of-thought-prompting]]", "[[concepts/tool-use]]", "[[concepts/claude-model-family-evolution]]"]
tags: [claude, reasoning, extended-thinking, test-time-compute, adaptive-thinking]
last_compiled: 2026-04-05
summary: "Claude's step-by-step reasoning capability that allocates additional compute at inference time: evolved from manual budget_tokens (Claude 4) to adaptive thinking (Claude 4.6) where the model dynamically decides reasoning depth."
---

## Overview

Extended thinking is [[entities/claude]]'s implementation of [[concepts/test-time-compute]] scaling -- the principle that allocating more computation at inference time (rather than training time) can dramatically improve reasoning quality. When enabled, Claude performs sequential reasoning steps before producing its final output, similar to how a human would work through a complex problem on paper before stating a conclusion.

Extended thinking was introduced with Claude 3.7 Sonnet and has evolved through three stages: manual budgets, interleaved thinking with tools, and adaptive thinking.

## Evolution

### Stage 1: Manual Extended Thinking (Claude 3.7 Sonnet, early 2025)
- Developers set explicit `budget_tokens` controlling maximum reasoning tokens
- Thinking output visible to developers (later summarized)
- Simple on/off toggle

### Stage 2: Extended Thinking with Tools (Claude 4, May 2025)
- Models alternate between reasoning and tool calls within a single turn
- Interleaved thinking enables sophisticated multi-step agentic workflows
- 65% fewer shortcut behaviors compared to previous models

### Stage 3: Adaptive Thinking (Claude 4.6, February 2026)
- Model dynamically decides when and how much to think
- Controlled by `effort` parameter: "low", "medium", "high"
- Replaces manual `budget_tokens` (now deprecated on 4.6 models)
- More efficient: allocates reasoning where it matters, skips it where trivial

## How It Works

### API Configuration

**Adaptive thinking (recommended for 4.6):**
```json
{
  "thinking": {"type": "adaptive"},
  "effort": "medium"
}
```

**Manual thinking (legacy):**
```json
{
  "thinking": {"type": "enabled", "budget_tokens": 10000}
}
```

### Display Options

| Mode | Output | Latency | Cost |
|------|--------|---------|------|
| Summarized (default) | Summary of reasoning | Standard | Full thinking tokens |
| Omitted | Empty thinking field + signature | Lower | Full thinking tokens |

In both modes, billing is based on full internal reasoning tokens -- the display mode only affects what's returned, not what's computed.

### Interleaved Thinking

A critical capability for agentic workflows: Claude can think between tool calls, processing tool results with additional reasoning before making the next decision. Example flow:

1. User asks complex question
2. Claude thinks about approach
3. Claude calls search tool
4. Claude thinks about search results
5. Claude calls calculation tool
6. Claude thinks about combined results
7. Claude produces final answer

This is auto-enabled on Opus 4.6 and Sonnet 4.6. Older Claude 4 models require the `interleaved-thinking-2025-05-14` beta header.

## Technical Constraints

- Cannot toggle thinking mid-assistant-turn (tool use loops are part of one turn)
- Only supports `tool_choice: "auto"` or `"none"` -- cannot force specific tools
- Must preserve complete thinking blocks when passing tool results back
- System prompt caching is preserved across thinking parameter changes
- Message caching is invalidated by thinking parameter changes

## When to Use

| Task Type | Recommended Mode | Reasoning |
|-----------|-----------------|-----------|
| Simple Q&A | No thinking or effort: "low" | Overhead not justified |
| Code generation | effort: "medium" | Moderate planning helps |
| Complex debugging | effort: "high" | Step-by-step analysis critical |
| Math proofs | effort: "high" | Formal reasoning requires depth |
| Multi-step research | Adaptive with tools | Interleaved thinking between tool calls |
| Quick classification | No thinking | Speed matters more than depth |

## Relationship to Other Concepts

Extended thinking is Claude's specific implementation of the broader [[concepts/test-time-compute]] paradigm. It is related to but distinct from [[concepts/chain-of-thought-prompting]]: CoT prompting asks the model to show reasoning in its text output, while extended thinking allocates actual additional compute for internal reasoning that may be summarized or hidden from the user.

## Sources

- [[sources/anthropic-extended-thinking-docs]] -- official API documentation with full technical details
- [[sources/anthropic-claude-4-announcement]] -- extended thinking with tool use introduction
- [[sources/anthropic-extended-thinking]] -- initial announcement of extended thinking

## Related Concepts

- [[concepts/test-time-compute]] -- the broader paradigm extended thinking implements
- [[concepts/reasoning-models]] -- landscape of reasoning-focused models
- [[concepts/chain-of-thought-prompting]] -- prompt-based reasoning (complementary technique)
- [[concepts/tool-use]] -- extended thinking interleaves with tool calls
- [[concepts/claude-model-family-evolution]] -- evolution across generations
