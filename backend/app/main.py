from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from agents import Runner, RunConfig

from app.agents.triage_agent import triage_agent
from app.services.agent_run_service import create_agent_run
from app.db.database import get_db
from app.models.agent_response import AgentResponse
from app.models.run_context import RunContext
from app.services.agent_run_service import create_agent_run
from app.services.thread_service import (
    create_thread,
    create_thread_item,
    get_thread,
    get_thread_items,
)
from app.services.memory_service import (
    get_memory_items,
    save_memory_item,
)

load_dotenv()

app = FastAPI(title="Student Services Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://student-services-frontend-381407246613.asia-southeast1.run.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    thread_items = get_thread_items(
        db=db,
        thread_id=thread.id,
    )

    memory_items = get_memory_items(
        db=db,
        thread_id=thread.id,
    )

    memory_context = "\n".join(
    f"{item.key}: {item.value}"
    for item in memory_items
    )   
    
    agent_input = []

    if memory_context:
        agent_input.append(
            {
                "role": "system",
                "content": (
                    "Saved student memory:\n"
                    f"{memory_context}\n\n"
                    "Use this information when relevant. "
                    "Do not claim the student provided information "
                    "that is not listed here."
                ),
            }
        )

    agent_input.extend(
        {
            "role": item.role,
            "content": item.content,
        }
        for item in thread_items
    )

    context = RunContext(
        db=db,
        thread_id=thread.id,
    )


    result = await Runner.run(
        triage_agent,
        agent_input,
        context=context,
        run_config=RunConfig(
            workflow_name="Student Services Assistant",
        ),
    )

    agent_output = result.final_output

    for memory_update in agent_output.memory_updates:
        save_memory_item(
            db=db,
            thread_id=thread.id,
            key=memory_update.key,
            value=memory_update.value,
        )

    create_thread_item(
        db=db,
        thread_id=thread.id,
        role="assistant",
        content=agent_output.answer,
    )

    create_agent_run(
        db=db,
        thread_id=thread.id,
        agent_name=result.last_agent.name,
    )

    return AgentResponse(
        answer=agent_output.answer,
        category=agent_output.category,
        handled_by_agent=result.last_agent.name,
        handoff_reason=agent_output.handoff_reason,
        action_items=agent_output.action_items,
        memory_updates=agent_output.memory_updates,
        needs_human=agent_output.needs_human,
        thread_id=thread.id,
    )