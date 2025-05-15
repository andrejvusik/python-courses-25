# Задача 3 - проверка типов параметров.
# Напишите декоратор @type_check, который проверяет, что параметры функции
# соответствуют указанным типам. Если нет - выбрасывает исключение TypeError.
# Пример:
# @type_check(int, int)
# def add(a, b):
#     …


def type_check(*types):
    def type_check_decorator(func):
        def wrapper(*args):
            print(args, type(args))
            print(types, type(types))
            for i, arg in enumerate(args):
                if not isinstance(arg, types[i]):
                    raise TypeError(
                        f'#{i} argument "{arg}" is not a "{types[i].__name__}".'
                    )
            result = func(*args)
            return result

        return wrapper

    return type_check_decorator


@type_check(int, int)
def test_func(a, b):
    print(a, b)


test_func(1, "t")
