from LExpressProperty import Agent

AGENT = Agent()
REF = AGENT.collect(payment = "buy", property_type = "house", sort_by = "least expensive")
print(REF)
