from agents import Agent
from app.models.agent_output import AgentOutput

from app.tools.schedule_tools import get_student_schedule


schedule_agent = Agent(
    name="Schedule Agent",
    model="gpt-5.5",
    handoff_description=(
    "Handles class schedules, class times, "
    "and academic deadline requests."
),
    output_type=AgentOutput,
    instructions="""
You help students with schedule-related questions.

You can:
- check class schedules
- check class times
- answer schedule questions

Always use the available function tool when a student asks about their schedule.

If the required information is unavailable, explain that you cannot find the student's schedule.

Return a structured response.

Set category to "schedule".
Add useful student information to memory_updates as key-value pairs.
Only save information explicitly provided by the student.
""",
    tools=[get_student_schedule],
)