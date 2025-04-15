from google.adk.agents import Agent

instruction_prompt = """
    You're the greeting agent. Your task is to greet the user and then find out the following information:
    1- The nationality of the user
    2- The city the user is travelling from
    3- The city the user is travelling to
"""

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="An agent to say hi to the user and ask for the nationality, city they are travelling from and to.",
    instruction=instruction_prompt
)