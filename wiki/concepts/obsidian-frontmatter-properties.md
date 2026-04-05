---
title: "Obsidian Frontmatter and Properties"
type: concept
sources: ["[[sources/stephango-vault-organization]]", "[[sources/dsebastien-obsidian-plugins-2026]]", "[[sources/nxcode-obsidian-ai-second-brain-2026]]"]
related: ["[[entities/obsidian]]", "[[entities/dataview]]", "[[concepts/vault-organization]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "YAML frontmatter properties in Obsidian provide structured metadata for notes — enabling Dataview queries, AI retrieval, search filtering, and database-like views via the Bases feature."
---

## Overview

Properties in [[entities/obsidian]] are structured metadata stored as YAML frontmatter at the top of markdown files. They provide a key-value layer that transforms plain notes into queryable data, enabling plugins like [[entities/dataview]] to treat the vault as a database and AI tools to perform precise retrieval.

Properties sit at the intersection of two principles: the [[concepts/file-over-app]] commitment to plain text (YAML is human-readable) and the need for structured data in a knowledge management system.

## Syntax and Structure

Properties are defined between triple-dash delimiters at the top of a note:

```yaml
---
title: "Article Title"
type: concept
tags: [obsidian, pkm]
created: 2026-04-05
rating: 7
author: "Steph Ango"
related: ["[[concepts/vault-organization]]"]
---
```

## Property Types

Obsidian recognizes several property types, configured in `.obsidian/types.json`:

| Type | Example | Notes |
|------|---------|-------|
| Text | `title: "My Note"` | Default type |
| Number | `rating: 7` | For Dataview calculations |
| Date | `created: 2026-04-05` | ISO 8601 format |
| Checkbox | `published: true` | Boolean values |
| List | `tags: [a, b, c]` | YAML arrays |
| Date & time | `modified: 2026-04-05T14:30` | Full timestamp |

## Display Modes

Properties can be rendered in three modes (Settings > Editor > Properties in document):

- **Visible** — Properties shown with a visual editor
- **Hidden** — Properties collapsed by default
- **Source** — Raw YAML displayed (necessary for viewing nested properties)

The **Properties view** core plugin provides vault-wide property management. Renaming a property through this view updates all occurrences across the entire vault.

## Querying Properties

### With Dataview

[[entities/dataview]] is the primary tool for querying properties:

```
TABLE rating, author, created
FROM "wiki/concepts"
WHERE rating >= 5
SORT created DESC
```

Dataview also supports inline fields using the `[key:: value]` syntax within note content, enabling property-like metadata without frontmatter.

### With Obsidian Search

Native search supports property filtering with operators: equals, contains, greater than, etc. For example: `[rating: > 5]` finds all notes with rating above 5.

### With Bases

Obsidian's Bases feature (November 2025) provides native database views (tables, lists) over notes filtered by properties — reducing dependence on Dataview for simple queries.

## Design Principles (from Steph Ango)

[[entities/steph-ango]]'s property design principles from his personal vault:

1. **Reusability** — Same property names across categories (e.g., `author` for books, articles, papers)
2. **Composability** — Templates combine different property sets
3. **Short names** — Brief property names for efficient typing
4. **Central type definition** — `.obsidian/types.json` defines property types once

His common properties include: dates (created, start, end, published), people (author, director, artist, cast, host, guests), themes (genre, type, topic, related), locations (neighborhood, city, coordinates), and rating (1-7 scale).

## Properties for AI Retrieval

For AI integration ([[concepts/obsidian-ai-integration]]), well-structured properties are critical:

- **Tags** enable targeted queries: `#meeting`, `#decision`, `#research`
- **Project references** scope AI responses to relevant contexts
- **Status fields** help AI understand note lifecycle (draft, active, archived)
- **Date fields** enable temporal queries and weekly reviews
- **People fields** support meeting preparation workflows

## Properties in This Knowledge Base

This LLM-KB uses a structured property schema:

- **type**: `concept`, `source-summary`, `entity`, `comparison`, `meta`, `index`, `log`
- **sources**: Array of wikilinks to source summaries
- **related**: Array of wikilinks to related articles
- **last_compiled**: ISO date of last compilation
- **summary**: One-line summary for the summaries cheat sheet
- **entity_type** (entities only): `person`, `tool`, `org`, `paper`, `dataset`

## Sources

- [[sources/stephango-vault-organization]] — Ango's property design principles
- [[sources/dsebastien-obsidian-plugins-2026]] — Metadata Menu and Sentinel plugins for property management
- [[sources/nxcode-obsidian-ai-second-brain-2026]] — properties for AI context engineering

## Related Concepts

- [[entities/dataview]] — the primary tool for querying properties
- [[concepts/vault-organization]] — properties enable organizational strategies
- [[concepts/markdown-as-universal-interface]] — YAML frontmatter as structured layer atop markdown
- [[concepts/obsidian-ai-integration]] — properties enable precise AI retrieval
