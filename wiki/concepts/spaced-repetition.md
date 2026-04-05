---
title: "Spaced Repetition"
type: concept
sources: ["[[sources/spaced-repetition-knowledge-management]]"]
related: ["[[concepts/evergreen-notes]]", "[[concepts/zettelkasten]]", "[[concepts/personal-knowledge-management]]", "[[entities/anki]]"]
last_compiled: 2026-04-05
summary: "A learning technique that combats the forgetting curve through adaptively scheduled review — essential complement to PKM systems that build connections (Zettelkasten, evergreen notes) by ensuring knowledge is actually retainable and recallable."
---

## Overview

Spaced repetition is a learning technique based on Hermann Ebbinghaus's 1885 discovery of the forgetting curve: without reinforcement, humans lose approximately 50% of new information within an hour and 90% within a week. Spaced repetition combats this through adaptively scheduled review — successfully recalled items are reviewed at progressively longer intervals, while difficult items return sooner.

## Core Mechanisms

### The Forgetting Curve
Ebbinghaus demonstrated that memory decay follows a predictable exponential curve. Each successful retrieval at the point of near-forgetting strengthens the memory trace and extends the interval before the next review is needed. This transforms learning from a brute-force activity (cramming) into an efficient, scientifically-grounded process.

### Active Recall
Spaced repetition is paired with active recall — being asked a question and attempting to retrieve the answer, rather than passively re-reading material. Active recall strengthens neural pathways and reveals understanding gaps that passive review misses. The combination of spaced timing and active retrieval is one of the most well-supported findings in learning science.

### The Algorithms
- **SM-2**: The classic Supermemo algorithm (1987), still widely used
- **FSRS (Free Spaced Repetition Scheduler)**: Modern ML-based algorithm that optimizes intervals for individual performance patterns, now implemented in [[entities/anki]]

## The Structure Preservation Problem

A critical challenge for knowledge management: breaking complex knowledge into flashcards risks losing sight of how concepts interconnect. The solution involves creating structural cards alongside content cards:

- **Hierarchy cards**: Visual representations of how main sections relate
- **Connection cards**: Test relationships between concepts
- **Sequence cards**: Test understanding of staged processes
- **Context cards**: Show where information fits in broader arguments

## Relationship to PKM

Spaced repetition and PKM systems like [[concepts/zettelkasten]] and [[concepts/evergreen-notes]] serve fundamentally different but complementary purposes:

| Dimension | PKM (Zettelkasten/Evergreen) | Spaced Repetition |
|-----------|------------------------------|-------------------|
| Primary goal | Build connections, generate insights | Retain and recall facts |
| Activity | Writing and linking | Reviewing and retrieving |
| Scale | Grows with knowledge | Fixed review load |
| Output | New ideas | Better memory |

[[entities/andy-matuschak]] explicitly distinguishes evergreen notes from spaced repetition, noting that "existing spaced repetition tools discourage the incremental synthesis that evergreen notes require." However, the regular revisiting of notes in a Zettelkasten approximates spaced repetition organically — you encounter old ideas when linking new ones.

Some tools bridge both worlds: **RemNote** integrates note-taking with spaced repetition, and **Obsidian** plugins bring flashcard review directly into PKM workflows.

## Sources
- [[sources/spaced-repetition-knowledge-management]] — comprehensive overview with practical guidance

## Related Concepts
- [[concepts/zettelkasten]] — complementary: builds connections while SRS ensures retention
- [[concepts/evergreen-notes]] — Matuschak distinguishes from SRS but notes overlap
- [[concepts/personal-knowledge-management]] — the broader domain
- [[entities/anki]] — the standard implementation
