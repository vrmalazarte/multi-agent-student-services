from typing import Literal

from pydantic import BaseModel

from app.models.memory_update import MemoryUpdate


class AgentOutput(BaseModel):
    answer: str
    category: Literal[
        "general",
        "billing",
        "schedule",
        "escalation",
    ]
    handoff_reason: str | None
    action_items: list[str]
    memory_updates: list[MemoryUpdate]
    needs_human: bool