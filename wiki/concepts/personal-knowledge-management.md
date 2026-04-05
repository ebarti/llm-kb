---
title: "Personal Knowledge Management (PKM)"
type: concept
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/glenrhodes-karpathy-workflow]]", "[[sources/antigravity-post-code-ai-workflow]]"]
related: ["[[concepts/second-brain]]", "[[concepts/llm-knowledge-base]]", "[[concepts/obsidian-as-ide]]"]
last_compiled: 2026-04-05
summary: "The practice of capturing, organizing, and retrieving personal knowledge — transformed by LLMs from manual note-taking (Notion/Obsidian) to AI-compiled, queryable wikis with automatic synthesis and gap-filling."
---

## Overview

Personal Knowledge Management (PKM) refers to systematic approaches for managing what you know. Traditional tools (Notion, Obsidian, Roam, Logseq) require humans to write, tag, and link notes manually. LLMs have fundamentally changed this: instead of human-authored notes, an LLM can compile raw sources into structured, interlinked knowledge — with humans acting as curators and questioners rather than authors.

## Evolution: Manual → AI-Augmented → AI-Maintained

**Manual PKM (pre-2024):**
- Tools: Notion, Obsidian, Roam, Logseq, Evernote
- Human writes notes, creates tags, builds links manually
- Knowledge stays where you put it — no synthesis
- Problem: management overhead grows with scale; systems become unmaintainable

**AI-augmented PKM (2023–2024):**
- Tools: Notion AI, Obsidian Copilot, etc.
- Human still authors; AI helps with writing, search, Q&A
- Knowledge grows faster but structure is still human-maintained

**AI-maintained PKM (2025–present, Karpathy approach):**
- Human curates *what* to ingest; LLM handles *everything else*
- Compilation, linking, concept synthesis, Q&A, health checks — all automated
- Human role: curator, questioner, validator

## The Unsustainability Problem

Gallagher's experience with Notion/Obsidian is representative: elaborate systems become unmaintainable as priorities shift. "Complex structures became unmaintainable as priorities shifted. Management overhead quickly outweighed benefits." The LLM-maintained approach addresses this directly by removing the human from the compilation and maintenance loop.

## The Product Gap

Karpathy noted the current state is "a hacky collection of scripts." The PKM product landscape is wide open for tools that:
- Abstract the technical setup (LLM API, directory structure, Obsidian)
- Provide quality scoring and deduplication at ingestion
- Offer scheduled compilation, health checks, and alerts
- Enable non-technical users to run LLM-maintained wikis

## Sources
- [[sources/gallagher-second-brain-knowledge-graphs]] — practitioner journey from Notion/Obsidian to graph-based LLM KB
- [[sources/glenrhodes-karpathy-workflow]] — Karpathy's system as PKM evolution
- [[sources/antigravity-post-code-ai-workflow]] — identifies the product gap

## Related Concepts
- [[concepts/second-brain]] — the LLM-powered version
- [[concepts/llm-knowledge-base]] — Karpathy's specific approach
- [[concepts/obsidian-as-ide]] — current tooling
- [[concepts/knowledge-base-product-gap]] — the market opportunity
