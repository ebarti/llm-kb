---
title: "Static Site Generators"
type: concept
sources: ["[[sources/pandoc-universal-converter]]", "[[sources/mdx-markdown-components]]", "[[sources/marp-markdown-presentations]]"]
related: ["[[concepts/markdown-ecosystem]]", "[[concepts/markdown-as-universal-interface]]", "[[concepts/mdx]]"]
last_compiled: 2026-04-05
summary: "Hugo, Jekyll, Astro, Eleventy, Gatsby, and Next.js all consume markdown as their primary content format — making markdown the default authoring language for the modern web."
---

## Overview

Static site generators (SSGs) transform markdown files into websites. They are the largest single category of markdown consumers, and their widespread adoption has cemented markdown as the default content format for the web.

## Major Generators

| Generator | Language | Markdown Handling | Key Strength |
|-----------|----------|------------------|--------------|
| **Hugo** | Go | Native markdown → HTML | Blazing build speed (milliseconds for thousands of pages) |
| **Jekyll** | Ruby | Markdown + Liquid templates | GitHub Pages integration, mature ecosystem |
| **Astro** | JS | Markdown, MDX, any data source | Islands architecture, minimal JS shipped |
| **Eleventy** | JS | Markdown + flexible templating | Zero-opinion, ships no JS by default |
| **Gatsby** | JS | Markdown via GraphQL | Rich plugin ecosystem, data layer |
| **Next.js** | JS | Markdown/MDX + ISR/SSR | Hybrid static/dynamic rendering |

## Why Markdown Won

SSGs could have standardized on any content format — HTML, reStructuredText, YAML, JSON. Markdown won because:

1. **Author experience**: Writers think in paragraphs and headings, not `<div>` tags
2. **Separation of concerns**: Markdown handles content; templates handle presentation
3. **Tooling ecosystem**: Every editor supports markdown; many support markdown-specific features
4. **Git-friendly**: Markdown diffs are human-readable; HTML diffs are noise
5. **LLM-friendly**: AI can generate and edit markdown content natively

## YAML Frontmatter as the Interface

SSGs established [[concepts/yaml-frontmatter]] as the standard contract between content and presentation:
- Frontmatter provides page metadata (title, date, tags, layout)
- The SSG template system reads frontmatter to control rendering
- This same pattern now powers [[concepts/llm-knowledge-base]] systems

## Relevance to Knowledge Management

SSGs demonstrate that a folder of markdown files is not just a personal knowledge store — it's a publishable website waiting to happen. The same wiki files that an LLM compiles and queries can be deployed as a public or team knowledge base with zero additional authoring.

## Sources

- [[sources/pandoc-universal-converter]] — Pandoc enables markdown → any presentation format
- [[sources/mdx-markdown-components]] — MDX brings interactivity to SSG content
- [[sources/marp-markdown-presentations]] — Marp applies the SSG pattern to slides

## Related Concepts

- [[concepts/markdown-ecosystem]] — SSGs as the web publishing branch
- [[concepts/markdown-as-universal-interface]] — SSGs cementing markdown as the web content standard
- [[concepts/mdx]] — interactive markdown for SSGs
- [[concepts/yaml-frontmatter]] — the metadata standard that SSGs popularized
