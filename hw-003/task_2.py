# Task 2. Write a function that merges two dictionaries. Use recursion.
# Both dictionaries can have any level of nesting.
# Other collections can be nested: dictionaries, lists, sets, tuples.
# Example:
# >> dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
# >> dict_b = {“d”: 1, “b”: {“c”: 2, “e”: 3}}
# >> merge_dicts(dict_a, dict_b)
# >> print(dict_a)
# {“a”: 1, “b”: {“c”: 2, “e”: 3, “f”: 4}, “d”: 1}


def merge_dicts(dict_1, dict_2):
    while len(dict_2) > 0:
        el_d_2 = dict_2.popitem()
        el_dict_2 = dict([el_d_2])
        if el_d_2[0] in dict_1.keys() and (type(dict_1[el_d_2[0]]) == list):
            dict_1[el_d_2[0]].append(el_d_2[1])
        elif (el_d_2[0] in dict_1.keys()
              and (type(dict_1[el_d_2[0]]) == dict
                   and type(el_d_2[1]) == dict)):
            merge_dicts(dict_1[el_d_2[0]], el_d_2[1])
        else:
            dict_1.update(el_dict_2)


# Checking the functionality of the function

dict_a = {"a": 1, "b": {"c": 1, "f": 4}, "u": [3, 5, 7, {"e": 8}], "k": 9}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}, "u": {"e": 7, "w": 9}}
merge_dicts(dict_a, dict_b)
print(dict_a)
