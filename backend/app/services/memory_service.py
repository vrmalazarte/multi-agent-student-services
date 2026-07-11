from sqlalchemy.orm import Session

from app.db.models import MemoryItem


def create_memory_item(
    db: Session,
    thread_id: int,
    key: str,
    value: str,
) -> MemoryItem:
    memory_item = MemoryItem(
        thread_id=thread_id,
        key=key,
        value=value,
    )

    db.add(memory_item)
    db.commit()
    db.refresh(memory_item)

    return memory_item