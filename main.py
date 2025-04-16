import asyncio
import logging
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part
from travel_helper.agent import root_agent as travel_helper_agent

from dotenv import load_dotenv
load_dotenv()

APP_NAME = "adk_tutorial_app"
USER_ID = "user_1"
SESSION_ID = "session_1"

logger = logging.getLogger(__name__)

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


async def call_agent(runner, query):
  content = Content(role='user', parts=[Part(text=query)])
  response_text = ""

  async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content):
      pretty_print_event(event)

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


def pretty_print_event(event):
    logger.debug(f"[{event.author}] event, final: {event.is_final_response()}")

    for part in event.content.parts:
        if part.text:
            logger.debug(f"  ==> text: {part.text}")
        elif part.function_call:
            func_call = part.function_call
            logger.debug(f"  ==> func_call: {func_call.name}, args: {func_call.args}")
        elif part.function_response:
            func_response = part.function_response
            logger.debug(f"  ==> func_response: {func_response.name}, response: {func_response.response}")


def setup_logger():
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


async def main():
    runner = setup_runner(travel_helper_agent)

    print("Welcome! Start chatting with the agent. Type 'exit' to end.")
    while True:
        user_input = input(">>> User: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        await call_agent(runner, user_input)


if __name__ == '__main__':
    setup_logger()
    asyncio.run(main())