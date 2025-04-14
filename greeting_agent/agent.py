from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Agent to say hi to the user and ask for the city they are travelling from and to.",
    instruction="You are the greeting agent. Your task is to find out the city the user travelling from and to."
)