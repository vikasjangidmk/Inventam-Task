from typing import Dict, Any, List
import re, time, uuid
from .schemas import AgentResult
from .db import load_agent_config

class BaseAgent:
    def __init__(self, name: str):
        self.name = name
        self.instructions = ""
        self.guardrails = {}
    async def load(self):
        cfg = await load_agent_config(self.name)
        if cfg:
            self.instructions = cfg.get("instructions", "")
            self.guardrails = cfg.get("guardrails", {})
    def apply_guardrails_text(self, prompt: str) -> bool:
        if self.guardrails.get("forbid_personal_data", True) and re.search(r"\b\d{12,16}\b", prompt):
            return False
        return True

class GeneralQAAgent(BaseAgent):
    async def run(self, prompt: str, context: Dict[str, Any], guardrails: Dict[str, Any]) -> AgentResult:
        start = time.time()
        if not self.apply_guardrails_text(prompt):
            resp = "I cannot process requests containing raw personal financial data. Please redact."
            trace = {"request_id": str(uuid.uuid4()), "agent_name": self.name, "processing_time_ms": int((time.time()-start)*1000), "guardrails_passed": False}
            return AgentResult(assistant_response=resp, action_items=[], required_connection_config={}, trace=trace)
        # Placeholder — integrate actual LLM call here if desired
        resp = f"[GeneralQAAgent] Short answer: {prompt[:200]}"
        trace = {"request_id": str(uuid.uuid4()), "agent_name": self.name, "processing_time_ms": int((time.time()-start)*1000), "guardrails_passed": True}
        return AgentResult(assistant_response=resp, action_items=[{"type":"clarify","text":"Short or detailed?"}], required_connection_config={}, trace=trace)

class TaskPlannerAgent(BaseAgent):
    async def run(self, prompt: str, context: Dict[str, Any], guardrails: Dict[str, Any]) -> AgentResult:
        start = time.time()
        resp = ("[TaskPlannerAgent] Plan:\n"
                "1. Define scope & acceptance criteria\n2. Build prototype (1-2 weeks)\n3. Validate and safety-test\n4. Deploy Canary\n")
        actions = [{"type":"plan","milestones":["scope","prototype","validation","deploy"], "est_hours":[8,40,16,8]}]
        trace = {"request_id": str(uuid.uuid4()), "agent_name": self.name, "processing_time_ms": int((time.time()-start)*1000), "guardrails_passed": True}
        return AgentResult(assistant_response=resp, action_items=actions, required_connection_config={}, trace=trace)

class DataQueryAgent(BaseAgent):
    async def run(self, prompt: str, context: Dict[str, Any], guardrails: Dict[str, Any]) -> AgentResult:
        start = time.time()
        resp = ("[DataQueryAgent] Clarifying: Which DB and timeframe? Proposed SQL template:\n"
                "SELECT user_id, event_time, action FROM events WHERE event_time >= '{{start}}' AND event_time < '{{end}}' LIMIT 1000;")
        actions = [{"type":"ask","questions":["Which DB?","Which time range?"]}]
        trace = {"request_id": str(uuid.uuid4()), "agent_name": self.name, "processing_time_ms": int((time.time()-start)*1000), "guardrails_passed": True}
        return AgentResult(assistant_response=resp, action_items=actions, required_connection_config={}, trace=trace)

class IntegrationAgent(BaseAgent):
    async def run(self, prompt: str, context: Dict[str, Any], guardrails: Dict[str, Any]) -> AgentResult:
        start = time.time()
        resp = ("[IntegrationAgent] Recommended integrations:\n- Slack: webhook\n- Jira: API token\nSecurity: store tokens in secrets manager.")
        actions = [{"type":"config","required_fields":{"slack_webhook":"url","jira_api_token":"token"}}]
        trace = {"request_id": str(uuid.uuid4()), "agent_name": self.name, "processing_time_ms": int((time.time()-start)*1000), "guardrails_passed": True}
        return AgentResult(assistant_response=resp, action_items=actions, required_connection_config={"secrets":"use-vault"}, trace=trace)
