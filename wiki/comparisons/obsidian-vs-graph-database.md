---
title: "Obsidian (File-Based) vs. Graph Database Storage"
type: comparison
subjects: ["[[concepts/obsidian-as-ide]]", "[[concepts/knowledge-graph]]"]
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/graphiti-temporal-knowledge-graphs]]"]
last_compiled: 2026-04-06
summary: "Comparing file-system-based knowledge storage (markdown + Obsidian) with graph database storage (SQLite, Neo4j) as substrates for LLM-maintained knowledge bases."
---

## Overview

The storage substrate of an LLM knowledge base determines what operations are efficient, what is human-readable, and what tools are available for navigation and maintenance. Two approaches dominate the sources in this wiki: file-based storage using markdown files viewed in [[entities/obsidian]] (Karpathy's approach), and graph database storage using [[entities/sqlite]], [[entities/neo4j]], or similar (Gallagher's and Graphiti's approaches). This comparison examines the practical implications of each choice for developers building LLM-maintained knowledge systems.

## Comparison Table

| Dimension | File-Based (Markdown + Obsidian) | Graph Database (SQLite/Neo4j) |
|-----------|--------------------------------|-------------------------------|
| Data format | Plain text `.md` files | Structured nodes and edges |
| Human readability | High (any text editor) | Low (requires DB client or UI) |
| LLM compatibility | Native (markdown is training data) | Requires serialization |
| Structure | Implicit (wikilinks, headers) | Explicit (typed nodes, labeled edges) |
| Querying | LLM reads files + natural language | SQL/Cypher + structured queries |
| Version control | Native Git (plain text) | Requires DB snapshots or migration scripts |
| Temporal tracking | Manual (file dates, inline notes) | Built-in (Graphiti validity windows) |
| Graph visualization | Obsidian graph view (link-based) | Neo4j Browser, custom graph UIs |
| Plugin ecosystem | Rich (Obsidian community) | Database-specific tooling |
| Backup/portability | Copy directory | Export/import database |
| Setup complexity | Low (mkdir + install Obsidian) | Moderate to high (install DB, define schema) |
| Best for | Research synthesis, personal learning | Task management, operational knowledge, temporal reasoning |

## Detailed Analysis

**The readability factor**: The most significant practical difference is human readability. A markdown file can be opened in any text editor, read top-to-bottom, and understood immediately. A SQLite database requires a query tool, knowledge of the schema, and SQL proficiency. For personal knowledge bases where the human regularly reads and browses content, this readability advantage is decisive.

**The structural power factor**: [[entities/sam-gallagher]] articulated the case for databases: "an intelligent knowledge system can't just manipulate text, it must understand structure." Typed nodes (Task, Note, Person, Project) with labeled edges (part_of, mentions, related_to) enable queries that wikilinks cannot express: "find all tasks related to Project X that mention Person Y." For task and project management, this structural expressiveness matters.

**The temporal factor**: [[entities/graphiti]]'s temporal validity windows require a database to implement efficiently. Tracking when facts became true and when they were superseded is a first-class database operation but a manual, error-prone process in markdown files. For knowledge bases where information changes over time, graph databases have a clear advantage.

**The LLM factor**: LLMs are trained extensively on markdown, making them natural markdown authors. Serializing graph database contents into a format the LLM can reason over adds a translation layer. Conversely, storing LLM output in a database requires parsing structured information from natural language output -- a lossy process.

## When to Use Each

**Use file-based (Obsidian) when:**
- Human reading and browsing is a primary use case
- The knowledge is primarily research and reference material
- Git-based version control is desired
- Infrastructure simplicity is a priority
- The LLM is the primary author and reader

**Use graph database when:**
- Structured queries over typed relationships are needed
- Temporal tracking of facts is required
- The knowledge base serves task/project management
- Multiple systems need to query the same knowledge
- Schema enforcement prevents data quality issues

## Sources

- [[sources/karpathy-llm-knowledge-bases]] -- file-based markdown + Obsidian approach
- [[sources/gallagher-second-brain-knowledge-graphs]] -- SQLite + ChromaDB graph approach
- [[sources/graphiti-temporal-knowledge-graphs]] -- Neo4j-backed temporal graph approach
