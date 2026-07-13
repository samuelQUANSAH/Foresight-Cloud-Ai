# Interview Talk Track

## Opening
I built this as a healthcare prior-authorization triage workflow. The business goal is not to replace a clinician or reviewer. The goal is to reduce manual effort, ground recommendations in approved policy, and give the client an auditable workflow they can safely own.

## Architecture explanation
I split the system into five agents: planner, retrieval, compliance, decision, and critic. The supervisor controls the workflow and owns the shared state. This mirrors how I would use LangGraph in production: stateful orchestration, conditional routing, retries, and human escalation.

## Tradeoffs
For interview speed, I used local policy chunks and deterministic scoring instead of a hosted vector database. In production, I would use pgvector, Qdrant, Pinecone, Azure AI Search, or Bedrock Knowledge Bases depending on the client's cloud environment and compliance needs.

## Guardrails
The critic checks confidence, evidence presence, and PII risk before final output. I also use escalation by default when a recommendation can affect patient access to care.

## Observability
Every agent appends structured trace events. In production, I would send those traces to LangSmith, Langfuse, Arize Phoenix, or OpenTelemetry so the client can monitor latency, cost, quality, and failure modes.

## Strong closing
This is not just a demo. It is a reusable pattern: regulated intake, evidence retrieval, policy reasoning, guardrails, and human-in-the-loop escalation. The same architecture can be adapted for BFSI disputes, underwriting, compliance review, or customer support operations.
