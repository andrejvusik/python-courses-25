# Task 7.
# Implement a function merge_sorted_list that takes two sorted lists
# and returns a new sorted list containing elements from both lists.


def merge_sorted_list(list_a, list_b):
    while len(list_b):
        x = list_b.pop(0)
        for i, item in enumerate(list_a):
            if x <= item:
                list_a.insert(i, x)
                break
            elif x > list_a[-1]:
                list_a.append(x)
    return list_a


# Checking the functionality of the function

first_list = [1, 2, 3, 5, 7, 10, 11, 19, 22, 34, 36]
second_list = [1, 4, 5, 9, 11, 12, 13, 15, 22, 33, 99]

print(
    f"A sorted list containing elements from both lists: "
    f"{merge_sorted_list(first_list, second_list)}"
)
