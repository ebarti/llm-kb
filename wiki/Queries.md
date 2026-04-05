---
title: "Dataview Queries"
type: reference
last_updated: 2026-04-05
reading_time: "3 min"
---

# Dataview Queries Reference

Pre-built Dataview queries for exploring and maintaining the knowledge base. Copy any query into a note or use directly from this page (requires the Dataview plugin).

---

## All Concepts Sorted by Source Count

```dataview
TABLE length(sources) AS "Source Count", summary
FROM "wiki/concepts"
WHERE type = "concept"
SORT length(sources) DESC
```

---

## All Sources with Related Concepts

```dataview
TABLE related AS "Related Concepts", last_compiled, summary
FROM "wiki/sources"
WHERE type = "source-summary"
SORT last_compiled DESC
```

---

## All Entities by Type

```dataview
TABLE entity_type AS "Entity Type", summary, url
FROM "wiki/entities"
WHERE type = "entity"
GROUP BY entity_type
```

---

## Articles Missing Summaries

```dataview
LIST
FROM "wiki"
WHERE !summary OR summary = ""
```

---

## Articles by Tag

```dataview
TABLE file.tags AS "Tags", type, summary
FROM "wiki"
WHERE file.tags
FLATTEN file.tags AS tag
GROUP BY tag
```

---

## Recent Ingests Timeline

```dataview
TABLE date_ingested AS "Ingested", type, summary
FROM "wiki"
WHERE date_ingested
SORT date_ingested DESC
```

---

## Cross-Reference Matrix: Sources and Concepts They Discuss

```dataview
TABLE WITHOUT ID
  file.link AS "Source",
  length(related) AS "Concepts Linked",
  related AS "Concepts"
FROM "wiki/sources"
SORT length(related) DESC
```

---

## Orphan Detection

Articles with no incoming backlinks (may need attention):

```dataview
LIST
FROM "wiki/sources" OR "wiki/concepts" OR "wiki/entities" OR "wiki/comparisons"
WHERE length(file.inlinks) = 0
```

---

## Stale Articles (Not Updated in 30+ Days)

```dataview
TABLE last_compiled AS "Last Compiled", summary
FROM "wiki/sources" OR "wiki/concepts"
WHERE last_compiled AND date(last_compiled) < date(now) - dur(30 days)
SORT last_compiled ASC
```

---

## Most Linked-To Articles

```dataview
TABLE length(file.inlinks) AS "Incoming Links", length(file.outlinks) AS "Outgoing Links", type
FROM "wiki"
SORT length(file.inlinks) DESC
LIMIT 20
```

---

## All Articles with Frontmatter Field Listing

```dataview
TABLE type, last_compiled, length(sources) AS "Sources", length(related) AS "Related"
FROM "wiki"
WHERE type AND type != "meta" AND type != "index" AND type != "log"
SORT type, file.name
```

---

## Articles by Compilation Date

```dataview
TABLE type, summary
FROM "wiki"
WHERE last_compiled
GROUP BY last_compiled
SORT last_compiled DESC
```

---

## Concepts Not Referenced by Any Source

```dataview
LIST
FROM "wiki/concepts"
WHERE !sources OR length(sources) = 0
```

---

## Full Text Search Helpers

To find articles mentioning specific terms, use Obsidian's built-in search (`Cmd+Shift+F`) with these patterns:

- `path:wiki/concepts "RAG"` -- concepts mentioning RAG
- `path:wiki/sources "Karpathy"` -- sources mentioning Karpathy
- `tag:#risk` -- articles tagged with risk
- `[summary:` -- articles with summary field (regex search)

---

*Install the Dataview community plugin to render these queries. In Obsidian: Settings > Community Plugins > Browse > "Dataview" > Install > Enable.*
