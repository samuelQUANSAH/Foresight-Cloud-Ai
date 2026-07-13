from src.schemas import CaseRequest
from src.agents.supervisor import run_case


def evaluate_sample_case():
    case = CaseRequest(
        member_id="M-2001",
        request_type="prior_authorization",
        procedure="MRI Lumbar Spine",
        diagnosis="lower back pain",
        clinical_notes="Patient reports pain but conservative therapy is not documented.",
    )
    result = run_case(case)
    return {
        "has_evidence": bool(result.evidence),
        "has_confidence": result.confidence > 0,
        "routes_uncertain_case_to_human": result.needs_human_review,
        "has_trace": bool(result.trace),
    }


if __name__ == "__main__":
    print(evaluate_sample_case())
