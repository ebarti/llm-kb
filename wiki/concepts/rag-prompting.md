---
title: "RAG Prompting"
type: concept
sources: ["[[sources/promptingguide-rag-prompting]]", "[[sources/lakera-prompt-engineering-guide]]"]
related: ["[[concepts/prompt-engineering]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/chain-of-thought-prompting]]", "[[concepts/llm-qa-over-documents]]"]
last_compiled: 2026-04-05
summary: "Prompt engineering techniques specific to RAG pipelines — query rewriting (HyDE, Query2Doc), context integration, and generation prompts — where 'weak retrieval makes things messy, but weak prompts make things unusable.'"
---

## Overview

RAG prompting refers to the [[concepts/prompt-engineering]] techniques used specifically within Retrieval-Augmented Generation pipelines. RAG systems combine information retrieval (finding relevant documents) with text generation (producing answers), and prompting plays a critical role at both stages.

The key insight is that prompt design is just as important as retrieval quality in RAG systems. A perfect retriever with a poorly prompted generator still produces poor results.

## Prompting at Each RAG Stage

### Query Stage (Before Retrieval)
Prompt techniques that improve what gets retrieved:
- **Query2Doc**: Use the LLM to expand the user's query into a richer document
- **HyDE (Hypothetical Document Embeddings)**: Generate a hypothetical answer, then use it as the search query
- **ITER-RETGEN**: Iterative retrieval-generation cycles

### Context Integration Stage
How to present retrieved documents to the generator:
- Concatenate retrieved documents with the original query
- Use XML tags or delimiters to clearly separate documents from instructions
- Include source metadata for attribution

### Generation Stage
How to prompt the generator to use the context:
- Instruct the model to ground responses in retrieved documents
- Ask for quotes before synthesis (Anthropic's recommendation)
- Use [[concepts/chain-of-thought-prompting]] for explicit reasoning over retrieved content
- Include [[concepts/few-shot-prompting]] examples showing proper citation behavior

## Connection to This KB

This KB system uses a form of RAG without vector search — the LLM reads summaries.md (the retrieval index), navigates to relevant full articles, then synthesizes answers. The prompting principles for RAG apply directly to improving the KB's Q&A quality.

## Sources
- [[sources/promptingguide-rag-prompting]] — RAG prompting overview with query rewriting techniques
- [[sources/lakera-prompt-engineering-guide]] — Context-rich prompting as a prompt type

## Related Concepts
- [[concepts/prompt-engineering]] — parent domain
- [[concepts/rag-vs-index-based-retrieval]] — when to use RAG vs simpler approaches
- [[concepts/chain-of-thought-prompting]] — reasoning within RAG pipelines
- [[concepts/llm-qa-over-documents]] — this KB's approach to Q&A
