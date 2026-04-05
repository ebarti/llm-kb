---
title: "Vault Separation"
type: concept
sources: ["[[sources/antigravity-post-code-ai-workflow]]"]
related: ["[[concepts/hallucination-contamination]]", "[[concepts/obsidian-as-ide]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Steph Ango's (Obsidian CEO) recommendation to maintain a clean human-curated Obsidian vault separately from agent-generated content, preventing hallucination contamination of personal knowledge."
---

## Overview

Vault separation is the practice of keeping LLM-generated wiki content in a separate Obsidian vault from human-curated personal notes. Recommended by Steph Ango (Obsidian CEO) as a direct response to Karpathy's LLM knowledge base approach.

## The Problem It Solves

LLMs occasionally hallucinate — generating plausible-sounding but incorrect connections or facts. In an LLM-maintained wiki, these errors get written into wiki articles and persist as part of the knowledge substrate. If this wiki is mixed with human-curated personal notes, the hallucinations can contaminate trusted knowledge.

## Implementation

**Two-vault pattern:**
- **Clean vault**: Human-curated notes, personal writing, trusted references. The LLM can read this but never writes here.
- **Agent vault**: LLM-maintained wiki, compiled from ingested sources. The LLM reads and writes here freely.

**In practice:**
- The `wiki/`, `raw/`, and `output/` directories live in the agent vault
- Personal notes and trusted references stay in the clean vault
- Cross-reference across vaults via file system links, not Obsidian wikilinks

## When to Override

For users who fully understand the hallucination risk and want unified search across personal notes and wiki content, a single vault with clear directory separation (and disciplined linting) may be acceptable. The key is intentionality.

## Sources
- [[sources/antigravity-post-code-ai-workflow]] — documents Steph Ango's recommendation

## Related Concepts
- [[concepts/hallucination-contamination]] — the risk being mitigated
- [[concepts/obsidian-as-ide]] — Obsidian as the vault viewer
- [[concepts/linting-and-health-checks]] — complementary mitigation
