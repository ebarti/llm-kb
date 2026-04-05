---
title: "Second Brain"
type: concept
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/decodingai-second-brain-rag]]"]
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/personal-knowledge-management]]", "[[concepts/knowledge-graph]]"]
last_compiled: 2026-04-05
summary: "A personal AI system that stores, organizes, and retrieves the user's own knowledge — implemented either as a markdown wiki (Karpathy), a graph database (Gallagher), or a RAG pipeline (Decoding AI), all using LLMs as the intelligence layer."
---

## Overview

The "second brain" concept refers to an external system that augments human cognition by storing and organizing personal knowledge in a way that can be retrieved and synthesized on demand. LLMs have dramatically expanded what's possible here — moving from passive note storage to active knowledge compilation and Q&A.

## Key Implementations

### Markdown Wiki (Karpathy)
- Storage: flat markdown files in a directory tree
- Retrieval: LLM reads index files + full articles within context window
- Intelligence: LLM compiles, links, and answers from the wiki
- Scale: ~100 articles, ~400K words
- Best for: research knowledge synthesis, personal learning

### Graph Database (Gallagher / Knowledge Graph Kit)
- Storage: SQLite graph with typed nodes (Task, Note, Person, Project) and labeled edges
- Retrieval: semantic search (ChromaDB) + structured graph queries
- Intelligence: LLM adds notes, creates connections, answers queries
- Best for: personal task/project management, relationship tracking

### Production RAG (Decoding AI)
- Storage: MongoDB vector database with embedded chunks
- Retrieval: semantic + hybrid search (Contextual Retrieval)
- Intelligence: fine-tuned Llama 3.1 8B + agentic RAG with smolagents
- Scale: 1000s of documents
- Best for: team-scale knowledge bases, production reliability

## Shared Principles Across All Approaches

1. **LLM as intelligence layer**: The LLM isn't just retrieval — it synthesizes, connects, and maintains
2. **Source provenance**: Raw input is preserved; derived knowledge traces back to sources
3. **Incremental enrichment**: New inputs add to, not replace, existing knowledge
4. **Natural language interface**: Users interact via conversation, not structured queries

## The Filing Loop (Karpathy's Key Innovation)

What distinguishes the LLM-KB from static note-taking: query outputs get filed back into the knowledge base. Every question asked enriches the system. This compounding effect doesn't exist in RAG (which doesn't remember query results) or fine-tuning (which requires retraining).

## Sources
- [[sources/gallagher-second-brain-knowledge-graphs]] — graph-based personal KB
- [[sources/decodingai-second-brain-rag]] — production RAG approach

## Related Concepts
- [[concepts/llm-knowledge-base]] — the Karpathy markdown approach
- [[concepts/personal-knowledge-management]] — the broader domain
- [[concepts/knowledge-graph]] — graph-based representations
- [[concepts/rag-vs-index-based-retrieval]] — retrieval comparison
