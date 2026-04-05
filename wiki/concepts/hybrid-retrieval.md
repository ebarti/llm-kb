---
title: "Hybrid Retrieval"
type: concept
sources: ["[[sources/kg-vs-vector-db-glean]]", "[[sources/rag-vs-kg-enterprise-phyvant]]", "[[sources/graphrag-microsoft-research]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/vector-databases]]", "[[concepts/graphrag]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Combining knowledge graphs and vector databases for AI retrieval: graphs provide entity relationships, permissions, and multi-hop reasoning while vectors enable semantic search over unstructured content."
---

## Overview

Hybrid retrieval combines [[concepts/knowledge-graph]] structures with [[concepts/vector-databases]] for AI applications, addressing the fundamental limitations of each approach used in isolation. Pure vector RAG fails on relationship-heavy queries and entity resolution; pure knowledge graphs miss document-level details and unstructured content. The hybrid approach handles what neither can alone.

## Architecture Patterns

### Graph-Scoped Search

Use graph queries to narrow the searchable content space, then apply vector similarity within that subset:
1. Graph query identifies relevant entities and their scope (e.g., "documents owned by this team")
2. Vector search finds semantically relevant passages within that scope
3. Results are grounded in both relationship context and semantic relevance

### Graph-Informed Ranking

Rerank vector search results using graph signals:
- **Recency**: Temporal properties from the graph prioritize current information
- **Authority**: Entity importance scores from graph centrality
- **Organizational proximity**: How closely related the source is to the query context
- **Permissions**: Access control enforced through graph-modeled relationships

### Entity-Aware Agents

AI agents reason about relationships through graph traversal while retrieving detailed context via vector search:
1. **Query reception**: User asks about internal data
2. **Graph interrogation**: Check verified knowledge about mentioned entities and relationships
3. **RAG augmentation**: Retrieve document details informed by graph context
4. **LLM synthesis**: Generate answers combining relationship knowledge and document grounding

## Why Hybrid Outperforms Pure Approaches

### RAG Failure Modes (addressed by graph)

- **Entity resolution**: RAG cannot recognize that "John Smith," "J. Smith," and "VP of Engineering" are the same person — graphs model entity identity explicitly
- **Temporal blindness**: RAG retrieves by semantic similarity, not validity — graphs store temporal properties indicating when facts were true
- **Contradiction handling**: RAG cannot reason about conflicting information — graphs can model provenance and recency
- **Multi-hop reasoning**: RAG retrieves isolated chunks — graphs traverse relationships

### Knowledge Graph Failure Modes (addressed by vectors)

- **Cold start**: Graphs start empty while vector RAG provides immediate value from documents
- **Unstructured content**: Graphs require structured data modeling; vectors handle messy documents natively
- **Semantic similarity**: Graphs model explicit relationships; vectors capture implicit semantic connections
- **Maintenance burden**: Graphs require ongoing ontology maintenance; vector stores update automatically with new documents

## Enterprise Implementation

[[sources/kg-vs-vector-db-glean]] recommends designing layered implementations:
1. Establish graph foundations for core entities and permissions
2. Overlay vector search for unstructured content coverage
3. Build ranking layers that combine both signals

Architecture choice should follow data reality, risk profile, AI roadmap, and operational ownership — not industry trends.

## Sources

- [[sources/kg-vs-vector-db-glean]] — detailed hybrid architecture analysis
- [[sources/rag-vs-kg-enterprise-phyvant]] — enterprise failure modes and hybrid recommendation
- [[sources/graphrag-microsoft-research]] — GraphRAG as a specific hybrid implementation

## Related Concepts

- [[concepts/knowledge-graph]] — the graph component
- [[concepts/vector-databases]] — the vector component
- [[concepts/graphrag]] — a specific hybrid implementation
- [[concepts/rag-vs-index-based-retrieval]] — the broader retrieval debate
