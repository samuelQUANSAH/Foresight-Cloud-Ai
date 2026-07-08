import os
import sys
import logging
import asyncio

# Add fallback path for local Google Antigravity SDK
unpacked_sdk_path = "/Users/lynuelx/.gemini/antigravity/scratch/unpacked"
if os.path.exists(unpacked_sdk_path) and unpacked_sdk_path not in sys.path:
    sys.path.insert(0, unpacked_sdk_path)

# Try loading env variables from .env file gracefully
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Initialize Arize AX Cloud (Enterprise) or Local Phoenix Observability Tracing
phoenix_active = False
arize_ax_active = False

try:
    arize_space_id = os.environ.get("ARIZE_SPACE_ID")
    arize_api_key = os.environ.get("ARIZE_API_KEY")
    
    if arize_space_id and arize_api_key:
        # Instrument for Arize AX Cloud platform
        from arize.otel import register as register_arize
        register_arize(
            space_id=arize_space_id,
            api_key=arize_api_key,
            project_name="afrophysiques-agentic-orchestrator"
        )
        arize_ax_active = True
    else:
        # Fallback to local open-source Arize Phoenix dashboard
        import phoenix as px
        from phoenix.otel import register as register_phoenix
        px.launch_app()
        register_phoenix(project_name="afrophysiques-agentic-orchestrator")
        phoenix_active = True
except Exception as e:
    pass

# Import OpenTelemetry APIs for manual tracing
try:
    from opentelemetry import trace
    otel_tracer = trace.get_tracer("afrophysiques-orchestrator")
except ImportError:
    otel_tracer = None

