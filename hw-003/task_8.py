# Task 8*.
# Implement a merge_sort function that takes an unsorted list and
# sorts it using the "merge sort" algorithm.


def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list

    first_list, second_list = (merge_sort(unsorted_list[:len(unsorted_list) // 2]),
                               merge_sort(unsorted_list[len(unsorted_list) // 2:]))

    result_list = []
    first_list_count = second_list_count = 0

    for i in range(len(unsorted_list)):
        if first_list_count < len(first_list) and second_list_count < len(second_list):
            if first_list[first_list_count] < second_list[second_list_count]:
                result_list.append(first_list[first_list_count])
                first_list_count += 1
            elif first_list[first_list_count] >= second_list[second_list_count]:
                result_list.append(second_list[second_list_count])
                second_list_count += 1
        elif first_list_count == len(first_list):
            result_list.append(second_list[second_list_count])
            second_list_count += 1
        elif second_list_count == len(second_list):
            result_list.append(first_list[first_list_count])
            first_list_count += 1

    return result_list


# Checking the functionality of the function

list_a = [14, 8, 2, 17, 5, 3, 1, 9, 6, 7, 10, 8, 9, 2, 3]

print(merge_sort(list_a))
