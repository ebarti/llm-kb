---
title: "LLM OS"
type: concept
sources: ["[[sources/karpathy-llm-os-concept]]", "[[sources/karpathy-2025-llm-year-review]]"]
related: ["[[concepts/software-2-0]]", "[[concepts/context-windows]]", "[[concepts/virtual-context-management]]", "[[concepts/llm-knowledge-base]]", "[[entities/andrej-karpathy]]"]
tags: [karpathy, LLM-OS, operating-system, architecture, software-3.0]
date_ingested: 2026-04-05
last_compiled: 2026-04-05
summary: "Karpathy's metaphor reframing LLMs not as chatbots but as the kernel of a new operating system: CPU (reasoning), RAM (context window), filesystem (RAG), with natural language as the programming interface."
---

## Overview

The LLM OS is [[entities/andrej-karpathy]]'s influential metaphor (September 2023) for understanding large language models as the kernel of a new computing platform rather than as conversational chatbots. The framework maps familiar OS concepts onto LLM capabilities, providing a mental model for building AI-native applications.

## The Architecture Mapping

| OS Concept | LLM Equivalent | Details |
|-----------|---------------|---------|
| CPU | Reasoning engine | The LLM's core inference capability |
| RAM | Context window | 128K-1M+ tokens of working memory |
| Filesystem | RAG / knowledge stores | External memory accessed via retrieval |
| Applications | Specialized prompts/tools | Task-specific capabilities |
| Heartbeat | Token generation rate | ~20 tokens/second processing rhythm |
| Kernel | The LLM itself | Orchestrates all resources and I/O |

## Key Ideas

- **Platform competition mirrors OS wars**: GPT, Claude, Gemini, and Llama compete like Windows, macOS, and Linux. Developers build on these platforms rather than creating intelligence from scratch.
- **Software 3.0**: Natural language prompts as the programming interface. "The hottest new programming language is English."
- **"Fallible savants"**: LLMs are brilliantly capable in some domains and embarrassingly weak in others — "jagged intelligence" rather than general competence.
- **"Iron Man suit" design**: Rather than full autonomy, build systems that augment humans through AI generation + human verification loops with adjustable autonomy levels.

## How It Connects

- **[[concepts/software-2-0]]** — LLM OS is the platform-level manifestation of the Software 2.0/3.0 evolution
- **[[concepts/context-windows]]** — The "RAM" of the LLM OS, with all its constraints
- **[[concepts/virtual-context-management]]** — OS-inspired memory management for LLMs (e.g., [[entities/memgpt]])
- **[[concepts/llm-knowledge-base]]** — A specific "application" running on the LLM OS
- **[[concepts/context-engineering]]** — The "systems programming" discipline for the LLM OS

## Implications for This Knowledge Base

The LLM-maintained wiki described by Karpathy is essentially an application running on the LLM OS. The raw files are the "disk," the summaries and indexes are the "file allocation table," the context window is the "RAM," and the LLM's reasoning is the "CPU" that transforms ingested knowledge into compiled wiki articles. Understanding this analogy clarifies the design choices in the KB architecture.

## Open Questions

- Will LLM "operating systems" converge (like POSIX) or fragment (like mobile)?
- How does the "RAM" constraint (context window) shape application architecture?
- When does the LLM OS metaphor break down — what aspects of LLMs resist OS analogy?

## Sources

- [[sources/karpathy-llm-os-concept]] — Original X thread and elaborations
- [[sources/karpathy-2025-llm-year-review]] — Retrospective on Cursor and Claude Code as LLM OS "applications"
