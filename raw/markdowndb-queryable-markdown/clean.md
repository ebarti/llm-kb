---
title: "MarkdownDB: Queryable Markdown Files"
source: "https://markdowndb.com/"
author: "MarkdownDB Contributors"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [markdown, database, sqlite, querying, frontmatter, knowledge-management]
type: article
status: raw
discovered_via: search
---

# MarkdownDB: Turn Markdown Files into Structured Data

## What It Is

MarkdownDB is "an open JS library to turn markdown files into structured, queryable data (SQL and JSON)." It transforms plain markdown documents into a searchable database, enabling developers to build content-driven applications rapidly.

## Core Functionality

Converts markdown files into an SQLite database with a queryable API. Users index markdown folders using the command-line tool (`npx mddb`), which generates a `markdown.db` file containing structured data extracted from the content.

## Key Features

**Metadata Extraction**:
- YAML frontmatter parsing
- Automatic task detection from checkboxes
- Tag extraction from both frontmatter and document body
- Link and backlink identification

**Advanced Capabilities**:
- Computed fields via plugin functions
- SQL querying for complex searches
- JSON API for programmatic access
- Filtering by frontmatter field values

## How It Treats Markdown as a Database

Users can "query your collection of markdown files like a database" to find documents matching specific criteria — such as all posts by a certain author, created within a date range, or containing particular tags.

## Query Methods

1. **SQL**: Direct queries against the SQLite index
2. **Node.js API**: Framework-agnostic JavaScript methods like `getFiles()` with filter conditions

## Use Cases

- Blog platforms, documentation sites, digital gardens
- Knowledge management systems, wiki implementations

## Significance

MarkdownDB bridges the gap between plain-text markdown and structured databases. Files remain as markdown on disk (preserving all plain-text advantages), while the SQLite index adds queryability without sacrificing portability.
