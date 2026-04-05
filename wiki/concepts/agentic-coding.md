---
title: "Agentic Coding"
type: concept
sources: ["[[sources/claude-code-agentic-coding]]", "[[sources/devin-ai-software-engineer]]", "[[sources/pebblous-agentic-framework-explosion]]", "[[sources/redmonk-agentic-ides-2025]]", "[[sources/faros-ai-coding-agents-2026]]", "[[sources/osmani-llm-coding-workflow-2026]]", "[[sources/morphllm-codex-vs-claude-code]]", "[[sources/wikipedia-vibe-coding]]", "[[sources/greptile-state-of-ai-coding-2025]]"]
related: ["[[concepts/agentic-workflows]]", "[[concepts/swe-bench]]", "[[entities/claude-code]]", "[[entities/devin-ai]]", "[[entities/openai-codex]]", "[[concepts/post-code-ai-workflow]]", "[[concepts/ai-coding-assistants]]", "[[concepts/spec-driven-development]]", "[[concepts/ai-pair-programming]]", "[[concepts/developer-experience-ai]]", "[[concepts/software-2-0]]", "[[concepts/vibe-coding]]", "[[concepts/ai-code-generation]]", "[[comparisons/codex-vs-claude-code]]", "[[comparisons/vibe-coding-vs-agentic-engineering]]"]
last_compiled: 2026-04-05
summary: "AI agents that autonomously write, test, debug, and ship code — from Devin's 2024 debut to Claude Code's $2.5B revenue, transforming developers from coders to coordinators."
---

## Overview

Agentic coding is the application of [[concepts/agentic-workflows]] to software development: AI agents that can autonomously read codebases, plan implementations, write code, run tests, debug failures, and iterate until the task is complete. Rather than autocompleting single lines of code, agentic coding systems handle entire implementation workflows end-to-end.

This represents the next stage of [[concepts/post-code-ai-workflow]] — a shift where developers move from writing code to defining goals and reviewing agent output. As Anthropic reports, the role change is "from coding to coordination," with engineers focusing on architecture, product thinking, and orchestrating multiple agents in parallel.

## Key Milestones

### Devin (March 2024)
[[entities/devin-ai]] by Cognition Labs was the first system marketed as a fully autonomous AI software engineer. It achieved 13.86% on SWE-bench at launch, 7x the previous state-of-the-art of 1.96%. Devin operates in a sandboxed environment with shell, editor, and browser — the same tools human developers use.

### Claude Code (February 2025 - present)
[[entities/claude-code]] launched as a research preview in February 2025, went GA in May 2025, and reached $1B annualized revenue by November 2025. By March 2026, revenue hit $2.5B. It reads full codebases, plans across multiple files, executes changes, runs tests, and iterates on failures.

### Computer Use (March 2026)
Claude gained the ability to interact with desktop GUIs — opening files, navigating browsers, clicking buttons, filling forms — expanding from code-only to full computer operation.

### SWE-bench Progress
The benchmark tells the story of rapid improvement:
- 2024 launch: 1.96% SOTA → Devin at 13.86%
- 2025: ~75% on SWE-bench Verified
- 2026: Claude Opus 4.5 leads at 80.9% on SWE-bench Verified

## The Developer Role Shift

Key data from Anthropic's 2026 research:
- Developers use AI in approximately **60%** of their work
- They can **fully delegate** only **0-20%** of tasks
- The gap reflects that agentic coding augments rather than replaces developers

The new developer workflow: define the goal, provide context (via CLAUDE.md files, task descriptions), let the agent implement, review and iterate on the output. Engineers who master this coordination skill ship faster while maintaining quality.

## Three Autonomous Coding Approaches

Pebblous identifies three distinct paths in 2025 agent frameworks:

1. **Reinforcement Learning** (agent-lightning, Microsoft): Train agents via reward signals. High performance but needs accurate reward functions.
2. **Self-Improvement** (hermes-agent, NousResearch): Agents accumulate reusable skills from successful tasks. Excellent for repetitive workflows.
3. **Test-Driven Development** (superpowers, obra): Write tests first, then generate code to pass them. 129K GitHub stars — resonates with code quality concerns.

All three are bottlenecked by [[concepts/data-quality-bottleneck]]: the more autonomous the agent, the more data quality determines the ceiling.

## Real-World Impact

- **Rakuten**: 7-hour autonomous task in a 12.5M-line codebase with 99.9% numerical accuracy
- **TELUS**: 13,000+ custom AI solutions, 30% faster engineering, 500,000+ hours saved
- **Zapier**: 89% AI adoption across the organization, 800+ agents deployed
- **Anthropic**: Majority of internal code now written by Claude Code

## Developer Requirements for Agentic IDEs (2025)

[[sources/redmonk-agentic-ides-2025]] identifies 10 must-haves that mark the shift from "AI Code Assistants" to "Agentic IDEs":

1. **Background agents** — Queue tasks for overnight/async execution
2. **Persistent memory** — Remember context across sessions
3. **Predictable pricing** — Token cost transparency (2025 saw pricing volatility)
4. **MCP integration** — [[concepts/model-context-protocol]] as standard protocol for external tools
5. **Multi-agent orchestration** — Dashboard for parallel agents
6. **Spec-driven development** — [[concepts/spec-driven-development]] as human-AI contracts
7. **Reliability** — Consistent performance under load
8. **Human-in-the-loop controls** — Prevent destructive autonomous actions
9. **Rollbacks** — Checkpoint and restore capability
10. **Skills** — Reusable, version-controlled workflow modules

44% of Claude-assisted work consisted of tasks engineers "wouldn't have enjoyed doing themselves" (Anthropic internal study).

## Multi-Agent Future (2026)

The next frontier is coordinated agent teams that divide complex projects into parallel workstreams, communicate mid-task, and deliver production-ready code. Gartner predicts 40% of enterprise applications will embed AI agents by end of 2026.

## Market Landscape (2025-2026)

Notable entrants: Windsurf, ByteDance Trae, AWS Kiro, IBM Project Bob, Augment Code (first ISO/IEC 42001 certified), JetBrains Junie, Google Antigravity. CLI agents (Claude Code, Cline, Aider, Continue.dev) gained significant traction among terminal-first developers. See [[concepts/ai-coding-assistants]] for the full landscape taxonomy.

## Sources

- [[sources/claude-code-agentic-coding]] — eight trends and real-world impact data
- [[sources/devin-ai-software-engineer]] — Devin as first autonomous coding agent
- [[sources/pebblous-agentic-framework-explosion]] — three paths in autonomous coding frameworks
- [[sources/redmonk-agentic-ides-2025]] — 10 developer requirements for agentic IDEs
- [[sources/faros-ai-coding-agents-2026]] — comprehensive 2026 competitive landscape
- [[sources/osmani-llm-coding-workflow-2026]] — practitioner workflow for supervising agents

## Related Concepts

- [[concepts/agentic-workflows]] — the broader paradigm
- [[concepts/swe-bench]] — the primary evaluation benchmark
- [[entities/claude-code]] — leading agentic coding tool
- [[entities/devin-ai]] — first autonomous coding agent
- [[concepts/post-code-ai-workflow]] — the workflow transformation
- [[concepts/ai-coding-assistants]] — the complete tool landscape
- [[concepts/spec-driven-development]] — planning practice for effective agentic coding
- [[concepts/ai-pair-programming]] — predecessor interaction model
- [[concepts/developer-experience-ai]] — how agentic tools reshape daily workflow
