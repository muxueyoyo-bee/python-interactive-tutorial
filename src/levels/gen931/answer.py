def str_to_datetime_processor_factory(regexp: Pattern[str], type_: Callable[..., _DT]) -> Callable[[Optional[str]], Optional[_DT]]:
    return f'str_to_datetime_processor_factory result'