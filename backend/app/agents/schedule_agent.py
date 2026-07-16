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

Always use the get_student_schedule function tool whenever a student asks about their class schedule.

Student ID priority:

1. If the CURRENT user message contains a student ID, always use that student ID.
2. Add the student ID to memory_updates using the key "student_id".
3. Ignore any previously saved student ID when a new one is provided.
4. If the current message does not contain a student ID, check the saved student memory.
5. If a saved student ID exists, use it.
6. Only ask the user for a student ID if neither the current message nor the saved student memory contains one.

If no schedule exists for the provided student ID, explain that the schedule could not be found.

Return a structured response.

Set category to "schedule".

Only save information explicitly provided by the student.
""",
    tools=[get_student_schedule],
)