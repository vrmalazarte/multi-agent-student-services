from agents import Agent

from app.tools.escalation_tools import create_support_ticket


escalation_agent = Agent(
    name="Escalation Agent",
    model="gpt-5.5",
    instructions="""
You help students with issues that require human support.

Examples include:
- account access problems
- technical issues
- requests that cannot be answered confidently

Always use the available function tool to create a support ticket.

After creating the ticket, let the student know that their issue has been escalated.
""",
    tools=[create_support_ticket],
)