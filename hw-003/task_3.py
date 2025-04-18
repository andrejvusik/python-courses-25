# Task 3. Write a decorator log_calls that writes the call time, name, and
# arguments of the called function to a file. One function call is one line in the file.
# The decorator must accept the name of the file to write to as a parameter.
from datetime import datetime


def log_calls(func, log_file="log_file.txt"):
    def wrapper(*args, **kwargs):
        launch_time = datetime.now()
        func_name = func.__name__
        func_args = args
        func_kwargs = kwargs

        fh = open(log_file, "a")
        fh.write(
            f"{launch_time}. Launched function: {func_name}. Arguments: {func_args}, {func_kwargs}.\n"
        )
        fh.close()

        result = func(*args, **kwargs)

        return result

    return wrapper


# Checking the functionality of the function


@log_calls
def test_func_1(*args, **kwargs):
    print("Test 1 function.")


@log_calls
def test_func_2(*args):
    print("Test 2 function.")


@log_calls
def test_func_3(**kwargs):
    print("Test 3 function.")


test_func_1(1, 2, 5, test_1="test1")

test_func_2(3, 6, 8)

test_func_3(test_3="test3")
