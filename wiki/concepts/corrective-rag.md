---
title: "Corrective RAG (CRAG)"
type: concept
sources: ["[[sources/self-reflective-rag-langgraph]]", "[[sources/agentic-rag-survey]]"]
related: ["[[concepts/agentic-rag]]", "[[concepts/self-rag]]", "[[concepts/retrieval-augmented-generation]]", "[[concepts/rag-hallucinations]]"]
last_compiled: 2026-04-05
summary: "A RAG enhancement that evaluates retrieval quality via a lightweight evaluator, falls back to web search when vectorstore results are poor, and refines knowledge by grading individual document strips."
---

## Overview

Corrective RAG (CRAG) is an advanced [[concepts/retrieval-augmented-generation]] technique that focuses on improving the **quality and robustness of retrieved evidence** before it reaches the generation stage. While [[concepts/self-rag]] improves how the model reasons over evidence, CRAG improves the evidence itself.

## Three Key Innovations

### 1. Retrieval Evaluator
A lightweight evaluator assesses the overall quality of retrieved documents for a query, returning a **confidence score** for each document. This determines whether the retrieved evidence is sufficient for answering the query, or whether additional sources are needed.

### 2. Web Search Supplementation
When the vectorstore retrieval is deemed **ambiguous or irrelevant** (based on evaluator scores), CRAG automatically invokes web search to supplement the context. The query is rewritten to optimize for web search effectiveness. This fallback mechanism ensures the system isn't limited to the quality and coverage of its indexed document collection.

### 3. Knowledge Refinement
Retrieved documents are **partitioned into strips** (smaller segments), and each strip is graded individually for relevance. Irrelevant strips are filtered out, leaving only the most pertinent information for the generator. This fine-grained filtering prevents irrelevant content within otherwise-relevant documents from distracting the LLM.

## Implementation with LangGraph

The [[entities/langgraph]] implementation simplifies the original CRAG paper:
- If **any** retrieved document is judged irrelevant, web search is triggered
- Query rewriting optimizes the web search query
- Both vectorstore and web results are available to the generator
- Pydantic-modeled outputs ensure consistent binary routing logic

## When CRAG Helps Most

CRAG is particularly valuable when:
- The vectorstore has incomplete coverage of the knowledge domain
- Queries may fall outside the scope of indexed documents
- Information freshness matters (web search provides current data)
- The cost of a wrong answer is high (medical, legal, financial domains)

## Sources

- [[sources/self-reflective-rag-langgraph]] — LangGraph implementation
- [[sources/agentic-rag-survey]] — positioning in agentic RAG taxonomy

## Related Concepts

- [[concepts/self-rag]] — complementary approach focused on reasoning quality
- [[concepts/agentic-rag]] — the orchestrating superset
- [[concepts/rag-hallucinations]] — the problem CRAG mitigates
- [[concepts/retrieval-augmented-generation]] — the base pipeline
