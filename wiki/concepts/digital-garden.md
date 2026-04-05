---
title: "Digital Garden"
type: concept
sources: ["[[sources/appleton-digital-garden-history]]", "[[sources/stephango-vault-organization]]"]
related: ["[[concepts/networked-thought]]", "[[concepts/evergreen-notes]]", "[[concepts/learning-in-public]]", "[[concepts/zettelkasten]]", "[[entities/maggie-appleton]]", "[[entities/obsidian]]", "[[concepts/file-over-app]]"]
last_compiled: 2026-04-05
summary: "A philosophy of public knowledge-sharing that rejects chronological blogging in favor of continuously evolving, densely linked notes organized by topological relationships — featuring six core patterns including learning in public, epistemic status markers, and independent ownership."
---

## Overview

A digital garden is a publicly accessible collection of interconnected notes that evolve over time, organized by contextual relationships rather than publication dates. Unlike blogs (which present polished, time-stamped articles in reverse chronological order), digital gardens embrace imperfection, continuous revision, and non-linear exploration. They are the public expression of [[concepts/networked-thought]] and [[concepts/evergreen-notes]] practices.

The concept traces from Mark Bernstein's 1998 "Hypertext Gardens" through Mike Caufield's pivotal 2015 essay "The Garden and the Stream: a Technopastoral," which established the philosophical framework: **Streams** are ephemeral, timeline-based information flows (Twitter, email, blogs), while **Gardens** are richly linked landscapes that accumulate knowledge over time.

## Six Core Patterns

### 1. Topography Over Timelines
Gardens organize content through contextual relationships, not publication dates. Bidirectional links connect related ideas, allowing multiple entry points and non-linear exploration. There is no "most recent" feed — only a web of related concepts.

### 2. Continuous Growth
Notes begin as seedlings and mature indefinitely. Unlike a blog post (written once, published, abandoned), a garden note evolves through repeated revision as understanding deepens. This reflects genuine learning processes rather than presenting finished thoughts.

### 3. Imperfection and Learning in Public
Gardens embrace incompleteness. Many gardeners use **epistemic status markers** to signal how developed an idea is:
- **Seedling**: rough, newly planted thought
- **Budding**: developing idea with some supporting evidence
- **Evergreen**: well-developed, thoroughly considered

This transparency about knowledge maturity is the opposite of performative expertise. It embodies [[concepts/learning-in-public]] — sharing your learning journey as it happens.

### 4. Playful, Personal, and Experimental
Each garden reflects its creator's unique thinking patterns. Standardized templates are resisted in favor of creative expression through diverse mediums and unconventional layouts.

### 5. Intercropping and Content Diversity
Gardens integrate multiple media types: essays, diagrams, videos, code snippets, and audio. This mirrors sustainable agriculture's intercropping practice.

### 6. Independent Ownership
Gardens must exist on personally controlled domains, not commercial platforms. This ensures long-term control, data portability, and protection against platform dissolution — aligned with the IndieWeb movement.

## Key Figures

- **Mike Caufield**: Established the Garden vs. Stream philosophical foundation (2015)
- **[[entities/maggie-appleton]]**: Compiled comprehensive patterns and history
- **Tom Critchlow**: Added "campfires" to the metaphor framework (2018)
- **Joel Hooks**: "My blog is a digital garden, not a blog" (2019)
- **Amy Hoy**: Historical analysis of how blogging platforms standardized the chronological format

## The Garden vs. The Stream

| Dimension | Garden | Stream |
|-----------|--------|--------|
| Organization | Topological (by relationship) | Chronological (by date) |
| Content state | Evolving, never finished | Published, static |
| Navigation | Non-linear, exploratory | Linear, reverse-chronological |
| Authorial stance | Learning in public | Polished expertise |
| Audience relationship | Collaborative exploration | Performance |
| Platform | Self-hosted | Commercial (Medium, Twitter) |

## Relationship to Other PKM Concepts

Digital gardens are the *public-facing* expression of what [[concepts/zettelkasten]] and [[concepts/evergreen-notes]] accomplish privately. Where those systems are personal thinking tools, digital gardens extend the networked thought paradigm to public knowledge sharing. The [[concepts/second-brain]] methodology (via [[entities/tiago-forte]]) focuses on private productivity; digital gardens focus on communal knowledge cultivation.

## Publishing with Obsidian

[[entities/obsidian]] is the most popular authoring tool for digital gardens because its wikilink-based note structure maps naturally to hyperlinked web pages. Several publishing methods exist:

- **Obsidian Publish** ($10/month) — Official solution with one-click publishing, graph view, search, and custom domains
- **Digital Garden Plugin** (free, open source) — Community plugin deploying to Vercel/Netlify via GitHub; supports interactive graph, search, Dataview queries, and per-note feature control
- **Forestry.md** — Managed hosting with one-click setup
- **Static site generators** — [[entities/steph-ango]] uses Jekyll + GitHub + Netlify with a separate vault for his public site. Popular alternatives: Quartz (Hugo-based, purpose-built for Obsidian), Astro, Eleventy

Ango's publishing workflow demonstrates the [[concepts/file-over-app]] principle in action: the same markdown files that work in Obsidian compile directly to a public website via standard open-source tools.

## Sources
- [[sources/appleton-digital-garden-history]] — comprehensive history and six patterns
- [[sources/stephango-vault-organization]] — Ango's personal publishing pipeline

## Related Concepts
- [[concepts/networked-thought]] — the underlying paradigm
- [[concepts/evergreen-notes]] — the private practice that gardens make public
- [[concepts/learning-in-public]] — core garden philosophy
- [[concepts/zettelkasten]] — the private thinking tool counterpart
- [[concepts/file-over-app]] — enables publishing via standard file-based toolchains
- [[entities/obsidian]] — the primary authoring tool for digital gardens
