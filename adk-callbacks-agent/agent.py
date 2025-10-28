from google.adk.agents.llm_agent import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext
from google.genai.types import Content, Part
from typing import Any, Dict, Optional

# A sample agent with a dummy tool and callbacks for demonstration purposes.
# Docs: https://google.github.io/adk-docs/callbacks/


# Before Agent Callback
# Ideal for logging, pre-execution validation checks, or skipping agent execution.
def before_agent_callback(callback_context: CallbackContext) -> Optional[Content]:

    print(f"▶ before_agent_callback")
    print(f"  Agent: {callback_context.agent_name}")
    print(f"  Invocation ID: {callback_context.invocation_id}")
    print(f"  Current State: {callback_context.state.to_dict()}")

    # Return Content to skip agent execution
    test_skip = False
    if test_skip:
        print(f"  Agent skipped")
        return Content(
            parts=[
                Part(
                    text=f"Agent '{callback_context.agent_name}' skipped by 'before_agent_callback'."
                )
            ],
            role="model",  # Assign model role to the overriding response
        )

    # Allow default behavior
    return None


# After Agent Callback
# Ideal for logging, post-execution validation checks, or modifying/augmenting final response.
def after_agent_callback(callback_context: CallbackContext) -> Optional[Content]:

    print(f"▶ after_agent_callback")
    print(f"  Agent: {callback_context.agent_name}")
    print(f"  Invocation ID: {callback_context.invocation_id}")
    print(f"  Current State: {callback_context.state.to_dict()}")

    # Return Content to modify the final response
    test_modify = False
    if test_modify:
        print(f"  Agent response modified")
        return Content(
            parts=[
                Part(text=f"This is additional response added by after_agent_callback.")
            ],
            role="model",  # Assign model role to the overriding response
        )
    # Allow default behavior
    return None


# Before Model Callback
# Ideal for logging, inspection/modification of LlmRequest, or skipping model call.
def before_model_callback(
    callback_context: CallbackContext, llm_request: LlmRequest
) -> Optional[LlmResponse]:

    print(f"▶ before_model_callback")
    print(f"  Agent: {callback_context.agent_name}")
    print(f"  Invocation ID: {callback_context.invocation_id}")

    # Inspect the last user message in the request
    test_inspect = False
    if test_inspect:
        last_user_message = ""
        if llm_request.contents and llm_request.contents[-1].role == "user":
            if llm_request.contents[-1].parts:
                last_user_message = llm_request.contents[-1].parts[0].text
        print(f" Inspecting last user message: '{last_user_message}'")

    # Return LlmResponse to skip model call
    test_skip = False
    if test_skip:
        print(f"  Model call skipped")
        return LlmResponse(
            content=Content(
                parts=[
                    Part(
                        text=f"Model call skipped by 'before_model_callback' for agent '{callback_context.agent_name}'."
                    )
                ],
                role="model",  # Assign model role to the overriding response
            )
        )
    # Allow default behavior
    return None


# After Model Callback
# Ideal for logging, inspection/modification of LlmResponse.
def after_model_callback(
    callback_context: CallbackContext, llm_response: LlmResponse
) -> Optional[LlmResponse]:

    print(f"▶ after_model_callback")
    print(f"  Agent: {callback_context.agent_name}")
    print(f"  Invocation ID: {callback_context.invocation_id}")

    # Inspect the model response
    test_inspect = False
    if test_inspect:
        response_text = ""
        if llm_response.content and llm_response.content.parts:
            response_text = llm_response.content.parts[0].text
        print(f"  Inspecting model response: '{response_text}'")

    # Modify the model response
    test_modification = False
    if test_modification:
        print(f"  Model response modified to be uppercase")
        modified_response = LlmResponse(
            content=Content(
                parts=[
                    Part(
                        text=f"[Modified by after_model_callback] {llm_response.content.parts[0].text.upper()}"
                    )
                ],
                role="model",
            )
        )
        return modified_response

    # Allow default behavior
    return None


def before_tool_callback(
    tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext
) -> Optional[Dict]:

    print(f"▶ before_tool_callback")
    print(f"  Agent: {tool_context.agent_name}")
    print(f"  Invocation ID: {tool_context.invocation_id}")
    print(f"  Tool: {tool.name}")

    # Allow default behavior
    return None


def after_tool_callback(
    tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext, tool_response: Dict
) -> Optional[Dict]:

    print(f"▶ after_tool_callback")
    print(f"  Agent: {tool_context.agent_name}")
    print(f"  Invocation ID: {tool_context.invocation_id}")
    print(f"  Tool: {tool.name}")

    # Allow default behavior
    return None


def get_weather(location: str) -> str:
    return f"The weather in {location} is sunny with a high of 75°F."


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A helpful assistant for user questions.",
    instruction="Answer user questions to the best of your knowledge",
    tools=[get_weather],
    before_agent_callback=before_agent_callback,
    after_agent_callback=after_agent_callback,
    before_model_callback=before_model_callback,
    after_model_callback=after_model_callback,
    before_tool_callback=before_tool_callback,
    after_tool_callback=after_tool_callback,
)
