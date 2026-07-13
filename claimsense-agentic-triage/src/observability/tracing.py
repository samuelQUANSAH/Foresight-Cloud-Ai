from datetime import datetime, timezone
from typing import Any, Dict


def add_trace(state, agent_name: str, event: str, metadata: Dict[str, Any] | None = None):
    state.trace.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "agent": agent_name,
        "event": event,
        "metadata": metadata or {},
    })
    return state
