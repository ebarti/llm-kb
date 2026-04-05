---
title: "MDX (Markdown + JSX)"
type: concept
sources: ["[[sources/mdx-markdown-components]]"]
related: ["[[concepts/markdown-ecosystem]]", "[[concepts/markdown-as-universal-interface]]", "[[concepts/static-site-generators]]"]
last_compiled: 2026-04-05
summary: "MDX extends markdown with JSX components — enabling interactive, component-based content within markdown documents while compiling to JavaScript at build time with zero runtime."
---

## Overview

MDX is an authoring format that blends markdown prose with JSX components. It enables embedding React (or Preact/Vue) components directly within markdown documents — interactive charts, alerts, code playgrounds, or any custom component — while preserving markdown's simplicity for surrounding prose.

## How It Works

1. Author writes markdown with embedded JSX: `<Chart color="#fcb32c" year={2023} />`
2. MDX compiler processes the file at build time
3. Output is standard JavaScript compatible with any JSX framework
4. Zero runtime overhead — all compilation happens during the build stage

## Key Properties

- **"Everything is a component"** — MDX files themselves become importable components
- **Component mapping** — customize which React component renders for each markdown element (e.g., custom `<h1>`, `<table>`, `<code>`)
- **Plugin ecosystem** — extends via Remark (markdown) and Rehype (HTML) plugins
- **Framework integration** — works with Next.js, Docusaurus, Vite, Gatsby, Storybook

## Significance for Knowledge Management

MDX demonstrates that markdown's "universal interface" property doesn't require sacrificing interactivity. A knowledge base can be stored as markdown/MDX files that:
- Render as static documentation for reading
- Include interactive visualizations for exploration
- Remain version-controllable in git
- Stay human-readable in any text editor (JSX is still plain text)

The tradeoff is that MDX files require a JavaScript build step to render fully — they're not as instantly portable as pure markdown. But they degrade gracefully: the markdown prose remains readable even without the JSX components.

## Sources

- [[sources/mdx-markdown-components]] — official MDX documentation and architecture

## Related Concepts

- [[concepts/markdown-ecosystem]] — MDX as the interactivity layer
- [[concepts/markdown-as-universal-interface]] — MDX extends markdown's reach without breaking its core properties
- [[concepts/static-site-generators]] — the primary consumers of MDX content
