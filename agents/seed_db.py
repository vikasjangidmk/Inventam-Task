import asyncio
from .db import insert_agent_config
async def seed():
    docs = [
        {"agent_name":"GeneralQAAgent", "instructions":"Answer general user questions, be concise.", "guardrails":{"forbid_personal_data":True,"max_response_tokens":400}},
        {"agent_name":"TaskPlannerAgent","instructions":"Produce step-by-step plans and milestones.","guardrails":{"forbid_personal_data":True,"max_response_tokens":600}},
        {"agent_name":"DataQueryAgent","instructions":"Propose DB query templates and clarify dataset schema.","guardrails":{"forbid_personal_data":True,"max_response_tokens":400}},
        {"agent_name":"IntegrationAgent","instructions":"Suggest integrations and required config fields.","guardrails":{"forbid_personal_data":True,"max_response_tokens":400}}
    ]
    for d in docs:
        await insert_agent_config(d)
    print("Seeded agent_configs.")
if __name__ == "__main__":
    asyncio.run(seed())
