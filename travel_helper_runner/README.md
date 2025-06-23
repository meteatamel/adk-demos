# Travel Helper Agent Runner

## Introduction

When you create an agent in ADK, you can use `adk run` to interact with the agent from a provided CLI interface 
or `adk web` to interact with the agent from a provided Web UI. This is great for development and testing, but 
it's important to understand how you can interact with the agent programmatically. This typically involves
creating a runner with a session and the agent.

Take a look at the [main.py](main.py) for details.

> [!CAUTION]  
> Before you start, make sure to follow the [setup](../setup.md) page.

## Run

Run the agent runner with [travel_helper](../travel_helper) agent.

```shell
python main.py
```

You should be able to interact with it similar to the `adk run` CLI:

```shell
Session created: App='agent_runner', User='user_1', Session='session_1'
Runner created for agent 'travel_helper_agent'.
Welcome! Start chatting with the agent. Type 'exit' to end.
>>> User: Hi
<<< Agent: Hi there! I'm here to help you with pre-departure information for your trip. To get started, 
could you please tell me your nationality, the city you're travelling from, and the city you're travelling to?
```

You can change logging level to `DEBUG`:

```python
#logger.setLevel(logging.INFO)
logger.setLevel(logging.DEBUG)
```

And see more details on what happens under the covers:

```shell
python main.py
...
>>> User: Cyprus, traveling from London to Dubai
Warning: there are non-text parts in the response: ['function_call', 'function_call', 'function_call', 'function_call', 'function_call'],returning concatenated text result from text parts,check out the non text parts for full response from model.
[travel_helper_agent] event, final: False
  ==> func_call: google_search_agent, args: {'request': 'visa requirements for Cypriot citizens traveling to Dubai'}
  ==> func_call: currency_agent, args: {'request': 'GBP to AED'}
  ==> func_call: weather_agent, args: {'request': 'weather in Dubai'}
  ==> func_call: google_search_agent, args: {'request': 'how to get from Dubai airport to city center'}
  ==> func_call: google_search_agent, args: {'request': 'top 10 tourist attractions in Dubai'}
```
