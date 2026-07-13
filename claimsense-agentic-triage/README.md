# Agentic Forward Deployed Engineer Demo

## Project: ClaimSense Agentic Triage

**Client scenario:** A healthcare payer receives thousands of prior authorization and claims exception requests each week. Operations leaders need faster triage, better evidence grounding, and clearer audit trails without replacing human reviewers.

**Problem statement:** Build a multi-agent AI workflow that ingests a request, retrieves policy evidence, checks compliance and PII risks, produces a reviewer-ready recommendation, and routes uncertain cases to a human.

This demo is designed for a 2.5-hour technical interview. It emphasizes reliability, guardrails, observability, and client-facing communication over unnecessary complexity.

## Business outcome

- Reduce manual review time for routine cases.
- Ground AI output in approved policy documents.
- Give compliance teams a traceable decision path.
- Package the solution as reusable IP for healthcare, BFSI, and other regulated workflows.

## Multi-agent architecture

```text
User Request
   ↓
Supervisor Agent
   ↓
Planner Agent → creates task plan
   ↓
Retrieval Agent → pulls policy context
   ↓
Compliance Agent → checks PII, risk, policy gaps
   ↓
Decision Agent → drafts recommendation
   ↓
Critic Agent → validates groundedness, confidence, escalation
   ↓
Final Response / Human Review Queue
```

## Why this fits the role

- **60% engineering:** FastAPI app, agent modules, schemas, retrieval, guardrails, tests.
- **20% research:** policy evidence retrieval and reasoning over domain documents.
- **20% architecture:** reusable orchestration pattern, clear state object, evaluation hooks, observability.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.demo
uvicorn src.api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Sample API request

```json
{
  "member_id": "M-10492",
  "request_type": "prior_authorization",
  "procedure": "MRI Lumbar Spine",
  "diagnosis": "chronic lower back pain with new radiating symptoms",
  "clinical_notes": "Patient completed 6 weeks of physical therapy. Pain is worsening. No red flags documented.",
  "urgency": "standard"
}
```

## Production-grade talking points

1. I start with a clear state model so every agent reads and writes predictable fields.
2. I separate planning, retrieval, compliance, decisioning, and critique so the system is easier to test.
3. I put guardrails before final output: PII checks, citation requirements, confidence thresholds, and escalation rules.
4. I treat the human reviewer as part of the architecture, not an afterthought.
5. I make the workflow observable through structured traces, latency, confidence, and escalation reasons.

## What I would improve with more time

- Replace local keyword retrieval with pgvector, Qdrant, Pinecone, or Azure AI Search.
- Add LangGraph state transitions for retries and conditional routing.
- Add LangSmith, Langfuse, Arize Phoenix, or OpenTelemetry traces.
- Add auth, RBAC, tenant isolation, and audit logging.
- Add evaluation datasets for accuracy, faithfulness, latency, cost, and escalation quality.
