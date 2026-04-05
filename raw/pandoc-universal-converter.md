---
title: "Pandoc: Universal Document Converter"
source: "https://pandoc.org/"
author: "John MacFarlane"
date_published: 2025-01-01
date_ingested: 2026-04-05
tags: [pandoc, markdown, conversion, document-formats, haskell, open-source]
type: article
status: raw
discovered_via: search
---

# Pandoc: Universal Document Converter

## Overview

Pandoc is a comprehensive markup format conversion tool described as "a universal document converter" and "your swiss-army knife" for converting files between different markup formats. Written in Haskell, released under GPL, copyright 2006-2025 by John MacFarlane.

## Architecture

Modular design with:
- Separate reader and writer modules for each input/output format
- An Abstract Syntax Tree (AST) at its core, with Haskell, JSON, and XML representations
- Custom readers and writers can be created using Lua
- Template system and filter framework for extensibility

## Supported Format Categories

**Lightweight Markup**: Markdown variants (CommonMark, GFM, MultiMarkdown, PHP Markdown Extra), reStructuredText, AsciiDoc, Emacs Org-Mode, Textile, Djot

**Web Formats**: HTML4/5, XHTML, chunked HTML output

**Publishing**: EPUB (v2/3), FictionBook2, LaTeX, ConTeXt, DocBook, JATS

**Data & Office**: Microsoft Word (.docx), RTF, OpenOffice/LibreOffice (.odt), Excel spreadsheets, Jupyter notebooks

**Specialized**: Wiki markups (MediaWiki, DokuWiki, etc.), slide presentations (reveal.js, Beamer, PowerPoint), PDF (via multiple engines), terminal ANSI output

## Key Features

**Markdown Extensions**: Document metadata (title, author, date), footnotes, tables, definition lists, superscript/subscript, strikeout, syntax highlighting for code blocks

**Mathematics**: Native LaTeX math support with multiple HTML rendering methods including MathJax and MathML conversion

**Citations & Bibliographies**: Automated citation system supporting hundreds of CSL styles with bibliographic data in BibTeX, BibLaTeX, CSL JSON, or YAML formats

## Significance

Pandoc establishes markdown as a hub format for document conversion. Because Pandoc can read and write so many formats with markdown as its lingua franca, it makes markdown the practical center of the document format universe.
