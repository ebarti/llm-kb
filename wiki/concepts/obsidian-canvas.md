---
title: "Obsidian Canvas"
type: concept
sources: ["[[sources/dsebastien-obsidian-plugins-2026]]"]
related: ["[[entities/obsidian]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/obsidian-graph-view]]", "[[entities/excalidraw]]"]
last_compiled: 2026-04-05
summary: "Obsidian Canvas provides infinite spatial boards for mapping notes, media, and ideas — enhanced by the Advanced Canvas plugin for flowcharts, presentations, and graph integration."
---

## Overview

Canvas is a core [[entities/obsidian]] feature (not a community plugin) that provides infinite spatial boards where users can arrange notes, images, links, and text cards on a freeform 2D surface. It enables spatial thinking — organizing ideas by physical position and proximity rather than hierarchical folders or linear lists.

Canvas files are stored as `.canvas` JSON files in the vault, maintaining [[concepts/file-over-app]] principles: they are local, readable, and version-controllable.

## Core Capabilities

- **Embed existing notes**: Drag notes from the vault onto the canvas as live previews
- **Text cards**: Create standalone text blocks directly on the canvas
- **Media support**: Add images, PDFs, and web content
- **Connections**: Draw edges between cards to show relationships
- **Groups**: Organize cards into labeled groups
- **Colors**: Color-code cards and connections for visual categorization

## Advanced Canvas Plugin

The community-developed Advanced Canvas plugin significantly extends the core feature:

- **Flowcharts**: Create structured flowchart layouts with directional edges
- **Presentations**: Use canvas as a slide deck with navigation between groups
- **Graph integration**: `.canvas` files indexed by metadata cache for graph view, backlinks, and outgoing links
- **Custom styling**: Shapes, colors, borders, and arrows for nodes and edges
- **Collapsible groups**: Toggle group visibility for complex canvases
- **Portals**: Embed one canvas inside another
- **Auto-resizing nodes**: Content-aware sizing
- **Focus mode**: Distraction-free canvas editing
- **Frontmatter support**: Full frontmatter for `.canvas` files
- **Search**: Full-text search across all nodes within a canvas
- **Export**: PNG/SVG export with transparency and privacy mode

## Creative Use Cases

Beyond typical mind-mapping, practitioners use Canvas for:

- **Collision boards**: Drop everything you care about onto a blank canvas, intentionally without order, then drag pieces together to create unexpected connections
- **Book brains**: Main book note at center, surrounded by clusters of key ideas, quotes, and personal reactions
- **Project dashboards**: Central project note linked to meeting notes, decisions, and reference material
- **Research synthesis**: Map relationships between sources, concepts, and arguments spatially

## Canvas vs. Excalidraw

| Dimension | Canvas | [[entities/excalidraw]] |
|-----------|--------|------------|
| Purpose | Spatial note arrangement | Freehand drawing and diagramming |
| Content type | Note embeds, text cards, links | Sketches, diagrams, handwritten notes |
| Structure | Cards + edges | Freeform shapes and lines |
| File format | `.canvas` (JSON) | `.excalidraw` (JSON) |
| Best for | Knowledge mapping | Visual thinking and diagram creation |

## Relevance to LLM-KB

Canvas could serve as a spatial visualization layer for LLM-KB content — for example, arranging concept articles spatially to show relationships that the graph view represents as a network. However, canvas files are JSON (not markdown), making them harder for LLMs to author programmatically. The Claude Code canvas integration (via skills) represents an emerging bridge between LLM authoring and spatial visualization.

## Sources

- [[sources/dsebastien-obsidian-plugins-2026]] — Canvas-related plugins

## Related Concepts

- [[entities/obsidian]] — the platform
- [[concepts/obsidian-graph-view]] — complementary network visualization
- [[entities/excalidraw]] — complementary freehand visualization
- [[concepts/obsidian-plugin-ecosystem]] — Advanced Canvas as plugin extension
