def connection_memoize(func):
    def decorated(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return decorated