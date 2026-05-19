class PydanticUserError(PydanticErrorMixin, RuntimeError):
    pass
class PydanticSchemaGenerationError(PydanticUserError):
    pass
class PydanticInvalidForJsonSchema(PydanticUserError):
    pass
class PydanticForbiddenQualifier(PydanticUserError):
    pass