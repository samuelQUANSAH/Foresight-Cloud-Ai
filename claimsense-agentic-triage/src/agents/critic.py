from src.guardrails.policy import should_escalate, detect_unnecessary_pii
from src.observability.tracing import add_trace


def run_critic(state):
    text = f"{state.request.clinical_notes} {state.recommendation or ''}"
    pii_flags = detect_unnecessary_pii(text)
    needs_review, reasons = should_escalate(state.confidence, state.retrieved_evidence, pii_flags)

    # Regulated healthcare workflow: even good AI recommendations can be reviewer-assisted.
    if "materially affect patient access" not in reasons and state.confidence < 0.9:
        reasons.append("regulated healthcare decision requires reviewer verification")
        needs_review = True

    state.needs_human_review = needs_review
    state.escalation_reasons = reasons
    return add_trace(state, "critic", "validated output", {
        "needs_human_review": needs_review,
        "reasons": reasons,
    })
