

class LazyMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases):
        a = 1
        return {}

    def __call__(cls, expression, *args, **kwargs):
        expression_result = expression()

        # Пересоздадим класс при вызове отнаследуя от результата expression
        cls_instance = LazyMeta.__new__(
            LazyMeta,
            cls.__name__,
            (type(expression_result),),
            {expression.__name__: expression},

        )

        # Активируем базовый call
        instance = super().__call__(cls_instance, expression, expression_result, *args, **kwargs)

        return instance

    def __new__(mcs, cls_name, bases, classdict):
        cls_instance = super().__new__(mcs, cls_name, bases, classdict)

        return cls_instance


class Lazy(metaclass=LazyMeta):

    def __new__(cls, cls_instance, expression, expression_result, *args):
        res = cls_instance.__new__(
            cls_instance,
            expression_result,
            *args,
        )
        return res

    def __init__(self, expression, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        object.__setattr__(self, 'expression', expression)
