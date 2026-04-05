---
title: "Self-Reflective RAG with LangGraph"
source: "https://blog.langchain.com/agentic-rag-with-langgraph/"
author: "LangChain Team"
date_published: 2024-06-15
date_ingested: 2026-04-05
tags: [self-rag, crag, agentic-rag, langgraph, reflection, retrieval]
type: article
status: raw
discovered_via: search
---

# Self-Reflective RAG with LangGraph

## Core Concept

Self-reflective RAG uses an LLM to "self-correct poor quality retrieval and/or generations" through iterative feedback loops rather than simple linear pipelines.

## Cognitive Architectures for RAG

Three architectural approaches:
1. **Chain**: LLM generates answers based on retrieved documents
2. **Routing**: LLM selects between different retrievers based on query characteristics
3. **State Machines**: Enable loops and conditional transitions — ideal for self-reflective systems

LangGraph implements the state machine approach, allowing "flow engineering" with specific decision points and retry mechanisms.

## CRAG (Corrective RAG)

Three key innovations:
- **Retrieval evaluator**: Assesses document quality with confidence scoring
- **Web supplementation**: Invokes web search when vectorstore retrieval is ambiguous or irrelevant
- **Knowledge refinement**: Partitions documents into strips, grades them individually, filters irrelevant content

Implementation triggers web search if any document is irrelevant, uses query rewriting to optimize web searches.

## Self-RAG

Uses four reflection tokens trained into the model:
- **Retrieve**: Determines whether to fetch documents (yes/no/continue)
- **ISREL**: Evaluates passage relevance to questions
- **ISSUP**: Checks whether generation is supported by retrieved chunks
- **ISUSE**: Grades generation usefulness (scale 1-5)

Practical implementation grades all documents collectively, performing single generation from relevant chunks rather than per-chunk generation, reducing latency while maintaining quality checks.

## Agentic RAG (Superset)

Agentic RAG orchestrates all components through an external agent loop with five components: Router, Retriever, Grader, Generator, and Hallucination Checker. Can use any LLM without fine-tuning, swap retrieval strategies dynamically, and add/remove components as needed.

## Implementation

Both CRAG and Self-RAG use Pydantic-modeled outputs as OpenAI tools for "consistent binary logic" for conditional routing. Execution traces demonstrate clear node progression through the state machine, enabling full auditability.
