from google.adk.agents import Agent
from google.adk.tools import google_search

instruction_prompt = """
    You're a researching agent. You're given a topic and your task is to use Google Search to provide a one paragraph
    summary on the topic.
"""

root_agent = Agent(
    name="google_search_agent",
    model="gemini-2.0-flash",
    description="Agent to provide a one paragraph summary on the topic asked",
    instruction=instruction_prompt,
    tools=[google_search]
)