from src.schemas import CaseRequest
from src.agents.supervisor import run_case


if __name__ == "__main__":
    sample = CaseRequest(
        member_id="M-10492",
        request_type="prior_authorization",
        procedure="MRI Lumbar Spine",
        diagnosis="chronic lower back pain with new radiating symptoms",
        clinical_notes="Patient completed 6 weeks of physical therapy. Pain is worsening. No red flags documented.",
        urgency="standard",
    )
    result = run_case(sample)
    print(result.model_dump_json(indent=2))
