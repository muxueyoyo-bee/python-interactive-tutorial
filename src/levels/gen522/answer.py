class UnpackException(Exception):
    pass
class BufferFull(UnpackException):
    pass
class OutOfData(UnpackException):
    pass
class FormatError(ValueError, UnpackException):
    pass