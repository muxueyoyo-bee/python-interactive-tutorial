class TemplateError(Exception):
    pass
class TemplateNotFound(IOError, LookupError, TemplateError):
    pass
class TemplateSyntaxError(TemplateError):
    pass
class TemplateRuntimeError(TemplateError):
    pass