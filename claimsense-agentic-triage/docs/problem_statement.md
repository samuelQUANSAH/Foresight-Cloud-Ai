# Sample Problem Statement

## Title
ClaimSense: Multi-Agent Prior Authorization Triage

## Client
A healthcare payer with high prior-authorization volume and strict compliance requirements.

## Pain point
Clinical operations teams spend too much time manually reviewing routine prior-authorization requests. Existing workflows are slow, inconsistent, and difficult to audit. Leaders want AI assistance, but they need evidence grounding, guardrails, and human review before operational ownership.

## Solution
Build a multi-agent orchestration pipeline that receives a prior-authorization case, retrieves relevant policy evidence, evaluates documentation quality, checks compliance risk, drafts a recommendation, and escalates uncertain cases to a human reviewer.

## Agents
1. Supervisor Agent: controls the workflow.
2. Planner Agent: breaks the request into tasks.
3. Retrieval Agent: retrieves policy evidence.
4. Compliance Agent: checks PII and risk.
5. Decision Agent: drafts the recommendation.
6. Critic Agent: validates confidence, citations, and escalation.

## Success criteria
- Functional API endpoint.
- Evidence-grounded recommendation.
- Confidence score.
- Human review routing.
- Structured trace for observability.
- Reusable design that can become client-facing IP.
