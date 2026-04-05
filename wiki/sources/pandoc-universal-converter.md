---
title: "Source: Pandoc — Universal Document Converter"
type: source-summary
source: "[[raw/pandoc-universal-converter]]"
related: ["[[concepts/markdown-ecosystem]]", "[[entities/pandoc]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "Pandoc converts between dozens of markup and document formats via a markdown-centric AST — effectively making markdown the hub of the document format universe."
reading_time: "2 min"
---

## Key Points

- Universal converter between 40+ formats: Markdown, HTML, LaTeX, DOCX, EPUB, PDF, reStructuredText, Org-Mode, wiki markups, presentations, and more
- Modular reader/writer architecture centered on an Abstract Syntax Tree (AST)
- Enhanced Markdown with tables, footnotes, citations, math, definition lists, metadata
- Automated citation system supporting hundreds of CSL styles
- Custom readers/writers can be written in Lua
- Available as both a Haskell library and CLI tool, GPL-licensed, maintained since 2006

## Detailed Summary

Pandoc is the single most important tool validating markdown's position as a universal document format. Its architecture tells the story: any input format is parsed into an AST, and any output format is generated from that AST. Markdown serves as the most natural human-readable representation of that AST — making it the practical lingua franca of document conversion.

By supporting conversion between Markdown and Word, LaTeX, HTML, EPUB, PDF, wiki formats, and presentation slides, Pandoc ensures that writing in markdown imposes no ceiling on output format. A researcher can write in markdown, generate a LaTeX paper, a Word document for collaborators, an HTML version for the web, and slides for a conference — all from the same source.

Pandoc's 20-year history (2006-2026) also demonstrates the durability of the markdown-centric approach: the tool has outlasted numerous proprietary document platforms.

## Related Concepts

- [[concepts/markdown-ecosystem]] — Pandoc as the conversion backbone
- [[concepts/markdown-as-universal-interface]] — Pandoc proves markdown is a universal interchange format
- [[entities/pandoc]] — the tool itself
- [[concepts/plain-text-longevity]] — Pandoc ensures plain text can always reach any target format
