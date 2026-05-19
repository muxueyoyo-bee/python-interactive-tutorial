class SphinxError(Exception):
    pass
class SphinxWarning(SphinxError):
    pass
class ApplicationError(SphinxError):
    pass
class ExtensionError(SphinxError):
    pass