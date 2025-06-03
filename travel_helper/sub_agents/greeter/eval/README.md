# Greeter Agent Evaluation

Let's see how we can evaluate the greeter agent. 

The greeter agent simply greets the traveler and gathers the necessary information about the trip. 
It doesn't use any tools, so `tool_trajectory_avg_score` does not make sense but its response can be evaluated 
with `response_match_score`. 

## Evaluation set

First, let's create a reference user session and save as an evaluation. You can create this manually but using the 
`adk web` tool is the easiest. 

Inside the [sub_agents](../../../sub_agents) folder, start the `adk web`: 

```shell
adk web
```

Select the `greeter` agent and type `Hi`. You should get a response like this: 

```shell
Hello there! Welcome!

To help me find the best travel options for you, could you please tell me:

What is your nationality?
Which city are you traveling from?
Which city are you traveling to?
```

This is actually a perfect response that we can save as an evaluation as follows:

1- Go to `Eval` tab.
2- Select `Create Evaluation Set` and give it a name `greeter`. This creates a `greeter.evalset.json` file.
3- Click on the `greeter` eval set, select `Add current session to greeter`, and give the eval case a name `case1`. 

At this point, you should have eval case `case1` added to the eval set `greeter.evalset.json`.

## Evaluation criteria

Next, define the evaluation criteria in a configuration file. In this case, we simply want to see if the response
is similar to the reference response in the eval set. Define a `test_config.json` file as follows:

```json
{
  "criteria": {
    "response_match_score": 0.8
  }
}
```

`response_match_score` metric compares the agent's response to the expected response using the ROUGE similarity metric.

You can see both files defined in the [greeter/eval](../sub_agents/greeter/eval) folder.

## Run evaluation

Time to run evaluation. 

Inside the [sub_agents](../../../sub_agents) folder:

```shell
adk eval greeter greeter/eval/greeter.evalset.json --config_file_path greeter/eval/test_config.json --print_detailed_results
```

You should get a response like this:

```shell
Using evaluation criteria: {'response_match_score': 0.8}
Running Eval: greeter:case1
Computing metrics with a total of 1 Vertex Gen AI Evaluation Service API requests.
All 1 metric requests are successfully computed.
Evaluation Took:0.621312458999455 seconds
Result: ✅ Passed

*********************************************************************
Eval Run Summary
greeter:
  Tests passed: 1
  Tests failed: 0
*********************************************************************
```