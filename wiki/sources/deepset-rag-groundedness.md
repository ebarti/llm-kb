---
title: "Source: Measuring LLM Groundedness in RAG Systems"
type: source-summary
source: "[[raw/deepset-rag-groundedness]]"
related: ["[[concepts/faithfulness-and-groundedness]]", "[[concepts/rag-evaluation]]", "[[concepts/hallucination-detection]]"]
last_compiled: 2026-04-05
summary: "deepset's production approach to RAG groundedness: numerical scoring per response, document reference analysis for retrieval quality, statement-level citation annotation, and continuous production monitoring via observability dashboards."
---

## Key Points

- Groundedness = degree to which RAG answers are supported by retrieved documents (opposite of hallucination)
- Groundedness score tracks changes over time through observability dashboards
- Document reference analysis reveals retrieval quality by tracking which document positions support answers
- Cost optimization: limiting retrieved documents from 10 to 6 eliminated 40% of LLM processing costs
- Reference Predictor provides statement-level source citations, working reliably across all LLM types
- Production monitoring across 1-60 day timeframes enables degradation detection

## Detailed Summary

deepset's Haystack platform provides the most production-oriented approach to [[concepts/faithfulness-and-groundedness]] evaluation. Where academic papers focus on benchmark scores, this article focuses on **continuous monitoring** in deployed systems.

The **Groundedness Score** is a numerical metric computed for each RAG pipeline response, tracking quality over time. The **Document Reference Analysis** is particularly novel: by tracking which document positions are most frequently used to support answers, it reveals retrieval quality issues. If lower-ranked documents are cited more than higher-ranked ones, the retriever needs improvement.

The **Reference Predictor** decomposes responses into individual claims and annotates each with source citations. Unlike LLM-generated citations (which are unreliable), this works reliably across all LLM types and enables end-user verification.

For [[concepts/llm-knowledge-base]] operators, the key insight is that groundedness monitoring enables both **cost optimization** (reducing unnecessary retrieved documents) and **quality assurance** (detecting degradation before users notice).

## Related Concepts

- [[concepts/faithfulness-and-groundedness]] — the core metric detailed
- [[concepts/rag-evaluation]] — the evaluation framework this extends
- [[concepts/hallucination-detection]] — closely related detection capability
- [[concepts/linting-and-health-checks]] — analogous monitoring in KB context
