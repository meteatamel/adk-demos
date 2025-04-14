from greeting_agent.agent import root_agent as greeting_agent
from google_search_agent.agent import root_agent as google_search_agent
from weather_agent.agent import root_agent as weather_agent
from google.adk.agents import Agent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from google.adk.tools.agent_tool import AgentTool

from dotenv import load_dotenv
load_dotenv()

APP_NAME = "adk_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_1"

def setup_runner(agent):
    session_service = InMemorySessionService()
    session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    print(f"Session created: App='{APP_NAME}', User='{USER_ID}', Session='{SESSION_ID}'")

    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    print(f"Runner created for agent '{runner.agent.name}'.")
    return runner


def call_agent(runner, query):
  content = Content(role='user', parts=[Part(text=query)])
  events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

  final_response_text = "Agent did not produce a final response."

  for event in events:
      if event.is_final_response():
          if event.content and event.content.parts:
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate:
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          break # Stop processing events once the final response is found

  print(f"<<< Agent: {final_response_text}")


def main():

    coordinator_agent = Agent(
        name="coordinator_agent",
        model="gemini-2.0-flash",
        # instruction="Route user requests: Always start with greeting_agent, weather questions to weather_agent, "
        #             "anything else to google_search_agent.",
        # description="Main task coordinator.",
        instruction=("Ask the user which city they're travelling from and to with greeting_agent, then tell the user "
                     "the weather in the destination city using weather_agent and also a brief history of the destination"
                     "city with google_search_agent"),
        #sub_agents=[greeting_agent, google_search_agent, weather_agent]
        tools=[AgentTool(agent=greeting_agent), AgentTool(agent=google_search_agent), AgentTool(agent=weather_agent)]
    )

    runner = setup_runner(coordinator_agent)

    print("Welcome! Start chatting with the agent. Type 'exit' to end.")
    while True:
        user_input = input(">>> User: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        call_agent(runner, user_input)


if __name__ == '__main__':
    main()