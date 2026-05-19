def to_streamed_response_wrapper(func):
    def wrapped(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return wrapped