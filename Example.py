from LExpressProperty import Agent

AGENT = Agent()
DATA = AGENT.collect(payment = "Buy", property_type = "Apartment", sort_by = "Most Recent")
print(AGENT.json(DATA))
