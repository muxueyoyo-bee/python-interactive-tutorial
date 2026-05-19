def crypto_adapter(func):
    def continuation(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return continuation