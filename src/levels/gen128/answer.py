class HTTPException(StarletteHTTPException):
    pass
class WebSocketException(StarletteWebSocketException):
    pass
class FastAPIError(RuntimeError):
    pass
class DependencyScopeError(FastAPIError):
    pass