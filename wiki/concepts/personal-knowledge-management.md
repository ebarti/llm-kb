---
title: "Personal Knowledge Management (PKM)"
type: concept
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/glenrhodes-karpathy-workflow]]", "[[sources/antigravity-post-code-ai-workflow]]", "[[sources/forte-building-second-brain]]", "[[sources/zettelkasten-de-introduction]]", "[[sources/sebastien-agentic-knowledge-management]]", "[[sources/memex-vannevar-bush]]", "[[sources/llms-for-knowledge-work-arxiv]]"]
related: ["[[concepts/second-brain]]", "[[concepts/llm-knowledge-base]]", "[[concepts/obsidian-as-ide]]", "[[concepts/zettelkasten]]", "[[concepts/evergreen-notes]]", "[[concepts/digital-garden]]", "[[concepts/para-method]]", "[[concepts/progressive-summarization]]", "[[concepts/spaced-repetition]]", "[[concepts/memex-and-tools-for-thought]]", "[[concepts/agentic-knowledge-management]]", "[[concepts/networked-thought]]"]
last_compiled: 2026-04-05
summary: "The practice of capturing, organizing, and retrieving personal knowledge — transformed by LLMs from manual note-taking (Notion/Obsidian) to AI-compiled, queryable wikis with automatic synthesis and gap-filling."
reading_time: "2 min"
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

## The Full PKM Methodology Landscape

Beyond the AI evolution, PKM encompasses a rich ecosystem of pre-AI methodologies that remain influential:

### Classical Methodologies
- [[concepts/zettelkasten]] — Luhmann's atomic, hypertextually linked note system (1950s–1998)
- [[concepts/para-method]] + [[concepts/progressive-summarization]] — Forte's BASB: organize by actionability, distill in layers (2017)
- [[concepts/evergreen-notes]] — Matuschak's durable, concept-oriented notes that accumulate insight (2019)
- [[concepts/digital-garden]] — public, continuously evolving knowledge sharing with epistemic status markers
- [[concepts/spaced-repetition]] — complementary retention system ensuring knowledge is recallable ([[entities/anki]])

### Historical Lineage
- [[concepts/memex-and-tools-for-thought]] — from Bush's 1945 memex through Engelbart, Nelson, and Berners-Lee to modern PKM tools

### AI Frontier
- [[concepts/agentic-knowledge-management]] — AI agents proactively monitor and act on knowledge bases (2025–2026)

## Sources
- [[sources/gallagher-second-brain-knowledge-graphs]] — practitioner journey from Notion/Obsidian to graph-based LLM KB
- [[sources/glenrhodes-karpathy-workflow]] — Karpathy's system as PKM evolution
- [[sources/antigravity-post-code-ai-workflow]] — identifies the product gap
- [[sources/forte-building-second-brain]] — BASB: CODE + PARA methodology
- [[sources/zettelkasten-de-introduction]] — canonical Zettelkasten method guide
- [[sources/sebastien-agentic-knowledge-management]] — defines the agentic PKM frontier
- [[sources/memex-vannevar-bush]] — historical lineage from 1945
- [[sources/llms-for-knowledge-work-arxiv]] — empirical evidence of LLM adoption in knowledge work

## Related Concepts
- [[concepts/second-brain]] — the LLM-powered version
- [[concepts/llm-knowledge-base]] — Karpathy's specific approach
- [[concepts/obsidian-as-ide]] — current tooling
- [[concepts/knowledge-base-product-gap]] — the market opportunity

## Related Entities

- [[entities/andrej-karpathy]] — pioneer of LLM-maintained PKM
- [[entities/sam-gallagher]] — graph-based PKM practitioner
- [[entities/notion]] — traditional PKM tool
- [[entities/vannevar-bush]] — historical vision (Memex)
- [[entities/memex]] — 1945 proto-hypertext personal knowledge device

## Related Comparisons

- [[comparisons/manual-pkm-vs-llm-pkm]] — traditional vs. AI-maintained PKM
