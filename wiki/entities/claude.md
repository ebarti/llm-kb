---
title: "Claude"
type: entity
entity_type: tool
sources: ["[[sources/anthropic-claude-prompting-best-practices]]", "[[sources/anthropic-extended-thinking]]", "[[sources/wikipedia-claude-language-model]]", "[[sources/anthropic-claude-models-overview]]", "[[sources/anthropic-claude-3-family-announcement]]", "[[sources/anthropic-claude-4-announcement]]", "[[sources/improvado-claude-vs-chatgpt-vs-gemini-2026]]"]
related: ["[[entities/anthropic]]", "[[entities/dario-amodei]]", "[[entities/claude-code]]", "[[concepts/prompt-engineering]]", "[[concepts/system-prompt-design]]", "[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]", "[[concepts/constitutional-ai]]", "[[concepts/extended-thinking]]", "[[concepts/claude-model-family-evolution]]", "[[concepts/responsible-scaling-policy]]", "[[comparisons/claude-vs-gpt-vs-gemini]]"]
last_compiled: 2026-04-05
summary: "Anthropic's frontier LLM family named after Claude Shannon; spans four generations (Claude 1-4.6) with Opus/Sonnet/Haiku tiers, up to 1M context, adaptive thinking, and market-leading coding benchmarks."
---

## Overview

Claude is [[entities/anthropic]]'s family of large language models, named after Claude Shannon, the mathematician who pioneered information theory. First released in March 2023, Claude has evolved through four major generations with a consistent three-tier structure: **Opus** (highest capability), **Sonnet** (balanced), and **Haiku** (fastest/cheapest). As of April 2026, the latest generation is Claude 4.6.

Claude is trained using [[concepts/constitutional-ai]] -- a self-critique and revision process guided by explicit written principles -- combined with RLHF. This produces a model that is helpful without being evasive, engaging with difficult queries by explaining reasoning rather than refusing.

## Current Model Lineup (April 2026)

| Model | Context | Max Output | Price (in/out per MTok) | Key Strength |
|-------|---------|------------|------------------------|--------------|
| **Opus 4.6** | 1M tokens | 128K | $5/$25 | Most intelligent; agents and coding |
| **Sonnet 4.6** | 1M tokens | 64K | $3/$15 | Best speed/intelligence balance |
| **Haiku 4.5** | 200K tokens | 64K | $1/$5 | Fastest; near-frontier intelligence |

All current models support text and image input, multilingual capabilities, vision, extended thinking, and are available via Claude API, AWS Bedrock, and Google Vertex AI.

## Key Features (Claude 4.6)

- **Adaptive thinking**: Dynamically decides when and how much to reason (replaces manual budget_tokens)
- **Subagent orchestration**: Natively recognizes when tasks benefit from delegation to subagents
- **Agent teams**: Multiple agents work on different parts simultaneously
- **Computer use**: Screen navigation, keyboard/mouse simulation (since October 2024)
- **Memory files**: Creates persistent context for long-running tasks
- **XML tag preference**: Benefits from XML-style tags for structured prompts
- **Prefill deprecation**: Prefilled responses on the last assistant turn are no longer supported
- **Long-context grounding**: Put documents at top, queries at bottom for up to 30% quality improvement
- **Context awareness**: Tracks remaining context window and manages accordingly

## Extended Thinking / Reasoning

Claude 3.7 Sonnet (February 2025) introduced [[concepts/extended-thinking]], making Claude a [[concepts/reasoning-models|hybrid reasoning model]]:

- **Toggle**: Same model operates as standard LLM or reasoning model with extended thinking
- **Thinking budget**: Configurable [[concepts/test-time-compute|test-time compute]] allocation
- **Performance**: 96.5% on GPQA physics subset; math accuracy scales logarithmically with token budget
- **Visible thinking**: Raw reasoning chain shown to users for transparency and trust
- **Self-regulation**: Model stops thinking before budget is exhausted when further deliberation won't help
- **Best domains**: Math, physics, competitive coding, in-depth analysis, debugging

