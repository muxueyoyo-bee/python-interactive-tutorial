class ConsoleError(Exception):
    pass
class StyleSyntaxError(ConsoleError):
    pass
class StyleStackError(ConsoleError):
    pass
class NotRenderableError(ConsoleError):
    pass