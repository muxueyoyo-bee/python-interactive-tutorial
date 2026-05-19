class ClickException(Exception):
    pass
class UsageError(ClickException):
    pass
class FileError(ClickException):
    pass