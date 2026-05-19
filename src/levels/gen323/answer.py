class HTTPError(Exception):
    pass
class PoolError(HTTPError):
    pass
class SSLError(HTTPError):
    pass
class ProxyError(HTTPError):
    pass