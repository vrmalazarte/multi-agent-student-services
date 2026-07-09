from agents import function_tool


@function_tool
def create_support_ticket(issue: str) -> str:
    """
    Creates a support ticket for a student.
    """

    ticket_id = "TICKET-1001"

    return (
        f"Support ticket {ticket_id} has been created for the following issue: "
        f"{issue}"
    )