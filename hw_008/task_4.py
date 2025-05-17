# Задача 4 - ограничение частоты вызовов.
# Напишите декоратор @rate_limit, который разрешает
# только X вызовов в Y секунд (например, 5 раз в 60 сек).
import functools
import time


def rate_limit(x, y):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if wrapper.start_time is None:
                wrapper.start_time = time.time()
            r_time = time.time()
            y_time = int(r_time - wrapper.start_time)
            if wrapper.retries < x:
                wrapper.retries += 1
                result = func(*args, **kwargs)
                return result
            elif wrapper.retries >= x and y_time < y:
                print(
                    f"Function is running too often. Try again in {y - y_time} seconds."
                )
                return None
            elif wrapper.retries >= x and y_time > y:
                wrapper.retries = 1
                wrapper.start_time = time.time()
                result = func(*args, **kwargs)
                return result
            return None

        wrapper.retries = 0
        wrapper.start_time = None
        return wrapper

    return decorator


@rate_limit(5, 10)
def print_hello_world():
    print("Hello World!")


def hello_world():
    while True:
        user_input = input('Press enter to continue... Or enter "Q" to exit: ')
        if user_input.lower() == "q":
            break
        else:
            print_hello_world()
            continue
    print("Bye!")


hello_world()
