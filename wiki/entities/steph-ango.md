---
title: "Steph Ango"
type: entity
entity_type: person
sources: ["[[sources/antigravity-post-code-ai-workflow]]", "[[sources/stephango-file-over-app]]", "[[sources/stephango-vault-organization]]", "[[sources/stephango-dialectic-interview]]"]
related: ["[[entities/obsidian]]", "[[concepts/vault-separation]]", "[[concepts/hallucination-contamination]]", "[[concepts/file-over-app]]", "[[concepts/vault-organization]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/digital-garden]]"]
last_compiled: 2026-04-05
summary: "CEO of Obsidian, designer, and writer — articulated the 'file over app' philosophy, vault separation pattern, and a bottom-up approach to PKM with fractal journaling."
reading_time: "2 min"
---

## Overview

Steph Ango is the CEO of Obsidian, the markdown-based knowledge management application that serves as the viewing frontend in Karpathy's LLM knowledge base workflow. Ango's contribution to the LLM-KB discourse is his recommendation of vault separation: maintaining a clean human-curated Obsidian vault separate from an agent-generated vault for LLM-compiled content.

This recommendation directly addresses the [[concepts/hallucination-contamination]] risk. When LLMs compile wikis, they occasionally generate plausible but incorrect connections or facts. If agent-generated content is stored in the same vault as a user's personal, trusted notes, these hallucinations can contaminate the user's primary knowledge base. Ango's two-vault pattern provides a clean architectural boundary between trusted human knowledge and potentially imperfect LLM output.

## Key Contributions

- **Vault separation pattern**: The recommendation to maintain a "clean vault" (human-curated, trusted) separate from an "agent vault" (LLM-maintained, potentially hallucinated) has become a foundational best practice in the LLM-KB community. It is cited across multiple sources as the primary mitigation strategy for hallucination contamination.

- **Product perspective on LLM-KB**: As the CEO of the tool most commonly used as the LLM-KB frontend, Ango's endorsement of the workflow pattern while cautioning about contamination risk carries significant weight. It validates the approach while identifying the most important guardrail.

## Role in LLM Knowledge Bases

Ango represents the tool-maker perspective in the LLM-KB ecosystem. While Karpathy provides the methodology and researchers like the STORM and KARMA teams provide the academic foundations, Ango speaks from the position of someone building the tools that practitioners use daily. His vault separation recommendation has become the standard advice for anyone implementing Karpathy's workflow, directly shaping the [[concepts/vault-separation]] concept article.

## "File Over App" Philosophy

Beyond vault separation, Ango is best known for articulating the [[concepts/file-over-app]] philosophy — a "civilizational stance" that files in open formats outlast any application. Key tenets:

- "In the fullness of time, the files you create are more important than the tools you use to create them"
- "Plain text formats maximize the chance your data survives a thousand years"
- "If you want your writing readable on computers from the 2060s or 2160s, it's important that your notes can be read on computers from the 1960s"
- An appeal to developers to prioritize user data ownership over proprietary lock-in

## Company Principles

Obsidian operates with five manifesto principles:
1. **Independence** — no venture capital, no investors
2. **User-only funding** — funded entirely by users
3. **Small team** — 7-12 people
4. **Privacy** — end-to-end encrypted sync
5. **Data durability** — local-first, open formats

"The company is secondary to my personal goals of using the tool I want." This inverted priority — building for himself first — creates a tight feedback loop as a daily power user.

## Personal Vault and Workflow

Ango's personal vault (described in [[sources/stephango-vault-organization]]) demonstrates his principles:
- **Flat structure**: Root, References, Clippings, Attachments, Daily, Templates — no nested subfolders
- **Profuse internal links** including unresolved ones as "breadcrumbs for future connections"
- **Fractal journaling**: Timestamped fragments → monthly summaries → yearly reviews — "a fractal web of my life"
- **Manual random revisits** — explicitly rejects LLM automation for review, valuing understanding through personal maintenance
- **7-point rating system** (1=evil, 7=perfect/life-changing)
- **Publishing**: Separate vault → Jekyll → GitHub → Netlify for his [[concepts/digital-garden]]

## Design Philosophy

"The recipe for success is caring more than someone else." Key design principles from the Dialectic interview:
- **Constraints as creativity**: Self-imposed constraints become your signature
- **Zigzagging development**: Alternate between maximalist exploration and minimalist shipping
- **Dogfooding**: Uses Obsidian daily as primary tool, testing every feature personally

## Mentioned In

- [[sources/stephango-file-over-app]] — the "file over app" manifesto
- [[sources/stephango-vault-organization]] — personal vault structure and workflow
- [[sources/stephango-dialectic-interview]] — company principles, design philosophy, and creative process
- [[sources/antigravity-post-code-ai-workflow]] -- vault separation recommendation for LLM-KB contamination prevention
