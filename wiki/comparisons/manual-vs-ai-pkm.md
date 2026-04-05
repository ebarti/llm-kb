---
title: "Manual PKM vs AI-Maintained PKM"
type: comparison
subjects: ["[[concepts/personal-knowledge-management]]", "[[concepts/llm-knowledge-base]]", "[[concepts/agentic-knowledge-management]]"]
sources: ["[[sources/sebastien-agentic-knowledge-management]]", "[[sources/forte-building-second-brain]]", "[[sources/zettelkasten-de-introduction]]", "[[sources/llms-for-knowledge-work-arxiv]]"]
last_compiled: 2026-04-05
summary: "The four stages of PKM evolution compared: Manual (human writes everything), AI-assisted (AI helps with individual tasks), AI-maintained (LLM compiles and links), and Agentic (AI proactively monitors and acts) — tradeoffs in control, quality, scalability, and human role."
---

## Overview

Personal knowledge management is undergoing a fundamental transformation driven by LLMs. This comparison traces the four stages of that evolution, examining what changes at each stage and what is gained or lost.

## The Four Stages

### Stage 1: Manual PKM (Pre-2023)
**Examples**: Traditional [[concepts/zettelkasten]], [[concepts/para-method]], Obsidian/Notion without AI

| Dimension | Manual PKM |
|-----------|-----------|
| Who writes | Human |
| Who organizes | Human |
| Who connects | Human |
| Who retrieves | Human (search, browsing) |
| Scalability | Limited (~hundreds of notes before overhead dominates) |
| Quality ceiling | High (human judgment throughout) |
| Key weakness | Management overhead grows with scale; systems become unmaintainable |

### Stage 2: AI-Assisted PKM (2023-2024)
**Examples**: Notion AI, Obsidian Copilot, ChatGPT for drafting

| Dimension | AI-Assisted PKM |
|-----------|----------------|
| Who writes | Human (AI drafts) |
| Who organizes | Human |
| Who connects | Human (AI suggests) |
| Who retrieves | AI (semantic search, Q&A) |
| Scalability | Moderate improvement |
| Quality ceiling | High (human still validates) |
| Key weakness | Still human-bottlenecked for structure and maintenance |

### Stage 3: AI-Maintained PKM (2025)
**Examples**: Karpathy's [[concepts/llm-knowledge-base]], STORM

| Dimension | AI-Maintained PKM |
|-----------|-------------------|
| Who writes | LLM (compiles from raw sources) |
| Who organizes | LLM (creates structure, links, index) |
| Who connects | LLM (discovers and articulates relationships) |
| Who retrieves | LLM (reads index, navigates to relevant articles) |
| Scalability | High (~100s of articles, ~400K+ words) |
| Quality ceiling | Medium-high (depends on source quality + [[concepts/hallucination-contamination]] risk) |
| Key weakness | Human must validate; no proactive behavior |

### Stage 4: Agentic PKM (2025-2026)
**Examples**: [[concepts/agentic-knowledge-management]], OpenClaw, Notion v3.0 AI Agents

| Dimension | Agentic PKM |
|-----------|------------|
| Who writes | AI agents (continuously) |
| Who organizes | AI agents (proactively) |
| Who connects | AI agents (monitoring for new connections) |
| Who retrieves | AI agents (surfacing relevant knowledge unprompted) |
| Scalability | Highest (continuous autonomous operation) |
| Quality ceiling | Uncertain (trust and validation are open problems) |
| Key weakness | Security risks, hallucination propagation, trust deficit |

## Key Tradeoffs

### Control vs. Scalability
Manual PKM gives maximum control but doesn't scale. Agentic PKM scales infinitely but requires trusting AI with your knowledge infrastructure. The arXiv study found that 70% of knowledge workers want automation, but significant trust barriers remain.

### Quality vs. Volume
Human-written notes are higher quality per-note but fewer in number. AI-maintained systems produce more comprehensive coverage but with [[concepts/hallucination-contamination]] risk. The [[concepts/data-quality-bottleneck]] applies at every stage: garbage in, garbage out.

### Effort vs. Serendipity
The manual effort of Zettelkasten linking creates deeper understanding and more surprising connections. AI-generated links are faster but may be superficially obvious. The question is whether AI can replicate the "communication partner" quality that Luhmann valued — the system's ability to surprise you.

## The Human Role Across Stages

| Stage | Human Role |
|-------|-----------|
| Manual | Author, organizer, curator, questioner |
| AI-Assisted | Author, organizer, curator, questioner (AI helps with drafts) |
| AI-Maintained | **Curator**, questioner, validator (no longer writes or organizes) |
| Agentic | **Director**, validator (sets goals, approves actions) |

The shift from "author" to "curator" to "director" mirrors the broader transformation described in [[concepts/post-code-ai-workflow]].

## Sources
- [[sources/sebastien-agentic-knowledge-management]] — defines the agentic stage
- [[sources/forte-building-second-brain]] — the manual BASB methodology
- [[sources/zettelkasten-de-introduction]] — the manual Zettelkasten method
- [[sources/llms-for-knowledge-work-arxiv]] — evidence of adoption and trust barriers
