from src.guardrails.policy import detect_unnecessary_pii
from src.schemas import AgentFinding
from src.observability.tracing import add_trace


def run_compliance(state):
    text = " ".join([
        state.request.member_id,
        state.request.procedure,
        state.request.diagnosis,
        state.request.clinical_notes,
    ])
    pii_flags = detect_unnecessary_pii(text)
    summary = "No unnecessary PII detected." if not pii_flags else "Potential unnecessary PII detected."
    confidence = 0.9 if not pii_flags else 0.45
    state.findings.append(AgentFinding(
        agent="compliance",
        summary=summary,
        confidence=confidence,
        evidence=pii_flags,
    ))
    return add_trace(state, "compliance", "completed compliance check", {"pii_flags": pii_flags})
