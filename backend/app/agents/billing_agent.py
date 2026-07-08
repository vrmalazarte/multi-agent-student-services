from agents import Agent

from app.tools.billing_tools import get_student_balance

billing_agent = Agent(
    name="Billing Agent",
    model="gpt-5.5",
    instructions="""
You help students with billing-related questions.

You can:
- check tuition balances
- answer payment questions
- explain billing information

Always use the available function tool when a student asks about their balance.

If the required information is unavailable, explain that you cannot find the student's record.
""",
    tools=[get_student_balance],
)