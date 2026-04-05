---
title: "Knowledge Graph vs. Wiki"
type: comparison
subjects: ["[[concepts/knowledge-graph]]", "[[concepts/llm-knowledge-base]]"]
sources: ["[[sources/karma-multi-agent-knowledge-graph]]", "[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/graphiti-temporal-knowledge-graphs]]", "[[sources/karpathy-llm-knowledge-bases]]", "[[sources/pebblous-cheap-ontology]]"]
last_compiled: 2026-04-06
summary: "Comparing formal knowledge graphs (nodes/edges with typed relationships) against flat markdown wikis (files with wikilinks) as substrates for LLM-maintained knowledge bases."
---

## Overview

This comparison addresses the most fundamental architectural choice in LLM knowledge base design: should knowledge be stored as formal graph structures (entities, relationships, types, and schemas) or as human-readable markdown files with implicit structure via wikilinks? The sources in this wiki present three graph-based approaches ([[entities/karma]], [[entities/graphiti]], [[entities/sam-gallagher]]'s Knowledge Graph Kit) against [[entities/andrej-karpathy]]'s markdown wiki approach, and each has distinct strengths.

The choice is not purely technical -- it reflects a deeper question about who the knowledge base serves. Graphs optimize for machine queryability and structural precision; wikis optimize for human readability and LLM friendliness. The best choice depends on whether the primary consumer is a human reader, an AI agent, or a formal reasoning system.

## Comparison Table

| Dimension | Knowledge Graph (Formal) | Markdown Wiki (Flat) |
|-----------|------------------------|---------------------|
| Structure | Explicit nodes, edges, types, schemas | Implicit via wikilinks and directory structure |
| Query language | Cypher, SPARQL, or structured API | LLM natural language over index files |
| Temporal support | Built-in (Graphiti's validity windows) | Manual (file dates, inline notes) |
| Human readability | Low (requires graph UI or queries) | High (plain text in any editor) |
| LLM friendliness | Moderate (requires graph serialization) | High (markdown is native LLM output) |
| Conflict detection | Formal (KARMA's multi-agent verification) | Informal (LLM linting passes) |
| Schema enforcement | Yes (typed entities and relationships) | No (conventions enforced by LLM prompts) |
| Setup complexity | High (graph DB, schema design, ontology) | Low (directory structure + LLM) |
| Cost | $10M-$20M enterprise; lower for personal graph DBs | API costs only |
| Scale | Enterprise (KARMA: 1000s of papers) | Personal (~100-400 articles) |
| Auditability | Provenance to episodes/sources | Provenance to raw/ files |
| Version control | Requires graph DB snapshots | Native Git integration (plain text) |
| Best for | Scientific literature, operational knowledge, task management | Research synthesis, personal learning, document Q&A |

## Detailed Analysis

**The structure debate**: [[entities/sam-gallagher]] articulated the core tension: "an intelligent knowledge system can't just manipulate text, it must understand structure." His Knowledge Graph Kit stores notes as typed nodes (Task, Note, Person, Project) with labeled edges (part_of, mentions, related_to) in [[entities/sqlite]], enabling structural queries impossible with flat markdown. However, Karpathy's system implicitly encodes structure through wikilinks, article types (source vs. concept), and LLM-maintained metadata -- enough structure for research synthesis even if not formally queryable.

**The temporal gap**: [[entities/graphiti]]'s temporal validity windows expose a genuine limitation of markdown wikis. Facts that change over time (product roadmaps, competitive landscapes, personnel) need explicit "valid from/until" timestamps. Markdown handles this only through manual notes or file dates, which is adequate for static research (papers do not change) but insufficient for operational knowledge. This is where formal graphs have a clear advantage.

**The cost disruption**: The [[concepts/cheap-ontology]] analysis quantifies the cost difference dramatically. Enterprise knowledge graphs have historically required $10M-$20M in investment with only 27% reaching production. Karpathy's markdown approach costs only API fees. Even personal graph tools like [[entities/sqlite]] + [[entities/chromadb]] require more setup than markdown + Obsidian. The 1,000-fold expansion in LLM context windows made the markdown approach viable by enabling the LLM to load entire wikis.

**The convergence**: Both approaches share core principles: raw input preserved as source of truth, LLM-derived structured knowledge separate from raw data, incremental enrichment from new sources, and conflict detection. The difference is representation: formal triplets (entity, relation, entity) vs. markdown prose with wikilinks. As LLMs become better at reasoning over both representations, the practical gap may narrow.

## When to Use Each

**Use a knowledge graph when:**
- Facts change over time and you need temporal tracking
- Relationships have formal types that enable structured queries
- The knowledge base serves AI agents needing precise entity/relation lookups
- Scale exceeds what context windows can handle
- Multiple teams contribute and schema enforcement prevents conflicts

**Use a markdown wiki when:**
- Human readability is a priority
- The primary use case is research synthesis and personal learning
- Scale is personal to small-team (~100-400 articles)
- Infrastructure simplicity matters (files + LLM, no database)
- Version control with Git is desired
- The filing loop (compounding knowledge from queries) is valued

## Sources

- [[sources/karma-multi-agent-knowledge-graph]] -- formal KG enrichment at research scale
- [[sources/gallagher-second-brain-knowledge-graphs]] -- personal graph with SQLite + ChromaDB
- [[sources/graphiti-temporal-knowledge-graphs]] -- temporal context graphs as middle ground
- [[sources/karpathy-llm-knowledge-bases]] -- the markdown wiki reference implementation
- [[sources/pebblous-cheap-ontology]] -- cost and historical comparison
