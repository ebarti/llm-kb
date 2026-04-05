---
title: "Source: File over App — Steph Ango"
type: source-summary
source: "[[raw/stephango-file-over-app]]"
related: ["[[concepts/file-over-app]]", "[[entities/steph-ango]]", "[[entities/obsidian]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "Steph Ango's manifesto for digital longevity: files you control in open formats outlast any app — Obsidian is built on this principle."
---

## Key Points

- "If you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read"
- Files outlast applications — "Apps are ephemeral, but your files have a chance to last"
- Notes should be readable on a computer from the 1960s to still work in the 2160s
- This is an appeal to tool makers to accept software's temporary nature and give users data ownership
- Obsidian implements this via local markdown files that exist independently of the application
- Draws parallels to physical artifacts (Egyptian hieroglyphs, manuscripts) that survive centuries without technology dependency

## Detailed Summary

"File over App" is the philosophical manifesto underlying [[entities/obsidian]]'s design decisions. [[entities/steph-ango]] argues that most digital creations are trapped in proprietary formats, stored on remote servers, and locked behind logins — making them fundamentally vulnerable to the inevitable death of the applications that created them.

The essay inverts the typical technology narrative: instead of apps being the valuable artifact and data being disposable, Ango argues data (files) is the permanent thing and apps are the disposable thing. This has direct architectural consequences for Obsidian: local-first storage, plain markdown format, no proprietary database, and the ability to edit vault files with any text editor.

The philosophy directly supports [[concepts/markdown-as-universal-interface]] — markdown satisfies the "File over App" criteria because it is human-readable without any application, version-controllable, and future-proof. It also validates the LLM-KB approach: because the entire knowledge base is plain markdown files, it remains accessible regardless of which LLM or tooling is used.

## Notable Quotes

> "In the fullness of time, the files you create are more important than the tools you use to create them."

> "If you want your writing to still be readable on a computer from the 2060s or 2160s, it's important that your notes can be read on a computer from the 1960s."

## Related Concepts

- [[concepts/file-over-app]] — the philosophy this essay defines
- [[concepts/markdown-as-universal-interface]] — markdown as the implementation of file-over-app principles
- [[entities/steph-ango]] — the author and CEO of Obsidian
- [[entities/obsidian]] — the tool built on this philosophy
