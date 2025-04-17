# Currency Agent

## Introduction

This agent provides the currency rate information for the traveler between the host country and the destination country. 
It has a function that uses a currency API to get the conversion rate. This function is used as a tool in the agent.
 
Take a look at the [agent.py](agent.py) for details. It's an agent that uses Google Search as a tool. 

## Run agent - terminal

Outside the folder of the agent use `adk run`:

```shell
adk run ./currency
```

Now you can ask to convert currencies:

```shell
user: 1 GBP to EUR
[currency_agent]: 1 British Pounds (GBP) = 1.168 Euros (EUR)
```

You don't even need to know the exact currencies. The agent can guess from city or country information:

```shell
user: currency from France to Brazil
[currency_agent]: 1 Euros (EUR) = 6.6671 Brazilian Real (BRL)
```

---

Nice! Go back to [travel_helper](../../README.md) to continue building the rest of the agents.