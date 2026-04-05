---
title: "Karpathy's LLM Knowledge Bases: The Post-Code AI Workflow"
source: "https://antigravity.codes/blog/karpathy-llm-knowledge-bases"
author: "Antigravity Codes"
date_published: 2026-04-04
date_ingested: 2026-04-05
tags: [llm-knowledge-base, post-code, workflow, agentic-ai, knowledge-management]
type: article
status: raw
discovered_via: search
---

# Karpathy's LLM Knowledge Bases: The Post-Code AI Workflow

## Core Concept

Andrej Karpathy has shifted his focus from code generation to **knowledge compilation**. As he stated, "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge."

His approach involves using LLMs to automatically compile raw source documents into structured, interconnected markdown wikis that serve as queryable knowledge substrates.

## The 6-Step Workflow

### 1. Data Ingestion
Raw documents—articles, papers, repositories, datasets, images—go into a `raw/` directory. Karpathy uses the Obsidian Web Clipper to convert web content to markdown and downloads images locally for LLM reference.

### 2. LLM Compilation
An LLM incrementally transforms raw materials into a structured wiki with:
- Article summaries across all source documents
- Backlinks between related concepts
- Categorized content architecture
- Full concept articles with cross-references

### 3. Scale
Once reaching critical mass (Karpathy's example: ~100 articles, ~400,000 words), the wiki becomes powerful enough for the LLM to answer complex, multi-step research questions requiring hours of manual synthesis.

### 4. Querying
Users ask the LLM sophisticated questions; it follows links, synthesizes across articles, and provides comprehensive answers grounded in the knowledge base.

### 5. Multi-Format Output
Results render as markdown files, Marp slide decks, or Matplotlib visualizations, all viewable in Obsidian.

### 6. Health Checks
Automated "linting" identifies inconsistencies, discovers missing connections, and flags outdated information.

## Evolution of Karpathy's Approach

| Period | Concept | Shift |
|--------|---------|-------|
| Feb 2025 | Vibe Coding | Accept all AI-generated code without review |
| Dec 2025 | "Never felt this behind" | Recognition of magnitude shift in AI capabilities |
| Jan 2026 | Agentic Engineering | Orchestrate AI agents with human oversight |
| Apr 2026 | **LLM Knowledge Bases** | **Move beyond code to knowledge orchestration** |

## Real-World Applications

- **Competitive Intelligence**: Ingest competitor websites, job postings, filings; compile strategic analysis
- **Technical Due Diligence**: Analyze architecture patterns, debt signals, team expertise distribution
- **Literature Reviews**: Compile methodology comparisons, citation networks, research gaps
- **Developer Documentation**: Create queryable knowledge bases about internal decisions and architecture
- **Product Research**: Synthesize user feedback into pain point analysis and feature prioritization
- **Compliance**: Map regulatory requirements to current controls and surface gaps
- **Personal Learning**: Build structured curricula from articles and tutorials

## Key Community Reactions

**Steph Ango (Obsidian CEO)** recommended vault separation: maintain a clean personal vault and a separate "messy vault" for agent-generated content, preventing contamination of human-curated knowledge.

**Elvis Saravia (DAIR.AI)** confirmed the pattern's effectiveness, emphasizing that proper data structure is foundational to LLM-based knowledge curation and discovery.

The **Graph RAG connection** emerged: Karpathy's approach represents a manual, markdown-based implementation of graph-based retrieval, visualizing interconnected knowledge nodes.

## Critical Concern: Contamination Risk

The main risk identified: hallucinated connections could corrupt the wiki and influence future queries. Mitigation strategies include tracing all claims back to `raw/` source files and running systematic health checks.

## Minimum Viable Setup

```
my-research/
  raw/          # Source documents
  wiki/         # LLM-compiled output
  output/       # Query results, slides, charts
  _meta/        # Compilation state
```

**Steps:**
1. Install Obsidian + Web Clipper
2. Populate `raw/` with source materials
3. Write a compilation prompt specifying wiki rules
4. Run LLM compilation (incremental updates after first run)
5. Query the wiki with complex questions
6. Schedule automated health checks

## Advanced Patterns

- **Multi-source ingestion**: Automate input from web articles, PDFs, YouTube transcripts, GitHub repos, podcasts, RSS feeds
- **Compilation profiles**: Different strategies for research vs. competitive intelligence vs. learning wikis
- **Scheduled checks**: Daily incremental builds, weekly consistency audits, monthly fact verification
- **Cross-wiki linking**: Surface connections across separate knowledge bases
- **Version control**: Git-track markdown for history, diffing, and rollback capability

## Why This Matters

**From code generation to knowledge orchestration**: Once LLMs solve code generation adequately, the bottleneck shifts to understanding problem domains deeply enough to know what to build.

**Markdown as universal interface**: The entire workflow uses markdown—human-readable, LLM-friendly, version-controllable, tool-agnostic, and future-proof.

**Developer role transformation**: Developers become curators and questioners rather than coders or agent orchestrators. They decide what to ingest, what to ask, and how to validate; LLMs handle organization and maintenance.

The developers who thrive will be those with the strongest knowledge systems—structured, maintained, queryable repositories giving AI agents the context for exceptional work.
