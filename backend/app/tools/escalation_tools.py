from agents import RunContextWrapper, function_tool

from app.models.run_context import RunContext
from app.services.support_ticket_service import create_support_ticket as save_support_ticket


@function_tool
def create_support_ticket(
    context: RunContextWrapper[RunContext],
    issue: str,
) -> str:
    """
    Creates a support ticket for a student.
    """

    support_ticket = save_support_ticket(
        db=context.context.db,
        thread_id=context.context.thread_id,
        issue=issue,
    )

    ticket_id = f"TICKET-{support_ticket.id}"

    return (
        f"Support ticket {ticket_id} has been created for the following issue: "
        f"{issue}"
    )