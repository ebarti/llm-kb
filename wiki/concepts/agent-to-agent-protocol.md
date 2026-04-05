---
title: "Agent-to-Agent Protocol (A2A)"
type: concept
sources: ["[[sources/zilliz-function-calling-vs-mcp-vs-a2a]]", "[[sources/google-ai-agent-protocols]]", "[[sources/composio-api-integration-patterns]]"]
related: ["[[concepts/model-context-protocol]]", "[[concepts/multi-agent-systems]]", "[[concepts/tool-use-standards]]", "[[concepts/agentic-workflow-patterns]]"]
last_compiled: 2026-04-05
summary: "Google's protocol for inter-agent collaboration: agents publish Agent Cards for capability discovery, delegate tasks dynamically, and coordinate in real time. Complementary to MCP (tools) — A2A handles 'expertise' and agent-to-agent communication."
---

## Overview

The Agent-to-Agent Protocol (A2A) is a specification introduced by Google that enables specialized AI agents to discover each other, advertise capabilities, delegate tasks dynamically, and coordinate work in real time. While [[concepts/model-context-protocol]] standardizes how agents access tools and data, A2A standardizes how agents collaborate with each other.

The key insight is that MCP addresses data access while A2A addresses expertise — knowledge and capabilities that live with specialized remote agents rather than in databases or APIs.

## Architecture

A2A uses a client/remote model:
- **Client agents** manage tasks and coordinate workflows
- **Remote agents** execute delegated tasks based on their specializations

### Agent Cards
Agents publish discovery documents called "Agent Cards" at a well-known endpoint (`/.well-known/agent-card.json`). These cards describe:
- Agent capabilities and specializations
- Available endpoints and skills
- Communication protocols supported

Other agents discover capabilities at runtime without pre-configuration or code changes.

## How It Works

1. An agent needs expertise it doesn't have (e.g., pricing analysis)
2. It discovers relevant agents via their published Agent Cards
3. It delegates the task to the best-suited remote agent
4. The remote agent executes and returns results
5. Progress is coordinated in real time with secure updates

## Relationship to MCP

A2A and [[concepts/model-context-protocol]] are complementary, not competing:

| Dimension | MCP | A2A |
|-----------|-----|-----|
| **Handles** | Tool and data access | Agent-to-agent collaboration |
| **Question answered** | "What tools can my agent use?" | "How can my agents work together?" |
| **Connects to** | Databases, APIs, files | Other specialized agents |
| **Addresses** | Data | Expertise |

In practice, agents use MCP to access tools and data, and A2A to collaborate with other agents. A layered architecture combining both is recommended for complex systems.

## Current Status

A2A is still early-stage compared to MCP:
- Introduced by Google as part of the Agent Development Kit (ADK)
- Limited ecosystem support as of early 2026
- Expected to become crucial as multi-agent systems mature
- Part of Google's broader six-protocol agent stack (MCP, A2A, UCP, AP2, A2UI, AG-UI)

## Sources
- [[sources/zilliz-function-calling-vs-mcp-vs-a2a]] — three-way protocol comparison
- [[sources/google-ai-agent-protocols]] — A2A as part of six-protocol stack
- [[sources/composio-api-integration-patterns]] — A2A as pattern 5

## Related Concepts
- [[concepts/model-context-protocol]] — the complementary tool/data protocol
- [[concepts/multi-agent-systems]] — the broader multi-agent architecture A2A enables
- [[concepts/tool-use-standards]] — the evolving standards landscape
- [[concepts/agentic-workflow-patterns]] — workflow patterns that benefit from A2A
