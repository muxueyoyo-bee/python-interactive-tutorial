def default_on_error(conn: HTTPConnection, exc: Exception) -> Response:
    return f'default_on_error result'