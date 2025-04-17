# Google Search Agent

## Introduction

This agent provides some useful information to the traveler such as the entry rules to destination country, how to
get from the airport to the city center, and top tourist attractions in the destination city. It uses Google Search
as a tool.
 
Take a look at the [agent.py](agent.py) for details. It's an agent that uses Google Search as a tool. 

## Run agent - terminal

Outside the folder of the agent use `adk run`:

```shell
adk run ./google_search
```

Now you can ask about any travel topic to your agent:

```shell
user: Hi
[google_search_agent]: Hi, I'm ready to help you with your travel research. What travel topic are you interested in today?

user: I'm interested in top 10 tourist destinations in Dubai
[google_search_agent]: Dubai is a city known for its modern architecture, luxury shopping, and vibrant nightlife. Some of the top tourist destinations include the Burj Khalifa, the world's tallest building, offering breathtaking views, and the Dubai Mall, a shopping and entertainment paradise with over 1,200 shops, an aquarium, and an ice rink.

Other popular attractions include the Palm Jumeirah, a man-made island with luxury resorts; the Dubai Fountain, and the Dubai Desert, where you can experience dune bashing and traditional Arabic dinners. You may also want to visit the Al Fahidi Historical Neighbourhood to experience the traditional culture of Dubai.
```

---

Nice! Go back to [travel_helper](../../README.md) to continue building the rest of the agents.