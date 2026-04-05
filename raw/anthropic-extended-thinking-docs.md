---
title: "Building with Extended Thinking - Claude API Docs"
source: "https://platform.claude.com/docs/en/build-with-claude/extended-thinking"
author: "Anthropic"
date_published: 2026-04-05
date_ingested: 2026-04-05
tags: [claude, extended-thinking, reasoning, chain-of-thought, api]
type: article
status: raw
discovered_via: search
---

# Building with Extended Thinking - Claude API Docs

## Overview

Extended thinking gives Claude enhanced reasoning for complex tasks while providing varying transparency into step-by-step thought processes.

## Supported Models

All Claude 4+ models support extended thinking:
- Claude Opus 4.6 (adaptive thinking recommended)
- Claude Sonnet 4.6 (adaptive thinking recommended)
- Claude Haiku 4.5
- Claude Opus 4.5, 4.1, 4
- Claude Sonnet 4.5, 4
- Claude Sonnet 3.7 (deprecated)

## Two Modes

### Manual Extended Thinking
- Set `thinking.type: "enabled"` with `budget_tokens` parameter
- Budget sets maximum tokens for internal reasoning
- Must be less than `max_tokens`
- Claude may not use entire budget, especially above 32K
- Deprecated on Claude 4.6 models

### Adaptive Thinking (Recommended for 4.6)
- Set `thinking.type: "adaptive"` with `effort` parameter ("low"/"medium"/"high")
- Claude dynamically decides when and how much to think
- Evolution from fixed budgets to intelligent resource allocation

## Display Options

### Summarized (Default)
- Returns summary of full thinking process
- Billed for full thinking tokens, not summary
- Different model handles summarization (thinking model doesn't see summary)

### Omitted
- Returns empty thinking field with signature only
- Faster streaming, text response begins sooner
- Still charged for full thinking tokens
- Reduces latency, not cost

## Interleaved Thinking

Claude can think between tool calls for sophisticated multi-step reasoning:
- Auto-enabled on Opus 4.6 and Sonnet 4.6 with adaptive thinking
- Requires beta header on older Claude 4 models
- `budget_tokens` represents total budget across all thinking blocks in a turn

## Key Technical Details

### Token Counting
- Charged for complete internal reasoning (full tokens)
- Summarization adds minimal latency
- Thinking blocks in tool-use continuations cached as input tokens

### Prompt Caching
- System prompt caching preserved when thinking parameters change
- Message caching invalidated by thinking parameter changes

### Tool Use Constraints
- Only supports `tool_choice: "auto"` or `tool_choice: "none"`
- Cannot force specific tools
- Must preserve complete thinking blocks during tool-use loops
- Cannot toggle thinking mid-assistant-turn

### Output Limits
- Opus 4.6: up to 128K output tokens
- Sonnet 4.6 & Haiku 4.5: up to 64K output tokens
- Batch API: up to 300K with beta header

## Best Practices
1. Use adaptive thinking on 4.6 models
2. Set appropriate budget_tokens for complex problems
3. Preserve thinking blocks in tool use
4. Use display: "omitted" for latency-sensitive applications
5. Cache system prompts preferentially
6. Plan thinking strategy per completed turn, not mid-turn
