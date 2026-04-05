---
title: "Manual PKM vs. LLM-Maintained PKM"
type: comparison
subjects: ["[[concepts/personal-knowledge-management]]", "[[concepts/llm-knowledge-base]]"]
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/antigravity-post-code-ai-workflow]]", "[[sources/karpathy-llm-knowledge-bases]]", "[[sources/pebblous-cheap-ontology]]"]
last_compiled: 2026-04-06
summary: "Comparing traditional human-authored personal knowledge management (Zettelkasten, Notion, Obsidian notes) with LLM-maintained knowledge bases where the AI authors and organizes all content."
---

## Overview

Personal knowledge management (PKM) has undergone a paradigm shift. For decades, PKM meant human-authored, human-organized note systems -- from index cards (Zettelkasten) to digital tools like [[entities/notion]], Roam Research, Logseq, and [[entities/obsidian]]. With the advent of capable LLMs, a new model has emerged where the LLM handles authoring, organizing, linking, and maintaining knowledge while the human acts as curator and questioner. This comparison examines the strengths and weaknesses of each approach and the tradeoffs involved in ceding authorship to an AI.

## Comparison Table

| Dimension | Manual PKM | LLM-Maintained PKM |
|-----------|-----------|-------------------|
| Author | Human | LLM |
| Human role | Writer, organizer, linker | Curator, questioner, validator |
| Scalability | Limited by human time/attention | Limited by LLM context/cost |
| Knowledge synthesis | Manual (human connects ideas) | Automated (LLM cross-references across sources) |
| Maintenance burden | High (grows with collection size) | Low (LLM handles maintenance) |
| Quality ceiling | Human expertise and effort | LLM capability + source quality |
| Hallucination risk | None (human writes from understanding) | Present (LLM can fabricate connections) |
| Personal voice | Strong (human's own words and thinking) | Absent (LLM's generic style) |
| Compounding | Only through human re-reading | Automatic (filing loop) |
| Discovery | Manual browsing, serendipity | LLM-suggested connections and new articles |
| Setup complexity | Low (install app, start writing) | Moderate (LLM API, directory structure, prompts) |
| Trust | High (you wrote it) | Lower (LLM may have hallucinated) |

## Detailed Analysis

**The sustainability problem**: [[entities/sam-gallagher]]'s experience is representative. He initially used Notion, Clickup, and Obsidian with elaborate systems, but found that "complex structures became unmaintainable as priorities shifted" and "management overhead quickly outweighed benefits." This is the fundamental problem with manual PKM at scale: the more notes you take, the more time you spend organizing and maintaining them, until the system collapses under its own weight.

**The automation solution**: Karpathy's LLM-KB eliminates this maintenance burden by making the LLM responsible for everything beyond raw source curation. The human decides what to ingest (selecting quality sources for `raw/`), what to ask (posing questions to the LLM), and what to validate (reviewing LLM output for errors). Everything else -- summarization, concept extraction, cross-linking, index maintenance, health checks -- is automated.

**The trust deficit**: The critical tradeoff is trust. In manual PKM, every note reflects the human's own understanding -- there is no hallucination risk. In LLM-maintained PKM, every article is potentially contaminated by [[concepts/hallucination-contamination]]. [[entities/steph-ango]]'s [[concepts/vault-separation]] recommendation addresses this by keeping human-curated notes physically separate from LLM-generated content.

**The thinking benefit**: Manual PKM advocates argue that the process of writing notes by hand forces deeper engagement with the material. The Zettelkasten method, for example, requires rephrasing ideas in your own words, which strengthens understanding. LLM-maintained PKM loses this learning-through-writing benefit, though it gains the ability to process far more material and surface connections a human might miss.

**The middle ground**: AI-augmented PKM (2023-2024 era tools like Notion AI, Obsidian Copilot) offers a middle path: the human still authors notes, but AI assists with search, summarization, and suggestion. This preserves the personal voice and learning benefits while reducing some maintenance burden, but it does not achieve the full automation of Karpathy's approach.

## When to Use Each

**Use manual PKM when:**
- The process of writing deepens your understanding (learning use case)
- Personal voice and perspective matter (creative writing, journaling)
- Trust and accuracy are paramount (medical notes, legal records)
- The knowledge collection is small enough to maintain manually
- You value the serendipity of browsing your own notes

**Use LLM-maintained PKM when:**
- The volume of source material exceeds what you can manually process
- Cross-source synthesis is more valuable than personal reflection
- You need ongoing Q&A capability over a growing knowledge base
- The filing loop's compounding benefit matters for your workflow
- You are comfortable with the hallucination risk and have mitigation strategies

## Sources

- [[sources/gallagher-second-brain-knowledge-graphs]] -- practitioner journey from manual PKM failure to LLM-powered graph
- [[sources/antigravity-post-code-ai-workflow]] -- developer role transformation from author to curator
- [[sources/karpathy-llm-knowledge-bases]] -- the LLM-maintained PKM reference workflow
- [[sources/pebblous-cheap-ontology]] -- historical context for the cost and accessibility shift
