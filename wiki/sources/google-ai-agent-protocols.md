---
title: "Source: Developer's Guide to AI Agent Protocols (Google)"
type: source-summary
source: "[[raw/google-ai-agent-protocols]]"
related: ["[[concepts/model-context-protocol]]", "[[concepts/agent-to-agent-protocol]]", "[[concepts/ai-agent-integration-patterns]]", "[[entities/google-adk]]"]
last_compiled: 2026-04-05
summary: "Google's guide to six AI agent protocols: MCP (tool access), A2A (agent collaboration), UCP (commerce), AP2 (payments), A2UI (dynamic UI), AG-UI (streaming events) — all integrated via Google's ADK."
---

## Key Points
- Six protocols forming a complete agent stack: MCP, A2A, UCP, AP2, A2UI, AG-UI
- MCP: "single standard connection pattern for hundreds of servers" — tools advertise capabilities for auto-discovery
- A2A: agents publish Agent Cards at /.well-known/agent-card.json for runtime discovery
- UCP: strongly-typed commerce schemas across REST, MCP, A2A
- AP2: cryptographic authorization with IntentMandate/PaymentMandate/PaymentReceipt
- A2UI: declarative JSON with 18 component primitives for agent-composed UIs
- AG-UI: SSE-based streaming events (TOOL_CALL_START, TEXT_MESSAGE_CONTENT, etc.)
- All integrated through Google's Agent Development Kit (ADK)
- Key principle: "Add protocols as you need them" — start with MCP, expand as requirements grow

## Detailed Summary

This Google Developers blog post presents the most comprehensive view of the emerging agent protocol stack. It describes six protocols that, together, cover the full lifecycle of agent interactions:

1. [[concepts/model-context-protocol]] handles data access — agents discover and use tools through standardized MCP servers
2. [[concepts/agent-to-agent-protocol]] enables inter-agent collaboration via Agent Cards for capability discovery
3. Universal Commerce Protocol (UCP) standardizes commerce workflows with strongly-typed schemas
4. Agent Payments Protocol (AP2) adds cryptographic authorization and audit trails
5. Agent-to-User Interface Protocol (A2UI) enables agents to compose UIs from 18 declarative primitives
6. Agent-User Interaction Protocol (AG-UI) standardizes streaming events between agents and frontends

The article demonstrates all six working together in a restaurant supply chain example, and introduces Google's [[entities/google-adk]] as the framework integrating all protocols.

## Related Concepts
- [[concepts/model-context-protocol]] — the foundational data access protocol
- [[concepts/agent-to-agent-protocol]] — the inter-agent collaboration protocol
- [[concepts/ai-agent-integration-patterns]] — the full pattern landscape
- [[concepts/agentic-workflow-patterns]] — how these protocols enable workflow patterns
