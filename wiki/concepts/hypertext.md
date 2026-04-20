---
title: "Hypertext"
type: concept
sources: ["[[sources/wikipedia-project-xanadu]]", "[[sources/wikipedia-as-we-may-think]]"]
related: ["[[entities/ted-nelson]]", "[[entities/vannevar-bush]]", "[[concepts/memex]]", "[[concepts/transclusion]]", "[[concepts/semantic-web]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "Nonsequential writing with reader-chosen paths through linked documents — coined by Ted Nelson in 1965, rooted in Bush's Memex (1945), partially realized by the World Wide Web, and foundational to wiki-based knowledge systems."
---

## Overview

Hypertext is text displayed on a computer that contains links to other text, enabling nonsequential reading and writing. The term was coined by [[entities/ted-nelson]] in 1965. The concept traces to [[entities/vannevar-bush]]'s [[concepts/memex]] (1945) and was partially realized by the World Wide Web (1989).

Hypertext is foundational to wiki-based [[concepts/knowledge-representation]] systems, including the [[concepts/llm-knowledge-base]] approach that uses wikilinks as its core linking mechanism.

## Key Ideas

### Nonsequential Writing
Nelson's original vision: readers choose their own path through a document rather than following a single linear sequence. Different readers could traverse the same content in different orders based on their interests.

### Links as First-Class Objects
In Nelson's conception, links are as important as the documents they connect. They should be bidirectional, typed (indicating the nature of the relationship), and persistent.

### The Web's Partial Implementation
Tim Berners-Lee's World Wide Web (1989) implemented hypertext but in a simplified form:
- **One-directional** links (Nelson wanted bidirectional)
- **No transclusion** (Nelson wanted documents to include live content from others)
- **Breakable** links (no guarantee URLs persist)
- **No version tracking** (Nelson wanted full revision history)
- **No micropayments** (Nelson envisioned built-in royalties)

## Historical Chain

| Year | Milestone | Innovation |
|------|-----------|------------|
| 1945 | Bush's "As We May Think" | Associative trails between documents |
| 1960 | Nelson conceives Xanadu | Nonsequential, version-tracked documents |
| 1965 | Nelson coins "hypertext" | Formal term and concept |
| 1968 | Engelbart's NLS demo | Live hyperlinked collaborative editing |
| 1987 | Apple HyperCard | Hypertext for personal computing |
| 1989 | Berners-Lee proposes WWW | HTTP + HTML hyperlinks |
| 2001 | Wikipedia launched | Collaborative wikilinked encyclopedia |
| 2020 | Roam Research / Obsidian | Bidirectional links for personal knowledge |
| 2026 | Karpathy's LLM-KB | LLM-maintained wikilinks across compiled wiki |

## Connection to LLM Knowledge Bases

The [[concepts/llm-knowledge-base]] approach uses Obsidian-style wikilinks as its hypertext mechanism. These provide:
- Bidirectional linking (Obsidian's backlinks panel realizes Nelson's vision)
- A navigable knowledge graph (the link structure IS the ontology)
- LLM-maintained cross-references (solving the manual maintenance burden that plagued earlier hypertext systems)

## Sources
- [[sources/wikipedia-project-xanadu]] — Nelson's vision and its development
- [[sources/wikipedia-as-we-may-think]] — Bush's precursor concept

## Related Concepts
- [[entities/ted-nelson]] — coined the term
- [[concepts/memex]] — the conceptual precursor
- [[concepts/transclusion]] — Nelson's more radical idea
- [[concepts/semantic-web]] — machine-readable extension of hypertext
- [[concepts/markdown-as-universal-interface]] — the modern hypertext substrate for LLM-KBs
