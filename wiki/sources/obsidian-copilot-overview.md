---
title: "Source: Copilot for Obsidian Overview"
type: source-summary
source: "[[raw/obsidian-copilot-overview]]"
related: ["[[entities/obsidian-copilot]]", "[[concepts/obsidian-ai-integration]]", "[[entities/obsidian]]"]
last_compiled: 2026-04-05
summary: "Copilot for Obsidian: model-agnostic AI assistant with vault search, RAG, project workspaces, inline editing, and 100K+ users — all data stored as plain markdown."
---

## Key Points

- 100,000+ users, won "Best LLM Integration Award 2024" from Obsidian
- Model-agnostic: supports OpenAI, Anthropic, Google, LM Studio, Ollama, and any OpenAI-compatible model
- All data (memory, chat history, system prompts, custom commands) stored as plain markdown in the vault
- Project workspaces with isolated models, system prompts, and chat history per project
- Supports 50+ file types including PDFs, images, and Office documents
- Lexical search (no setup) and semantic indexing for deeper recall
- 2026 features: web tab reading, YouTube clipper, Quick Ask floating panel, side-by-side diff view
- Free with BYOK; Copilot Plus offers lifetime access via one-time payment
- Companion app "Miyo" provides desktop semantic search

## Detailed Summary

[[entities/obsidian-copilot]] represents the most mature AI integration for Obsidian, distinguishing itself through model agnosticism and data ownership principles aligned with Obsidian's [[concepts/file-over-app]] philosophy. By storing all AI-related data as plain markdown files in the vault, Copilot avoids the database lock-in that plagues many AI tools.

The project workspaces feature is particularly relevant to the LLM-KB workflow: each project can have its own model selection, system prompt, and context window, enabling different AI configurations for different knowledge domains without interference.

The 2026 updates show convergence with the LLM-KB approach: web clipper commands, YouTube transcription, and URL fetching mirror the INGEST operation. The composer with diff preview mirrors the COMPILE operation. What's missing compared to the full LLM-KB architecture is the structured compilation pipeline — Copilot assists with individual notes rather than maintaining a complete wiki structure.

## Related Concepts

- [[entities/obsidian-copilot]] — the tool described
- [[concepts/obsidian-ai-integration]] — the broader AI integration landscape
- [[concepts/file-over-app]] — Copilot follows this by storing all data as markdown
