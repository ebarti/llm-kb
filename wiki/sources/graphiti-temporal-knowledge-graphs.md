---
title: "Source: Graphiti — Temporal Context Graphs for AI Agents"
type: source-summary
source: "[[raw/graphiti-temporal-knowledge-graphs]]"
related: ["[[concepts/knowledge-graph]]", "[[concepts/temporal-knowledge]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Graphiti: open-source temporal graph framework for AI agents with time-windowed facts, incremental updates, hybrid retrieval (semantic + BM25 + graph), and full provenance — the middle ground between markdown wikis and enterprise KGs."
reading_time: "2 min"
---

## Key Points
- Context graph = temporal graph: entities + relationships + facts with validity windows (when true → when superseded)
- Four components: Entities (nodes), Facts/Relationships (edges with time windows), Episodes (raw provenance), Custom Types (Pydantic ontology)
- Hybrid retrieval: semantic + keyword (BM25) + graph-based search
- Incremental updates: no batch recomputation; old facts invalidated not deleted
- Full provenance: every derived fact traces to Episodes (source documents)
- Middle ground: more structured than markdown wiki, more accessible than KARMA

## Detailed Summary

Graphiti occupies the gap between Karpathy's simple markdown wiki and enterprise knowledge graph systems like KARMA. Its killer feature for AI agents: temporal validity windows. Rather than a static graph where facts are true or false, Graphiti tracks when facts became true and when they were superseded. This is critical for agents operating in changing environments (e.g., "what was the product roadmap last quarter vs. today?").

The Episodes concept mirrors Karpathy's `raw/` directory: all derived knowledge traces back to source documents, enabling auditability and correction. The hybrid retrieval combining semantic embeddings, BM25 keyword search, and graph traversal provides more robust retrieval than any single method alone.

The open-source/Zep split (Graphiti as engine, Zep as managed service) mirrors the pattern seen across knowledge management tools: open core for experimentation, managed service for production.

## Related Concepts
- [[concepts/knowledge-graph]] — the representation
- [[concepts/temporal-knowledge]] — Graphiti's unique contribution
- [[concepts/rag-vs-index-based-retrieval]] — retrieval methods compared
- [[concepts/llm-knowledge-base]] — the simpler alternative
