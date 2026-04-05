---
title: "MDX"
type: entity
entity_type: tool
sources: ["[[sources/mdx-markdown-components]]"]
related: ["[[concepts/mdx]]", "[[concepts/markdown-ecosystem]]", "[[concepts/static-site-generators]]"]
last_compiled: 2026-04-05
summary: "Authoring format that blends markdown with JSX components — 'Markdown for the component era' — with zero runtime, compiling to JavaScript at build time."
---

## Overview

MDX is an authoring format and compiler that enables writing JSX (React/Preact/Vue components) within markdown documents. It extends markdown's reach into interactive, component-based content while preserving markdown's simplicity for prose.

## Key Properties

- Zero runtime — compiles to JavaScript at build time
- "Everything is a component" — MDX files are importable components
- Component mapping for customizing markdown element rendering
- Extensible via Remark and Rehype plugin ecosystem

## Framework Integration

Docusaurus, Next.js, Vite, Rollup, esbuild, webpack, Gatsby, Storybook.

## Technical Packages

- `@mdx-js/mdx` (core compiler)
- `@mdx-js/react`, `@mdx-js/preact`, `@mdx-js/vue`
- Bundler-specific integrations
- `remark-mdx` for AST-level processing

## Mentioned In

- [[sources/mdx-markdown-components]] — official documentation overview
- [[concepts/mdx]] — the format as a concept
- [[concepts/markdown-ecosystem]] — MDX as the interactivity layer
