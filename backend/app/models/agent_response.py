from typing import Literal

from pydantic import BaseModel


class AgentResponse(BaseModel):
    answer: str
    category: Literal[
        "general",
        "billing",
        "schedule",
        "escalation",
    ]
    handled_by_agent: str
    handoff_reason: str | None
    action_items: list[str]
    memory_updates: list[str]
    needs_human: bool