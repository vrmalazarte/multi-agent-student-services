from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import MemoryItem


def save_memory_item(
    db: Session,
    thread_id: int,
    key: str,
    value: str,
) -> MemoryItem:
    statement = select(MemoryItem).where(
        MemoryItem.thread_id == thread_id,
        MemoryItem.key == key,
    )

    memory_item = db.scalar(statement)

    if memory_item is None:
        memory_item = MemoryItem(
            thread_id=thread_id,
            key=key,
            value=value,
        )

        db.add(memory_item)
    else:
        memory_item.value = value

    db.commit()
    db.refresh(memory_item)

    return memory_item


def get_memory_items(
    db: Session,
    thread_id: int,
) -> list[MemoryItem]:
    statement = select(MemoryItem).where(
        MemoryItem.thread_id == thread_id
    )

    return list(db.scalars(statement).all())