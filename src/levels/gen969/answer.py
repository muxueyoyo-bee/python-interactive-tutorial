def wrap_interpreter(func):
    def interpret_statement(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return interpret_statement