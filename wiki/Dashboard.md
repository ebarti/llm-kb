---
title: "Dashboard"
type: dashboard
last_updated: 2026-04-05
reading_time: "3 min"
---

# LLM Knowledge Base Dashboard

---

## Quick Stats

| Metric             | Count   |
| ------------------ | ------- |
| Sources            | 11      |
| Concepts           | 20      |
| Entities           | 0       |
| Comparisons        | 0       |
| Total Articles     | 31      |
| Raw Files Compiled | 11 / 11 |

> Tip: Install the Dataview plugin for live stats. Then replace the table above with:

```dataview
TABLE length(rows) AS "Count"
FROM "wiki"
WHERE type
GROUP BY type
```

---

## Recently Compiled

```dataview
TABLE summary, last_compiled
FROM "wiki/sources" OR "wiki/concepts"
SORT last_compiled DESC
LIMIT 10
```

---

## Recently Modified

```dataview
TABLE file.mtime AS "Modified", type, summary
FROM "wiki"
SORT file.mtime DESC
LIMIT 10
```

---

## Top Connected Concepts (Hub Nodes)

The most connected articles in the wiki, based on incoming + outgoing wikilinks:

| Article | Incoming | Outgoing | Total |
|---------|----------|----------|-------|
| [[concepts/llm-knowledge-base]] | 24 | 5 | 29 |
| [[concepts/wiki-compilation]] | 8 | 2 | 10 |
| [[concepts/rag-vs-index-based-retrieval]] | 10 | 2 | 12 |
| [[concepts/knowledge-graph]] | 6 | 4 | 10 |
| [[concepts/hallucination-contamination]] | 5 | 4 | 9 |
| [[concepts/linting-and-health-checks]] | 5 | 2 | 7 |
| [[concepts/personal-knowledge-management]] | 5 | 4 | 9 |
| [[concepts/multi-agent-systems]] | 4 | 3 | 7 |
| [[concepts/data-quality-bottleneck]] | 3 | 4 | 7 |
| [[concepts/obsidian-as-ide]] | 5 | 2 | 7 |

---

## Orphan Watch

Articles with no incoming links from other wiki pages:

```dataview
LIST
FROM "wiki/sources" OR "wiki/concepts" OR "wiki/entities" OR "wiki/comparisons"
WHERE length(file.inlinks) = 0
```

Currently known orphans (static):
- [[sources/karpathy-llm-knowledge-bases]] (root source, referenced only from `_index.md`)

---

## Quick Actions

- **New article**: Create from template with `Cmd+Shift+T`
- **Search wiki**: `Cmd+Shift+F` for full-text search
- **Graph view**: `Cmd+Shift+G` to visualize connections
- **Quick switcher**: `Cmd+O` to jump to any article

| Action | Link |
|--------|------|
| Browse all articles | [[_index]] |
| View summaries | [[_meta/summaries]] |
| View link graph | [[_meta/links]] |
| View compilation manifest | [[_meta/manifest]] |
| Pre-built queries | [[Queries]] |
| Graph analysis | [[Graph]] |
| Tag index | [[Tags]] |
| Compilation log | [[log]] |

---

## Tag Cloud

```dataview
LIST WITHOUT ID
FROM "wiki"
FLATTEN file.tags AS tag
GROUP BY tag
```

> Note: Tags will appear here once articles include `tags:` in their frontmatter. Use tags like `#architecture`, `#risk`, `#retrieval`, `#workflow`, `#multi-agent`, `#ontology`, `#pkm`.

---

## Article Type Breakdown

```dataview
TABLE WITHOUT ID
  type AS "Type",
  length(rows) AS "Count",
  map(rows, (r) => link(r.file.path, r.file.name)) AS "Articles"
FROM "wiki"
WHERE type AND type != "meta" AND type != "index" AND type != "log" AND type != "dashboard"
GROUP BY type
SORT length(rows) DESC
```

---

## Stale Articles

Articles not updated in the last 30 days:

```dataview
TABLE last_compiled, summary
FROM "wiki/sources" OR "wiki/concepts"
WHERE last_compiled AND date(last_compiled) < date(now) - dur(30 days)
SORT last_compiled ASC
LIMIT 15
```

---

*Last manual update: 2026-04-05. Most sections use Dataview for live data.*
