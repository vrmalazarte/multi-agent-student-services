from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from agents import Runner, RunConfig

from app.agents.triage_agent import triage_agent
from app.db.database import get_db
from app.models.agent_response import AgentResponse
from app.models.run_context import RunContext
from app.services.agent_run_service import create_agent_run
from app.services.thread_service import (
    create_thread,
    create_thread_item,
    get_thread,
)

load_dotenv()

app = FastAPI(title="Student Services Assistant API")


class ChatRequest(BaseModel):
    message: str
    thread_id: int | None = None


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat")
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):

    if request.thread_id is None:
        thread = create_thread(db)
    else:
        thread = get_thread(
            db=db,
            thread_id=request.thread_id,
        )

        if thread is None:
            raise HTTPException(
                status_code=404,
                detail="Thread not found",
            )

    create_thread_item(
        db=db,
        thread_id=thread.id,
        role="user",
        content=request.message,
    )

    context = RunContext(
        db=db,
        thread_id=thread.id,
    )

    result = await Runner.run(
        triage_agent,
        request.message,
        context=context,
        run_config=RunConfig(
            workflow_name="Student Services Assistant",
        ),
    )

    create_thread_item(
        db=db,
        thread_id=thread.id,
        role="assistant",
        content=result.final_output,
    )

    create_agent_run(
        db=db,
        thread_id=thread.id,
        agent_name=result.last_agent.name,
    )

    return AgentResponse(
        answer=result.final_output,
        category="general",
        handled_by_agent=result.last_agent.name,
        handoff_reason=None,
        action_items=[],
        memory_updates=[],
        needs_human=False,
    )