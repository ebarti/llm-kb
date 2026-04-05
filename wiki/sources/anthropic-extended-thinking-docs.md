---
title: "Source: Building with Extended Thinking - Claude API Docs"
type: source-summary
source: "[[raw/anthropic-extended-thinking-docs]]"
related: ["[[entities/claude]]", "[[concepts/extended-thinking]]", "[[concepts/reasoning-models]]", "[[concepts/test-time-compute]]"]
tags: [claude, extended-thinking, reasoning, api]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Official Anthropic documentation on extended thinking: manual vs adaptive modes, interleaved thinking with tools, display options (summarized/omitted), token counting, and caching behavior."
---

## Key Points

- Two modes: manual (budget_tokens) deprecated on 4.6; adaptive (effort parameter) recommended
- Thinking output can be summarized (default) or omitted for lower latency
- Billed for full thinking tokens regardless of display mode
- Interleaved thinking enables reasoning between tool calls -- auto-enabled on 4.6 models
- Cannot toggle thinking mid-assistant-turn or force specific tools
- System prompt caching preserved when thinking parameters change; message caching is not
- All Claude 4+ models support extended thinking; Claude Haiku 4.5 supports it but not adaptive mode
- Opus 4.6: up to 128K output; Sonnet 4.6/Haiku 4.5: up to 64K; Batch API: up to 300K

## Detailed Summary

The extended thinking documentation is the technical reference for implementing Claude's step-by-step reasoning capabilities. It details two modes: manual (deprecated on 4.6) where developers set explicit token budgets, and adaptive (recommended for 4.6) where Claude dynamically allocates reasoning effort based on task complexity. Interleaved thinking -- the ability to reason between tool calls -- enables sophisticated multi-step workflows. The documentation covers streaming behavior, prompt caching interactions, tool-use constraints, and zero-data-retention eligibility.

## Metadata

- **Author**: Anthropic
- **Date Published**: 2026 (continuously updated)
- **Format**: API documentation
- **URL**: https://platform.claude.com/docs/en/build-with-claude/extended-thinking
