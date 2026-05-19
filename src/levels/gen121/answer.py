def make_tool_searcher(func):
    def search_available_tools(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print('after call')
        return result
    return search_available_tools