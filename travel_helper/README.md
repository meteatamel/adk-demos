# Travel Helper Agent

## Introduction

Before you travel, you need to know some essential pre-departure information such as the entry rules for the country 
you're travelling to, the weather in the destination, the currency of the destination, top tourist spots and so on. 
Of course, you can search this information for every trip but that takes time and it's so old school! 

Instead, let's build a travel helper agent! This agent gathers the necessary information about the upcoming trip 
and provides essential pre-departure information you need for your trip.

Travel Helper Agent will rely on other agents to help. Follow these steps to build the sub-agents and then connect
them into a root agent:

* [Greeter Agent](#greeter-agent)
* [Google Search Agent](#google-search-agent)
* [Weather Agent](#weather-agent)
* [Currency Agent](#currency-agent)
* [Travel Helper Agent](#travel-helper-agent)

## Greeter Agent

First, we need to greet the traveler and gather the necessary information about the upcoming trip such as the nationality
of the traveler, departure and arrival cities. 

That's what this agent is for!

Go through [greeter](./sub_agents/greeter) to build the agent. 

## Google Search Agent

Next, we want to provide some useful information to the travel such as the entry rules to destination country, how to
get from the airport to the city center, and top tourist attractions in the destination city. 

Google Search is great for this kind of information and it's available as a tool to ADK.

Go through [google_search](./sub_agents/google_search) to build a Google Search agent.

## Weather Agent

TODO

## Currency Agent

TODO

## Travel Helper Agent

TODO


