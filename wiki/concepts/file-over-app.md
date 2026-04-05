---
title: "File Over App"
type: concept
sources: ["[[sources/stephango-file-over-app]]", "[[sources/stephango-dialectic-interview]]", "[[sources/stephango-vault-organization]]"]
related: ["[[concepts/markdown-as-universal-interface]]", "[[concepts/obsidian-as-ide]]", "[[concepts/obsidian-plugin-ecosystem]]", "[[concepts/vault-separation]]", "[[entities/steph-ango]]", "[[entities/obsidian]]"]
last_compiled: 2026-04-05
summary: "Steph Ango's philosophy that files in open formats outlast any application — the foundational design principle behind Obsidian's local-first, plain-text architecture."
---

## Overview

"File over app" is a design philosophy articulated by [[entities/steph-ango]], CEO of [[entities/obsidian]]. The core claim: if you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. All software is ephemeral; the files you create are more important than the tools you use to create them.

## Key Arguments

### Digital Vulnerability

Most contemporary digital creations lack user control. They are stored on remote servers, locked behind logins, and trapped in proprietary formats that become incompatible as platforms evolve or shut down. Cloud-first architectures make data dependent on a company's survival and pricing decisions.

### Historical Precedent

Ango draws parallels to physical artifacts — Egyptian hieroglyphs, manuscripts, paintings — that have survived centuries without technology dependency. The medium (stone, paper, canvas) outlasts any specific tool used to create it. For digital creations, the equivalent of a durable medium is an open file format stored locally.

### The 1960s-to-2160s Test

> "If you want your writing to still be readable on a computer from the 2060s or 2160s, it's important that your notes can be read on a computer from the 1960s."

Plain text and markdown pass this test. Proprietary database formats, cloud APIs, and binary blobs do not.

### Civilizational Stance

In the Dialectic interview, Ango escalates the philosophy: "File over App" is not just a product design choice but a "civilizational stance." Plain text formats "maximize the chance your data survives a thousand years." This frames data ownership as a matter of cultural preservation, not just user preference.

The philosophy serves both users and developers:
- **For users**: Choose tools that produce portable, open-format files stored on your own device
- **For developers**: Accept software's temporary nature and give people ownership over their data

## Implementation in Obsidian

[[entities/obsidian]] is the purest implementation of File over App in the knowledge management space:
- All notes stored as plain markdown files on the user's local filesystem
- No proprietary database — just a folder of `.md` files
- Any editor can read/write the same files
- Sync is optional and end-to-end encrypted
- The vault works even if Obsidian the company disappears tomorrow
- Even [[entities/obsidian-copilot]] stores AI chat history, system prompts, and memory as plain markdown in the vault

Ango's company manifesto reinforces this with five principles: independence, user-only funding (no investors), small team (7-12 people), privacy, and data durability. Obsidian is funded entirely by users, not venture capital — eliminating the growth-at-all-costs pressure that drives many competitors toward lock-in.

## Broader Influence

The File over App philosophy has influenced the broader "local-first" software movement. Other tools aligned with these principles include Logseq (open-source, local markdown/org-mode), Zettlr (academic markdown editor), Standard Notes (encrypted local notes), and plain text accounting tools (hledger, beancount).

## Relationship to the AI Era

File-over-app becomes even more important in the AI era because:
- LLMs read plain text natively — no proprietary SDK needed to process your knowledge
- [[concepts/llm-knowledge-base]] systems like Karpathy's operate directly on markdown files
- Tools like [[entities/markitdown]] convert proprietary formats TO markdown for LLM consumption
- AI agents can read, write, and version-control markdown files using standard tools

The irony: AI makes proprietary formats *less* necessary, not more. If an LLM can compile, summarize, and query your knowledge, it doesn't need a proprietary platform — it just needs readable files.

## Sources

- [[sources/stephango-file-over-app]] — the original essay
- [[sources/stephango-dialectic-interview]] — deepened as "civilizational stance"
- [[sources/stephango-vault-organization]] — implementation in Ango's personal vault

## Related Concepts

- [[concepts/markdown-as-universal-interface]] — markdown as the practical file format for file-over-app
- [[concepts/obsidian-as-ide]] — Obsidian as the embodiment of the philosophy
- [[concepts/obsidian-plugin-ecosystem]] — the ecosystem enabled by open file access
- [[concepts/vault-separation]] — vault architecture built on file-based principles
- [[concepts/personal-knowledge-management]] — PKM as the primary domain where file-over-app matters
