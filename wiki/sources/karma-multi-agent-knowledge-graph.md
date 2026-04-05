---
title: "Source: KARMA — Multi-Agent LLM Framework for Knowledge Graph Enrichment"
type: source-summary
source: "[[raw/karma-multi-agent-knowledge-graph]]"
related: ["[[concepts/knowledge-graph]]", "[[concepts/multi-agent-systems]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "NeurIPS 2025 Spotlight paper: nine-agent LLM framework for automated KG enrichment achieving 83.1% accuracy on 1,200 PubMed articles with 18.6% conflict reduction — the research-grade counterpart to markdown wikis."
reading_time: "1 min"
---

## Key Points
- Nine specialized collaborative LLM agents: entity discovery, relation extraction, schema alignment, conflict resolution
- Tested on 1,200 PubMed articles across 3 domains
- 38,230 new entities discovered; 83.1% LLM-verified correctness; 18.6% conflict edge reduction
- NeurIPS 2025 Spotlight paper
- Formal graph triplets (entity, relation, entity) vs. Karpathy's natural-language markdown

## Detailed Summary

KARMA is the research-grade automated approach to building and enriching knowledge graphs from unstructured text. Nine collaborative agents handle the full pipeline: parsing documents, verifying extractions against existing data, integrating new information, resolving conflicts, and maintaining schema adherence.

The key contrast with Karpathy's approach: KARMA builds formal graph structures (triplets with schema constraints), while Karpathy uses human-readable markdown with wikilinks. KARMA scales to thousands of scientific papers; Karpathy's approach targets ~100 articles with emphasis on auditability and human readability.

Both share the core architecture: raw documents → LLM extraction/compilation → structured knowledge → querying. KARMA adds formal conflict resolution and schema validation; Karpathy's system adds the "filing loop" (query outputs enrich the KB) and health check linting.

## Related Concepts
- [[concepts/knowledge-graph]] — the target representation
- [[concepts/multi-agent-systems]] — the nine-agent architecture
- [[concepts/llm-knowledge-base]] — the contrasting personal approach
