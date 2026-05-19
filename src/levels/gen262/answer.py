def make_pass_decorator(object_type: type[T], ensure: bool) -> t.Callable[[t.Callable[te.Concatenate[T, P], R]], t.Callable[P, R]]:
    return f'make_pass_decorator result'