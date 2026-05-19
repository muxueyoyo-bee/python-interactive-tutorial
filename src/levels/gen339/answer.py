class PythonVersionError(Exception):
    pass
class PythonVersionNotFoundError(PythonVersionError):
    pass
class NoCompatiblePythonVersionFoundError(PythonVersionError):
    pass
class InvalidCurrentPythonVersionError(PythonVersionError):
    pass