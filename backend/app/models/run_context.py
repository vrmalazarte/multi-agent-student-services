from dataclasses import dataclass

from sqlalchemy.orm import Session


@dataclass
class RunContext:
    db: Session
    thread_id: int