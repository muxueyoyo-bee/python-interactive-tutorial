def make_pass_decorator(func):
    def decorator(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return decorator