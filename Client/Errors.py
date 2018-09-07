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
