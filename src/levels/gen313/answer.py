def start_response(status: str, response_headers: list[tuple[str, str]], exc_info: OptExcInfo | None) -> typing.Callable[[bytes], typing.Any]:
    return f'start_response result'