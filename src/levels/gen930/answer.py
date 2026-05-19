def str_to_datetime_processor_factory(func):
    def process(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return process