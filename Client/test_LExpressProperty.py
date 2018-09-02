from LExpressProperty import Agent

AGENT = Agent()

PAYMENT_LIST = ["Buy", "Rent", "Holiday"]

PROPERTY_LIST = ["House", "Townhouse", "Apartment",
                 "Penthouse", "Residential Complex",
                 "Residential Land", "Agricultural Land",
                 "Commercial Land", "Offices", "Commercial Space",
                 "Building", "Warehouse", "Hotel Resort",
                 "Stock-in-trade", "Room", "Guesthouse",
                 "Bungalow"]

SORT_LIST = ["Most Recent", "Least Recent", "Most Expensive",
             "Least Expensive"]

for PAYMENT in PAYMENT_LIST:
    for PROPERTY in PROPERTY_LIST:
        for SORT in SORT_LIST:
            AGENT.collect(payment = PAYMENT, property_type = PROPERTY, sort_by = SORT, output = False)
            print("LExpressProperty.Agent.collect(" + "payment = " + PAYMENT + ", property_type = " + PROPERTY + ", sort_by = " + SORT + ")" + " [✔]")
