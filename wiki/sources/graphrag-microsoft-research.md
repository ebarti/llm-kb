---
title: "Source: GraphRAG — Unlocking LLM Discovery on Narrative Private Data"
type: source-summary
source: "[[raw/graphrag-microsoft-research]]"
related: ["[[concepts/graphrag]]", "[[concepts/knowledge-graph]]", "[[concepts/rag-vs-index-based-retrieval]]", "[[entities/microsoft-graphrag]]"]
last_compiled: 2026-04-05
summary: "Microsoft Research's GraphRAG system uses LLM-extracted knowledge graphs with Leiden community detection and hierarchical summarization to dramatically outperform baseline RAG on holistic and cross-document queries."
reading_time: "2 min"
---

## Key Points

- GraphRAG addresses two critical RAG failure modes: inability to connect disparate information through shared attributes, and poor performance on holistic/thematic summarization queries
- The system builds a knowledge graph from text via LLM extraction, applies Leiden community detection for hierarchical clustering, then generates bottom-up community summaries
- Three query modes: Global Search (corpus-wide themes via community summaries), Local Search (entity-specific via neighbor traversal), DRIFT Search (local + community context)
- Consistently outperforms baseline RAG on comprehensiveness, diversity, and source provenance while maintaining equivalent faithfulness

## Detailed Summary

Microsoft Research developed GraphRAG as a structured, hierarchical approach to RAG that replaces naive semantic-search with graph-based retrieval. The core insight is that many important questions require either connecting information across documents (multi-hop reasoning) or understanding dataset-wide themes — both of which flat vector retrieval handles poorly.

The indexing pipeline has four stages: (1) text segmentation into TextUnits, (2) LLM-based extraction of all entities, relationships, and claims, (3) Leiden algorithm clustering to organize the entity graph hierarchically, and (4) bottom-up community summarization. This pre-computed structure allows the system to answer questions at multiple levels of abstraction.

The evaluation demonstrated dramatic advantages: when asked "What has Novorossiya done?" baseline RAG returned nothing, while GraphRAG identified specific activities with source provenance. For thematic queries like "What are the top 5 themes?" baseline RAG retrieved irrelevant results, while GraphRAG accurately captured the dataset's major themes.

## Notable Quotes

> "GraphRAG consistently outperforms baseline RAG on comprehensiveness, human enfranchisement, and diversity."

## Related Concepts

- [[concepts/graphrag]] — the core system described in this source
- [[concepts/knowledge-graph]] — GraphRAG builds and queries knowledge graphs from text
- [[concepts/rag-vs-index-based-retrieval]] — GraphRAG represents a structured alternative to flat vector RAG
- [[entities/microsoft-graphrag]] — the specific tool/project
