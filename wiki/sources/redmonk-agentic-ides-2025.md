---
title: "Source: 10 Things Developers Want from Agentic IDEs (2025)"
type: source-summary
source: "[[raw/redmonk-agentic-ides-2025]]"
related: ["[[concepts/agentic-coding]]", "[[concepts/spec-driven-development]]", "[[concepts/model-context-protocol]]", "[[concepts/developer-experience-ai]]"]
last_compiled: 2026-04-05
summary: "RedMonk analyst identifies 10 must-haves for agentic IDEs: background agents, persistent memory, predictable pricing, MCP, multi-agent orchestration, spec-driven dev, reliability, HITL controls, rollbacks, and skills."
---

## Key Points

- Marks the shift from "AI Code Assistants" (2023-2024) to "Agentic IDEs" (2025)
- 10 requirements: background agents, persistent memory, predictable pricing, MCP, multi-agent orchestration, spec-driven development, reliability, human-in-the-loop controls, rollbacks, skills
- MCP (Anthropic) achieved rapid adoption as the standard integration protocol
- 44% of Claude-assisted work consisted of tasks engineers "wouldn't have enjoyed doing themselves"
- Notable 2025 market entrants: Windsurf, Trae (ByteDance), AWS Kiro, IBM Project Bob, Augment Code, Junie (JetBrains)

## Detailed Summary

Kate Holterhoff's RedMonk analysis captures the transition moment in developer tooling. The framing shift from "assistant" to "agent" is not just marketing — it reflects genuine capability changes where tools now execute multi-step workflows autonomously rather than simply suggesting code completions.

The 10 requirements map to distinct developer pain points: background agents address the desire for overnight task execution; persistent memory addresses the frustration of repeatedly re-explaining project context; predictable pricing addresses the 2025 billing surprises from Cursor, Claude Code, and Replit.

The spec-driven development requirement (#6) aligns with [[sources/osmani-llm-coding-workflow-2026]] — both argue that requirements.md/design.md files serve as contracts between humans and AI, preventing the common failure of AI "going off the rails" mid-implementation.

The skills requirement (#10) represents a new paradigm: reusable, version-controlled workflow modules that encode institutional knowledge, making AI assistance compound over time rather than starting fresh each session.

## Related Concepts

- [[concepts/agentic-coding]] — The core shift this article documents
- [[concepts/spec-driven-development]] — Requirement #6
- [[concepts/model-context-protocol]] — Requirement #4, now an industry standard
- [[concepts/developer-experience-ai]] — All 10 requirements map to DX concerns
