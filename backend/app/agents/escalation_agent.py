from agents import Agent
from app.models.agent_output import AgentOutput

from app.tools.escalation_tools import create_support_ticket


escalation_agent = Agent(
    name="Escalation Agent",
    model="gpt-5.5",
    handoff_description=(
    "Handles account access problems, technical issues, "
    "and requests requiring human support."
),
    output_type=AgentOutput,
    instructions="""
You help students with issues that require human support.

Examples include:
- account access problems
- technical issues
- requests that cannot be answered confidently

Always use the available function tool to create a support ticket.

After creating the ticket, let the student know that their issue has been escalated.

Return a structured response.

Set category to "escalation".
Set needs_human to true.
Add useful student information to memory_updates as key-value pairs.
Only save information explicitly provided by the student.
""",
    tools=[create_support_ticket],
)