from google.adk.agents import Agent
from google.adk.tools import google_search
from ...libs import constants

instruction_prompt = """
    You're a travel researching agent. You're given a travel topic and your task is to use Google Search to provide 
    a 1-2 paragraph summary on the topic. 
"""

root_agent = Agent(
    name="google_search_agent",
    model=constants.MODEL,
    description="Agent to search and provide a summary on a given travel topic",
    instruction=instruction_prompt,
    tools=[google_search]
)