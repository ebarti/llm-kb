---
title: "How I use Obsidian"
source: "https://stephango.com/vault"
author: "Steph Ango"
date_published: 2024-01-01
date_ingested: 2026-04-05
tags: [obsidian, vault-organization, pkm, workflow]
type: article
status: raw
discovered_via: search
---

# How I use Obsidian — Steph Ango

## Core Philosophy

Ango advocates a "bottom-up approach to note-taking" that "embraces chaos and laziness to create emergent structure." He prioritizes the "file over app" philosophy, ensuring notes remain as portable files in standard formats.

## Vault Structure

**Root Directory:** Contains personal writings — journal entries, essays, evergreen notes, and daily reflections.

**Reference Folders:**
- **References:** External subjects (books, movies, places, people, podcasts)
- **Clippings:** Articles and essays written by others

**Administrative Folders:**
- **Attachments:** Images, audio, videos, PDFs
- **Daily:** Daily notes named `YYYY-MM-DD.md` (for linking only, not writing)
- **Templates:** Note templates

Ango deliberately avoids nested subfolders, preferring "speed and laziness" in organization.

## Organization Principles

Key Rules:
- Avoid folders for organization
- Use internal links profusely
- Always pluralize categories and tags
- Employ `YYYY-MM-DD` date format universally
- Maintain a single weekly to-do list
- Use 7-point rating scale

Navigation relies on the quick switcher, backlinks, and internal linking rather than file exploration.

## Linking Strategy

Ango extensively uses internal links, including unresolved ones (breadcrumbs for future connections). Journal entries frequently reference external entries across different folders, creating a "branching" knowledge web traceable over time.

## Fractal Journaling Method

Throughout the day, Ango captures individual thoughts using Obsidian's unique note hotkey, creating timestamped entries (`YYYY-MM-DD HHmm`). He periodically reviews these fragments, compiling monthly summaries, then yearly reviews — creating "a fractal web of my life" at varying detail levels.

He manually performs "random revisits" using the random note function to rediscover past ideas, create missing connections, and maintain consistency. He explicitly rejects automating this with language models, valuing the understanding gained through personal maintenance.

## Properties and Templates

Nearly all notes use templates with metadata properties including:
- **Dates:** Created, start, end, published
- **People:** Author, director, artist, cast, host, guests
- **Themes:** Genre, type, topic, related notes
- **Locations:** Neighborhood, city, coordinates
- **Ratings:** 1-7 scale

Property design principles: reusability across categories, composable templates, and short names for efficient typing. The `.obsidian/types.json` file defines property types.

## Rating System

Uses a 7-point integer scale:
- 7: Perfect, life-changing
- 6: Excellent, worth repeating
- 5: Good, enjoyable
- 4: Passable
- 3: Bad, avoid if possible
- 2: Atrocious, actively avoid
- 1: Evil, harmful

## Tools and Plugins

- **Theme:** Minimal with Flexoki color scheme
- **Web Clipper:** Saves articles from the web
- **Obsidian Sync:** Synchronizes across devices
- **Obsidian Bases:** Views notes by category
- **Obsidian Maps:** Location-based note organization
- **Obsidian Git:** Pushes notes to GitHub

## Publishing Workflow

Ango maintains a separate vault for his public website, using Jekyll as a static site generator to compile Markdown notes into HTML. The Obsidian Git plugin pushes changes to GitHub, where Netlify automatically compiles and deploys. He uses his Permalink Opener plugin to preview drafts against live versions.

The site uses the Flexoki color palette. He recommends alternatives like Quartz, Astro, Eleventy, and Hugo for those preferring different generators.

## Stylistic Consistency

Ango emphasizes that "having a consistent style collapses hundreds of future decisions into one," allowing focus. He recommends creating personal style guides and writing down organizational rules.
