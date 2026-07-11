from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Thread, ThreadItem


def create_thread(db: Session) -> Thread:
    thread = Thread()

    db.add(thread)
    db.commit()
    db.refresh(thread)

    return thread


def create_thread_item(
    db: Session,
    thread_id: int,
    role: str,
    content: str,
) -> ThreadItem:
    thread_item = ThreadItem(
        thread_id=thread_id,
        role=role,
        content=content,
    )

    db.add(thread_item)
    db.commit()
    db.refresh(thread_item)

    return thread_item


def get_thread(
    db: Session,
    thread_id: int,
) -> Thread | None:
    return db.get(Thread, thread_id)


def get_thread_items(
    db: Session,
    thread_id: int,
) -> list[ThreadItem]:
    statement = (
        select(ThreadItem)
        .where(ThreadItem.thread_id == thread_id)
        .order_by(ThreadItem.created_at)
    )

    return list(
        db.scalars(statement).all()
    )