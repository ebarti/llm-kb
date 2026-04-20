---
title: "Transclusion"
type: concept
sources: ["[[sources/wikipedia-project-xanadu]]"]
related: ["[[entities/ted-nelson]]", "[[concepts/hypertext]]", "[[concepts/memex]]"]
last_compiled: 2026-04-05
summary: "Ted Nelson's concept of including content from one document inside another by reference rather than by copy — never widely adopted but anticipating modern content embedding, syndication, and wiki transclusion."
---

## Overview

Transclusion is [[entities/ted-nelson]]'s concept (from Project Xanadu) of including content from one document inside another by reference rather than by copying. When the source changes, all documents that transclude it update automatically. This differs fundamentally from copy-paste, which creates disconnected duplicates.

## Key Properties

- **Live reference**: Transcluded content reflects the source's current state
- **Provenance**: The origin of every piece of content is always traceable
- **Single source of truth**: Edits happen in one place and propagate everywhere
- **Attribution**: Built-in credit/royalty tracking for content creators

## Why It Matters for Knowledge Systems

Transclusion addresses the **duplication problem** in knowledge management: information copied across multiple documents becomes inconsistent when one copy is updated but others are not. This is precisely the challenge that [[concepts/wiki-compilation]] addresses through a single raw/ source of truth compiled into multiple wiki articles.

## Partial Realizations

- **Wiki templates**: MediaWiki's double-brace template syntax transcludes template content
- **Obsidian embeds**: The embed syntax (bang + double-bracketed note name) includes one note's content in another
- **RSS/Atom feeds**: Syndication as a form of content reference
- **Git submodules**: Code inclusion by reference
- **iframes**: Web content embedding (crude form)

## Sources
- [[sources/wikipedia-project-xanadu]] — transclusion as Xanadu's core concept

## Related Concepts
- [[concepts/hypertext]] — the broader system transclusion belongs to
- [[entities/ted-nelson]] — the inventor
- [[concepts/wiki-compilation]] — modern single-source-of-truth approach
