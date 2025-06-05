from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from travel_helper.sub_agents.currency.agent import root_agent as currency_agent
from travel_helper.sub_agents.google_search.agent import root_agent as google_search_agent
from travel_helper.sub_agents.greeter.agent import root_agent as greeter_agent
from travel_helper.sub_agents.weather.agent import root_agent as weather_agent
from travel_helper.sub_agents.filesystem_assistant.agent import root_agent as filesystem_assistant_agent

instruction_prompt = """
    You're an agent to provide essential pre-departure information for a traveler.

    Rules:
    - Always start the chat by explaining the traveler how you can help using the `greeter_agent`.  
    - Once you have user's input, tell the user that you're gathering information and go ahead gathering information 
      with the tools without asking for more confirmations.
    - Gather entry requirements, airport to city center, and top tourist attractions with `google_search_agent`.
    - Gather currency information with `currency_agent`.
    - Gather weather information with `weather_agent`.
    - Make sure you follow the response format below. Don't skip any section.
 """

# If running locally, you can also have file system access to save the information
instruction_prompt_for_filesystem = """
    - Once all the information is generated, ask the user if they want to save the generated travel information to a file.
    If so, use `filesystem_assistant_agent` to save the information in a file.
"""

response_format = """
    Response format:
    
    SUMMARY
    -------
    You're travelling from city1, country1 to city2,country2 with a country passport.

    ENTRY REQUIREMENTS
    ------------------
    Visa required? <Just answer with Yes/No and how many days one can stay>
    
    Entry requirements: <explain the entry requirements in more detail>

    CURRENCY
    -------
    <Find the currency1 of country1 and currency2 of country2. Calculate and display the currency rate from currency1
     to currency2. If you don't have the currency info just say: I don't have conversion rate from currency1 to currency2.>

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
    instruction=instruction_prompt + response_format,
    # If running locally, you can also have file system access to save the information
    # instruction=instruction_prompt + instruction_prompt_for_filesystem + response_format,
    tools=[
        AgentTool(agent=greeter_agent),
        AgentTool(agent=google_search_agent),
        AgentTool(agent=weather_agent),
        AgentTool(agent=currency_agent),
        AgentTool(agent=filesystem_assistant_agent)
    ]
    # sub_agents=[greeter_agent, google_search_agent, weather_agent, currency_agent]
)