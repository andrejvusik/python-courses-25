# Задача 5 - предупреждение о медленных функциях.
# Напишите декоратор @warn_if_slow, который выводит предупреждение,
# если выполнение функции занимает больше, чем X секунд.
# Пример:
# def warn_if_slow(threshold=1.0):
#     …
# @warn_if_slow
# def very_slow_function():
#     time.sleep(10)
import functools
import threading
import time


def warn_if_slow(threshold=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            def timer_print(func_name, interval):
                print(
                    f"The function {func_name} takes longer than "
                    f"{interval} seconds to execute."
                )

            slow_timer = threading.Timer(
                threshold, timer_print, (func.__name__, threshold)
            )
            slow_timer.start()
            result = func(*args, **kwargs)
            slow_timer.cancel()
            return result

        return wrapper

    return decorator


@warn_if_slow(threshold=3.0)
def very_slow_function():
    time.sleep(4)
    print("Ready!")


very_slow_function()
