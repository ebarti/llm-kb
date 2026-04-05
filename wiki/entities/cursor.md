---
title: "Cursor"
type: entity
entity_type: tool
sources: ["[[sources/faros-ai-coding-agents-2026]]", "[[sources/dextralabs-claude-cursor-copilot-30day]]", "[[sources/metr-ai-developer-productivity-study]]", "[[sources/redmonk-agentic-ides-2025]]", "[[sources/qodo-ai-coding-assistants-2026]]"]
related: ["[[concepts/ai-coding-assistants]]", "[[concepts/agentic-coding]]", "[[entities/claude-code]]", "[[entities/github-copilot]]", "[[comparisons/cursor-vs-claude-code-vs-copilot]]"]
last_compiled: 2026-04-05
summary: "AI-native IDE (VS Code fork) that leads the market with $2B+ ARR and $29.3B valuation by March 2026 — praised for 'magical' inline editing, codebase indexing, and agent mode."
---

## Overview

Cursor is an AI-native integrated development environment built as a fork of VS Code, rebuilt around AI capabilities. It provides inline code completions, multi-file editing, codebase indexing for project-level awareness, a composer mode for complex changes, and an agent mode for autonomous task execution.

## Key Facts

- **Type:** AI-native IDE (VS Code fork)
- **Pricing:** Pro $20/mo, Pro+/Ultra tiered, Teams $40/user/mo, Enterprise custom
- **Revenue:** Surpassed $2B annualized revenue by March 2026 (doubled from $1B in November 2025)
- **Valuation:** $29.3B (March 2026)
- **Market Position:** Most widely used AI coding IDE

## Key Features

- **Tab completions:** Predictive code suggestions as you type
- **Inline edits:** Generate and modify code directly in the editor
- **Composer mode:** Multi-file changes coordinated through natural language
- **Agent mode:** Autonomous task execution with tool use
- **Codebase indexing:** Project-level understanding of code structure and dependencies
- **Next Edit Predictions:** Anticipates where and what you'll edit next

## Strengths

- Seamless VS Code integration — familiar environment for existing VS Code users
- "Genuinely magical" inline code generation ([[sources/dextralabs-claude-cursor-copilot-30day]])
- Fast autocomplete with minimal friction for small-to-medium tasks
- Stays "out of the way" — praised for not disrupting developer flow
- Shipped greenfield features in 1 day vs. 3-day estimate in practitioner testing

## Weaknesses

- Struggles with large refactors and complex repo-wide changes
- Requires external API calls — data privacy concerns for enterprise
- Struggles with TypeScript generics and complex type manipulation
- Requires editor migration (switching away from existing IDE)
- Pricing volatility in 2025 with usage-based shift

## Role in METR Study

[[sources/metr-ai-developer-productivity-study]] used Cursor Pro with Claude 3.5/3.7 Sonnet as the primary AI tool. The study found 19% slowdown for experienced developers, though this may reflect limited Cursor-specific proficiency (~50 hours) rather than the tool's inherent capability.

## Mentioned In

- [[sources/faros-ai-coding-agents-2026]] — Top-tier agent, baseline comparison tool
- [[sources/dextralabs-claude-cursor-copilot-30day]] — 9/10 backend, 9/10 frontend, 9/10 greenfield
- [[sources/metr-ai-developer-productivity-study]] — Primary tool used in the RCT
- [[sources/redmonk-agentic-ides-2025]] — Pricing concerns noted
- [[sources/qodo-ai-coding-assistants-2026]] — Tier 2 IDE assistant, $20/mo pro
