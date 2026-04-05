---
title: "Source: Marp — Markdown Presentation Ecosystem"
type: source-summary
source: "[[raw/marp-markdown-presentations]]"
related: ["[[concepts/markdown-ecosystem]]", "[[entities/marp]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "Marp converts markdown into presentation slides (HTML, PDF, PowerPoint) — demonstrating that markdown can replace proprietary formats even for visual content."
reading_time: "2 min"
---

## Key Points

- Write slide decks in CommonMark markdown with `---` as slide separators
- Exports to HTML, PDF, and PowerPoint via Chrome/Chromium rendering
- Three built-in themes; custom themes via CSS
- Ecosystem: VS Code extension, CLI, Marp Core engine, Marpit framework
- Pluggable architecture for extending functionality
- MIT-licensed open source

## Detailed Summary

Marp extends markdown's reach into presentation slides — a domain traditionally dominated by PowerPoint, Keynote, and Google Slides. The tool demonstrates that markdown's "universal interface" property applies beyond documents and websites.

The technical approach is elegant: standard CommonMark markdown with horizontal rules as slide boundaries, directives for per-slide styling, and the Marpit framework providing the rendering pipeline. Because presentations are just markdown files, they gain all the benefits: version control via git, editing in any text editor, easy collaboration, and future-proof storage.

Marp's ecosystem approach (VS Code extension + CLI + core library + framework) mirrors the broader markdown tooling pattern: a simple format at the center, with specialized tools for different workflows.

## Related Concepts

- [[concepts/markdown-ecosystem]] — Marp as presentation tooling within the ecosystem
- [[concepts/markdown-as-universal-interface]] — extending markdown's reach to presentations
- [[entities/marp]] — the tool itself
- [[concepts/plain-text-longevity]] — presentations stored as durable plain text
