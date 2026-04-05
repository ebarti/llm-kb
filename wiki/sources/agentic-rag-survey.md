---
title: "Source: Agentic RAG Survey"
type: source-summary
source: "[[raw/agentic-rag-survey]]"
related: ["[[concepts/agentic-rag]]", "[[concepts/multi-agent-systems]]", "[[concepts/retrieval-augmented-generation]]"]
last_compiled: 2026-04-05
summary: "ArXiv survey classifying agentic RAG systems by agent cardinality, control structure, autonomy level, and knowledge representation — identifying reflection, planning, tool use, and multi-agent collaboration as key patterns."
reading_time: "1 min"
---

## Key Points

- Traditional RAG: static workflows, limited adaptability for complex tasks
- Agentic RAG: autonomous agents dynamically manage retrieval and refinement
- Design patterns: reflection, planning, tool use, multi-agent collaboration
- Taxonomy: agent cardinality × control structure × autonomy level × knowledge representation
- Applications: healthcare, finance, education, enterprise document processing
- Open challenges: evaluation methods, coordination mechanisms, memory management, governance

## Detailed Summary

This survey from arXiv provides the most comprehensive taxonomy of [[concepts/agentic-rag]] systems to date. The key insight is that traditional [[concepts/retrieval-augmented-generation]] follows predetermined paths, while agentic systems dynamically adapt their workflows based on query complexity and retrieval quality.

The taxonomy classifies systems along four dimensions, enabling principled comparison across the growing landscape of agentic retrieval architectures. The survey positions [[concepts/self-rag]] as improving reasoning over evidence, [[concepts/corrective-rag]] as improving evidence quality, and Agentic RAG as the orchestrating superset.

## Related Concepts

- [[concepts/agentic-rag]] — the surveyed paradigm
- [[concepts/multi-agent-systems]] — multi-agent coordination in RAG
- [[concepts/self-rag]] — a key sub-pattern
- [[concepts/corrective-rag]] — a key sub-pattern
