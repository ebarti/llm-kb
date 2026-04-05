---
title: "Source: Karpathy's LLM Knowledge Bases: The Post-Code AI Workflow"
type: source-summary
source: "[[raw/antigravity-post-code-ai-workflow]]"
related: ["[[concepts/llm-knowledge-base]]", "[[concepts/wiki-compilation]]", "[[concepts/post-code-ai-workflow]]", "[[concepts/hallucination-contamination]]", "[[concepts/markdown-as-universal-interface]]"]
last_compiled: 2026-04-05
summary: "Broadest analysis of Karpathy's LLM KB shift: the 6-step workflow, developer role transformation, real-world applications across 7 domains, hallucination contamination risk, and minimum viable setup."
reading_time: "2 min"
---

## Key Points
- Karpathy framing: "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge"
- The shift: Vibe Coding (Feb 2025) → Agentic Engineering (Jan 2026) → LLM Knowledge Bases (Apr 2026)
- 6 steps: ingest → compile → scale → query → multi-format output → health checks
- 7 real-world applications: competitive intelligence, due diligence, literature reviews, documentation, product research, compliance, personal learning
- Steph Ango (Obsidian CEO): use **vault separation** — clean personal vault separate from agent-generated content
- Markdown is the universal interface: human-readable, LLM-friendly, version-controllable, tool-agnostic

## Detailed Summary

This Antigravity Codes article is the most comprehensive analysis of what Karpathy's approach means for developers. It places the LLM KB within a broader intellectual trajectory: from "vibe coding" (accepting all AI-generated code without review) through agentic engineering to the current focus on knowledge orchestration.

The article documents community reactions: Steph Ango recommends vault separation to prevent AI-hallucinated content from contaminating human-curated personal wikis; Elvis Saravia confirms the pattern's effectiveness. The key risk — hallucination contamination propagating through the wiki — is addressed by tracing all claims back to `raw/` source files.

The minimum viable setup is refreshingly simple: `raw/`, `wiki/`, `output/`, `_meta/` directories + Obsidian + Web Clipper + LLM API.

The article concludes with a bold claim: "The developers who thrive will be those with the strongest knowledge systems."

## Notable Quotes
> "A large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge." — Karpathy
> "Developers become curators and questioners rather than coders or agent orchestrators."

## Related Concepts
- [[concepts/llm-knowledge-base]] — the system
- [[concepts/post-code-ai-workflow]] — the broader shift
- [[concepts/markdown-as-universal-interface]] — markdown as the format
- [[concepts/hallucination-contamination]] — the main risk
- [[concepts/vault-separation]] — Steph Ango's recommendation
