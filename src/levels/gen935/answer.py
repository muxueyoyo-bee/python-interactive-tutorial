def result_tuple(fields: Sequence[str], extra: Optional[Any]) -> Callable[[Iterable[Any]], Row[Unpack[TupleAny]]]:
    return f'result_tuple result'