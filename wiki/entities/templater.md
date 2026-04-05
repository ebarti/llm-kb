---
title: "Templater"
type: entity
entity_type: tool
sources: ["[[sources/dsebastien-obsidian-plugins-2026]]"]
related: ["[[entities/obsidian]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/vault-organization]]"]
last_compiled: 2026-04-05
summary: "Obsidian's advanced templating plugin (230K+ installs): dynamic variables, JavaScript execution, file manipulation, conditional logic, and user prompts — the automation backbone of power-user workflows."
---

## Overview

Templater is the sixth most installed [[entities/obsidian]] community plugin (230,000+ installs) and the automation backbone of most power-user workflows. It defines a templating language that goes far beyond Obsidian's built-in template feature, enabling dynamic variables, JavaScript execution, file manipulation, conditional logic, and interactive user prompts.

## Key Capabilities

**Dynamic Variables**: Access file properties, system information, dates, and vault metadata within templates.

**JavaScript Execution**: The `<%* %>` syntax executes arbitrary JavaScript, enabling:
- File creation and manipulation
- Date calculations and navigation links
- API calls and external data fetching
- Conditional logic and loops

**User Prompts**: Templates can prompt users for input during note creation, enabling interactive workflows.

**File Manipulation**: Rename or move files programmatically based on template logic.

**Template Triggers**: Automatically apply templates when files are created in specific folders.

## Syntax

- `<% %>` — Variable expansion (automatically resolves Templater functions)
- `<%* %>` — JavaScript execution block (full JS environment)
- `<%= %>` — Output expression result inline

## Common Use Cases

- Daily notes with navigation buttons (previous/next day links)
- Meeting notes with attendee prompts and auto-dated filenames
- Book/movie review templates with pre-filled metadata properties
- Project templates with folder creation and linked notes
- Automated weekly review compilation

## Role in LLM-KB

In the [[concepts/llm-knowledge-base]] approach, Templater's role is limited because the LLM generates content programmatically rather than through templates. However, Templater is valuable for the human-facing side: creating quick-capture templates for raw source ingestion, standardizing frontmatter properties, and automating the creation of notes that the LLM will later process.

## Mentioned In

- [[sources/dsebastien-obsidian-plugins-2026]] — identified as part of the foundational plugin trio (Dataview, Templater, QuickAdd)
