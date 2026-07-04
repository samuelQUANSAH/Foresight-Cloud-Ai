from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class CaseRequest(BaseModel):
    member_id: str
    request_type: str
    procedure: str
    diagnosis: str
    clinical_notes: str
    urgency: str = "standard"


class AgentFinding(BaseModel):
    agent: str
    summary: str
    confidence: float = Field(ge=0, le=1)
    evidence: List[str] = []


class CaseState(BaseModel):
    request: CaseRequest
    plan: List[str] = []
    retrieved_evidence: List[str] = []
    findings: List[AgentFinding] = []
    recommendation: Optional[str] = None
    confidence: float = 0.0
    needs_human_review: bool = False
    escalation_reasons: List[str] = []
    trace: List[Dict[str, Any]] = []


class CaseResponse(BaseModel):
    recommendation: str
    confidence: float
    needs_human_review: bool
    escalation_reasons: List[str]
    evidence: List[str]
    trace: List[Dict[str, Any]]
