---
title: "ChromaDB"
type: entity
entity_type: tool
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]"]
related: ["[[concepts/vector-databases]]", "[[concepts/knowledge-graph]]", "[[concepts/second-brain]]", "[[entities/sqlite]]", "[[entities/faiss]]", "[[entities/pgvector]]"]
last_compiled: 2026-04-06
summary: "An open-source embedding database used in Gallagher's Knowledge Graph Kit to provide semantic vector search over graph nodes alongside SQLite structural storage."
reading_time: "2 min"
---

## Overview

ChromaDB is an open-source vector database (embedding database) designed for AI applications. It stores high-dimensional embedding vectors and supports semantic similarity search, making it possible to find conceptually related content even when exact keywords do not overlap. ChromaDB is notable for its developer-friendly API, lightweight footprint, and easy integration with Python-based LLM workflows.

In the context of this knowledge base, ChromaDB appears as a key component of Sam Gallagher's Knowledge Graph Kit, where it provides the semantic search layer on top of a [[entities/sqlite]] graph database. While the SQLite database stores the structural graph (nodes, edges, types, relationships), ChromaDB enables finding related nodes by meaning rather than by explicit link traversal or keyword matching.

## Key Features

- **Lightweight and embeddable**: ChromaDB can run in-process alongside application code, making it suitable for personal-scale projects without requiring separate database infrastructure.

- **Python-native API**: Designed for easy integration with Python-based AI workflows, including LangChain, LlamaIndex, and custom agent pipelines.

- **Automatic embedding**: ChromaDB can compute embeddings automatically using built-in embedding functions, reducing the setup required for vector search.

- **Metadata filtering**: Supports filtering search results by metadata alongside vector similarity, enabling hybrid queries that combine semantic meaning with structured attributes.

## Role in LLM Knowledge Bases

ChromaDB illustrates the spectrum of vector database options discussed in [[concepts/vector-databases]]. It sits between full-scale production vector databases (Pinecone, Weaviate, Milvus) and simple in-memory solutions. For personal knowledge management applications like Gallagher's Knowledge Graph Kit, ChromaDB provides just enough semantic search capability without the operational complexity of a dedicated vector database service.

In the broader context of [[concepts/rag-vs-index-based-retrieval]], ChromaDB represents the vector search approach: embed content into vectors, then retrieve by semantic similarity at query time. Karpathy's alternative -- LLM-maintained index files and one-line summaries navigated directly by the LLM -- avoids the need for any vector database at personal scale, though ChromaDB could serve as a useful upgrade path when the wiki grows beyond context window limits.

## Mentioned In

- [[sources/gallagher-second-brain-knowledge-graphs]] -- used as the vectorization layer in the Knowledge Graph Kit alongside SQLite
