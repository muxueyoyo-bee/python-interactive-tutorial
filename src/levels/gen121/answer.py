class TaskException(Exception):
    pass
class InvalidTask(TaskException):
    pass
class TaskResultDoesNotExist(TaskException):
    pass
class TaskResultMismatch(TaskException):
    pass