---
title: "Claude"
type: entity
entity_type: tool
sources: ["[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/anthropic-extended-thinking]]"]
related: ["[[entities/anthropic]]", "[[concepts/prompt-engineering]]", "[[concepts/system-prompt-design]]", "[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]"]
last_compiled: 2026-04-05
summary: "Anthropic's frontier LLM family (Opus, Sonnet, Haiku); Claude 4.6 features adaptive thinking, native subagent orchestration, and preference for XML-structured prompts."
---

## Overview

Claude is [[entities/anthropic]]'s family of large language models, comprising three tiers: Claude Opus (highest capability), Claude Sonnet (balanced), and Claude Haiku (fastest/cheapest). As of 2026, the latest generation is Claude 4.6.

## Key Features (Claude 4.6)

- **Adaptive thinking**: Dynamically decides when and how much to reason (replaces manual budget_tokens)
- **Subagent orchestration**: Natively recognizes when tasks benefit from delegation to subagents
- **More concise and direct**: Less verbose than previous versions; provides fact-based progress
- **XML tag preference**: Benefits from XML-style tags for structured prompts
- **Prefill deprecation**: Prefilled responses on the last assistant turn are no longer supported
- **Long-context grounding**: Put documents at top, queries at bottom for up to 30% quality improvement
- **Context awareness**: Tracks remaining context window and manages accordingly

## Prompting Tips (Claude-Specific)

- Use `<example>`, `<instructions>`, `<context>` tags for structure
- "Think thoroughly" works better than prescriptive step-by-step instructions
- Dial back aggressive tool-use nudges from older models (Claude 4.6 may overtrigger)
- Use effort parameter (low/medium/high/max) to control thinking depth
- Ask Claude to self-check: "Before you finish, verify your answer against [criteria]"

## Extended Thinking / Reasoning (Claude 3.7 Sonnet)

Claude 3.7 Sonnet (February 2025) introduced extended thinking, making Claude a [[concepts/reasoning-models|hybrid reasoning model]]:

- **Toggle**: Same model operates as standard LLM or reasoning model with extended thinking.
- **Thinking budget**: Configurable [[concepts/test-time-compute|test-time compute]] allocation.
- **Performance**: 96.5% on GPQA physics subset; math accuracy scales logarithmically with token budget.
- **Visible thinking**: Raw reasoning chain shown to users for transparency and trust.
- **Self-regulation**: Model stops thinking before budget is exhausted when further deliberation won't help.
- **Best domains**: Math, physics, competitive coding, in-depth analysis, debugging.

This hybrid approach (choose System 1 or [[concepts/system-1-system-2-thinking|System 2]] per task) is distinctive compared to OpenAI's always-on o-series or DeepSeek's separate R1 model.

## Mentioned In
- [[sources/anthropic-claude-prompting-best-practices]] — Official prompting guide for Claude 4.6
- [[sources/anthropic-extended-thinking]] — Extended thinking feature and reasoning capabilities
