---
title: "Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG"
source: "https://arxiv.org/abs/2501.09136"
author: "Various (arXiv)"
date_published: 2025-01-15
date_ingested: 2026-04-05
tags: [agentic-rag, agents, retrieval, survey, multi-agent]
type: paper
status: raw
discovered_via: search
---

# Agentic Retrieval-Augmented Generation: A Survey

## Core Problem & Solution

Traditional RAG systems suffer from static workflows and limited adaptability for complex tasks. Agentic RAG embeds autonomous AI agents into the RAG pipeline to overcome these constraints through dynamic retrieval management and iterative refinement.

## Key Design Patterns

The paper identifies agentic design patterns including "reflection, planning, tool use, and multi-agent collaboration" that enable systems to manage diverse operational structures from sequential processes to adaptive teamwork.

## Taxonomy Framework

Classification based on:
- Agent cardinality (single vs. multiple agents)
- Control structure (how agents coordinate)
- Autonomy levels (decision-making capacity)
- Knowledge representation approaches

## Critical Capabilities

Agentic RAG systems deliver "flexibility, scalability, and context-awareness across diverse applications" by allowing agents to dynamically adapt workflows rather than following predetermined paths.

## Architecture Components

Five core components: Router, Retriever, Grader, Generator, and Hallucination Checker — orchestrated through an agent loop that can use any LLM without fine-tuning and swap retrieval strategies dynamically.

## Application Domains

Implementations in healthcare, finance, education, and enterprise document processing.

## Research Gaps

Open challenges: evaluation methodologies, agent coordination mechanisms, memory management, computational efficiency, and governance frameworks for deployed systems.

## Relationship to Self-RAG and CRAG

Self-RAG improves how the model reasons over evidence; CRAG improves quality of evidence itself. Agentic RAG is the superset, orchestrating both through external agent loops.
