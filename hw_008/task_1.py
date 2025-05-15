# Напишите декоратор @timing, который выводит на экран время выполнения
# функции в миллисекундах.
import time


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = int((end - start) * 1000)

        print(
            f'Execution time of the "{func.__name__}" function: '
            f" {run_time} milliseconds"
        )
        return result

    return wrapper


@timing
def test_function():
    time.sleep(0.966)


test_function()
