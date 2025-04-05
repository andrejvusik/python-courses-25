# Task 6.
# Write a function unique_elements that takes a nested list and returns unique elements.
# Example:
# >> list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2 ,3]]]]
# >> unique_elements(list_a)
# [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]


def unique_elements(user_list, result_list=None):
    if result_list is None:
        result_list = []
    for i in user_list:
        if (type(i) != list and tuple and set) and i not in result_list:
            result_list.append(i)
        elif (type(i) != list and tuple and set) and i in result_list:
            continue
        else:
            unique_elements(i, result_list)
    return result_list


# Checking the functionality of the function

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))
