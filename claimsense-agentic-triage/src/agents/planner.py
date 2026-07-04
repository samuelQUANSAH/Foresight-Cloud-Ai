from src.observability.tracing import add_trace


def run_planner(state):
    state.plan = [
        "Understand request and business objective",
        "Retrieve relevant policy evidence",
        "Check compliance and documentation risk",
        "Draft recommendation with confidence score",
        "Critique output and route to human if needed",
    ]
    return add_trace(state, "planner", "created task plan", {"steps": len(state.plan)})
