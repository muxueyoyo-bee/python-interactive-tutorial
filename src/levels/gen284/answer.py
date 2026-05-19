def fake_traceback(exc_value: BaseException, tb: TracebackType | None, filename: str, lineno: int) -> TracebackType:
    return f'fake_traceback result'