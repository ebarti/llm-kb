---
title: "Marp: Markdown Presentation Ecosystem"
source: "https://marp.app/"
author: "Marp Team"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [marp, markdown, presentations, slides, open-source]
type: article
status: raw
discovered_via: search
---

# Marp: Markdown Presentation Ecosystem

## Overview

Marp enables users to create slide decks using Markdown. "You only have to focus on writing your story in a Markdown document."

## Core Features

**Markdown-Based**: Built on CommonMark specifications. Horizontal rulers (`---`) separate slides.

**Theming**: Three built-in themes: `default`, `gaia`, and `uncover`. Custom themes via CSS. Markdown directives control design.

**Export Capabilities**: Converts to HTML, PDF, and PowerPoint formats, powered by Google Chrome/Chromium rendering.

**Extended Syntax**: Supports directives, image syntax, math typesetting, and auto-scaling features.

## Ecosystem Components

1. **Marp for VS Code** — Real-time editing and preview within VS Code
2. **Marp CLI** — Command-line tool for batch conversion
3. **Marp Core** — The conversion engine underlying official tools
4. **Marpit Framework** — "A skinny framework for creating HTML/CSS slide decks" with pluggable architecture for extending functionality

## Technical Foundation

Modular architecture: "Marp is essentially just a converter for Markdown." The Marpit framework handles transformation, developers extend via plugins.

## Licensing

All tools are MIT-licensed open-source projects.

## Significance

Marp demonstrates that markdown can serve as a source format not just for documents and websites, but also for presentations — another domain traditionally dominated by proprietary binary formats (PowerPoint, Keynote).
