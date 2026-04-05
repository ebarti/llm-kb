---
title: "Plain Text Longevity"
type: concept
sources: ["[[sources/sivers-plain-text-files]]", "[[sources/ango-file-over-app]]", "[[sources/mit-digital-preservation-formats]]"]
related: ["[[concepts/file-over-app]]", "[[concepts/markdown-as-universal-interface]]", "[[concepts/markdown-ecosystem]]"]
last_compiled: 2026-04-05
summary: "Plain text is the only digital format guaranteed to be readable decades or centuries from now — validated by individual practitioners, Obsidian's CEO, and institutional archivists."
reading_time: "3 min"
---

## Overview

Plain text longevity is the observation that `.txt` and `.md` files will be readable on any computer from the 1960s through the 2160s, while proprietary formats routinely become inaccessible within a single decade. This property makes plain text the only responsible choice for knowledge that matters.

## The Longevity Argument

Three independent sources converge on the same conclusion:

**Individual practice** ([[entities/derek-sivers]]): Since 1990, Sivers has written everything in plain text — four books, 400 blog posts, decades of journals. Every platform transition (DOS to Mac to Linux, desktop to mobile) was seamless because plain text requires no migration. "You will outlive these companies. Your writing should outlive you."

**Tool philosophy** ([[entities/steph-ango]]): The CEO of [[entities/obsidian]] frames this as "file over app" — if your notes must be readable on computers from the 2060s or 2160s, they need to be readable on computers from the 1960s. Plain text satisfies this constraint; proprietary databases do not.

**Institutional guidance** ([[sources/mit-digital-preservation-formats]]): MIT Libraries recommends plain text (US-ASCII, UTF-8, UTF-16) as the preferred preservation format for text content. Their five criteria — open standards, community adoption, published documentation, lossless compression, no encryption — are precisely what plain text provides.

## Why Proprietary Formats Fail

The historical record is unambiguous:

| Format | Status |
|--------|--------|
| WordPerfect (.wpd) | Effectively unreadable without conversion |
| Lotus 1-2-3 (.wk1) | Requires specialized tools to open |
| HyperCard stacks | Lost when Apple discontinued HyperCard |
| Google Notebook | Shut down 2012; all data exported or lost |
| Evernote (.enex) | Proprietary XML; company struggling financially |
| Plain text (.txt, .md) | Unchanged and universally readable since the 1960s |

## Markdown as Structured Plain Text

Markdown occupies an ideal position: it IS plain text (readable in any editor, stored as UTF-8), but with lightweight structural conventions that both humans and machines interpret consistently. A markdown file opened in Notepad is perfectly readable. A markdown file opened in Obsidian or VS Code gains navigation, linking, and rendering.

This is why [[concepts/markdown-as-universal-interface]] builds on plain text longevity rather than replacing it. Markdown doesn't add a layer of proprietary encoding — it adds conventions that degrade gracefully to readable text.

## Implications for Knowledge Management

For personal knowledge management, the plain text longevity principle means:

1. **Store knowledge as files, not database rows** — files survive tool changes; database records don't
2. **Use open, text-based formats** — markdown, YAML, CSV, JSON are all plain text
3. **Version control with git** — text diffs are meaningful; binary diffs are not
4. **Avoid cloud-only storage** — local files + sync beats cloud-only every time
5. **Treat any non-text format as ephemeral output** — PDFs and PPTX are generated artifacts, not sources of truth

## Sources

- [[sources/sivers-plain-text-files]] — 35+ years of personal practice validating the approach
- [[sources/ango-file-over-app]] — philosophical framework from the Obsidian CEO
- [[sources/mit-digital-preservation-formats]] — institutional archival guidance

## Related Concepts

- [[concepts/file-over-app]] — the philosophy that files must outlast apps
- [[concepts/markdown-as-universal-interface]] — markdown as structured plain text
- [[concepts/markdown-ecosystem]] — the tools that make plain text powerful without sacrificing longevity
- [[concepts/personal-knowledge-management]] — PKM requires durable storage
