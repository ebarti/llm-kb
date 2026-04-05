---
title: "Self-RAG (Self-Reflective Retrieval-Augmented Generation)"
type: concept
sources: ["[[sources/self-reflective-rag-langgraph]]", "[[sources/agentic-rag-survey]]"]
related: ["[[concepts/agentic-rag]]", "[[concepts/corrective-rag]]", "[[concepts/retrieval-augmented-generation]]", "[[concepts/rag-hallucinations]]"]
last_compiled: 2026-04-05
summary: "An advanced RAG framework that trains four reflection tokens into the model — Retrieve, ISREL, ISSUP, ISUSE — enabling self-assessment of when to retrieve, what's relevant, and whether outputs are evidence-supported."
---

## Overview

Self-RAG (Self-Reflective Retrieval-Augmented Generation) is an advanced AI framework that improves the factual accuracy of [[concepts/retrieval-augmented-generation]] by incorporating a **self-reflective mechanism**. Unlike standard RAG, which always retrieves and always generates in a fixed pipeline, Self-RAG dynamically decides when and how to retrieve information, evaluates the relevance of retrieved data, and critiques its own outputs to ensure they are supported by evidence.

The key innovation is training **reflection tokens** directly into the language model, enabling it to introspect about retrieval necessity and output quality without requiring external tools or multi-model orchestration.

## Reflection Tokens

Self-RAG introduces four specialized tokens that the model learns to generate during training:

| Token | Purpose | Outputs |
|---|---|---|
| **Retrieve** | Should I fetch documents for this query? | yes / no / continue |
| **ISREL** | Is this retrieved passage relevant to the question? | relevant / irrelevant |
| **ISSUP** | Is my generated text supported by the retrieved chunks? | fully supported / partially / no support |
| **ISUSE** | How useful is this complete response? | 1-5 scale |

These tokens are generated inline during inference, creating a self-monitoring loop within a single model forward pass.

## How It Differs from Standard RAG

In standard RAG, every query triggers retrieval, and the model generates from whatever was retrieved — even if the documents are irrelevant or the generation contradicts the evidence. Self-RAG breaks this by:

1. **Selective retrieval**: The model can decide a query doesn't need external evidence (e.g., "What is 2+2?") and skip retrieval entirely
2. **Relevance filtering**: Retrieved passages are evaluated before being used for generation
3. **Grounded generation**: The ISSUP token enables checking whether the output is actually supported by evidence, not just plausible-sounding
4. **Quality scoring**: The ISUSE token provides an overall utility assessment

## Practical Implementation

In the [[entities/langgraph]] implementation, the approach is simplified for production use:
- Documents are graded collectively rather than individually (reducing latency)
- A single generation pass is made from all relevant chunks (rather than per-chunk generation as in the original paper)
- Pydantic-modeled outputs ensure consistent binary routing logic
- Full execution traces through the state machine enable auditability

## Relationship to Other Approaches

Self-RAG focuses on improving **reasoning over evidence** — making the model better at deciding what to retrieve and whether its outputs are grounded. By contrast, [[concepts/corrective-rag]] focuses on improving the **quality of evidence** by evaluating and supplementing retrieval results.

[[concepts/agentic-rag]] is the orchestrating superset that can employ both Self-RAG's reflection capabilities and CRAG's evidence improvement, plus additional tools and multi-step planning.

## Sources

- [[sources/self-reflective-rag-langgraph]] — LangGraph implementation details
- [[sources/agentic-rag-survey]] — positioning within agentic RAG taxonomy

## Related Concepts

- [[concepts/agentic-rag]] — the broader paradigm Self-RAG belongs to
- [[concepts/corrective-rag]] — complementary approach focused on evidence quality
- [[concepts/rag-hallucinations]] — the problem Self-RAG addresses
- [[concepts/retrieval-augmented-generation]] — the base pipeline being enhanced
