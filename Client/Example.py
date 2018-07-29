from LExpressProperty import Agent

AGENT = Agent()
DATA = AGENT.collect(payment = "Buy", property_type = "House", sort_by = "Most Recent")
print(AGENT.json(DATA))
