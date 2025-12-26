from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .semantic_router import route_intent
from .agents_impl import GeneralQAAgent, TaskPlannerAgent, DataQueryAgent, IntegrationAgent
from .schemas import AgentRequest, AgentResult
from .db import load_agent_config
import asyncio
import re

app = FastAPI(title="Dynamic Agent Router")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENT_MAP = {
    "general_query": GeneralQAAgent("GeneralQAAgent"),
    "task_planning": TaskPlannerAgent("TaskPlannerAgent"),
    "data_query": DataQueryAgent("DataQueryAgent"),
    "integration": IntegrationAgent("IntegrationAgent"),
}

# Preload the agent configs (optional)
@app.on_event("startup")
async def startup_event():
    # Load agent configs asynchronously
    tasks = []
    for agent in AGENT_MAP.values():
        tasks.append(agent.load())
    await asyncio.gather(*tasks)

@app.post("/run", response_model=AgentResult)
async def run_agent(req: AgentRequest):
    prompt = req.user_prompt
    # 1) intent routing
    intent, confidence, scores = route_intent(prompt)
    # 2) map to agent
    agent = AGENT_MAP.get(intent)
    if not agent:
        agent = AGENT_MAP["general_query"]
    # 3) load config (ensure latest)
    await agent.load()
    # 4) guardrail quick check (PII pattern)
    if agent.guardrails.get("forbid_personal_data", True) and " " in prompt and any([c.isdigit() for c in prompt]) and len(repr(prompt))>1000:
        # very conservative check — for demo
        raise HTTPException(status_code=400, detail="Request contains potential PII. Redact and retry.")
    # 5) run agent
    result = await agent.run(prompt, req.context or {}, agent.guardrails)
    # 6) attach routing info to trace
    result.trace.update({"intent": intent, "intent_confidence": round(confidence, 3), "all_scores": scores})
    return result
