---
title: "Obsidian Graph View"
type: concept
sources: ["[[sources/nxcode-obsidian-ai-second-brain-2026]]", "[[sources/dsebastien-obsidian-plugins-2026]]"]
related: ["[[entities/obsidian]]", "[[concepts/knowledge-graph]]", "[[concepts/obsidian-as-ide]]", "[[concepts/linting-and-health-checks]]"]
last_compiled: 2026-04-05
summary: "Obsidian's graph view visualizes notes as nodes and links as edges — useful for seeing clusters, orphans, and connection patterns, but limited in analytical depth without plugins like InfraNodus."
---

## Overview

The Graph View is [[entities/obsidian]]'s built-in visualization of the vault's link structure. Every note is rendered as a node, and every `[[wikilink]]` as an edge, creating a dynamic, interactive network visualization. It provides a "bird's-eye view" of how knowledge is organized and connected.

## Core Capabilities

- **Global graph**: Shows all notes and their connections across the entire vault
- **Local graph**: Shows connections for the currently open note (backlinks and forward links within configurable depth)
- **Filtering**: Filter by tags, folders, file paths, or search queries
- **Color coding**: Group nodes by folder, tag, or other criteria
- **Interactive**: Drag, zoom, and pan; clicking a node opens the corresponding note

## Uses in Knowledge Management

### Pattern Discovery

The graph reveals clusters of densely connected notes (topic areas), bridge notes that connect different clusters, and isolated notes that may need more links. This visual pattern recognition is difficult to achieve through text-based navigation alone.

### Orphan Detection

Notes with no incoming or outgoing links appear as isolated dots in the graph. This directly supports [[concepts/linting-and-health-checks]] — orphan detection is one of the standard lint operations for wiki health.

### Knowledge Architecture

The graph view makes the LLM's [[concepts/wiki-compilation]] structure visible: source summaries link to concept articles, which link to entity pages, creating a layered network that the graph renders as distinct clusters.

## Limitations

Obsidian's default graph view is primarily a visualization tool, not an analytical one. It lacks:

- Network science metrics (betweenness centrality, community detection)
- Content gap analysis
- Automated clustering
- Export for external analysis

## Advanced Graph Plugins

Several plugins extend the graph view's analytical capabilities:

- **InfraNodus** — AI-enhanced knowledge graph providing network science metrics, content gap identification, and structural analysis of thinking patterns. Uses community detection and betweenness centrality scores.
- **Graph Analysis** — Adds centrality metrics and community detection to the graph view
- **Graph Banner** — Displays a mini graph view as a header in each note
- **Advanced Canvas** — Enables `.canvas` files to be indexed by the metadata cache for graph view integration

## Graph View in LLM-KB Context

For this knowledge base, the graph view serves as the primary verification tool for compilation quality:

- **Well-connected concepts** appear as central nodes with many edges
- **Source summaries** should link to multiple concept and entity pages
- **Entity pages** should be referenced by relevant source summaries and concepts
- **Orphan articles** signal compilation gaps that the LLM should address

The graph view is especially valuable because the LLM cannot "see" its own link structure holistically — the human using Obsidian can spot structural issues at a glance that would require the LLM to read many files sequentially.

## Sources

- [[sources/nxcode-obsidian-ai-second-brain-2026]] — graph view as knowledge map
- [[sources/dsebastien-obsidian-plugins-2026]] — Graph Banner and visualization plugins

## Related Concepts

- [[concepts/knowledge-graph]] — formal graph representations vs. Obsidian's implicit link graph
- [[concepts/obsidian-as-ide]] — graph view as a core IDE feature
- [[concepts/linting-and-health-checks]] — graph view aids visual lint
- [[entities/obsidian]] — the platform providing the graph view
