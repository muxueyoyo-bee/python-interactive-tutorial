class PydanticTypeError(PydanticErrorMixin, TypeError):
    pass
class NoneIsNotAllowedError(PydanticTypeError):
    pass
class NoneIsAllowedError(PydanticTypeError):
    pass
class NotNoneError(PydanticTypeError):
    pass