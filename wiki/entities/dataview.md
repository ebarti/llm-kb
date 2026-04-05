---
title: "Dataview"
type: entity
entity_type: tool
sources: ["[[sources/karpathy-llm-knowledge-bases]]", "[[sources/dairai-llm-knowledge-bases-architecture]]", "[[sources/dsebastien-obsidian-plugins-2026]]"]
related: ["[[entities/obsidian]]", "[[concepts/obsidian-as-ide]]", "[[concepts/llm-knowledge-base]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/obsidian-frontmatter-properties]]"]
last_compiled: 2026-04-05
summary: "The most important Obsidian power-user plugin: a SQL-like query engine over vault metadata supporting DQL, inline queries, and JavaScript — with Datacore as its next-gen successor."
reading_time: "2 min"
---

## Overview

Dataview is one of the most popular community plugins for [[entities/obsidian]], providing a query language for treating a vault of markdown files as a lightweight database. It reads YAML frontmatter metadata from `.md` files and allows users to write inline queries that generate dynamic tables, lists, and task views based on file properties like `type`, `last_compiled`, `sources`, and `related`.

In an LLM-maintained knowledge base where every article has structured frontmatter (as seen throughout this wiki), Dataview becomes a powerful navigation and auditing tool. Users can query for all concept articles modified before a certain date, list all sources related to a specific concept, or generate dashboards showing compilation status across the entire wiki.

## Key Features

- **Query language (DQL)**: Dataview provides a SQL-like query language for filtering, sorting, and grouping markdown files by their frontmatter properties. For example, `TABLE summary FROM "wiki/concepts" WHERE type = "concept" SORT last_compiled DESC` would produce a table of all concept articles sorted by compilation date.

- **Inline queries**: Short expressions like `= this.sources` can be embedded directly in article text to dynamically display metadata values.

- **JavaScript API**: For complex queries, Dataview exposes a JavaScript API (`dataviewjs`) enabling arbitrary computations over vault metadata.

- **Dynamic rendering**: Query results update in real time as files change, making Dataview views always current without manual maintenance.

## Role in LLM Knowledge Bases

Dataview complements the LLM-maintained wiki by providing human-navigable views over the wiki's metadata structure. While the LLM maintains `_index.md` and `_meta/summaries.md` as flat files, Dataview can generate equivalent views dynamically from frontmatter, serving as a cross-check on the LLM's metadata maintenance. It is particularly useful for [[concepts/linting-and-health-checks]]: a Dataview query listing articles where `last_compiled` is older than the most recent raw file ingestion date can quickly identify stale content.

Dataview also supports the wiki's function as a readable, navigable knowledge artifact. While the LLM interacts with files via direct reading and writing, humans interact via Obsidian's rendering layer, where Dataview queries provide dashboard-like views that make the wiki's structure transparent.

## Data Sources

Dataview indexes three types of metadata:
- **YAML frontmatter**: Properties in the `---` block at file top (see [[concepts/obsidian-frontmatter-properties]])
- **Inline fields**: `[key:: value]` syntax embedded in note content
- **Implicit fields**: Automatically captured tags, links, tasks, and file properties (name, path, created, modified)

## Query Types

Three approaches to querying:
1. **DQL (Dataview Query Language)**: SQL-like syntax for most use cases — `LIST`, `TABLE`, `TASK`, `CALENDAR` output types with `FROM`, `WHERE`, `SORT`, `GROUP BY`, `FLATTEN` commands
2. **Inline queries**: Single-value displays embedded in text: `` `= this.sources` ``
3. **JavaScript queries** (`dataviewjs`): Full JS environment for complex logic — runs with plugin-level access (can read files, make network calls)

## Ecosystem Position

Identified by Sebastien Dubois as part of the foundational plugin trio (Dataview, [[entities/templater]], QuickAdd). **Datacore** is emerging as the next-generation successor to Dataview, promising improved performance and features.

Obsidian's native **Bases** feature (November 2025) provides simpler database views over properties, reducing dependence on Dataview for basic queries while Dataview remains essential for complex, programmatic queries.

## Mentioned In

- [[sources/karpathy-llm-knowledge-bases]] -- referenced as part of the Obsidian plugin ecosystem
- [[sources/dairai-llm-knowledge-bases-architecture]] -- plugin-based views for research indexing
- [[sources/dsebastien-obsidian-plugins-2026]] -- identified as the most important power-user plugin
