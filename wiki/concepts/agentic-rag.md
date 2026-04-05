---
title: "Agentic RAG"
type: concept
sources: ["[[sources/agentic-rag-survey]]", "[[sources/self-reflective-rag-langgraph]]", "[[sources/ragflow-rag-review-2025]]"]
related: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/self-rag]]", "[[concepts/corrective-rag]]", "[[concepts/multi-agent-systems]]", "[[entities/langgraph]]"]
last_compiled: 2026-04-05
summary: "The current frontier of RAG: autonomous agents orchestrate retrieval through reflection, planning, and tool use — dynamically adapting pipelines with routers, graders, generators, and hallucination checkers."
---

## Overview

Agentic RAG represents the current frontier of [[concepts/retrieval-augmented-generation]], embedding autonomous AI agents into the RAG pipeline to overcome the static, predetermined workflows of traditional systems. Rather than following a fixed retrieve-then-generate path, agentic systems dynamically adapt their behavior: deciding when to retrieve, evaluating retrieval quality, choosing between multiple retrieval strategies, and self-correcting when outputs are unsupported by evidence.

The 2025 arXiv survey on Agentic RAG identifies four key design patterns: **reflection** (evaluating and correcting own outputs), **planning** (decomposing complex queries into sub-tasks), **tool use** (dynamically selecting retrieval tools and external APIs), and **multi-agent collaboration** (coordinating specialized agents for different aspects of the pipeline).

## Architecture

The canonical agentic RAG architecture consists of five orchestrated components:

1. **Router**: Analyzes the incoming query and determines the appropriate retrieval strategy — vectorstore search, web search, SQL query, or direct generation without retrieval
2. **Retriever**: Executes the chosen retrieval strategy, potentially using [[concepts/hybrid-search]] combining multiple methods
3. **Grader**: Evaluates whether retrieved documents are relevant and sufficient for answering the query
4. **Generator**: Produces the response, grounded in the retrieved and graded evidence
5. **Hallucination Checker**: Verifies that the generated response is actually supported by the retrieved documents

These components are orchestrated through an **agent loop** implemented as a state machine (e.g., via [[entities/langgraph]]), enabling conditional transitions, retry logic, and fallback strategies.

## Cognitive Architectures

The LangChain team identifies three levels of RAG cognitive architecture:

| Architecture | Description | Self-Correction | Complexity |
|---|---|---|---|
| **Chain** | Linear retrieve → generate | None | Low |
| **Routing** | Query-dependent retriever selection | None | Medium |
| **State Machine** | Loops, conditionals, retry logic | Full | High |

Agentic RAG operates at the state machine level, enabling flow engineering with specific decision points and retry mechanisms.

## Key Sub-Patterns

### Self-RAG (Self-Reflective RAG)
[[concepts/self-rag]] trains four reflection tokens into the model: **Retrieve** (should I fetch documents?), **ISREL** (is this passage relevant?), **ISSUP** (is my generation supported by evidence?), and **ISUSE** (how useful is this response?). This enables the model to introspect about retrieval necessity and output quality without external tools.

### Corrective RAG (CRAG)
[[concepts/corrective-rag]] focuses on evidence quality through three mechanisms: a lightweight retrieval evaluator that scores document relevance, web search supplementation when vectorstore retrieval is poor, and knowledge refinement that partitions documents into strips and grades them individually.

### Relationship Between Patterns
In simple terms: Self-RAG improves **reasoning** over evidence, CRAG improves the **quality of evidence** itself, and Agentic RAG is the **orchestrating superset** that can employ both strategies plus any additional tools. A key advantage of the agentic approach is that any LLM can be used without special fine-tuning, and retrieval strategies can be swapped dynamically.

## Taxonomy

The arXiv survey classifies agentic RAG systems along four dimensions:

- **Agent cardinality**: Single agent vs. multi-agent collaboration
- **Control structure**: How agents coordinate (sequential, parallel, hierarchical)
- **Autonomy level**: Degree of independent decision-making
- **Knowledge representation**: Vector store, knowledge graph, SQL, hybrid

## Application Domains

Agentic RAG has been implemented across healthcare (multi-step clinical reasoning), finance (dynamic data source selection), education (adaptive tutoring with verified citations), and enterprise document processing (complex multi-hop queries across document collections).

## Open Challenges

- **Evaluation**: How to benchmark self-corrective systems (existing metrics focus on single-pass quality)
- **Coordination**: Optimal strategies for multi-agent retrieval collaboration
- **Memory management**: Maintaining state across extended agent interactions
- **Computational cost**: Agent loops multiply inference costs
- **Governance**: Auditability and control over autonomous retrieval decisions

## Sources

- [[sources/agentic-rag-survey]] — comprehensive taxonomy and classification
- [[sources/self-reflective-rag-langgraph]] — practical implementation with LangGraph
- [[sources/ragflow-rag-review-2025]] — positioning within RAG evolution

## Related Concepts

- [[concepts/retrieval-augmented-generation]] — the base paradigm being enhanced
- [[concepts/self-rag]] — reflection token sub-pattern
- [[concepts/corrective-rag]] — evidence quality sub-pattern
- [[concepts/multi-agent-systems]] — broader context of agent collaboration
- [[concepts/rag-hallucinations]] — the problem agentic RAG mitigates
