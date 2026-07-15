from agents import Agent
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from app.agents.billing_agent import billing_agent
from app.agents.schedule_agent import schedule_agent
from app.agents.escalation_agent import escalation_agent
from app.models.agent_output import AgentOutput

triage_agent = Agent(
    name="Triage Agent",
    model="gpt-5.5",
    output_type=AgentOutput,
    instructions=f"""
{RECOMMENDED_PROMPT_PREFIX}

You are the first agent that every student talks to.

Route the student to the correct specialist.

- For tuition, payments, balances, or invoices, call the handoff to the Billing Agent.
- For class schedules, class times, or deadlines, call the handoff to the Schedule Agent.
- For account issues, technical problems, or human support, call the handoff to the Escalation Agent.
- Answer only simple general questions yourself.

Use the full conversation history to understand follow-up messages.

When a specialist is required, call the appropriate handoff tool immediately.
Do not describe, announce, or promise a handoff.
""",
    handoffs=[
        billing_agent,
        schedule_agent,
        escalation_agent,
    ],
)