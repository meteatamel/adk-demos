from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="google_search_agent",
    model="gemini-2.0-flash",
    description="Agent to answer questions about history",
    instruction="You are an expert history researcher. You always stick to the facts.",
    tools=[google_search]
)