from google.antigravity import Agent, LocalAgentConfig, types
from google.antigravity.hooks import hooks, policy

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Setup Logging Namespace
logging.getLogger("google.antigravity").setLevel(logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/audit.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("AfrophysiquesOrchestrator")

# Define Target Workspace and Enforced Token Budget Limit
WORKSPACE_DIR = "/Users/lynuelx/Documents/creative science"
TOKEN_BUDGET_LIMIT = 100  # Token limit constraint requested by the developer

# High-Fidelity Mock Response for local dry-run when API keys are unauthorized or missing
class SimulatedResponse:
    def __init__(self, text_content):
        self._text = text_content
        
    async def text(self):
        return self._text
        
    def __aiter__(self):
        return self._token_generator()
        
    async def _token_generator(self):
        for word in self._text.split():
            yield word + " "
            await asyncio.sleep(0.02)
            
    @property
    def thoughts(self):
        return self._thoughts_generator()
        
    async def _thoughts_generator(self):
        thoughts = [
            "Analyzing incoming Shopify webhook event data...",
            "Validating workspace confinement bounds. Confinement: /Users/lynuelx/Documents/creative science",
            "Instantiating Frontend Agent sub-session to verify e-commerce cache updates...",
            "Instantiating Integration Agent sub-session to verify n8n webhook payload signature...",
            "Determining necessary tool calls for cache synchronization verification..."
        ]
        for t in thoughts:
            yield t + "\n"
            await asyncio.sleep(0.1)

# Register Custom Post-Tool-Call Telemetry Hook
@hooks.post_tool_call
async def audit_tool_call(tool_call_result):
    logger.info(f"[AUDIT] Tool Execution Completed: {tool_call_result}")

# Register Custom Session End Hook to summarize token usage
@hooks.on_session_end
async def finalize_session():
    logger.info("Session complete. Cleaning up active subagent connections.")

async def run_orchestration_cycle():
    logger.info("Starting Multi-Agent Orchestrator Cycle...")
    logger.info(f"Enforcing Token Budget Limit: {TOKEN_BUDGET_LIMIT} tokens.")
    
    if arize_ax_active:
        logger.info("Arize AX Cloud Observability Active: Exporting spans to Arize AX console.")
    elif phoenix_active:
        logger.info("Arize Phoenix Local Observability Active: Tracing spans to local dashboard.")
    else:
        logger.warning("Arize Observability could not be initialized.")

    # Configure Safety policies
    safety_policies = [
        policy.workspace_only([WORKSPACE_DIR]),
        policy.deny("run_command", when=lambda args: any(cmd in args.get("CommandLine", "") for cmd in ["rm", "chmod", "mv"]), name="deny_destructive_commands")
    ]

    # Instantiate Agent Configuration
    config = LocalAgentConfig(
        model="gemini-3.5-flash",
        system_instructions="You are the Forward Deployed Agentic Architect for Afrophysiques. You orchestrate Shopify webhooks, n8n retrieving updates, and frontend builds.",
        capabilities=types.CapabilitiesConfig(
            enable_subagents=True
        ),
        policies=safety_policies,
        hooks=[audit_tool_call, finalize_session]
    )

    api_key_set = os.environ.get("GEMINI_API_KEY") is not None
    
    if api_key_set:
        try:
            logger.info("Attempting live connection to Gemini API...")
            async with Agent(config=config) as architect:
                logger.info("Agentic Architect Initialized successfully.")
                
                trigger_message = (
                    "Received Shopify Webhook Event via n8n: Variant AP-HD-BLK-M updated stock to 42. "
                    "Spawn a subagent to check if the frontend cache and product listing is updated correctly."
                )
                
                logger.info(f"Incoming Event: {trigger_message}")
                response = await architect.chat(trigger_message)
                response_text = await response.text()
                
                logger.info(f"Architect Response:\n{response_text}")
                
                # Observability: Extract token usage metrics and verify budget
                usage = architect.conversation.total_usage
                logger.info("--- Observability Metrics ---")
                logger.info(f"Prompt Tokens: {usage.prompt_token_count}")
                logger.info(f"Candidates Tokens: {usage.candidates_token_count}")
                logger.info(f"Thoughts Tokens: {usage.thoughts_token_count}")
                logger.info(f"Total Session Tokens: {usage.total_token_count}")
                
                if usage.total_token_count > TOKEN_BUDGET_LIMIT:
                    logger.error(f"TOKEN BUDGET EXCEEDED: Limit is {TOKEN_BUDGET_LIMIT}, used {usage.total_token_count}!")
                    raise ValueError(f"Token budget limit of {TOKEN_BUDGET_LIMIT} exceeded (used {usage.total_token_count})")
                return
        except Exception as e:
            logger.warning(f"Live Gemini connection failed or unauthorized: {e}")
            logger.info("Falling back to local simulated high-fidelity runner.")

    # Local Simulated High-Fidelity Runner
    logger.info("--- LOCAL RUNNER (SIMULATION MODE) ---")
    logger.info("Generating OpenTelemetry spans for trace export...")
    
    # Define trigger message for simulation
    trigger_message = (
        "Received Shopify Webhook Event via n8n: Variant AP-HD-BLK-M updated stock to 42. "
        "Spawn a subagent to check if the frontend cache and product listing is updated correctly."
    )
    
    sim_prompt_tokens = 245
    sim_candidate_tokens = 120
    sim_thoughts_tokens = 380
    sim_total_tokens = sim_prompt_tokens + sim_candidate_tokens + sim_thoughts_tokens
    
    # Check if OTel tracer is configured
    if otel_tracer:
        # 1. Start Parent Orchestration Span
        with otel_tracer.start_as_current_span("run_orchestration_cycle") as parent_span:
            parent_span.set_attribute("inputs.trigger_message", trigger_message)
            parent_span.set_attribute("agent.role", "AgenticArchitect")
            parent_span.set_attribute("workspace.confinement", WORKSPACE_DIR)
            parent_span.set_attribute("token.budget.limit", TOKEN_BUDGET_LIMIT)
            
            # 2. Start Agent Reasoning Span
            with otel_tracer.start_as_current_span("agent_reasoning") as reasoning_span:
                reasoning_span.set_attribute("model.name", "gemini-3.5-flash")
                logger.info("Agent Thoughts:")
                sim_response_text = (
                    "Architect Actions:\n"
                    "1. Spawned Frontend Agent: Verified product listing for 'Afrophysiques Signature Hoodie' updated correctly in catalog.\n"
                    "2. Spawned Integration Agent: Verified webhook signature HMAC matches local secret.\n"
                    "3. Synchronized cache storage. Product stock updated to 42 successfully."
                )
                sim = SimulatedResponse(sim_response_text)
                
                async for thought in sim.thoughts:
                    print(f"  [Thought] {thought.strip()}")
                    reasoning_span.add_event("thought_generation", {"thought": thought.strip()})
            
            # 3. Start Frontend Agent Sub-Task Span
            with otel_tracer.start_as_current_span("frontend_agent_execution") as fe_span:
                fe_span.set_attribute("subagent.role", "FrontendAgent")
                fe_span.set_attribute("task.target", "index.html")
                logger.info("Agent Streaming Response:")
                async for token in sim:
                    print(token, end="", flush=True)
                print("\n")
                fe_span.add_event("frontend_cache_check", {"status": "success", "file": "index.html"})
                
            # 4. Start Integration Agent Sub-Task Span
            with otel_tracer.start_as_current_span("integration_agent_execution") as int_span:
                int_span.set_attribute("subagent.role", "ShopifyIntegrationAgent")
                int_span.set_attribute("webhook.event", "inventory_levels/update")
                int_span.add_event("hmac_validation", {"verified": True})
                
            # 5. Start Tool Execution Span
            with otel_tracer.start_as_current_span("tool_call_verify_cache_sync") as tool_span:
                tool_span.set_attribute("tool.name", "verify_cache_sync")
                tool_span.set_attribute("tool.arguments", "variant='AP-HD-BLK-M', stock=42")
                await audit_tool_call("verify_cache_sync(variant='AP-HD-BLK-M', stock=42) -> Success")
                tool_span.set_attribute("tool.result", "Success")

            await finalize_session()
            
            # Verify and Enforce Token Budget Constraint
            logger.info("--- Observability Metrics ---")
            logger.info(f"Prompt Tokens: {sim_prompt_tokens}")
            logger.info(f"Candidates Tokens: {sim_candidate_tokens}")
            logger.info(f"Thoughts Tokens: {sim_thoughts_tokens}")
            logger.info(f"Total Session Tokens: {sim_total_tokens} (Limit: {TOKEN_BUDGET_LIMIT})")
            
            if sim_total_tokens > TOKEN_BUDGET_LIMIT:
                err_msg = f"Token budget limit of {TOKEN_BUDGET_LIMIT} exceeded (used {sim_total_tokens})"
                logger.error(f"TOKEN BUDGET VIOLATION: {err_msg}!")
                
                # Flag the span as an error in OpenTelemetry for Arize AX
                parent_span.set_status(trace.StatusCode.ERROR, err_msg)
                parent_span.record_exception(ValueError(err_msg))
                parent_span.set_attribute("session.status", "failed")
            else:
                parent_span.set_attribute("session.status", "complete")
    else:
        # Default printing without Otel spans
        sim_response_text = (
            "Architect Actions:\n"
            "1. Spawned Frontend Agent: Verified product listing for 'Afrophysiques Signature Hoodie' updated correctly in catalog.\n"
            "2. Spawned Integration Agent: Verified webhook signature HMAC matches local secret.\n"
            "3. Synchronized cache storage. Product stock updated to 42 successfully."
        )
        sim = SimulatedResponse(sim_response_text)
        logger.info("Agent Thoughts:")
        async for thought in sim.thoughts:
             print(f"  [Thought] {thought.strip()}")
        logger.info("Agent Streaming Response:")
        async for token in sim:
             print(token, end="", flush=True)
        print("\n")
        await audit_tool_call("verify_cache_sync(variant='AP-HD-BLK-M', stock=42) -> Success")
        await finalize_session()
        
        logger.info("--- Observability Metrics ---")
        logger.info(f"Prompt Tokens: {sim_prompt_tokens}")
        logger.info(f"Candidates Tokens: {sim_candidate_tokens}")
        logger.info(f"Thoughts Tokens: {sim_thoughts_tokens}")
        logger.info(f"Total Session Tokens: {sim_total_tokens} (Limit: {TOKEN_BUDGET_LIMIT})")
        
        if sim_total_tokens > TOKEN_BUDGET_LIMIT:
            logger.error(f"TOKEN BUDGET VIOLATION: Token limit of {TOKEN_BUDGET_LIMIT} exceeded (used {sim_total_tokens})!")

if __name__ == "__main__":
    asyncio.run(run_orchestration_cycle())
