from travel_pre_departure.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

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
    runner = setup_runner(root_agent)

    print("Welcome! Start chatting with the agent. Type 'exit' to end.")
    while True:
        user_input = input(">>> User: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        call_agent(runner, user_input)


if __name__ == '__main__':
    main()