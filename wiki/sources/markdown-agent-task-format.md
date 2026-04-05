---
title: "Source: The Case for Markdown as Your Agent's Task Format"
type: source-summary
source: "[[raw/markdown-agent-task-format]]"
related: ["[[concepts/markdown-as-universal-interface]]", "[[concepts/yaml-frontmatter]]", "[[concepts/markdown-for-ai-agents]]"]
last_compiled: 2026-04-05
summary: "Advocates markdown+YAML frontmatter over JSON for AI agent task management: human-readable, git-native, agent-compatible, with Unix tooling for querying."
reading_time: "2 min"
---

## Key Points

- JSON creates friction: unreadable terminal output, noisy git diffs, syntax-heavy editing
- Markdown + YAML frontmatter combines structured metadata with natural language context
- AI agents already understand markdown from training data — no additional parsing needed
- Git version control becomes built-in project management with meaningful diffs
- Kanban boards can be implemented as directory structures queryable via grep/shell

## Detailed Summary

This article extends the markdown-as-universal-interface argument into a new domain: AI agent task management. Rather than storing task definitions in JSON (the typical machine-readable format), the author proposes markdown files with YAML frontmatter for structured metadata and markdown body for natural language context.

The key insight is that in an AI-agent workflow, the "reader" of task files is not just a machine parser but an LLM — and LLMs read markdown natively. This eliminates the traditional JSON-vs-readable-text tradeoff: markdown IS both machine-readable (to LLMs) and human-readable.

The article acknowledges limitations: event logs still benefit from JSONL, configuration from YAML/TOML, and message routing from Maildir conventions. The argument is specifically about the human-agent communication interface, not all machine-to-machine protocols.

## Related Concepts

- [[concepts/markdown-as-universal-interface]] — markdown as the bridge between human and AI communication
- [[concepts/yaml-frontmatter]] — structured metadata within markdown
- [[concepts/markdown-for-ai-agents]] — the specific use case of agents consuming markdown
- [[concepts/llm-knowledge-base]] — a related system where LLMs consume/produce markdown
