import weakref


class MyObject:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


def cache(func):

    def wrap(name):
        result = func(name)

        if not hasattr(wrap, '_cache'):
            wrap._cache = weakref.WeakValueDictionary()

        wrap._cache[name] = result

        return result

    return wrap


@cache
def create_object(name):
    return MyObject(name)


