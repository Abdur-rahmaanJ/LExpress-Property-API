import LExpressProperty

ENGINE = LExpressProperty.Engine()
DATA = ENGINE.collect(payment = "Buy", property_type = "House", sort_by = "Least Expensive", pages = 10)
print(DATA)
