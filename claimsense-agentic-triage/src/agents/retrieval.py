from src.rag.retriever import retrieve
from src.schemas import AgentFinding
from src.observability.tracing import add_trace


def run_retrieval(state):
    request = state.request
    query = f"{request.procedure} {request.diagnosis} {request.clinical_notes}"
    evidence = retrieve(query)
    state.retrieved_evidence = evidence
    state.findings.append(AgentFinding(
        agent="retrieval",
        summary=f"Retrieved {len(evidence)} relevant policy chunks.",
        confidence=0.85 if evidence else 0.2,
        evidence=evidence,
    ))
    return add_trace(state, "retrieval", "retrieved policy evidence", {"chunks": len(evidence)})
