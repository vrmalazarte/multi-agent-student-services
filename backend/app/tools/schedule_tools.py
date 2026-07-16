from agents import function_tool


@function_tool
def get_student_schedule(student_id: str) -> str:
    """
    Returns a student's class schedule.
    """

    mock_schedules = {
        "2026001": """
Monday
- 8:00 AM - Computer Networks
- 1:00 PM - Database Systems

Tuesday
- 9:00 AM - Software Engineering
""",

        "2026002": """
Monday
- 10:00 AM - Calculus
- 2:00 PM - Discrete Mathematics

Tuesday
- 8:00 AM - Object-Oriented Programming
""",

        "2026003": """
Monday
- 9:00 AM - Operating Systems
- 3:00 PM - Information Security

Tuesday
- 10:00 AM - Artificial Intelligence
""",
    }

    return mock_schedules.get(student_id, "Student schedule not found.")