# Travel Helper Evaluation

## Introduction

Let's now see how to evaluate agents and make sure they behave as you expect. 

First, read [Why Evaluate Agents](https://google.github.io/adk-docs/evaluate/) documentation page to get an overview of 
evaluations in ADK. 

You can evaluate two different aspects of an agent:

1. Final response: Evaluate the final response of the agent.
2. Trajectory and tool use: Evaluate how the agent got the response with the choice and order of the tools.

In ADK, evaluating an agent involves creating an evaluation set and measuring it with an evaluation criteria. 

An evaluation set contains multiple evaluations each representing a distinct session. Each evaluation consists of one or
more turns which include the user query, expected tool use, expected intermediate agent responses, and a reference response. 

Creating an evaluation set manually is complex but `adk web` tool can be used to convert a reference session into an 
evaluation within your evaluation set.

Once you have an evaluation set, you define an evaluation criteria to measure the performance of the agent against it.
Currently these are the available criteria:

```json
{
  "criteria": {
    "tool_trajectory_avg_score": 1.0,
    "response_match_score": 0.8
  }
}
```

Let's see how we can start evaluating some of the sub-agents. 

## Greeter Agent Evaluation

Follow [Greeter Agent Evaluation](../sub_agents/greeter/eval) to see how to evaluate the greeter agent.

## Currency Agent Evaluation

Follow [Currency Agent Evaluation](../sub_agents/currency/eval) to see how to evaluate the currency agent.

