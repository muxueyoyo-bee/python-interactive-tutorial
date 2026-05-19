class RequestException(IOError):
    pass
class InvalidJSONError(RequestException):
    pass
class HTTPError(RequestException):
    pass
class ConnectionError(RequestException):
    pass