from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from travel_helper.agent import root_agent as travel_helper_agent

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

  response_text = ""

  for event in events:
      # You can uncomment the line below to see *all* events during execution
      #print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

      if event.is_final_response():
          if event.content and event.content.parts:
             response_text += event.content.parts[0].text
          elif event.actions and event.actions.escalate:
             response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          break # Stop processing events once the final response is found
      else:
          if event.content and event.content.parts and event.content.parts[0].text:
              response_text += event.content.parts[0].text


  print(f"<<< Agent: {response_text}")


def main():
    runner = setup_runner(travel_helper_agent)

    print("Welcome! Start chatting with the agent. Type 'exit' to end.")
    while True:
        user_input = input(">>> User: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        call_agent(runner, user_input)


if __name__ == '__main__':
    #import logging
    #logging.basicConfig(level=logging.DEBUG) #, format='%(message)s')
    main()