from pydantic import BaseModel
from typing import Any, Dict, List, Optional

class AgentRequest(BaseModel):
    user_prompt: str
    context: Optional[Dict[str, Any]] = {}
    user_id: Optional[str] = None

class AgentResult(BaseModel):
    assistant_response: str
    action_items: List[Dict[str, Any]]
    required_connection_config: Dict[str, Any]
    trace: Dict[str, Any]
