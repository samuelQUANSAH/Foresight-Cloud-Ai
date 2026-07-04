from src.schemas import CaseRequest, CaseResponse, CaseState
from src.agents.planner import run_planner
from src.agents.retrieval import run_retrieval
from src.agents.compliance import run_compliance
from src.agents.decision import run_decision
from src.agents.critic import run_critic
from src.observability.tracing import add_trace


WORKFLOW = [run_planner, run_retrieval, run_compliance, run_decision, run_critic]


def run_case(request: CaseRequest) -> CaseResponse:
    state = CaseState(request=request)
    state = add_trace(state, "supervisor", "started workflow")

    for step in WORKFLOW:
        state = step(state)

    state = add_trace(state, "supervisor", "completed workflow")
    return CaseResponse(
        recommendation=state.recommendation or "No recommendation generated.",
        confidence=state.confidence,
        needs_human_review=state.needs_human_review,
        escalation_reasons=state.escalation_reasons,
        evidence=state.retrieved_evidence,
        trace=state.trace,
    )
