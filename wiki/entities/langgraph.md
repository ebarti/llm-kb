---
title: "LangGraph"
type: entity
entity_type: tool
sources: ["[[sources/self-reflective-rag-langgraph]]", "[[sources/agentic-rag-survey]]"]
related: ["[[concepts/agentic-rag]]", "[[concepts/self-rag]]", "[[concepts/corrective-rag]]", "[[concepts/multi-agent-systems]]"]
last_compiled: 2026-04-05
summary: "LangChain's framework for building stateful, multi-step LLM applications as state machines with cycles, conditional logic, and agent loops — the primary implementation platform for agentic RAG."
---

## Overview

LangGraph is a framework from the LangChain team for building stateful, multi-step LLM applications using a **state machine** architecture. Unlike simple chain-based workflows, LangGraph supports cycles (loops), conditional branching, and persistent state — making it the primary implementation platform for [[concepts/agentic-rag]] systems.

## Key Features

- **State machine architecture**: Nodes (processing steps) connected by edges (transitions) with conditional routing
- **Cycles and loops**: Essential for self-corrective workflows (retry, re-retrieve, re-evaluate)
- **Persistent state**: Maintains context across multiple agent steps
- **Execution traces**: Full auditability of decision-making paths through the graph

## Role in Agentic RAG

LangGraph enables the "flow engineering" that distinguishes [[concepts/agentic-rag]] from simple RAG chains. It implements:

- **[[concepts/self-rag]]**: Reflection tokens evaluated at each node, with conditional transitions based on quality assessment
- **[[concepts/corrective-rag]]**: Retrieval evaluation → web search fallback → knowledge refinement as a directed graph with conditional edges
- **Full agentic RAG**: Router → Retriever → Grader → Generator → Hallucination Checker as an orchestrated state machine

## Implementation Patterns

Both Self-RAG and CRAG implementations use Pydantic-modeled outputs as OpenAI tools to ensure "consistent binary logic" for conditional routing, enabling deterministic graph traversal based on LLM-generated assessments.

## Mentioned In

- [[sources/self-reflective-rag-langgraph]] — implementation of Self-RAG and CRAG
- [[sources/agentic-rag-survey]] — cited as key implementation framework
