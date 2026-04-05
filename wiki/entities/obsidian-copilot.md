---
title: "Obsidian Copilot"
type: entity
entity_type: tool
sources: ["[[sources/obsidian-copilot-overview]]", "[[sources/nxcode-obsidian-ai-second-brain-2026]]"]
related: ["[[entities/obsidian]]", "[[concepts/obsidian-ai-integration]]", "[[entities/smart-connections]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/file-over-app]]"]
last_compiled: 2026-04-05
summary: "The #1 downloaded AI plugin for Obsidian (100K+ users): model-agnostic chat assistant with vault RAG, project workspaces, diff-preview composer, and all data stored as plain markdown."
---

## Overview

Obsidian Copilot is the most widely adopted AI integration for [[entities/obsidian]], with over 100,000 users. Created by Logan Yang, it won the "Best LLM Integration Award 2024" from Obsidian and is the #1 AI plugin by downloads.

Copilot operates as an in-vault AI assistant with chat-based vault search, multi-model support, and expanding agentic capabilities. It distinguishes itself through model agnosticism and alignment with Obsidian's [[concepts/file-over-app]] philosophy — all data (memory, chat history, system prompts, custom commands) is stored as plain markdown files in the vault.

## Key Features

**Model Agnostic**: Supports OpenAI, Anthropic, Google, LM Studio, Ollama, and any OpenAI-compatible model. Users can switch providers without ecosystem lock-in.

**Vault Search & RAG**: Lexical search (zero setup) and semantic indexing for deep recall across thousands of notes. Surfaces related notes with inline citations. Drag-and-drop linking.

**Project Workspaces**: Isolated contexts with customizable models, system prompts, and chat history per project. Supports 50+ file types including PDFs, images, Office documents.

**Composer**: Rewrite or expand notes with diff preview (inline or side-by-side) before accepting changes.

**Self-Hosting**: Supports local or self-hosted models for full privacy.

## 2026 Updates

- Read web tabs directly in Obsidian
- Built-in YouTube and web clipper slash commands with mindmap generation
- Custom system prompt system with prompts stored as markdown files
- "Quick Ask" floating panel for inline AI questions at cursor position
- Side-by-side diff view for composer edits
- Companion desktop app "Miyo" with semantic search engine

## Pricing

- **Free**: Community plugin with bring-your-own-key (BYOK)
- **Copilot Plus**: Lifetime access with one-time payment

## Comparison with LLM-KB Approach

Copilot's web clipper commands mirror the LLM-KB INGEST operation. The composer with diff preview mirrors COMPILE. However, Copilot assists with individual notes rather than maintaining a complete, structured wiki. The LLM-KB approach (Claude Code + MCP) operates externally with full file system access, enabling systematic compilation that Copilot's plugin sandbox cannot achieve.

## Mentioned In

- [[sources/obsidian-copilot-overview]] — comprehensive feature overview
- [[sources/nxcode-obsidian-ai-second-brain-2026]] — listed as top AI plugin alongside Smart Connections
