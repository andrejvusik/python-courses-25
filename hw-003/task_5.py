# Task 5.
# Write a cache decorator that caches the result of a function call
# (stores it in a dictionary). When the function is called again with the same
# arguments, the decorator should return the result from the cache, instead of
# calling the decorated function.

#Dictionary of function result hashes
func_cashes_dict = {}

def cashes_dec(func):
    def wrapper(*args, **kwargs):
        kwargs_tuple = tuple(el for el in kwargs.items())
        if func_cashes_dict.get((func.__name__, args, kwargs_tuple)):
            func_result = func_cashes_dict[(func.__name__, args, kwargs_tuple)]
        else:
            func_result = func(*args, **kwargs)
            func_cashes_dict.update({(func.__name__, args, kwargs_tuple): func_result})
        return func_result
    return wrapper


# Checking the functionality of the function

@cashes_dec
def a_fanc(x):
    a = x
    print("The a_fanc function was launched")
    return a

@cashes_dec
def b_fanc(x, y):
    b = x + y
    print("The b_fanc function was launched")
    return b

@cashes_dec
def c_fanc(x=1, y=7):
    c = x + y
    print("The c_fanc function was launched")
    return c

a_fanc(1)
b_fanc(1, 2)
a_fanc(5)
a_fanc(1)
b_fanc(7, 9)
c_fanc(x=2, y=4)
c_fanc(x=2, y=4)
