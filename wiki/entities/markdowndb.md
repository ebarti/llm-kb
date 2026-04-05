---
title: "MarkdownDB"
type: entity
entity_type: tool
sources: ["[[sources/markdowndb-queryable-markdown]]"]
related: ["[[concepts/markdown-ecosystem]]", "[[concepts/yaml-frontmatter]]", "[[concepts/rag-vs-index-based-retrieval]]"]
last_compiled: 2026-04-05
summary: "Open-source JS library that indexes markdown files into SQLite for SQL/JSON querying — files remain on disk as plain text, with the database as a derived index."
---

## Overview

MarkdownDB transforms collections of markdown files into a structured, queryable SQLite database. The key design principle: markdown files remain the source of truth on disk; the SQLite database is a disposable, regenerable index.

## Key Features

- Indexes YAML frontmatter, tags, tasks/checkboxes, links, and backlinks
- SQL querying and Node.js API with filter conditions
- Computed fields via plugin functions
- CLI: `npx mddb` generates `markdown.db`
- Open source and extensible

## Use Cases

Blog platforms, documentation sites, digital gardens, knowledge management systems, wiki implementations.

## Significance

Bridges the fundamental tension between plain-text simplicity and database queryability. You get both: markdown's portability, readability, and durability, plus SQL's filtering, sorting, and aggregation.

## Mentioned In

- [[sources/markdowndb-queryable-markdown]] — full feature overview
- [[concepts/markdown-ecosystem]] — MarkdownDB as queryability infrastructure
