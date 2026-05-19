class EnvError(Exception):
    pass
class IncorrectEnvError(EnvError):
    pass
class EnvCommandError(EnvError):
    pass