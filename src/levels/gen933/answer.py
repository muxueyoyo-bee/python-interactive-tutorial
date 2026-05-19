def cache(fn: Callable[..., _R], self, con: Connection) -> _R:
    return f'cache result'