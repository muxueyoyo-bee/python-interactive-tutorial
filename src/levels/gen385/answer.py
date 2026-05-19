def make_encoded_write(func):
    def encoded_write(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return encoded_write