# Travel Helper Agent - Run

There are multiple ways to test and run the root agent locally.

# Run agent - CLI

You can use `adk run` to interact with the agent from a provided CLI interface: 

```shell
adk run ./travel_helper
```

You should start getting some pre-departure travel information:

```shell
user: Hi
[travel_helper_agent]: Hi there! I'm here to provide you with essential pre-departure information for your trip. To get started, could you please tell me your nationality, the city you're travelling from, and the city you're travelling to?

user: I'm from Cyprus and I'm traveling from London to Dubai
[travel_helper_agent]: Okay, I've got your information. I will now gather the essential pre-departure details for your trip from London to Dubai. Here's the information you requested:

SUMMARY
-------
You're travelling from London, UK to Dubai, UAE with a Cypriot passport.

ENTRY REQUIREMENTS
------------------
Visa required? No, Cypriots can stay in the UAE for 90 days without a visa.
...
```

# Run agent - web

You can use `adk web` to interact with the agent from a provided Web UI

Outside the folder of the agent use `adk web`:

```shell
adk web
```

Go to `http://0.0.0.0:8080`, choose your agent from the drop-down, and start chatting with your agent:

![ADK Web UI](images/adk-webui-travel-helper.png)

# Run agent - programmatically

`adk run` and `adk web` are great for development and testing, but at some point, you need to interact with the agent
programmatically. This typically involves creating a runner with a session and the agent.

Take a look at the [travel_helper_runner](../../travel_helper_runner) for details on how you can set this up. 

---

Go back to [Travel Helper Agent](../README.md) to continue.
