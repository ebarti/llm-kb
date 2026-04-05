---
title: "Source: GraphRAG — Unlocking LLM Discovery on Narrative Private Data"
type: source-summary
source: "[[raw/microsoft-graphrag]]"
related: ["[[concepts/graphrag]]", "[[concepts/retrieval-augmented-generation]]", "[[concepts/knowledge-graph]]", "[[entities/microsoft-research]]"]
last_compiled: 2026-04-05
summary: "Microsoft Research's GraphRAG system constructs knowledge graphs from text via LLM extraction, then uses community-level summaries to answer holistic queries that baseline RAG cannot — with provenance tracking."
reading_time: "2 min"
---

## Key Points

- Baseline RAG fails at holistic/aggregate queries over large document collections
- GraphRAG constructs knowledge graphs by extracting entities and relationships via LLMs
- Graph machine learning performs bottom-up clustering into semantic communities
- Pre-summarization at multiple abstraction levels enables theme-level understanding
- Outperforms baseline RAG on comprehensiveness, evidence provision, and viewpoint diversity
- Maintains similar faithfulness levels to baseline RAG (verified via SelfCheckGPT)
- Provides full provenance linking conclusions to source documents

## Detailed Summary

[[concepts/graphrag]] addresses two fundamental limitations of traditional [[concepts/retrieval-augmented-generation]]: the inability to connect disparate information sharing common attributes, and poor performance on holistic summarization queries. Microsoft's approach uses LLMs to extract a knowledge graph from raw text, then applies graph machine learning to create hierarchical community structures with pre-generated summaries.

The evaluation on Ukraine-Russia conflict news data is striking: when asked for top themes, baseline RAG returned irrelevant topics (urban development, economic growth) while GraphRAG correctly identified conflict, political entities, infrastructure concerns, and humanitarian issues. This demonstrates the fundamental gap between similarity-based chunk retrieval and structured knowledge understanding.

## Related Concepts

- [[concepts/graphrag]] — the approach detailed in this paper
- [[concepts/knowledge-graph]] — the underlying data structure
- [[concepts/retrieval-augmented-generation]] — the baseline being improved upon
- [[entities/microsoft-research]] — the research organization
