# Travel Helper Agent - sub-agents

Go through these steps to build the sub-agents. 

## Greeter Agent

First, we need to greet the traveler and gather the necessary information about the upcoming trip such as the nationality
of the traveler, departure and arrival cities. 

That's what this agent is for!

Go through [Greeter Agent](./greeter) to build the agent. 

## Google Search Agent

Next, we want to provide some useful information to the travel such as the entry rules to destination country, how to
get from the airport to the city center, and top tourist attractions in the destination city. 

Google Search is great for this kind of information and it's available as a tool to ADK.

Go through [Google Search Agent](./google_search) to build an agent using Google Search.

## Weather Agent

It's good to know how the weather is in the destination city before you get there. You can ask this to Google Search
but it's also possible to ask Weather APIs for more precise weather information. 

You can have functions calling any API as tools in ADK.

Go through [Weather Agent](./weather) to build an agent using Weather APIs.

## Currency Agent

Another useful information to know is the currency of the destination country and the currency rate between the home
country and the destination country. That's what the currency agent is for!

Go through [Currency Agent](./currency) to build an agent using a currency API to convert between currencies.

---

Go back to [Travel Helper Agent](../README.md) to continue building the root agent.
