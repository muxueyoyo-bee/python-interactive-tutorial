class RequestError(YoutubeDLError):
    pass
class UnsupportedRequest(RequestError):
    pass
class NoSupportingHandlers(RequestError):
    pass
class TransportError(RequestError):
    pass