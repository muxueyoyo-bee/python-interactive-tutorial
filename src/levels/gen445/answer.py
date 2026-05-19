def allow_rasterization(func):
    def draw_wrapper(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return draw_wrapper