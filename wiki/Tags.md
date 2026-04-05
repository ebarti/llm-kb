---
title: "Tag Index"
type: reference
last_updated: 2026-04-05
reading_time: "3 min"
---

# Tag Index

Browse all tags used across the knowledge base. Tags are defined in article frontmatter (`tags:` field) and inline (`#tag`).

---

## All Tags (Dataview)

```dataview
LIST WITHOUT ID tag + " (" + length(rows) + " articles)"
FROM "wiki"
FLATTEN file.tags AS tag
GROUP BY tag
SORT tag ASC
```

---

## Suggested Tag Taxonomy

The following tags are recommended for consistent categorization. Add them to article frontmatter as needed.

### A

- `#architecture` -- System design and structural patterns
- `#agent` -- LLM agent systems and multi-agent frameworks

### C

- `#comparison` -- Comparative analysis articles

### D

- `#data-quality` -- Data quality, cleaning, validation

### E

- `#evaluation` -- Benchmarks, metrics, testing

### F

- `#framework` -- Software frameworks and libraries

### G

- `#graph` -- Knowledge graphs, graph databases

### H

- `#hallucination` -- LLM hallucination and contamination risks

### I

- `#infrastructure` -- Databases, vector stores, deployment

### K

- `#knowledge-management` -- PKM, enterprise KM, knowledge workflows

### L

- `#llm` -- Large language models (general)

### M

- `#markdown` -- Markdown as knowledge substrate
- `#multi-agent` -- Multi-agent LLM systems

### O

- `#obsidian` -- Obsidian-specific features and workflows
- `#ontology` -- Ontology, taxonomy, schema design

### P

- `#pipeline` -- Data and compilation pipelines
- `#pkm` -- Personal knowledge management
- `#product` -- Product opportunities and gaps

### R

- `#rag` -- Retrieval-augmented generation
- `#retrieval` -- Information retrieval (general)
- `#risk` -- Risks, failure modes, mitigations

### S

- `#scale` -- Scalability considerations
- `#second-brain` -- Second brain / personal AI assistant

### T

- `#temporal` -- Time-aware knowledge, versioning
- `#tool` -- Specific tools (Obsidian, ChromaDB, etc.)

### W

- `#wiki` -- Wiki compilation and maintenance
- `#workflow` -- Human and LLM workflows

---

## Articles Per Tag (Dataview)

### Architecture
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#architecture")
```

### Risk
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#risk")
```

### Retrieval
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#retrieval") OR contains(file.tags, "#rag")
```

### Multi-Agent
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#multi-agent") OR contains(file.tags, "#agent")
```

### Knowledge Management
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#pkm") OR contains(file.tags, "#knowledge-management")
```

### Wiki & Pipeline
```dataview
LIST summary
FROM "wiki"
WHERE contains(file.tags, "#wiki") OR contains(file.tags, "#pipeline")
```

---

## Type-Based Browsing

Not using tags yet? Browse by article type instead:

- **Sources**: `path:wiki/sources` in search, or [[_index#Sources]]
- **Concepts**: `path:wiki/concepts` in search, or [[_index#Concepts]]
- **Entities**: `path:wiki/entities` in search
- **Comparisons**: `path:wiki/comparisons` in search

---

*Add tags to articles using the `tags:` frontmatter field (e.g., `tags: ["#architecture", "#llm"]`) or inline with `#tagname`. This page will automatically update via Dataview.*
