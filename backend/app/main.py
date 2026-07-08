from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from agents import Runner
from app.models.agent_response import AgentResponse

from app.agents.triage_agent import triage_agent

load_dotenv()

app = FastAPI(title="Student Services Assistant API")


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat")
async def chat(request: ChatRequest):
    result = await Runner.run(
        triage_agent,
        request.message,
    )

    return  AgentResponse(
    answer=result.final_output,
    category="general",
    handled_by_agent="Triage Agent",
    handoff_reason=None,
    action_items=[],
    memory_updates=[],
    needs_human=False,
)