from pathlib import Path

POLICY_PATH = Path(__file__).resolve().parents[2] / "data" / "policies.md"


def load_policy_chunks() -> list[str]:
    text = POLICY_PATH.read_text(encoding="utf-8")
    return [chunk.strip() for chunk in text.split("## ") if chunk.strip()]


def retrieve(query: str, top_k: int = 2) -> list[str]:
    chunks = load_policy_chunks()
    query_terms = set(query.lower().replace("/", " ").split())

    scored = []
    for chunk in chunks:
        chunk_terms = set(chunk.lower().replace("/", " ").split())
        score = len(query_terms.intersection(chunk_terms))
        scored.append((score, chunk))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for score, chunk in scored[:top_k] if score > 0]
