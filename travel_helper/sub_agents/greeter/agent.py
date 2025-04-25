from google.adk.agents import Agent

instruction_prompt = """
    You're the greeter agent. Your task is to greet the traveler and then find out the following travel information:
    1- The nationality of the traveler
    2- The city the traveler is travelling from
    3- The city the traveler is travelling to
"""

root_agent = Agent(
    name="greeter_agent",
    model="gemini-2.0-flash",
    description="An agent to greet the user and ask for the nationality, cities they are travelling from and to.",
    instruction=instruction_prompt
)