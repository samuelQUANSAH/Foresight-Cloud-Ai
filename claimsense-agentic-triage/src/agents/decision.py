from src.schemas import AgentFinding
from src.observability.tracing import add_trace


def run_decision(state):
    notes = f"{state.request.diagnosis} {state.request.clinical_notes}".lower()
    has_conservative_therapy = "physical therapy" in notes or "6 weeks" in notes or "six weeks" in notes
    has_neuro_symptoms = "radiating" in notes or "neurological" in notes or "numbness" in notes
    evidence_available = bool(state.retrieved_evidence)

    if has_conservative_therapy and has_neuro_symptoms and evidence_available:
        state.recommendation = (
            "Recommend conditional approval. The case appears to meet policy intent because documentation "
            "mentions conservative therapy and radiating symptoms. A human reviewer should verify that the "
            "clinical record explicitly supports medical necessity."
        )
        state.confidence = 0.82
    elif evidence_available:
        state.recommendation = (
            "Recommend human review before approval. The policy evidence was found, but the clinical notes "
            "do not clearly document all approval criteria."
        )
        state.confidence = 0.66
    else:
        state.recommendation = (
            "Do not automate a recommendation. Policy evidence was not retrieved, so this must be routed "
            "to a human reviewer."
        )
        state.confidence = 0.35

    state.findings.append(AgentFinding(
        agent="decision",
        summary=state.recommendation,
        confidence=state.confidence,
        evidence=state.retrieved_evidence,
    ))
    return add_trace(state, "decision", "drafted recommendation", {"confidence": state.confidence})
