# Foresight-Cloud-Ai

Welcome to the **Foresight-Cloud-Ai** project repository. This repository combines the **Afrophysiques E-Commerce storefront** and the **ClaimSense Multi-Agent Triage** orchestration system.

---

## 🌌 1. ClaimSense Multi-Agent Triage Demo

[`claimsense-agentic-triage/`](claimsense-agentic-triage/) contains a working multi-agent orchestration system: a supervisor agent coordinates Planner, Retrieval, Compliance, Decision, and Critic agents over a shared state object, with policy-grounded retrieval, PII/compliance guardrails, confidence-based human-review escalation, and structured tracing. 

See its [README](claimsense-agentic-triage/README.md) for local setup instructions and a sample API request.

---

## 🛍️ 2. Afrophysiques - Ultra-Modern Reactive E-commerce Store

This project is a comprehensive re-architecture of the Afrophysiques web application, transforming it from a legacy layout into an ultra-modern, reactive, and responsive e-commerce experience. The application utilizes **Shopify** for inventory and product management, coordinated via a multi-agent orchestration stack.

### The Triad Architecture

This repository is bounded by three operational integration pillars (the **Triad**):

```
       [ GitHub Repository ]
      /                     \
     /                       \
[ n8n Webhooks ] <-------> [ Claude Code / Antigravity Agent ]
```

1. **GitHub Repository**: The central host for version control, CI/CD pipelines, automated testing, and agent environment definitions.
2. **n8n Webhook Retrieves**: Real-time event routing. Shopify webhooks trigger n8n workflows, which transform payloads and retrieve data from inventory, forwarding details to our orchestration endpoints.
3. **Claude Code / Google Antigravity Integration**: Multi-agent orchestration. Autonomous subagents work concurrently to monitor, build, verify, and test components of the store.

### Directory Structure

```text
/Users/lynuelx/Documents/creative science/
├── README.md                           <- This file: Project blueprint and overview
├── docs/
│   ├── agents_architecture.md          <- Agent coordination, roles, and safety policies
│   ├── shopify_n8n_integration.md      <- Webhook schemas, n8n trigger paths, and API setups
│   ├── observability_and_security.md   <- Guardrails, secrets, and telemetry configuration
│   ├── frontend_roadmap.md             <- UX/UI requirements, styling specs, and Storefront API
│   └── deployment_testing_playbook.md   <- Git workflow, CI/CD verification, and sandbox testing
└── src/
    └── orchestrator.py                 <- Python orchestrator using Google Antigravity SDK
```

### Quick Start & Orchestration

The project orchestrator uses the **Google Antigravity SDK** to spawn and coordinate subagents.

#### Prerequisites
1. Python 3.10+
2. Installed dependencies: `pip install google-antigravity python-dotenv`
3. A valid `.env` file containing:
   ```env
   GEMINI_API_KEY="your_api_key_here"
   SHOPIFY_STOREFRONT_TOKEN="your_token_here"
   N8N_WEBHOOK_SECRET="your_secret_here"
   ```

#### Execution
To launch the agent orchestrator and execute structural tasks:
```bash
python3 src/orchestrator.py
```

### Next Steps
Please refer to the files in the `docs/` directory to explore detailed roadmaps for each subsystem:
* Read [agents_architecture.md](file:///Users/lynuelx/Documents/creative science/docs/agents_architecture.md) to understand agent roles and safety policies.
* Read [shopify_n8n_integration.md](file:///Users/lynuelx/Documents/creative science/docs/shopify_n8n_integration.md) for data flow specifications.
* Read [observability_and_security.md](file:///Users/lynuelx/Documents/creative science/docs/observability_and_security.md) for security and guardrails.
* Read [frontend_roadmap.md](file:///Users/lynuelx/Documents/creative science/docs/frontend_roadmap.md) for design and styling guidelines.
* Read [deployment_testing_playbook.md](file:///Users/lynuelx/Documents/creative science/docs/deployment_testing_playbook.md) for build pipelines.
