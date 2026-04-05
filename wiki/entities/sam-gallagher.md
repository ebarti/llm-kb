---
title: "Sam Gallagher"
type: entity
entity_type: person
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/second-brain]]", "[[concepts/personal-knowledge-management]]", "[[entities/sqlite]]", "[[entities/chromadb]]"]
last_compiled: 2026-04-06
summary: "Developer who built the Knowledge Graph Kit, an open-source MCP server using SQLite and ChromaDB, as a structure-first alternative to markdown-based personal knowledge management."
reading_time: "2 min"
---

## Overview

Sam Gallagher is a software developer and practitioner in the personal knowledge management space. His article "Using LLMs as a Second Brain: From Notes to Knowledge Graphs" documents his journey from using traditional productivity tools (Notion, Clickup, [[entities/obsidian]]) to developing the Knowledge Graph Kit -- an open-source MCP server that reimagines personal notes as nodes within a dynamic graph network rather than as files in a directory tree.

Gallagher's contribution to the LLM-KB discourse is his articulation of the structure-first vs. text-first debate. While Karpathy's system manipulates text (markdown files with wikilinks), Gallagher argues that "an intelligent knowledge system can't just manipulate text, it must understand structure." His Knowledge Graph Kit implements this philosophy using [[entities/sqlite]] for structural graph storage and [[entities/chromadb]] for semantic vector search.

## Key Contributions

- **Knowledge Graph Kit**: An open-source MCP (Model Context Protocol) server that provides four primitive node types (Task, Note, Person, Project) with relationship labels (part_of, mentions, related_to), stored in SQLite with ChromaDB vectorization for semantic search. The MCP packaging makes it directly usable as a tool for Claude Code and other AI agents.

- **Structure-first philosophy**: The insight that formal graph structure enables reasoning capabilities that flat text cannot support -- such as traversing typed relationships, filtering by node type, and surfacing connections between entities that share no keywords.

- **Practitioner journey narrative**: Gallagher's honest account of failing with elaborate Notion/Obsidian productivity systems provides valuable context for why LLM-maintained systems (whether text-based or graph-based) are appealing: they eliminate the management overhead that makes manual systems unsustainable.

## Role in LLM Knowledge Bases

Gallagher represents the graph-database perspective in the LLM-KB ecosystem, providing a counterpoint to Karpathy's markdown-centric approach. His work demonstrates that the LLM-as-intelligence-layer principle works equally well with a structured graph substrate (SQLite + ChromaDB) as with a flat file substrate (markdown + wikilinks). The key tradeoff he identifies: graphs are better for personal task/project management where typed relationships matter; markdown is better for research knowledge synthesis where human readability and LLM-friendliness matter.

## Mentioned In

- [[sources/gallagher-second-brain-knowledge-graphs]] -- full account of the journey from Notion/Obsidian to the Knowledge Graph Kit
