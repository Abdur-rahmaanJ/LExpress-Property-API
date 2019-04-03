from bs4 import BeautifulSoup
import requests

class Agent():
    """The main class of the LExpressProperty API."""

    requests_list = []

    def check_connection(self):
        """The internet connection to https://www.lexpressproperty.com/en/ is checked.
           Returns True if connection is successful, returns False if connection is unsuccessful."""

        try:
            server = requests.get("https://www.lexpressproperty.com/en/")
            return True
        except:
            return False

    def create_request(self, payment, property_type, sort_by):
        """A URL request is created based on the parameters payment, property_type and sort_by using
           the request_spec dictionary which translates the given parameters into a valid url request.
           Request_spec is continiously looped over until the correct key and appropriate url_segment
           are found."""

        request_spec = {
                        "buy": {"house": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/villa"},
                                "townhouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/townhouse"},
                                "apartment": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/apartment"},
                                "penthouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/penthouse"},
                                "residential complex": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/residential_complex"},
                                "residential land": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/residential_land"},
                                "agricultural land": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/agricultural_land"},
                                "commercial land": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/commercial_land"},
                                "office": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/offices"},
                                "commercial space": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/commercial_space"},
                                "warehouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/warehouse"},
                                "hotel_resort": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/hotel_resort"},
                                "stock-in-trade": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/stock_in_trade"},
                                "url_segment": "/buy-mauritius"},

                        "rent": {"house": {"most expensive": "?sort=-price&l=15", "url_segment": "/villa"},
                                 "townhouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/townhouse"},
                                 "apartment": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/apartment"},
                                 "penthouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/penthouse"},
                                 "residential complex": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/residential_complex"},
                                 "office": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/offices"},
                                 "commercial space": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/commercial_space"},
                                 "warehouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/warehouse"},
                                 "building": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/building"},
                                 "hotel_resort": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/hotel_resort"},
                                 "stock-in-trade": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/stock_in_trade"},
                                 "room": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/room"},
                                 "url_segment": "/rent-mauritius/all"},

                        "holiday": {"house": {"most expensive": "?sort=-price&l=15", "url_segment": "/villa"},
                                    "townhouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/townhouse"},
                                    "apartment": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/apartment"},
                                    "penthouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/penthouse"},
                                    "residential complex": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/residential_complex"},
                                    "guesthouse": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/guesthouse"},
                                    "bungalow": {"most expensive": "?sort=-price&l=15", "least expensive": "/?sort=price&l=15", "most recent": "?sort=-created_at&l=15", "least recent": "?sort=created_at&l=15", "url_segment": "/bungalow"},
                                    "url_segment": "/holidays-mauritius/all"}
                        }

        __payment__ = None
        __property_type__ = None
        __sort_by__ = None

        for payment_key in request_spec:
            if payment == payment_key:
                __payment__ = request_spec[payment]["url_segment"]
                for property_key in request_spec[payment]:
                    if property_type == property_key:
                        __property_type__ = request_spec[payment][property_type]["url_segment"]
                        for sort_by_key in request_spec[payment][property_type]:
                            if sort_by == sort_by_key:
                                __sort_by__ = request_spec[payment][property_type][sort_by]

        if __payment__ is None or __property_type__ is None or __sort_by__ is None:
            url_request = None
        else:
            url_request = "https://www.lexpressproperty.com/en" + __payment__ + __property_type__ + __sort_by__
        return url_request

    def extract_html(self, url_request, page_number):
        """Pulls all the relevent HTML from the given L'Express Property page."""

        page_request = url_request + page_number
        self.requests_list.append(page_request)
        server_response = requests.get(page_request).text
        soup = BeautifulSoup(server_response, "html.parser")
        html = soup.find_all("div", {"class": "text-box"})
        return html

    def parse(self, url_request, pages):
        """Parses the HTML returned from the given url_request, attempts to find real estate references
           and their specifics."""

        """Empty list of properties is created."""
        properties_list = []

        """Different URL's are generated by the Engine for the different pages of data."""
        self.__requests_list__ = []
        for iteration in range(1, (pages+1)):

            """Page number is generated."""
            page_number = "&p=" + str(iteration)

            """The soup is parsed for relevent data."""
            for html in self.extract_html(url_request, page_number):

                property_list = []

                try:
                    __title__ = html.h2.get_text().strip()
                except:
                    __title__ = None

                try:
                    prices = html.find("strong", {"class": "price"})
                    __price__ = "{} {}".format(prices.a.get_text().strip(), prices.em.get_text().strip())
                except:
                    __price__ = None

                try:
                    __link__ = html.a["href"]
                except:
                    __link__ = None

                try:
                    __location__ = html.address.get_text().strip()
                except:
                    __location__ = None

                try:
                    __description__ = html.p.get_text().strip()
                except:
                    __description__ = None

                feature_list = []
                try:
                    features = html.find("ul", {"class": "option-list"})
                    for feature in (features.find_all("li")):
                        feature_list.append(feature.get_text().strip())
                except:
                    pass

                details = {"Title" : __title__, "Price" : __price__, "Location" : __location__, "Description": __description__, "URL": __link__, "Features": feature_list}
                properties_list.append(details)

        return properties_list

    def get(self, payment = None, property_type = None, sort_by = "least expensive", pages = 1):
        """Collects and returns a list of real estate references in Mauritius based on the given parameters
           payment, property_type, sort_by and pages."""

        if self.check_connection() is True:
            url_request = self.create_request(payment, property_type, sort_by)
            if url_request is not None:
                results = self.parse(url_request, pages)
                return results
            else:
                raise IncorrectParameters("Please check your arguments for Agent.get()")
        else:
            raise ConnectionError("Please check your internet connection.")

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ConnectionError(Error):
    """Error message for a connection failure."""

    def __init__(self, message):
        self.message = message

class IncorrectParameters(Error):
    """Error message for incorrect arguments for Agent.get()"""

    def __init__(self, message):
        self.message = message
