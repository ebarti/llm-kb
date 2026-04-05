---
title: "Pandoc"
type: entity
entity_type: tool
sources: ["[[sources/pandoc-universal-converter]]"]
related: ["[[concepts/markdown-ecosystem]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "Universal document converter (Haskell, GPL) that converts between 40+ formats via a markdown-centric AST — maintained since 2006 by John MacFarlane."
---

## Overview

Pandoc is a command-line tool and Haskell library for converting between markup formats. Created by John MacFarlane in 2006 and continuously maintained for 20 years, it supports 40+ input/output formats including Markdown, HTML, LaTeX, Word DOCX, EPUB, PDF, reStructuredText, Org-Mode, and many wiki formats.

## Key Features

- **Modular reader/writer architecture** centered on an Abstract Syntax Tree (AST)
- **Enhanced Markdown** with tables, footnotes, citations, math, definition lists, metadata blocks
- **Automated citations** supporting hundreds of CSL styles (BibTeX, BibLaTeX, CSL JSON, YAML)
- **Custom Lua readers/writers** for extending format support
- **Template system** for customizing output
- **PDF generation** via LaTeX, ConTeXt, or wkhtmltopdf

## Significance

Pandoc is the single most important tool validating markdown as a universal interchange format. Its architecture — parse any input into an AST, generate any output from that AST — with markdown as the most natural human-readable AST representation — makes markdown the practical hub of the document format universe.

## Mentioned In

- [[sources/pandoc-universal-converter]] — detailed feature and architecture overview
- [[concepts/markdown-ecosystem]] — Pandoc as the conversion backbone
- [[concepts/markdown-as-universal-interface]] — Pandoc as proof of markdown's universality
