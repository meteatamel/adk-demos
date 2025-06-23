# Travel Helper Agent

## Introduction

Before you travel, you need to know some essential pre-departure information such as the entry rules for the country 
you're travelling to, the weather in the destination, the currency of the destination, top tourist spots and so on. 
Of course, you can search this information for every trip but that takes time and it's so old school! 

Instead, let's build a travel helper agent! This agent gathers the necessary information about the upcoming trip 
and provides essential pre-departure information you need for your trip.

> [!CAUTION]  
> Before you start, make sure to follow the [setup](../setup.md) page.

## Build sub-agents

Travel Helper Agent will rely on sub-agents to help. 

Go through [Travel Helper Agent - sub-agents](./sub_agents) to build the sub-agents first.

## Build root agent 

Once the sub-agents are built, it's time to combine them in a root agent.

Take a look at the [agent.py](agent.py) for details. 

## Run root agent

Once the root agent is built, go through [Travel Helper Agent - Run](./docs/run_agent.md) to test and run the root agent
locally.

## Deploy root agent

ADK has a few [deployment options](https://google.github.io/adk-docs/deploy/): Vertex AI Agent Engine, Cloud Run, or self-managed. 

Go through [Travel Helper Agent - Deploy Agent](./docs/deploy_agent.md) to deploy the root agent.

## Evaluate Agents

Let's now see how to evaluate agents and make sure they behave as you expect in [Travel Helper Agent - Evaluation](./docs/evaluate_agents.md).

## Filesystem Assistant Agent with Model Context Protocol

If you're running the agent locally, you might want to save the travel information in a text file. 

Go through [Filesystem Assistant Agent with Model Context Protocol](./sub_agents/filesystem_assistant) to build an agent
to have access to the file system using a reference MCP server and ADK's MCPToolset.

