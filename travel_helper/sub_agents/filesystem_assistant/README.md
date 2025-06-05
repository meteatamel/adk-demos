# Filesystem Assistant Agent with Model Context Protocol

## Introduction

The Model Context Protocol (MCP) is an open standard to standardize how LLMs communicate with external applications,
data sources and tools. MCP servers expose tools that MCP clients consume. 

There are [reference MCP servers](https://github.com/modelcontextprotocol/servers) that one can run locally and have apps
like Claude Desktop can use as tools. For example, this [quickstart](https://modelcontextprotocol.io/quickstart/user) 
shows how to use [Filesystem MCP Server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) and 
enable Claude Desktop to access the filesystem.

ADK has a [MCPToolset](https://google.github.io/adk-docs/tools/mcp-tools/) to integrate tools from external MCP servers
into your ADK agents.   

Let's build an ADK agent to have access to the filesystem using the reference MCP Filesystem Server. We can then use 
that agent to save the travel information to a file. 

Take a look at the [agent.py](agent.py) for details. 

## Run agent - terminal

Before running the travel helper with filesystem agent: 

1- In [agent.py](agent.py), change the `TARGET_FOLDER_PATH` to a location in your system. 
2- In the root [agent.py](../../agent.py), uncomment this line to change the instruction prompt to use the filesystem agent:
   ```
   # instruction=instruction_prompt + instruction_prompt_for_filesystem + response_format,
   ```

Outside the folder of the agent use `adk run`:

```shell
adk run ./weather
```

Ask about weather for different cities:

```shell
user: How's the weather in Dubai?
[weather_agent]: For the next 7 days, the weather in Dubai will be:
* Temperature: Min temperature between 21.1-24.5°C and Max temperature between 29.4-40.9°C
* Rain: There is 0 rain
* Wind: Max wind speed between 16-29.3km/h
* UV index: Max UV index between 8.3-8.7
```

