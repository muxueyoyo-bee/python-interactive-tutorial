def generate_list_convertor(func):
    def internal_convertor(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return internal_convertor