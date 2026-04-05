---
title: "Notion"
type: entity
entity_type: tool
sources: ["[[sources/gallagher-second-brain-knowledge-graphs]]", "[[sources/decodingai-second-brain-rag]]", "[[sources/pkm-tools-comparison-2026]]", "[[sources/eesel-confluence-notion-sharepoint]]"]
related: ["[[concepts/personal-knowledge-management]]", "[[concepts/knowledge-base-product-gap]]", "[[concepts/second-brain]]", "[[concepts/agentic-knowledge-management]]", "[[concepts/enterprise-knowledge-management]]", "[[entities/obsidian]]", "[[entities/logseq]]", "[[entities/confluence]]", "[[entities/sharepoint]]"]
last_compiled: 2026-04-05
summary: "Flexible block-based workspace with 100M+ users, ranked #1 for knowledge bases on G2. Expanding from PKM into enterprise work OS with autonomous AI Agent, Enterprise Search, Calendar, Mail, and Sites. Base plan includes AI; $10/user/month. Competes with Confluence (structured wiki) and SharePoint (compliance-focused)."
reading_time: "2 min"
---

## Overview

Notion is a cloud-based workspace application that combines note-taking, databases, wikis, project management, and collaboration features. It has become one of the most popular productivity tools in the tech industry, used by individuals and teams to organize information, manage projects, and maintain knowledge bases. Notion also offers Notion AI, an integrated AI assistant that can answer questions about workspace content.

In the context of LLM knowledge bases, Notion appears in two roles. First, it represents the traditional manual approach to personal knowledge management that both Gallagher and others found ultimately unsustainable -- elaborate systems that "became unmaintainable as priorities shifted" with "management overhead quickly outweighing benefits." Second, the Decoding AI pipeline uses a Notion database of AI/ML resources as its raw data source, feeding content through an ETL pipeline into MongoDB for RAG.

## Key Features

- **Flexible blocks**: Notion's block-based editor supports text, databases, kanban boards, galleries, calendars, and embeds, making it versatile for different knowledge types.

- **Notion AI**: An integrated AI assistant that can search, summarize, and answer questions about workspace content, representing the "AI-augmented PKM" phase described in [[concepts/personal-knowledge-management]].

- **Cloud-native**: Content is stored in Notion's cloud, accessible from any device. This contrasts with Obsidian's local-first approach and the LLM-KB's file-system-based storage.

- **API access**: Notion's API enables programmatic access to workspace content, which the Decoding AI pipeline uses for data extraction.

## Role in LLM Knowledge Bases

Notion represents the "before" state in the PKM evolution narrative. Gallagher's explicit description of failing with Notion before developing his Knowledge Graph Kit illustrates why LLM-maintained systems are appealing: they eliminate the manual overhead that makes traditional tools unsustainable at scale. Notion AI represents an intermediate step -- AI augmenting human authoring -- rather than the full LLM-maintained approach where the AI is the sole author.

In the [[concepts/knowledge-base-product-gap]] analysis, Notion AI is identified as one of the current alternatives that falls short of the full Karpathy pipeline: it assists with individual content items but does not implement the raw -> compile -> wiki -> Q&A -> file back -> lint cycle that defines the LLM-KB methodology.

## Enterprise Evolution (2025-2026)

Per [[sources/eesel-confluence-notion-sharepoint]], Notion has evolved far beyond its PKM origins into an enterprise knowledge platform:

- **100 million+ users**, ranked #1 for knowledge bases on G2
- **Notion AI Agent**: Autonomous multi-step task completion using workspace context, connected apps, and the web
- **Enterprise Search**: AI-powered search across connected applications
- **Expanded suite**: Sites, Forms, Calendar, Mail -- pulling more work into a single interface
- **Pricing**: $10/user/month (Plus), with AI included in base plans (unlike [[entities/sharepoint]] which charges $30/user/month extra for Copilot)

Notion now competes directly with [[entities/confluence]] (structured wiki for Jira teams) and [[entities/sharepoint]] (compliance-focused enterprise CMS). Its strength is flexibility and AI-first design; its weakness relative to SharePoint is compliance certification depth.

## Mentioned In

- [[sources/gallagher-second-brain-knowledge-graphs]] -- described as one of the traditional tools that became unmaintainable, motivating the move to graph-based LLM KB
- [[sources/decodingai-second-brain-rag]] -- used as the raw data source for the production RAG pipeline
- [[sources/eesel-confluence-notion-sharepoint]] -- compared against Confluence and SharePoint as enterprise knowledge platform
