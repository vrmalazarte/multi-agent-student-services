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

Before asking the user for a student ID, check the saved student memory included in the conversation context.

If the saved student memory contains a value like:

student_id: 2026001

use that student ID when calling the function tool.

Only ask the user for their student ID if no student_id exists in the saved student memory.

If the required information is unavailable, explain that you cannot find the student's schedule.

Return a structured response.

Set category to "schedule".

Only save information explicitly provided by the student.
""",
    tools=[get_student_schedule],
)