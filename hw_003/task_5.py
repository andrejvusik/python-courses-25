# Task 5.
# Write a cache decorator that caches the result of a function call
# (stores it in a dictionary). When the function is called again with the same
# arguments, the decorator should return the result from the cache, instead of
# calling the decorated function.

# Dictionary of function result hashes
func_cashes_dict: dict[list, int] = dict()


def cashes_dec(func):
    def wrapper(*args, **kwargs):
        kwargs_tuple = tuple(el for el in kwargs.items())
        if func_cashes_dict.get((func.__name__, args, kwargs_tuple)):
            func_result = func_cashes_dict[(func.__name__, args, kwargs_tuple)]
        else:
            func_result = func(*args, **kwargs)
            func_cashes_dict[(func.__name__, args, kwargs_tuple)] = func_result
        return func_result

    return wrapper


# Checking the functionality of the function


@cashes_dec
def a_func(x):
    a = x
    print("The a_func function was launched")
    return a


@cashes_dec
def b_func(x, y):
    b = x + y
    print("The b_func function was launched")
    return b


@cashes_dec
def c_func(x=1, y=7):
    c = x + y
    print("The c_func function was launched")
    return c


a_func(1)
b_func(1, 2)
a_func(5)
a_func(1)
b_func(7, 9)
c_func(x=2, y=4)
c_func(x=2, y=4)
