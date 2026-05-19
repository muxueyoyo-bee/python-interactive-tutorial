class UnsetMetadataPassedError(ValueError):
    pass
class NotFittedError(ValueError, AttributeError):
    pass
class ConvergenceWarning(UserWarning):
    pass
class DataConversionWarning(UserWarning):
    pass