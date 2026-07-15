from sqlalchemy.orm import Session

from app.db.models import AgentRun


def create_agent_run(
    db: Session,
    thread_id: int,
    agent_name: str,
) -> AgentRun:
    agent_run = AgentRun(
        thread_id=thread_id,
        agent_name=agent_name,
    )

    db.add(agent_run)
    db.commit()
    db.refresh(agent_run)

    return agent_run