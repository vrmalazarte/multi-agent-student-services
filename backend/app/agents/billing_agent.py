from agents import Agent
from app.models.agent_output import AgentOutput

from app.tools.billing_tools import get_student_balance

billing_agent = Agent(
    name="Billing Agent",
    model="gpt-5.5",
    output_type=AgentOutput,
    instructions="""
You help students with billing-related questions.

You can:
- check tuition balances
- answer payment questions
- explain billing information

Always use the available function tool when a student asks about their balance.

If the required information is unavailable, explain that you cannot find the student's record.

Return a structured response.

Set category to "billing".
Add useful student information to memory_updates as key-value pairs.
Only save information explicitly provided by the student.
""",
    tools=[get_student_balance],
)