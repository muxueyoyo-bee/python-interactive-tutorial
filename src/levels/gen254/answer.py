class ResolverException(Exception):
    pass
class RequirementsConflicted(ResolverException, Generic[RT, CT]):
    pass
class InconsistentCandidate(ResolverException, Generic[RT, CT]):
    pass
class ResolutionError(ResolverException):
    pass