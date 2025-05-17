# Задача 3 - проверка типов параметров.
# Напишите декоратор @type_check, который проверяет, что параметры функции
# соответствуют указанным типам. Если нет - выбрасывает исключение TypeError.
# Пример:
# @type_check(int, int)
# def add(a, b):
#     …
import functools


def type_check(*types):
    def type_check_decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            for arg, t in zip(args, types):
                if not isinstance(arg, t):
                    raise TypeError(f'#Argument "{arg}" is not a "{t.__name__}".')
            result = func(*args)
            return result

        return wrapper

    return type_check_decorator


@type_check(int, int)
def test_func(a, b):
    print(a, b)


test_func(1, "a")
