---
title: "Source: RAG Prompting (Prompt Engineering Guide)"
type: source-summary
source: "[[raw/promptingguide-rag-prompting]]"
related: ["[[concepts/rag-prompting]]", "[[concepts/prompt-engineering]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "DAIR.AI overview of RAG prompting: combining retrieval with generation, including query rewriting (Query2Doc, HyDE), N-shot prompting, and CoT within RAG pipelines."
---

## Key Points
- RAG combines information retrieval with text generation for knowledge-intensive tasks
- Three-step process: retrieve → integrate context → generate
- Reduces hallucinations by grounding responses in retrieved documents
- Key prompting techniques within RAG: query rewriting (Query2Doc, HyDE), N-shot, CoT
- "Weak retrieval makes things messy, but weak prompts make things unusable"
- RAG's internal knowledge can be modified efficiently without retraining

## Detailed Summary
This source covers how [[concepts/prompt-engineering]] techniques apply specifically within RAG pipelines. The key insight is that prompt design is just as critical in RAG as retrieval quality — a perfect retriever with a poorly prompted generator still produces poor results. The article covers query rewriting techniques (HyDE, Query2Doc) that use the LLM itself to improve retrieval before generation.

## Related Concepts
- [[concepts/rag-prompting]] — prompting within RAG systems
- [[concepts/rag-vs-index-based-retrieval]] — when to use RAG vs simpler approaches
- [[concepts/prompt-engineering]] — parent domain
