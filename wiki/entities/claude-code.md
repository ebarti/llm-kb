---
title: "Claude Code"
type: entity
entity_type: tool
sources: ["[[sources/claude-code-agentic-coding]]", "[[sources/faros-ai-coding-agents-2026]]", "[[sources/dextralabs-claude-cursor-copilot-30day]]", "[[sources/osmani-llm-coding-workflow-2026]]", "[[sources/qodo-ai-coding-assistants-2026]]"]
related: ["[[concepts/agentic-coding]]", "[[concepts/agentic-workflows]]", "[[entities/anthropic]]", "[[concepts/swe-bench]]", "[[concepts/model-context-protocol]]", "[[concepts/ai-coding-assistants]]", "[[comparisons/cursor-vs-claude-code-vs-copilot]]", "[[entities/cursor]]", "[[entities/github-copilot]]"]
last_compiled: 2026-04-05
summary: "Anthropic's agentic coding tool: reads codebases, edits files, runs tests, creates PRs — $2.5B annualized revenue by March 2026, leading SWE-bench Verified at 80.9%."
---

## Overview

Claude Code is [[entities/anthropic]]'s agentic coding system — a terminal-based tool that reads entire codebases, plans implementations across multiple files, executes changes, runs tests, and iterates on failures. It represents the most commercially successful [[concepts/agentic-coding]] product, reaching $2.5 billion in annualized revenue by March 2026.

## Key Features

- **Full codebase understanding**: Reads and navigates codebases of any size
- **Multi-file planning**: Plans implementations spanning many files
- **Test execution**: Runs test suites and iterates on failures
- **Git integration**: Commits, pushes, creates pull requests
- **Web browsing**: Reads documentation and searches the web
- **GitHub API**: Interacts with issues, PRs, and workflows
- **Computer Use** (March 2026): Opens files, navigates browsers, interacts with GUI applications

## Timeline

| Date | Milestone |
|------|-----------|
| February 2025 | Research preview launch |
| May 2025 | General availability |
| November 2025 | $1B annualized revenue |
| January 2026 | $1B annualized revenue (confirmed) |
| February 2026 | Claude Opus 4.6 released — tops agentic coding benchmarks |
| March 2026 | $2.5B annualized revenue; Computer Use capability added |

## Benchmark Performance

Claude Opus 4.5 leads [[concepts/swe-bench]] Verified with a score of 80.9% — resolving over 80% of real-world GitHub issues autonomously.

## Real-World Impact

- At Anthropic, the majority of code is now written by Claude Code
- Engineers focus on architecture, product thinking, and orchestrating multiple agents
- Available in terminal, IDE, desktop app, and browser

## Practitioner Assessment

Per [[sources/dextralabs-claude-cursor-copilot-30day]] (30-day head-to-head):
- **Backend:** 8.5/10 — "conversational depth" with clarifying questions before execution
- **Reasoning:** Superior for complex debugging; solved a 6-week production issue via rubber-duck questioning
- **Weakness:** Terminal-only interface limits frontend work; manual session management required
- **Verdict:** Best for deep reasoning and complex problem-solving; described as "the strongest coding brain"

Per [[sources/faros-ai-coding-agents-2026]]:
- Escalation path when other tools fail
- Higher costs offset by superior reasoning quality
- Most trusted for difficult, multi-file architectural problems

## Mentioned In

- [[sources/claude-code-agentic-coding]] — eight 2026 development trends and impact data
- [[sources/devin-ai-software-engineer]] — SWE-bench comparison
- [[sources/faros-ai-coding-agents-2026]] — top-tier agent with strongest reasoning
- [[sources/dextralabs-claude-cursor-copilot-30day]] — 30-day practitioner comparison
- [[sources/osmani-llm-coding-workflow-2026]] — recommended agentic tool in workflow
- [[sources/qodo-ai-coding-assistants-2026]] — Tier 4 CLI agent, $20-$200/mo
