---
title: "Smart Connections"
type: entity
entity_type: tool
sources: ["[[sources/nxcode-obsidian-ai-second-brain-2026]]"]
related: ["[[entities/obsidian]]", "[[concepts/obsidian-ai-integration]]", "[[entities/obsidian-copilot]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Leading free Obsidian AI plugin using RAG to enable conversational queries across the entire vault — works with local (Ollama) and cloud models."
---

## Overview

Smart Connections is the leading RAG-based AI plugin for [[entities/obsidian]], enabling conversational queries across an entire vault. It uses embeddings to identify relevant notes, then grounds LLM responses in the user's personal knowledge base.

## Key Features

- **RAG-powered vault QA**: Ask questions in natural language, get answers grounded in your notes
- **Note discovery**: Identifies semantically related notes that may not be explicitly linked
- **Multi-model support**: Works with both local (Ollama) and cloud models (OpenAI, Anthropic)
- **Free and open-source**: No subscription required
- **AI-powered note connections**: Goes beyond wikilinks to find conceptual connections via embeddings

## Position in AI Plugin Landscape

Smart Connections occupies the "vault QA" niche in the [[concepts/obsidian-ai-integration]] landscape. Compared to [[entities/obsidian-copilot]] (which emphasizes multi-model chat and composition), Smart Connections focuses specifically on vault-grounded retrieval. Its RAG approach is relevant to the [[concepts/rag-vs-index-based-retrieval]] debate: it demonstrates that vector-based retrieval adds value even for personal vaults, particularly for discovering non-obvious connections between notes.

## Mentioned In

- [[sources/nxcode-obsidian-ai-second-brain-2026]] — identified as the dominant AI plugin for vault-wide queries
