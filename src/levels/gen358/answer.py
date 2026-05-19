def build_environ(scope: HTTPScope, message: ASGIReceiveEvent, body: io.BytesIO) -> Environ:
    return f'build_environ result'