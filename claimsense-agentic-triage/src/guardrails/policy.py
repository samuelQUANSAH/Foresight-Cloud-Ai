import os
from typing import List


CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.75"))
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "5"))


def detect_unnecessary_pii(text: str) -> List[str]:
    risky_terms = ["ssn", "social security", "credit card", "bank account"]
    return [term for term in risky_terms if term in text.lower()]


def should_escalate(confidence: float, evidence: list[str], pii_flags: list[str]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    if confidence < CONFIDENCE_THRESHOLD:
        reasons.append(f"confidence below threshold {CONFIDENCE_THRESHOLD}")
    if not evidence:
        reasons.append("no policy evidence retrieved")
    if pii_flags:
        reasons.append(f"unnecessary PII detected: {', '.join(pii_flags)}")
    return bool(reasons), reasons
