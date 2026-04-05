---
title: "Vault Organization Strategies"
type: concept
sources: ["[[sources/stephango-vault-organization]]", "[[sources/nxcode-obsidian-ai-second-brain-2026]]"]
related: ["[[entities/obsidian]]", "[[entities/steph-ango]]", "[[concepts/obsidian-frontmatter-properties]]", "[[concepts/personal-knowledge-management]]", "[[concepts/file-over-app]]", "[[concepts/vault-separation]]"]
last_compiled: 2026-04-05
summary: "Strategies for organizing Obsidian vaults: flat folders + profuse links (Ango), PARA method, type-based folders, and AI-optimized architectures with context engineering."
---

## Overview

Vault organization is one of the most debated topics in the [[entities/obsidian]] community. The core tension is between **hierarchical folder structures** (easy to browse) and **flat link-based organization** (flexible, emergent, favored by [[entities/steph-ango]]). In practice, most productive vaults use a hybrid approach: a few top-level folders for broad categories, with internal links and tags providing the actual organizational structure.

## Major Approaches

### Ango's Bottom-Up Approach (Flat + Links)

[[entities/steph-ango]]'s personal vault uses:

- **Flat structure**: Root (personal writing), References, Clippings, Attachments, Daily, Templates — no nested subfolders
- **Navigation**: Quick switcher and backlinks, not folder browsing
- **Profuse internal links**: Including unresolved links as "breadcrumbs for future connections"
- **Emergent structure**: "Embraces chaos and laziness to create emergent structure"

Key rule: "Avoid folders for organization." Folders are for note *types* (references, daily, templates), not topics.

### PARA Method (Folder-Based)

Tiago Forte's PARA system organizes by actionability:

- **Projects** — Active work with deadlines
- **Areas** — Ongoing responsibilities
- **Resources** — Topics of interest
- **Archives** — Inactive items

Uses numbered prefixes (01-Projects, 02-Areas, etc.) for fixed sort order. More structured than Ango's approach but can create decision fatigue about where to file notes.

### Maps of Content (MOC)

Nick Milo's approach uses dedicated "map" notes that link to related notes on a topic. MOCs function as manually curated indexes — similar to what the `_index.md` file does in this LLM-KB, but maintained by a human.

### AI-Optimized Architecture

For vaults designed to work with AI tools (plugins or external agents), the NxCode guide recommends:

```
Vault/
├── Projects/
│   ├── website-redesign/
│   └── mobile-app/
├── Meetings/
├── Research/
├── Ideas/
└── Templates/
```

Context engineering principles:
- Descriptive filenames with dates: `2026-02-21-meeting-product-roadmap.md`
- Rich YAML frontmatter for precise retrieval
- Atomic notes (one concept per note) for better AI retrieval accuracy
- Consistent tagging: `#idea`, `#decision`, `#meeting`, `#research`
- Explicit [[wikilinks]] so AI can follow the relationship graph

### LLM-KB Architecture (This Vault)

The LLM knowledge base uses a purpose-built structure:

```
raw/            → Immutable ingested sources
wiki/           → LLM-maintained wiki
  sources/      → Per-source summaries
  concepts/     → Cross-source synthesis
  entities/     → People, tools, orgs, papers
  comparisons/  → Side-by-side analysis
  _meta/        → Metadata (summaries, links, manifest)
output/         → Generated artifacts
```

This is the most structured approach — folders correspond to article types, not topics. The LLM handles all filing decisions.

## Best Practices (Cross-Source Consensus)

Several principles appear across multiple sources:

| Practice | Rationale |
|----------|-----------|
| Use internal links profusely | Creates discoverable connections |
| Use `YYYY-MM-DD` dates everywhere | Consistent, sortable, parseable |
| Pluralize tags | Never wonder about singular vs. plural |
| Keep tags lowercase, 1-2 words | Reduces tag sprawl |
| Write a personal style guide | "Collapses hundreds of future decisions into one" (Ango) |
| Prefer one vault over multiple | Enables cross-domain connections |
| Use templates for consistency | Composable metadata properties |

## Vault Separation vs. Single Vault

There is a tension between the single-vault recommendation (maximizes connections) and [[concepts/vault-separation]] (separates trusted human content from potentially hallucinated AI content). For LLM-KB use cases, the Ango-recommended two-vault pattern makes sense: one vault for human-curated personal notes, a separate vault for the LLM-maintained wiki.

## Sources

- [[sources/stephango-vault-organization]] — Ango's personal vault structure and principles
- [[sources/nxcode-obsidian-ai-second-brain-2026]] — AI-optimized vault architecture

## Related Concepts

- [[concepts/obsidian-frontmatter-properties]] — metadata that enables vault querying
- [[concepts/personal-knowledge-management]] — the broader PKM methodology space
- [[concepts/file-over-app]] — vault organization built on file-first principles
- [[concepts/vault-separation]] — when and why to use multiple vaults
