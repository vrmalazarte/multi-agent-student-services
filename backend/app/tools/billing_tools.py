from agents import function_tool


@function_tool
def get_student_balance(student_id: str) -> str:
    """
    Returns a student's outstanding tuition balance.
    """

    mock_balances = {
        "2026001": "₱29,350.00",
        "2026002": "₱35,550.00",
        "2026003": "₱45,850.00",
    }

    return mock_balances.get(student_id, "Student record not found.")