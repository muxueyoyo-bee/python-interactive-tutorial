def login_required(func):
    def wrapped_view(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return wrapped_view