class PipError(Exception):
    pass
class DiagnosticPipError(PipError):
    pass
class ConfigurationError(PipError):
    pass
class InstallationError(PipError):
    pass