This hybrid approach (choose System 1 or [[concepts/system-1-system-2-thinking|System 2]] per task) is distinctive compared to OpenAI's always-on o-series or DeepSeek's separate R1 model.

**Claude 4.6 evolution**: Adaptive thinking replaces manual budgets -- the model dynamically allocates reasoning effort. Interleaved thinking enables reasoning between tool calls for sophisticated agentic workflows.

## Benchmarks

| Benchmark | Claude 3 Opus | Opus 4 | Opus 4.1 | Opus 4.5 | Opus 4.6 |
|-----------|--------------|--------|----------|----------|----------|
| SWE-bench Verified | -- | 72.5% | 74.5% | 80.9% | -- |
| GPQA Diamond | ~50% | -- | -- | -- | 80.8% |
| Needle-in-Haystack | >99% | -- | -- | -- | -- |
| METR 50% time horizon | -- | -- | -- | 14h 30m | -- |

Claude 3 Opus was the first model to surpass GPT-4 on multiple benchmarks (MMLU, GPQA, GSM8K) when released in March 2024.

## Release History

See [[concepts/claude-model-family-evolution]] for the complete 17-release timeline from Claude 1 (March 2023) through Claude Sonnet 4.6 (February 2026). Key milestones:

- **March 2023**: Claude 1 (9K context)
- **March 2024**: Claude 3 family (three-tier system, vision, 200K context, surpassed GPT-4)
- **June 2024**: Claude 3.5 Sonnet (outperformed Opus at lower cost; Artifacts)
- **October 2024**: Computer use capability
- **May 2025**: Claude 4 (extended thinking with tools, Claude Code GA, 72.5% SWE-bench)
- **February 2026**: Claude 4.6 (1M context, adaptive thinking, agent teams, 128K output)

## Constitutional AI

Claude's behavior is guided by a written constitution that has grown from initial principles (2022) to 23,000 words (2026). The 2026 constitution was authored by Amanda Askell with contributions from Joe Carlsmith, Chris Olah, Jared Kaplan, and Holden Karnofsky. See [[concepts/constitutional-ai]] for the full technical approach.

## Pricing History

Opus-tier pricing deflated 3x while capabilities improved:
- Opus 4/4.1: $15/$75 per MTok
- Opus 4.5/4.6: $5/$25 per MTok

## Products and Interfaces

- **claude.ai**: Web/desktop chat interface
- **Claude Code**: Terminal-based agentic coding ([[entities/claude-code]])
- **Claude Cowork** (January 2026): GUI for non-technical users
- **Claude Max** (April 2025): $100-$200/month power-user subscription
- **Claude Gov** (June 2025): Government/classified use
- **Persistent memory** (March 2026): Retains preferences across conversations

## Prompting Tips (Claude-Specific)

- Use `<example>`, `<instructions>`, `<context>` tags for structure
- "Think thoroughly" works better than prescriptive step-by-step instructions
- Dial back aggressive tool-use nudges from older models (Claude 4.6 may overtrigger)
- Use effort parameter (low/medium/high/max) to control thinking depth
- Ask Claude to self-check: "Before you finish, verify your answer against [criteria]"

## Mentioned In

- [[sources/anthropic-claude-prompting-best-practices]] -- official prompting guide for Claude 4.6
- [[sources/anthropic-extended-thinking]] -- extended thinking feature and reasoning capabilities
- [[sources/wikipedia-claude-language-model]] -- comprehensive release history
- [[sources/anthropic-claude-models-overview]] -- official API model specs
- [[sources/anthropic-claude-3-family-announcement]] -- Claude 3 launch and benchmarks
- [[sources/anthropic-claude-4-announcement]] -- Claude 4 launch and features
- [[sources/improvado-claude-vs-chatgpt-vs-gemini-2026]] -- 2026 frontier model comparison
