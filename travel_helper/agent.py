from google_search.agent import root_agent as google_search_agent
from travel_info_gather.agent import root_agent as travel_info_gather_agent
from weather.agent import root_agent as weather_agent
from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

instruction_prompt = """
    You're an agent to provide essential pre-departure information for a traveler.

    Rules:
    - Always start the chat by explaining the traveler how you can help.  
    - Get the following input from the traveler: their nationality, the city1 they're travelling from and the city2 they  
    are travelling to. 
    - Once you have the input, gather and display the following information in the response format below. 
    - Make sure you follow the response format strictly. Don't skip any section.
    
    Response format:
    
    SUMMARY
    -------
    You're travelling from city1, country1 to city2,country2 with a country passport.

    ENTRY REQUIREMENTS
    ------------------
    Visa required? <Just answer with Yes/No and how many days one can stay>
    
    Entry requirements: <explain the entry requirements in more detail>

    WEATHER
    -------
    <Display the weather in city2 today>

    AIRPORT TO CITY CENTER
    ----------------------
    <Explain how to get to the city center with public transportation or taxi>

    TOURIST ATTRACTIONS
    -------------------
    <Display top 10 tourist attractions in a plain text list format. One sentence explanation for each attraction>

    ----------------
    Enjoy your trip!
"""
root_agent = Agent(
    name="travel_helper_agent",
    model="gemini-2.0-flash",
    description="Travel helper agent to provide essential pre-departure information for a traveler",
    instruction=instruction_prompt,
    # sub_agents=[greeting_agent, google_search_agent, weather_agent]
    tools=[AgentTool(agent=travel_info_gather_agent), AgentTool(agent=google_search_agent), AgentTool(agent=weather_agent)]
)