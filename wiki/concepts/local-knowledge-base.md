---
title: "Local Knowledge Base"
type: concept
sources: ["[[sources/freecodecamp-local-rag-ollama]]", "[[sources/ollama-complete-guide]]", "[[sources/local-llm-hosting-tools-comparison]]", "[[sources/small-language-models-guide-2026]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/local-llm-inference]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[concepts/open-source-llms]]", "[[entities/ollama]]", "[[entities/chromadb]]"]
last_compiled: 2026-04-05
summary: "Running an LLM-powered knowledge base entirely on local hardware — using Ollama + open-source models + ChromaDB/FAISS — for privacy, offline operation, and zero API costs."
---

## Overview

A local knowledge base is an [[concepts/llm-knowledge-base]] that runs entirely on local hardware without any cloud API dependency. Instead of calling Claude, GPT-4, or other cloud LLMs, a local KB uses [[concepts/open-source-llms]] served through [[concepts/local-llm-inference]] tools like [[entities/ollama]] or [[entities/vllm]], combined with local vector databases like [[entities/chromadb]] or [[entities/faiss]] for retrieval.

This is directly relevant to the current KB system, which could potentially be adapted to run without the Claude API.

## Key Ideas

### Architecture for a Local KB

The standard local KB stack (as demonstrated in the freeCodeCamp tutorial):

1. **LLM Engine**: [[entities/ollama]] serving Qwen 3 (or DeepSeek, Llama, Mistral)
2. **Embedding Model**: nomic-embed-text (via Ollama) or sentence-transformers
3. **Vector Store**: [[entities/chromadb]] (local persistent storage)
4. **Orchestration**: LangChain connecting retrieval to generation
5. **Document Processing**: PyPDF, text splitters for ingestion

### RAG vs Index-Based Retrieval (Local Context)

This KB currently uses [[concepts/rag-vs-index-based-retrieval]] with an index-based approach (summaries.md, _index.md) that works well because the LLM can read the full index in its context window. A local version faces a tension:

- **Index-based** (current approach): Requires the LLM to read and reason over long index files. Works well with large context windows (128K+) but demands stronger reasoning from the model.
- **RAG-based**: Adds vector search to find relevant documents. More forgiving of weaker models since they only need to synthesize pre-retrieved content. But adds complexity (embedding pipeline, vector DB).

For a local KB, a **hybrid approach** may be optimal: use the index for navigation and vector search for content retrieval, reducing the reasoning burden on the local model.

### Practical Stack for This KB

To run this exact KB system locally:

**Minimum viable (8GB Mac)**:
- [[entities/ollama]] + Phi-4-mini (3.8B, Q4)
- Limited to simple Q&A and basic summaries
- Wiki compilation quality would be significantly reduced

**Good quality (32GB Mac)**:
- [[entities/ollama]] + DeepSeek Coder V2 or Qwen 3 14B (Q4)
- Adequate for source summaries, simple concept articles
- Complex multi-source synthesis may be inconsistent

**Near-cloud quality (64GB+ Mac or GPU server)**:
- [[entities/ollama]] or [[entities/vllm]] + Qwen 3.5 32B+ or DeepSeek V3 distilled
- Quality approaches cloud APIs for most tasks
- Complex compilation and linting feasible

### Critical Configuration

From the freeCodeCamp tutorial, key settings for local RAG:
- `num_ctx` must be 8192+ (Ollama default is insufficient)
- Chunk size: 1000 characters with 200 character overlap
- Retriever k=3 for similarity search
- nomic-embed-text recommended for local embeddings

### What Works Well Locally

- Q&A over compiled wiki content
- Source summarization (one source at a time)
- Link checking and orphan detection (linting)
- Embedding generation for vector search
- Simple entity page creation

### What Remains Challenging

- Multi-source synthesis (compiling concept articles from 5+ sources)
- Complex reasoning chains (inferring connections across distant articles)
- Long-context operations (reading 20+ wiki pages for comprehensive linting)
- Quality of generated prose (may need human editing)
- The "filing loop" where Q&A results compound back into the wiki

### Privacy and Offline Benefits

- All data stays on your machine — no content sent to cloud providers
- Works without internet connection
- No per-token costs after initial hardware investment
- Full control over model selection and behavior
- Suitable for sensitive or classified information

## Sources
- [[sources/freecodecamp-local-rag-ollama]] — complete local RAG tutorial with code
- [[sources/ollama-complete-guide]] — Ollama setup and API details
- [[sources/local-llm-hosting-tools-comparison]] — tool selection guidance
- [[sources/small-language-models-guide-2026]] — SLMs for minimal-hardware KB

## Related Concepts
- [[concepts/llm-knowledge-base]] — the cloud-based version of this concept
- [[concepts/local-llm-inference]] — the inference layer enabling local KB
- [[concepts/rag-vs-index-based-retrieval]] — retrieval strategy choice for local KB
- [[concepts/open-source-llms]] — model options for local KB
- [[concepts/small-language-models]] — lightweight models for constrained hardware
- [[comparisons/local-vs-cloud-knowledge-base]] — dedicated comparison
