---
title: "Source: Self-Reflective RAG with LangGraph"
type: source-summary
source: "[[raw/self-reflective-rag-langgraph]]"
related: ["[[concepts/agentic-rag]]", "[[concepts/self-rag]]", "[[concepts/corrective-rag]]", "[[entities/langgraph]]"]
last_compiled: 2026-04-05
summary: "LangChain's implementation guide for self-corrective RAG using LangGraph state machines — covering CRAG (web fallback on poor retrieval), Self-RAG (reflection tokens for quality control), and agentic orchestration."
reading_time: "2 min"
---

## Key Points

- Three RAG cognitive architectures: Chain, Routing, State Machines
- CRAG: retrieval evaluator + web fallback + knowledge refinement via document strip grading
- Self-RAG: four reflection tokens (Retrieve, ISREL, ISSUP, ISUSE) for quality control
- Agentic RAG is the superset: Router + Retriever + Grader + Generator + Hallucination Checker
- LangGraph implements state machine approach with loops and conditional transitions
- Pydantic-modeled outputs ensure consistent binary routing logic
- Full auditability via execution traces through state machine nodes

## Detailed Summary

This article from [[entities/langgraph]]'s team describes three increasingly sophisticated approaches to [[concepts/agentic-rag]]. The simplest (Chain) just retrieves and generates. Routing adds query-dependent retriever selection. State machines enable the self-reflective loops that define modern agentic RAG.

[[concepts/corrective-rag]] (CRAG) evaluates retrieval quality and falls back to web search when vectorstore results are poor. [[concepts/self-rag]] goes further by training reflection tokens directly into the model, enabling it to decide when to retrieve, assess relevance, check generation support, and grade usefulness.

The key insight is that Agentic RAG orchestrates all these capabilities through an external agent loop, meaning any LLM can be used without special fine-tuning.

## Related Concepts

- [[concepts/agentic-rag]] — the overarching paradigm
- [[concepts/self-rag]] — reflection token approach
- [[concepts/corrective-rag]] — web fallback approach
- [[entities/langgraph]] — the implementation framework
