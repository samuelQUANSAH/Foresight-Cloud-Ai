from fastapi import FastAPI
from src.schemas import CaseRequest, CaseResponse
from src.agents.supervisor import run_case

app = FastAPI(
    title="ClaimSense Agentic Triage API",
    version="0.1.0",
    description="Multi-agent prior authorization triage demo with retrieval, guardrails, and human review routing.",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/triage", response_model=CaseResponse)
def triage_case(request: CaseRequest):
    return run_case(request)
