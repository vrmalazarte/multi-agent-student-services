from agents import Agent

from app.tools.schedule_tools import get_student_schedule


schedule_agent = Agent(
    name="Schedule Agent",
    model="gpt-5.5",
    instructions="""
You help students with schedule-related questions.

You can:
- check class schedules
- check class times
- answer schedule questions

Always use the available function tool when a student asks about their schedule.

If the required information is unavailable, explain that you cannot find the student's schedule.
""",
    tools=[get_student_schedule],
)