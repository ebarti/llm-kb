---
title: "Source: Using LLMs as a Second Brain — From Notes to Knowledge Graphs"
type: source-summary
source: "[[raw/gallagher-second-brain-knowledge-graphs]]"
related: ["[[concepts/second-brain]]", "[[concepts/knowledge-graph]]", "[[concepts/llm-knowledge-base]]", "[[concepts/personal-knowledge-management]]"]
last_compiled: 2026-04-05
summary: "Practitioner account of building the Knowledge Graph Kit (MCP server): SQLite + ChromaDB graph with four node types, contrasting structure-first (graph) vs. text-first (markdown) approaches to personal knowledge management."
reading_time: "2 min"
---

## Key Points
- Key insight: "an intelligent knowledge system can't just manipulate text, it must understand structure"
- Knowledge Graph Kit: SQLite storage + ChromaDB vectorization + four node types (Task, Note, Person, Project)
- Relationship labels: part_of, mentions, related_to
- Semantic search surfaces connections even when keywords don't overlap
- Data layer precedence: the underlying structure matters more than the interface
- Open-source MCP server — same patterns as Karpathy but with formal graph structure

## Detailed Summary

Sam Gallagher's journey from Notion/Obsidian failure to Knowledge Graph Kit documents a key architectural choice: markdown files are text that LLMs can manipulate, but graphs are structures that LLMs can reason over. His system stores notes as nodes with typed relationships in SQLite, with ChromaDB providing semantic vector search on top.

This approach contrasts with Karpathy's markdown-centric system:
- **Gallagher**: explicit graph structure + semantic search → better for personal tasks, projects, and people
- **Karpathy**: flat markdown + LLM index navigation → better for research synthesis and document Q&A

Both use LLMs as the intelligence layer but differ in the substrate: Gallagher stores structure in a database; Karpathy encodes structure implicitly in markdown wikilinks and LLM-maintained index files.

The MCP server packaging makes the Knowledge Graph Kit directly usable as a Claude Code/agent tool.

## Related Concepts
- [[concepts/second-brain]] — the goal
- [[concepts/knowledge-graph]] — the approach
- [[concepts/personal-knowledge-management]] — the broader domain
- [[concepts/llm-knowledge-base]] — the contrasting text-first approach
