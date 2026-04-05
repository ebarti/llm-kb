---
title: "Source: How I use Obsidian — Steph Ango"
type: source-summary
source: "[[raw/stephango-vault-organization]]"
related: ["[[concepts/vault-organization]]", "[[entities/steph-ango]]", "[[entities/obsidian]]", "[[concepts/obsidian-frontmatter-properties]]"]
last_compiled: 2026-04-05
summary: "Steph Ango's personal vault structure: flat folders, profuse internal links, fractal journaling, 7-point rating system, and bottom-up emergent organization."
---

## Key Points

- Bottom-up approach: "embraces chaos and laziness to create emergent structure"
- Flat folder structure: Root (personal writing), References, Clippings, Attachments, Daily, Templates — no nested subfolders
- Navigation via quick switcher and backlinks, not folder browsing
- Internal links used profusely, including unresolved ones as "breadcrumbs for future connections"
- Fractal journaling: timestamped fragments → monthly summaries → yearly reviews
- Manual random revisits to rediscover ideas — explicitly rejects LLM automation for this
- 7-point rating system (1=evil, 7=perfect/life-changing)
- All notes use templates with composable metadata properties
- Consistent style collapses "hundreds of future decisions into one"
- Publishing via separate vault + Jekyll + GitHub + Netlify pipeline

## Detailed Summary

This is the most authoritative source on [[concepts/vault-organization]] because it comes from the CEO of Obsidian himself. Ango's system is intentionally minimal: a flat structure with only a few top-level folders, heavy reliance on links over hierarchy, and a preference for speed over categorization.

The fractal journaling method is particularly notable: individual timestamped thoughts are captured throughout the day, then manually compiled into monthly and yearly reviews. This creates a multi-resolution view of one's life. Crucially, Ango rejects using AI for this review process, valuing the understanding gained through personal curation — a direct contrast to the LLM-KB approach where the LLM performs all compilation.

The property system is well-thought-out: reusable across categories, composable via templates, and defined centrally in `.obsidian/types.json`. Properties include dates, people, themes, locations, and ratings — all queryable via [[entities/dataview]].

His publishing workflow (separate vault → Jekyll → GitHub → Netlify) demonstrates the [[concepts/digital-garden]] pattern, where a curated subset of notes is published to the web.

## Notable Quotes

> "Having a consistent style collapses hundreds of future decisions into one."

## Related Concepts

- [[concepts/vault-organization]] — this source defines the CEO's own approach
- [[concepts/obsidian-frontmatter-properties]] — detailed property design principles
- [[concepts/digital-garden]] — publishing subset of vault to web
- [[entities/steph-ango]] — the author
