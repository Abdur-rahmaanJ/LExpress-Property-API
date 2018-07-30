import requests
import json
from bs4 import BeautifulSoup

class Agent():

    __requests_list__ = []

    def json(self, data):
        json_data = json.dumps(data, indent = 4)
        return json_data

    def collect(self, payment = None, property_type = None, sort_by = "Least Expensive", output = False, pages = 1):

        # Internet connection is checked.
        connection_safe = False
        try:
            server = requests.get("https://www.lexpressproperty.com/en/")
            connection_safe = True
            # Console output.
            if output is True:
                print("[Connection established]")
        except:
            # Console output.
            if output is True:
                print("[Connection Failure]")

        if connection_safe is True:

            # This variable will remain True if all parameters are valid.
            valid_request = True 

            # Parameter: payment.
            if payment is not None:
                if property_type is None:
                    if payment in ["buy", "Buy", "BUY"]:
                        __payment__ = "/buy-mauritius/all"
                    elif payment in ["rent", "Rent", "RENT"]:
                        __payment__ = "/rent-mauritius/all"
                    elif payment in ["holiday", "Holiday", "HOLIDAY"]:
                        __payment__ = "/holidays-mauritius/all"
                    else:
                        __payment__ = ""
                        valid_request = False

                        # Console output.
                        if output is True:
                            print("[Invalid parameter: payment]")
                else:
                    if payment in ["buy", "Buy", "BUY"]:
                        __payment__ = "/buy-mauritius"
                    elif payment in ["rent", "Rent", "RENT"]:
                        __payment__ = "/rent-mauritius"
                    elif payment in ["holiday", "Holiday", "HOLIDAY", "holidays", "Holidays", "HOLIDAYS"]:
                        __payment__ = "/holidays-mauritius"
                    else:
                        __payment__ = ""
                        valid_request = False

                        # Console output.
                        if output is True:
                            print("[Invalid parameter: payment]")

            # Parmeter: property_type.
            if property_type is not None:
                if payment in ["buy", "Buy", "BUY"]:
                    if property_type in ["house", "House", "HOUSE", "villa", "Villa", "VILLA"]:
                        __property_type__ = "/villa"
                    elif property_type in ["townhouse", "Townhouse", "TOWNHOUSE"]:
                        __property_type__ = "/townhouse"
                    elif property_type in ["apartment", "Apartment", "APARTMENT", "apartments", "Apartments", "APARTMENTS"]:
                        __property_type__ = "/apartment"
                    elif property_type in ["penthouse", "Penthouse", "PENTHOUSE"]:
                        __property_type__ = "/penthouse"
                    elif property_type in ["residential complex", "residential-complex", "Residential Complex", "Residential-Complex", "RESIDENTIAL COMPLEX", "RESIDENTIAL-COMPLEX"]:
                        __property_type__ = "/residential_complex"
                    elif property_type in ["residential land", "residential-land", "Residential Land", "Residential-Land", "RESIDENTIAL LAND", "RESIDENTIAL-LAND"]:
                        __property_type__ = "residential_land"
                    elif property_type in ["agricultural land", "agricultural-land", "Agricultural Land", "Agricultural-Land", "AGRICULTURAL LAND", "AGRICULTURAL-LAND"]:
                        __property_type__ = "/agricultural_land"
                    elif property_type in ["commercial land", "commercial-land", "Commercial Land", "Commercial-Land", "COMMERCIAL LAND", "COMMERCIAL-LAND"]:
                        __property_type__ = "/commercial_land"
                    elif property_type in ["office", "Office", "OFFICE", "offices", "Offices", "OFFICES"]:
                        __property_type__ = "/offices"
                    elif property_type in ["commercial space", "commerical-land", "Commercial Space", "Commercial-Space", "COMMERCIAL LAND", "COMMERCIAL-LAND"]:
                        __property_type__ = "/commercial_space"
                    elif property_type in ["building", "Buildling", "BUILDING"]:
                        __property_type__ = "/warehouse"
                    elif property_type in ["warehouse", "Warehouse", "WAREHOUSE"]:
                        __property_type__ = "/warehouse"
                    elif property_type in ["hotel resort", "hotel-resort", "Hotel Resort", "Hotel-Resort", "HOTEL RESORT", "HOTEL-RESORT"]:
                        __property_type__ = "/hotel_resort"
                    elif property_type in ["stock-in-trade", "Stock-in-trade"]:
                        __property_type__ = "/stock_in_trade"
                    else:
                        __property_type__ = ""
                        valid_request = False

                        # Console output.
                        if output is True:
                            print("[Invalid parameter: property_type]")

                if payment in ["rent", "Rent", "RENT"]:
                    if property_type in ["house", "House", "HOUSE", "villa", "Villa", "VILLA"]:
                        __property_type__ = "/villa"
                    elif property_type in ["townhouse", "Townhouse", "TOWNHOUSE"]:
                        __property_type__ = "/townhouse"
                    elif property_type in ["apartment", "Apartment", "APARTMENT", "apartments", "Apartments", "APARTMENTS"]:
                        __property_type__ = "/apartment"
                    elif property_type in ["penthouse", "Penthouse", "PENTHOUSE"]:
                        __property_type__ = "/penthouse"
                    elif property_type in ["residential complex", "residential-complex", "Residential Complex", "Residential-Complex", "RESIDENTIAL COMPLEX", "RESIDENTIAL-COMPLEX"]:
                        __property_type__ = "/residential_complex"
                    elif property_type in ["office", "Office", "OFFICE", "offices", "Offices", "OFFICES"]:
                        __property_type__ = "/offices"
                    elif property_type in ["commercial space", "commerical-land", "Commercial Space", "Commercial-Space", "COMMERCIAL LAND", "COMMERCIAL-LAND"]:
                        __property_type__ = "/commercial_space"
                    elif property_type in ["building", "Buildling", "BUILDING"]:
                        __property_type__ = "/building"
                    elif property_type in ["warehouse", "Warehouse", "WAREHOUSE"]:
                        __property_type__ = "/warehouse"
                    elif property_type in ["hotel resort", "hotel-resort", "Hotel Resort", "Hotel-Resort", "HOTEL RESORT", "HOTEL-RESORT"]:
                        __property_type__ = "/hotel_resort"
                    elif property_type in ["stock-in-trade", "Stock-in-trade"]:
                        __property_type__ = "/stock_in_trade"
                    elif property_type in ["room", "Room", "ROOM"]:
                        __property_type__ = "/room"
                    else:
                        __property_type__ = ""
                        valid_request = False

                        # Console output.
                        if output is True:
                            print("[Invalid parameter: property_type]")

                if payment in ["holiday", "Holiday", "HOLIDAY", "holidays", "Holidays", "HOLIDAYS"]:
                    if property_type in ["house", "House", "HOUSE", "villa", "Villa", "VILLA"]:
                        __property_type__ = "/villa"
                    elif property_type in ["townhouse", "Townhouse", "TOWNHOUSE"]:
                        __property_type__ = "/townhouse"
                    elif property_type in ["apartment", "Apartment", "APARTMENT", "apartments", "Apartments", "APARTMENTS"]:
                        __property_type__ = "/apartment"
                    elif property_type in ["penthouse", "Penthouse", "PENTHOUSE"]:
                        __property_type__ = "/penthouse"
                    elif property_type in ["residential complex", "residential-complex", "Residential Complex", "Residential-Complex", "RESIDENTIAL COMPLEX", "RESIDENTIAL-COMPLEX"]:
                        __property_type__ = "/residential_complex"
                    elif property_type in ["guesthouse", "Guesthouse", "GUESTHOUSE"]:
                        __property_type__ = "/guesthouse"
                    elif property_type in ["bungalow", "Bungalow", "BUNGALOW"]:
                        __property_type__ = "/bungalow"
                    else:
                        __property_type__ = ""
                        valid_request = False

                        # Console output.
                        if output is True:
                            print("[Invalid parameter: property_type]")

            # Parameter: sort_by.
            if sort_by is not None:
                if sort_by in ["least expenisve", "least-expensive", "Least Expensive", "Least-Expensive", "LEAST EXPENSIVE", "LEAST-EXPENSIVE"]:
                    __sort_by__ = "/?sort=price&l=15"
                elif sort_by in ["most expensive", "most-expensive", "Most Expensive", "Most-Expensive", "MOST EXPENSIVE", "MOST-EXPENSVIE"]:
                    __sort_by__ = "?sort=-price&l=15"
                elif sort_by in ["most recent", "most-recent", "Most Recent", "Most-Recent", "MOST RECENT", "MOST-RECENT"]:
                    __sort_by__ = "?sort=-created_at&l=15"
                elif sort_by in ["least recent", "least-recent", "Least Recent", "Least-Recent", "LEAST RECENT", "LEAST-RECENT"]:
                    __sort_by__ = "?sort=created_at&l=15"
                else:
                    __sort_by__ = ""
                    valid_request = False

                    # Console output.
                    if output is True:
                        print("[Invalid parameter: sort_by]")

            # Empty list of properties is created.
            properties_list = []

            # Different URL's are generated by the Engine for the different pages of data.
            self.__requests_list__ = []
            for iteration in range(1, (pages+1)):

                # Page number is generated.
                __page_number__ = "&p=" + str(iteration)

                # URL request is created and sent.
                if valid_request is True:
                    url_request = ("https://www.lexpressproperty.com/en" + __payment__ + __property_type__ + __sort_by__ + __page_number__)
                    self.__requests_list__.append(url_request)
                    server_response = requests.get(url_request)

                    # Console output.
                    if output is True:
                        print("[" + str(server_response) + ", " + url_request + "]")

                    # Soup is created.
                    server_response = server_response.text
                    soup = BeautifulSoup(server_response, "html.parser")

                    # The soup is parsed for relevent data.
                    for html in soup.find_all("div", {"class": "text-box"}):

                        # List for the details of property is created.
                        property_list = []
                        
                        # Title is found.
                        try:
                            __title__ = html.h2.get_text().strip()
                        # The Title will be set as None if it cannot be extracted.
                        except:
                            __title__ = None

                        # The price is found.
                        try:
                            prices = html.find("strong", {"class": "price"})
                            price_one = prices.a.get_text().strip()
                            price_two = prices.em.get_text().strip()
                            __price__ = price_one + " " + price_two
                        # The price will be set as None if it cannot be extracted.
                        except:
                            __price__ = None

                        # Link is found.
                        try:
                            __link__ = html.a["href"]
                        # The link will be set as None if it cannot be extracted.
                        except:
                            __link__ = None

                        # Location is found.
                        try:
                            __location__ = html.address.get_text().strip()
                        # The location will be set as None if it cannot be extracted.
                        except:
                            __location__ = None

                        # Description is found.
                        try:
                            __description__ = html.p.get_text().strip()
                        # The description will be set as None if it cannot be extracted.
                        except:
                            __description__ = None

                        # Features of the property are found.
                        feature_list = []
                        try:
                            features = html.find("ul", {"class": "option-list"})
                            for feature in (features.find_all("li")):
                                feature_list.append(feature.get_text().strip())
                        except:
                            pass

                        # The details of the property are added to the property_list.
                        details = {"Title" : __title__, "Price" : __price__, "Location" : __location__, "Description": __description__, "URL": __link__, "Features": feature_list}
                        properties_list.append(details)

            # Retruning list is returned.
            return properties_list
    
        else:
            properties_list = []
            return properties_list

        # Console output.
        if output is True:
            print("[Termination]")
            print("")
