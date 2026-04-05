---
title: "RAG Hallucinations"
type: concept
sources: ["[[sources/rag-hallucinations-explained]]", "[[sources/ragflow-rag-review-2025]]"]
related: ["[[concepts/retrieval-augmented-generation]]", "[[concepts/hallucination-contamination]]", "[[concepts/agentic-rag]]", "[[concepts/self-rag]]", "[[concepts/rag-evaluation]]"]
last_compiled: 2026-04-05
summary: "Fabricated or incorrect outputs from RAG systems despite access to grounding sources — caused by retrieval failures, cross-document fusion errors, and confidence misalignment. Stanford found 17-33% hallucination in legal RAG tools."
---

## Overview

RAG hallucinations occur when [[concepts/retrieval-augmented-generation]] systems generate incorrect or fabricated information **despite having access to relevant source documents**. This distinguishes them from standard LLM hallucinations, which arise from a model operating purely on parametric memory. RAG hallucinations are particularly dangerous because users trust RAG systems to be grounded in evidence, creating a false sense of reliability.

Research from Stanford University found that specialized legal AI tools using RAG still hallucinate in **17 to 33% of cases** — a sobering statistic that underscores RAG's role as a hallucination reduction strategy, not an elimination strategy.

## Root Causes

RAG hallucinations arise from failures at two pipeline stages:

### Retrieval-Stage Failures

- **Topically relevant but factually wrong**: The retriever finds documents about the right topic but containing inaccurate information. This noise propagates directly into the generated answer.
- **Incomplete retrieval**: The retriever fails to find the most relevant documents, especially when queries require abstract reasoning or multi-hop connections.
- **Stale documents**: Retrieved evidence may be outdated, leading to answers based on superseded information.
- **Query ambiguity**: Vague queries retrieve diverse documents that may be individually valid but collectively contradictory.

### Generation-Stage Failures

- **Cross-document fusion errors**: The generator "synthesizes incorrect conclusions" by combining information from multiple documents in misleading ways, even when each individual document is accurate.
- **Confidence misalignment**: Models generate outputs with high confidence regardless of factual accuracy, creating authoritative-sounding but wrong answers.
- **Parametric memory override**: Models sometimes **ignore retrieved content entirely**, falling back to their training-time parametric knowledge even when the retrieved evidence contradicts it.
- **Distraction by irrelevant content**: Models can be "distracted" by irrelevant passages within retrieved documents, particularly in long documents where the answer isn't prominent.

## Comparative Hallucination Rates

| System Type | External Knowledge | Hallucination Rate |
|---|---|---|
| Vanilla LLM | None | High |
| Basic RAG | Retrieved documents | Medium |
| Mitigated RAG (Self-RAG, CRAG) | Retrieved + verified | Low |
| Human expert | Full domain knowledge | Very low |

## Mitigation Strategies

### Retrieval Improvements
- [[concepts/hybrid-search]] to catch both semantic and exact-match queries
- Dense retrievers with metadata filtering to improve precision
- [[concepts/reranking]] to push the most relevant documents to the top
- [[concepts/graphrag]] for queries requiring holistic understanding

### Generation Improvements
- Prompt engineering requiring explicit source citation
- Chain-of-thought reasoning anchored to specific retrieved passages
- Uncertainty modeling to enable "I don't know" responses when evidence is insufficient

### Self-Corrective Approaches
- [[concepts/self-rag]]: Reflection tokens evaluate retrieval relevance and generation support
- [[concepts/corrective-rag]]: Evaluates retrieval quality and supplements with web search
- [[concepts/agentic-rag]]: Full agent loop with hallucination checking as a pipeline stage

### Evaluation-Based
- [[concepts/rag-evaluation]] metrics like faithfulness scoring
- Factuality metrics (BERTScore, FactCC, QAGS)
- Continuous monitoring in production for drift

## Real-World Impact

The medical chatbot scenario illustrates the stakes: a RAG system retrieving outdated medical guidelines could produce an "incorrect — but authoritative — recommendation" with serious health consequences. In legal, financial, and healthcare domains, RAG hallucinations carry regulatory and liability risks that make mitigation non-optional.

## Sources

- [[sources/rag-hallucinations-explained]] — root causes, statistics, and mitigation strategies
- [[sources/ragflow-rag-review-2025]] — hallucination in context of RAG evolution

## Related Concepts

- [[concepts/hallucination-contamination]] — when hallucinations propagate into the knowledge base itself
- [[concepts/agentic-rag]] — self-corrective approaches to mitigation
- [[concepts/rag-evaluation]] — metrics for detecting hallucinations
- [[concepts/retrieval-augmented-generation]] — the pipeline where hallucinations occur
