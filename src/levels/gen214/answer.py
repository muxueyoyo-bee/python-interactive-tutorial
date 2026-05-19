def SpecificEncoder(func):
    def EncodePackedField(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return EncodePackedField