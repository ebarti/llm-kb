---
title: "MDX: Markdown for the Component Era"
source: "https://mdxjs.com/"
author: "MDX Contributors"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [mdx, markdown, react, jsx, components, static-sites]
type: article
status: raw
discovered_via: search
---

# MDX: Markdown for the Component Era

## What is MDX?

MDX is "an authorable format for writing JSX in markdown documents." It enables developers to blend markdown syntax with JSX components, allowing interactive content creation within markdown files.

## Core Functionality

MDX allows you to write markdown with embedded components through JSX. The compilation process converts this hybrid syntax into JavaScript compatible with any JSX-supporting framework. Example:

```
import {Chart} from './snowfall.js'
# Last year's snowfall
<Chart color="#fcb32c" year={2023} />
```

## Key Features

- **Integration**: "MDX blends markdown and JSX syntax to fit perfectly in JSX-based projects"
- **Component-centric**: "Everything is a component" — existing components work within MDX and MDX files themselves become importable components
- **Customization**: Component mapping allows developers to define which component renders for each markdown element
- **Simplicity**: "The simplicity and elegance of markdown remains, you use JSX only when you want to"
- **Performance**: "MDX has no runtime, all compilation occurs during the build stage"

## Supported Frameworks & Bundlers

MDX integrates with major tooling: Docusaurus, Next.js, Vite, Rollup, esbuild, webpack, and frameworks including React, Preact, and Vue.

## Technical Architecture

The platform includes specialized packages:
- `@mdx-js/mdx` (core compiler)
- Framework-specific packages (react, preact, vue)
- Bundler integrations (esbuild, rollup, loader, node-loader)
- `remark-mdx` plugin support
- Extensible via Rehype and Remark plugin ecosystem

## Use Cases

Ideal for long-form content requiring interactive elements like charts, alerts, and dynamic components within documentation or content-heavy applications.
