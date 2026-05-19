class AmbiguityError(Exception):
    pass
class BadMigrationError(Exception):
    pass
class CircularDependencyError(Exception):
    pass
class InconsistentMigrationHistory(Exception):
    pass