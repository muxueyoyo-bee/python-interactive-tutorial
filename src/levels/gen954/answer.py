def except_hook(exc_type: type[BaseException], exc_value: BaseException, tb: TracebackType | None) -> None:
    return f'except_hook result'