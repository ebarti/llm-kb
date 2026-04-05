---
title: "Source: MDX — Markdown for the Component Era"
type: source-summary
source: "[[raw/mdx-markdown-components]]"
related: ["[[concepts/mdx]]", "[[concepts/markdown-ecosystem]]", "[[entities/mdx]]"]
last_compiled: 2026-04-05
summary: "MDX extends markdown with JSX components, enabling interactive content within markdown documents — compiled at build time with no runtime overhead."
reading_time: "2 min"
---

## Key Points

- MDX blends markdown syntax with JSX, allowing React/Preact/Vue components inside markdown files
- "Everything is a component" — MDX files themselves become importable components
- Zero runtime: all compilation occurs at build time
- Extends via Remark and Rehype plugin ecosystem
- Integrates with Next.js, Docusaurus, Vite, Gatsby, and other major frameworks

## Detailed Summary

MDX represents a significant evolution of markdown: rather than just static text with formatting, MDX files can contain interactive JavaScript components. A documentation page can embed a live chart, an alert component, or a code playground — all while maintaining markdown's readable syntax for the prose content.

The key architectural insight is that MDX compiles to JavaScript at build time, not runtime. This means the "simplicity and elegance of markdown remains" — you use JSX only when you want to. The compilation pipeline uses the same Remark/Rehype ecosystem that powers standard markdown processing, making it compatible with existing markdown tooling.

MDX is widely adopted in technical documentation (Docusaurus, Next.js docs), design systems (Storybook), and content-heavy applications where static markdown isn't interactive enough but a full CMS is overkill.

## Notable Quotes

> "The simplicity and elegance of markdown remains, you use JSX only when you want to."

> "MDX has no runtime, all compilation occurs during the build stage."

## Related Concepts

- [[concepts/mdx]] — the format itself
- [[concepts/markdown-ecosystem]] — MDX as part of the broader markdown tool ecosystem
- [[concepts/markdown-as-universal-interface]] — MDX extends markdown's reach into interactive content
