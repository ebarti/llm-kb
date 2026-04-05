---
title: "LLM Knowledge Bases: A System Architecture Overview"
source: "https://academy.dair.ai/blog/llm-knowledge-bases-karpathy"
author: "DAIR.AI Academy (Elvis Saravia)"
date_published: 2026-04-01
date_ingested: 2026-04-05
tags: [llm-knowledge-base, wiki-compilation, obsidian, rag, architecture]
type: article
status: raw
discovered_via: search
---

# LLM Knowledge Bases: A System Architecture Overview

## Introduction

Andrej Karpathy recently presented an approach to constructing personal knowledge management systems using LLMs. Rather than relying on vector databases or complex retrieval-augmented generation (RAG) pipelines, his methodology employs a structured markdown wiki that an LLM gradually assembles and refines.

## Core Architecture

The system treats the language model as a "compiler" that ingests raw documents and generates a structured, cross-referenced knowledge repository. The wiki itself functions as the knowledge base—no embeddings or vector similarity search required at the scale of individual knowledge management.

## Four-Phase Operational Cycle

### Phase 1: Ingestion
Raw materials enter from multiple channels:
- Web articles transform into markdown files via Obsidian Web Clipper, with images stored locally
- Research papers and code repositories from academic and development sources accumulate in a `raw/` staging area
- All content initially lands in the `raw/` directory for LLM processing

### Phase 2: Compilation
The LLM incrementally constructs the structured knowledge system:
- **Index files** containing brief summaries serve as query entry points
- **Concept articles** (~100 documents, ~400K total words) organized thematically with internal references
- **Derived artifacts** including presentation decks, visualizations, and filed responses
- Automatic **link mapping** connecting related concepts

### Phase 3: Query and Enhancement
The system becomes operationally useful:
- **Obsidian IDE** enables wiki browsing and graph visualization
- **Q&A agents** handle complex research inquiries, producing markdown, slides, or charts
- **Search functionality** provides naive retrieval via web interface or CLI
- Query results feed back into the wiki continuously

### Phase 4: Maintenance and Validation
The LLM performs systematic checks:
- Data consistency verification
- Missing information recovery via web search
- Cross-concept connection identification
- Exploratory question generation

After validation, the cycle returns to compilation with the wiki expanding iteratively.

## Distinguishing Advantages

**No vector infrastructure needed** at personal scale (~100 articles)—index files plus context windows suffice.

**Cumulative exploration**—each query, visualization, and answer integrates into the knowledge base.

**Automated writing**—manual wiki editing becomes unnecessary; the LLM manages compilation, linking, and maintenance.

**Incremental updates**—new materials integrate into existing structures without reprocessing.

## Future Directions

Karpathy envisions leveraging the wiki to create synthetic training datasets for fine-tuning models, effectively encoding knowledge into model weights rather than relying solely on context windows.

## Implementation Requirements

The necessary tooling remains straightforward:
- Obsidian as IDE and file viewer
- Obsidian Web Clipper for content ingestion
- An LLM with sufficient context capacity
- Markdown directory structure

The key innovation centers on the workflow pattern: having an LLM progressively construct and sustain a structured knowledge repository from unprocessed sources, with every interaction contributing to system growth.

## Author's Extension: Research-Focused Implementation

The article author describes building an agent-based research indexing system. Using Obsidian for markdown storage and the qmd CLI tool for semantic indexing, hundreds of research papers become queryable and explorable. Interactive visualization artifacts generated through MCP tools within an agent orchestrator create a highly personalized research environment.
