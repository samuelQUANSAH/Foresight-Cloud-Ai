from src.schemas import CaseRequest
from src.agents.supervisor import run_case


def test_workflow_returns_recommendation_and_trace():
    request = CaseRequest(
        member_id="M-10492",
        request_type="prior_authorization",
        procedure="MRI Lumbar Spine",
        diagnosis="chronic lower back pain with radiating symptoms",
        clinical_notes="Patient completed 6 weeks of physical therapy.",
    )
    result = run_case(request)
    assert result.recommendation
    assert result.confidence > 0
    assert result.trace


def test_uncertain_case_routes_to_human():
    request = CaseRequest(
        member_id="M-10493",
        request_type="prior_authorization",
        procedure="MRI Lumbar Spine",
        diagnosis="back pain",
        clinical_notes="Patient reports pain. No prior treatment documented.",
    )
    result = run_case(request)
    assert result.needs_human_review is True
    assert result.escalation_reasons
