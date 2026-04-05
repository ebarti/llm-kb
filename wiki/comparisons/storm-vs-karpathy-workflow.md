---
title: "STORM vs. Karpathy Workflow"
type: comparison
subjects: ["[[concepts/automated-wiki-creation]]", "[[concepts/llm-knowledge-base]]"]
sources: ["[[sources/storm-automated-wiki-creation]]", "[[sources/karpathy-llm-knowledge-bases]]"]
last_compiled: 2026-04-06
summary: "Comparing STORM's single-shot automated article generation from web search with Karpathy's persistent, accumulating knowledge base that grows through iterative compilation and the filing loop."
---

## Overview

STORM and Karpathy's LLM-KB represent two fundamentally different philosophies for using LLMs to create structured knowledge. [[entities/storm]] automates the creation of standalone reference articles by simulating multi-perspective research conversations and generating outlines from web search results. Karpathy's workflow builds a persistent, incrementally growing knowledge base from curated sources, where every query enriches the system through the filing loop. The choice between these approaches depends on whether you need one-off reference articles or an accumulating research knowledge system.

## Comparison Table

| Dimension | STORM | Karpathy LLM-KB |
|-----------|-------|-----------------|
| Mode | Single-shot article generation | Persistent, accumulating KB |
| Input | Web search results per topic | Curated raw/ source documents |
| Output | One standalone article per run | Full wiki with cross-linked articles |
| Persistence | None (ephemeral per run) | Full (wiki grows over time) |
| Compounding | None | Yes (filing loop: queries enrich KB) |
| Research method | Multi-perspective agent conversations | Human-curated ingestion + LLM compilation |
| Source control | Web search with reliability filtering | Human selects sources for raw/ |
| Evaluation | FreshWiki benchmark, Wikipedia editor rubrics | LLM linting, provenance to raw/ files |
| Human role | Specify topic | Curate sources, ask questions, validate |
| Best for | Standalone reference articles | Research synthesis, personal learning |
| Agent architecture | Multi-agent (perspective simulation) | Single LLM per phase |
| Infrastructure | Web search API + LLM | Markdown files + LLM + Obsidian |

## Detailed Analysis

**The pre-writing innovation**: STORM's core contribution is automating the pre-writing phase of article creation. Rather than retrieving information and directly generating text, it simulates the research process: identifying diverse perspectives, conducting simulated expert conversations, and synthesizing outlines before writing. This produces more balanced and comprehensive coverage than a single-perspective approach.

**The accumulation advantage**: Karpathy's system has a unique property that STORM lacks: compounding knowledge. Every query, every exploration, every linting pass adds to the knowledge base. Over time, the wiki becomes richer and more interconnected, making future queries more productive. STORM starts fresh with every run, producing excellent individual articles but building no persistent knowledge store.

**Source curation vs. web search**: A critical difference lies in source quality control. Karpathy's approach relies on human curation of what enters `raw/` -- the human decides which sources are trustworthy. STORM relies on web search with automated reliability filtering based on Wikipedia guidelines. The Karpathy approach provides stronger source quality guarantees at the cost of manual effort; STORM is more automated but susceptible to source bias.

**Complementary rather than competing**: These approaches are not mutually exclusive. One could use STORM to generate initial articles on new topics, then integrate those articles into a Karpathy-style persistent wiki for ongoing enrichment. The STORM output would seed the wiki; the filing loop would refine and extend it over time.

## When to Use Each

**Use STORM when:**
- You need a well-researched article on a well-defined topic
- The topic is broadly covered on the web (public knowledge)
- You want automated, hands-off article generation
- You do not need persistent knowledge accumulation

**Use Karpathy's LLM-KB when:**
- You are building deep expertise in a research domain over weeks or months
- Sources are curated and not freely available on the web
- You want every exploration to compound into the knowledge base
- You value human control over source selection and quality
- You need ongoing Q&A capability against an evolving knowledge base

## Sources

- [[sources/storm-automated-wiki-creation]] -- full STORM system description and evaluation
- [[sources/karpathy-llm-knowledge-bases]] -- Karpathy's original workflow description
