# Task 1. Write a function that takes a list and flattens it.
# Use recursion. The function should modify the passed list,
# not create a new one.
# Example:
# >> list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
# >> flatten_list(list_a)
# >> print(list_a) [1, 2, 3, 4, 5, 6, 7, 8, 9]


def flatten_list(user_list, result_list=None):
    if result_list is None:
        result_list = []
    for i in user_list:
        if not isinstance(i,(list, tuple, set)):
            result_list.append(i)
        else:
            flatten_list(i, result_list)
    user_list.clear()
    user_list += result_list



# Checking the functionality of the function

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
flatten_list(list_a)
print(list_a)
