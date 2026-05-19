def build_format_selector(func):
    def syntax_error(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return syntax_error