# ADK Callbacks Demo Agent

This is a sample agent that shows different callbacks in ADK:

![Callback Flow](https://google.github.io/adk-docs/assets/callback_flow.png)

## Configure Google AI or Vertex AI

Before running the sample, create a `.env` file with your Google AI or Vertex AI information.

Here's an example for Vertex AI configuration:

```sh
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=your-google-cloud-project-id
GOOGLE_CLOUD_LOCATION=us-central1
```

## Run agent

You can flip the `test` flags in different callbacks and run the agent to see the behavior.

```sh
adk run .
```

You can skip agent execution in `before_agent_callback`:

```sh
[user]: Hi
▶ before_agent_callback
  Agent: root_agent
  Invocation ID: e-758abdd3-a990-468b-8ab1-6fdada842252
  Current State: {}
  Agent execution skipped
[root_agent]: Agent 'root_agent' execution skipped by 'before_agent_callback'.
```

You can modify the agent response in `after_agent_callback`:

```sh
Running agent root_agent, type exit to exit.
[user]: Hi
...
[root_agent]: Hello! How can I help you today?
▶ after_agent_callback
  Agent: root_agent
  Invocation ID: e-0c796cd8-7dfa-424b-8ad0-dbd5c86c384f
  Current State: {}
  Agent response modified
[root_agent]: This is additional response added by 'after_agent_callback'.
```

You can inspect the user message or skip model call in `before_model_callback`:

```sh
Running agent root_agent, type exit to exit.
[user]: Hi
...
▶ before_model_callback
  Agent: root_agent
  Invocation ID: e-89a3c5c8-ef8c-4b49-bd30-e6814e1f2f20
  Inspecting last user message: 'Hi'
  Model call skipped
[root_agent]: Model call skipped by 'before_model_callback'.
```

You can inspect or modify the model response in `after_model_callback`:

```sh
Running agent root_agent, type exit to exit.
[user]: Hi
...
▶ after_model_callback
  Agent: root_agent
  Invocation ID: e-98903f5c-c0ae-4736-ad07-14c3df23250f
  Inspecting model response: 'Hi there! How can I help you today?'
  Model response modified to be uppercase
[root_agent]: [Modified by after_model_callback] HI THERE! HOW CAN I HELP YOU TODAY?
```

You can skip the tool call or modify the tool response in `before_tool_callback`:

```sh
Running agent root_agent, type exit to exit.
[user]: Weather in London
...
▶ before_tool_callback
  Agent: root_agent
  Invocation ID: e-fb595e2f-cf62-4855-b6dd-1c1ab52cebf2
  Tool: get_weather
  Args: {'location': 'London'}
  Tool execution skipped for location London and returning tool response: The weather in London is always rainy and gloomy.
...
[root_agent]: The weather in London is always rainy and gloomy.
```

You can modify the tool response in `after_tool_callback`:

```sh
Running agent root_agent, type exit to exit.
[user]: Weather in Dubai
...
▶ after_tool_callback
  Agent: root_agent
  Invocation ID: e-64919742-9bc4-4a80-b7f2-fcfd2e6d18fd
  Tool: get_weather
  Args: {'location': 'Dubai'}
  Tool response: The weather in Dubai is sunny with a high of 75°F.
  Tool response modified for 'get_weather' to: The weather is always rainy and gloomy.
...
[root_agent]: The weather is always rainy and gloomy in Dubai.
```

## References

* [Documentation: Callbacks](https://google.github.io/adk-docs/callbacks/)