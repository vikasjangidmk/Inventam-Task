import os
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGODB_URI)
db = client.ai_platform

async def load_agent_config(agent_name: str) -> Optional[dict]:
    row = await db.agent_configs.find_one({"agent_name": agent_name})
    return row

async def insert_agent_config(doc: dict):
    await db.agent_configs.update_one({"agent_name": doc["agent_name"]}, {"$set": doc}, upsert=True)
