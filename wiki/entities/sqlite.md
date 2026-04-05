---
title: "SQLite"
type: entity
entity_type: tool
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]"]
related: ["[[entities/chromadb]]", "[[concepts/knowledge-graph]]", "[[concepts/second-brain]]"]
last_compiled: 2026-04-06
summary: "A lightweight, serverless relational database used as the structural storage layer in Gallagher's Knowledge Graph Kit for personal knowledge management."
reading_time: "2 min"
---

## Overview

SQLite is a self-contained, serverless, zero-configuration relational database engine that stores an entire database as a single file on disk. It is the most widely deployed database engine in the world, embedded in virtually every smartphone, web browser, and operating system. SQLite requires no separate server process -- applications read and write the database file directly, making it ideal for local, single-user applications.

In the LLM knowledge base domain, SQLite appears as the structural storage layer in Sam Gallagher's Knowledge Graph Kit. While Karpathy's approach uses the file system itself as the database (one `.md` file per article, with wikilinks as implicit edges), Gallagher chose SQLite to store an explicit graph of nodes and edges with typed relationships.

## Key Features

- **Zero configuration**: No server to install, configure, or manage. The entire database is a single file that can be copied, backed up, or version-controlled trivially.

- **Relational model**: Full SQL query support enables structured queries over knowledge graph nodes and edges -- something impossible with flat markdown files.

- **Embeddable**: SQLite runs in-process, making it suitable for MCP servers, CLI tools, and agent pipelines that need local structured storage without network dependencies.

- **Lightweight**: The entire library is under 1MB, with no external dependencies, making it the natural choice for personal-scale tools.

## Role in LLM Knowledge Bases

SQLite represents the relational-database approach to knowledge storage, contrasting with Karpathy's file-system-based approach. In Gallagher's Knowledge Graph Kit, SQLite stores four node types (Task, Note, Person, Project) with typed edges (part_of, mentions, related_to), enabling structural queries that markdown wikilinks cannot support. For example, "find all tasks related to Project X that mention Person Y" is a straightforward SQL join in SQLite but would require LLM-mediated natural language navigation in a markdown wiki.

The tradeoff is clear: SQLite provides structural querying power at the cost of human readability. You cannot open a SQLite file in a text editor and read it the way you can with markdown files in [[entities/obsidian]]. For personal task and project management (Gallagher's use case), the structural power justifies the readability cost. For research knowledge synthesis (Karpathy's use case), the readability and LLM-friendliness of markdown wins.

## Mentioned In

- [[sources/gallagher-second-brain-knowledge-graphs]] -- used as the local storage backend for the Knowledge Graph Kit's node/edge graph structure
