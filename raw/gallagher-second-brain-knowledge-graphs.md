---
title: "Using LLMs as a Second Brain: From Notes to Knowledge Graphs"
source: "https://medium.com/@gallaghersam95/using-llms-as-a-second-brain-from-notes-to-knowledge-graphs-e7912f3a1428"
author: "Sam Gallagher"
date_published: 2024-12-01
date_ingested: 2026-04-05
tags: [second-brain, knowledge-graph, personal-knowledge-management, mcp, sqlite]
type: article
status: raw
discovered_via: search
---

# Using LLMs as a Second Brain: From Notes to Knowledge Graphs

## Overview

Sam Gallagher explores transforming personal note-taking through LLM-powered graph structures rather than traditional file-based systems. The article documents his journey from struggling with rigid productivity tools to developing the **Knowledge Graph Kit**, an open-source MCP server for intelligent knowledge management.

## The Problem with Traditional Approaches

Gallagher initially experimented with elaborate productivity systems using Notion, Clickup, and Obsidian. While initially effective, these approaches faced critical limitations:

- Complex structures became unmaintainable as priorities shifted
- Management overhead quickly outweighed benefits
- Traditional markdown-based systems lacked structural understanding

His first serious attempt used **gemini-cli**, a lightweight LLM interface for local files. Though promising initially, it revealed a fundamental flaw: "an intelligent knowledge system can't just manipulate text, it must understand structure."

## The Knowledge Graph Kit Solution

Rather than organizing information as nested markdown files, Gallagher reimagined notes as nodes within a dynamic network. The system features:

**Core Components:**
- Four primitive node types: Task, Note, Person, Project
- Relationship labels: part_of, mentions, related_to
- SQLite database for local storage
- ChromaDB vectorization enabling semantic search

This architecture enables the system to surface conceptual connections even when keywords don't overlap, creating what Gallagher describes as "a living, dynamic, network."

## Practical Implementation Examples

**Example 1 - Health Logging:**
Users can add contextual notes (e.g., "Evening PT went well, did the 16 minute walk") and the system automatically searches relevant projects, creates appropriately titled notes, and establishes connections.

**Example 2 - Task Retrieval:**
Natural language queries like "Show me all personal tasks I have to do" leverage structured search to return filtered results by status and tags.

## Key Insights

1. **Data Layer Precedence**: The underlying structure matters more than the interface. The same graph can support multiple presentation layers beyond conversational LLM interaction.

2. **Iterative Evolution**: Each refinement builds organically on previous work. New node types, deeper connections, and flexible interfaces emerge naturally from a robust foundation.

3. **Adaptive Systems**: The goal isn't replicating one person's perfect system, but creating flexible infrastructure others can extend and customize.

## Contrast with Markdown-Only Approaches

Gallagher's approach differs from Karpathy's markdown wiki in key ways:
- **Structured graph** (SQLite + nodes/edges) vs. **flat markdown files**
- **Semantic vector search** (ChromaDB) vs. **index-based LLM navigation**
- **Formal node types** vs. **free-form concept articles**
- Better for personal task/project management; Karpathy's better for research knowledge synthesis

Both approaches share the core principle: LLMs should maintain and navigate knowledge structure, not just answer questions in isolation.
