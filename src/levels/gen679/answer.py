def custom_pydantic_encoder(type_encoders: dict[Any, Callable[[type[Any]], Any]], obj: Any) -> Any:
    return f'custom_pydantic_encoder result'