# Напишите декоратор @retry, который повторяет вызов функции N раз если
# функция выбросила исключение типа E, либо исключение, которое наследуется
# от E. Число N и тип исключения должны быть параметрами декоратора. Если
# функция выбросила исключение все N раз - @retry должен пробросить его
# дальше.
# Пример:
# @retry(TypeError, n=5)
# def func():
#     …
import functools


def retry(error, n=1):
    def retry_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries_left = n
            while retries_left:
                try:
                    func_result = func(*args, **kwargs)
                    return func_result
                except error as e:
                    retries_left -= 1
                    if not retries_left:
                        raise e
            return None

        return wrapper()

    return retry_decorator


@retry(ValueError, n=5)
def new_func():
    a = int(input("Input a number: "))
    print("Your number: ", a)
