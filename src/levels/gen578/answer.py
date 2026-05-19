def select_autoescape(func):
    def autoescape(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return autoescape