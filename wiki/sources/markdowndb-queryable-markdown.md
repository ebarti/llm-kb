---
title: "Source: MarkdownDB — Queryable Markdown Files"
type: source-summary
source: "[[raw/markdowndb-queryable-markdown]]"
related: ["[[concepts/markdown-ecosystem]]", "[[entities/markdowndb]]", "[[concepts/yaml-frontmatter]]"]
last_compiled: 2026-04-05
summary: "MarkdownDB indexes markdown files into SQLite for SQL/JSON querying while preserving files on disk — bridging the plain-text vs. database gap."
reading_time: "2 min"
---

## Key Points

- Converts markdown files into an SQLite database with queryable API
- Extracts: YAML frontmatter, tags, tasks/checkboxes, links/backlinks
- Query via SQL or Node.js API with filter conditions
- Files remain as markdown on disk — SQLite is a derived index, not the source of truth
- Computed fields via plugin functions for custom metadata
- Open source and extensible

## Detailed Summary

MarkdownDB addresses a fundamental limitation of plain-text knowledge systems: queryability. While markdown files are human-readable and future-proof, finding "all posts by author X tagged with Y from the last 6 months" requires either scanning every file or building an index.

MarkdownDB solves this by generating an SQLite database from markdown files, extracting structured data from YAML frontmatter, tags, links, and tasks. The crucial design decision is that the markdown files remain the source of truth — the SQLite database is a disposable, regenerable index. This preserves all the advantages of plain-text storage while adding the queryability of a database.

This approach is directly relevant to [[concepts/llm-knowledge-base]] systems: the wiki files remain as markdown (human-readable, LLM-friendly, git-trackable), while MarkdownDB or similar indexing tools provide the structured querying that markdown alone lacks.

## Related Concepts

- [[concepts/markdown-ecosystem]] — MarkdownDB as queryability infrastructure
- [[concepts/yaml-frontmatter]] — the structured metadata that MarkdownDB extracts
- [[concepts/rag-vs-index-based-retrieval]] — MarkdownDB as an alternative to vector search
- [[concepts/llm-knowledge-base]] — complementary infrastructure for markdown KBs
