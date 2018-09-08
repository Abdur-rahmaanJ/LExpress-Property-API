from Client import LExpressProperty

AGENT = LExpressProperty.Agent()
DATA = AGENT.get(payment = "buy", property_type = "house", sort_by = "most expensive", pages = 5)
print(DATA)

