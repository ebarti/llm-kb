---
title: "Temporal Knowledge"
type: concept
sources: ["[[sources/graphiti-temporal-knowledge-graphs]]"]
related: ["[[concepts/knowledge-graph]]", "[[concepts/llm-knowledge-base]]"]
last_compiled: 2026-04-05
summary: "Graphiti's core contribution: representing knowledge with temporal validity windows (when a fact became true and when it was superseded) rather than treating facts as eternally true or false — critical for AI agents in dynamic environments."
---

## Overview

Most knowledge systems treat facts as atemporal: a fact is true or false, with no concept of "true as of [date]" or "superseded by [new fact]." For static domains (mathematics, history) this works. For dynamic domains (product roadmaps, personnel, competitive landscape, medical guidelines), it fails badly.

## Graphiti's Solution

Graphiti models each fact (relationship edge) with a **validity window**:
- `valid_from`: when this fact became true
- `valid_until`: when this fact was superseded (null if still current)

Old facts are **invalidated**, not deleted — preserving historical context. This enables questions like "what did we know about X last quarter?" alongside "what do we know now?"

## Why This Matters for AI Agents

An AI agent operating over long time horizons accumulates memories that become outdated. Without temporal tracking:
- The agent doesn't know whether its knowledge about an entity is current or stale
- Conflicting facts (old and new) both appear equally valid
- The agent can't answer "when did X change?"

With Graphiti's temporal graphs, the agent can:
- Always retrieve the *current* state of an entity
- Query historical states ("what was true before date X?")
- Detect when new information contradicts existing (outdated) facts

## Contrast with Markdown Wiki

Karpathy's markdown wiki handles temporality via:
- File modification dates (implicit)
- Manual notes in articles ("updated March 2026")
- Linting health checks that flag stale content

This is sufficient for research knowledge (papers don't change) but insufficient for operational knowledge (org charts, product state, competitive analysis). Graphiti's explicit temporal model is superior for the latter.

## Sources
- [[sources/graphiti-temporal-knowledge-graphs]] — full Graphiti description

## Related Concepts
- [[concepts/knowledge-graph]] — the broader representation
- [[concepts/llm-knowledge-base]] — handles temporality implicitly via linting
