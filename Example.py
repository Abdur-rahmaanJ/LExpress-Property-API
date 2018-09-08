from Client import LExpressProperty

AGENT = LExpressProperty.Agent()
DATA = AGENT.get(payment = "rent", property_type = "room", sort_by = "least expensive", pages = 1)
print(DATA)
