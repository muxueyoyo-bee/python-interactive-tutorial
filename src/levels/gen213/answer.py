def SpecificDecoder(func):
    def DecodePackedField(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return DecodePackedField