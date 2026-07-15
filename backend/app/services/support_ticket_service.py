from sqlalchemy.orm import Session

from app.db.models import SupportTicket


def create_support_ticket(
    db: Session,
    thread_id: int,
    issue: str,
) -> SupportTicket:
    support_ticket = SupportTicket(
        thread_id=thread_id,
        issue=issue,
    )

    db.add(support_ticket)
    db.commit()
    db.refresh(support_ticket)

    return support_ticket