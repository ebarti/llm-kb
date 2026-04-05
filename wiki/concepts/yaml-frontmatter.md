---
title: "YAML Frontmatter"
type: concept
sources: ["[[sources/markdown-agent-task-format]]", "[[sources/markdowndb-queryable-markdown]]"]
related: ["[[concepts/markdown-as-universal-interface]]", "[[concepts/markdown-ecosystem]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "YAML frontmatter is the de facto standard for embedding structured metadata in markdown files — enabling queryability, categorization, and machine processing while preserving plain-text readability."
---

## Overview

YAML frontmatter is a block of structured key-value metadata at the top of a markdown file, delimited by triple dashes (`---`). Popularized by Jekyll in the early 2010s, it has become the universal standard for adding structured metadata to markdown content without sacrificing readability.

## Structure

```yaml
---
title: "Article Title"
author: "Name"
date: 2026-04-05
tags: [topic1, topic2]
status: draft
---

# Article content starts here...
```

## Why It Matters

YAML frontmatter solves a fundamental tension in plain-text knowledge management: markdown is great for human-readable prose, but knowledge systems also need structured, queryable metadata. Frontmatter provides this without:

- Requiring a database (metadata lives in the file itself)
- Breaking plain-text readability (YAML is human-readable)
- Creating vendor lock-in (any tool can parse YAML)
- Separating metadata from content (they travel together)

## Supported Features

- **Scalar values**: strings, numbers, dates, booleans
- **Lists/arrays**: tags, categories, related items
- **Nested objects**: complex metadata hierarchies
- **Multi-format support**: YAML (default), TOML, JSON alternatives

## Ecosystem Support

YAML frontmatter is recognized by virtually every markdown tool:

| Tool | Frontmatter Support |
|------|-------------------|
| [[entities/obsidian]] | Properties panel, Dataview queries, Templates |
| Hugo/Jekyll/Astro | Page metadata, routing, templating |
| [[entities/pandoc]] | Document metadata (title, author, date) |
| [[entities/markdowndb]] | Extracts into SQLite for SQL querying |
| GitHub | Renders metadata in markdown preview |
| VS Code | Extension-based parsing and display |

## Limitations

- Best for structured metadata, not long-form content
- Indentation-sensitive (YAML uses spaces, not tabs)
- `---` delimiter can conflict with markdown horizontal rules
- No built-in schema validation (unlike JSON Schema)
- Not ideal for deeply nested or extensive metadata

## Role in LLM Knowledge Bases

In [[concepts/llm-knowledge-base]] systems, YAML frontmatter serves as the machine-readable metadata layer:
- `status` fields track compilation state
- `tags` enable categorization and discovery
- `sources` and `related` fields encode the knowledge graph
- `last_compiled` dates support staleness detection
- LLMs can read and write frontmatter natively

## Sources

- [[sources/markdown-agent-task-format]] — frontmatter for AI agent task management
- [[sources/markdowndb-queryable-markdown]] — frontmatter extraction into queryable databases

## Related Concepts

- [[concepts/markdown-as-universal-interface]] — frontmatter makes markdown machine-queryable
- [[concepts/markdown-ecosystem]] — frontmatter is the metadata standard across the ecosystem
- [[concepts/llm-knowledge-base]] — frontmatter as the KB's structured metadata layer
