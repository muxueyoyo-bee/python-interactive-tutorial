def delegate_names(func):
    def add_delegate_accessors(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return add_delegate_accessors