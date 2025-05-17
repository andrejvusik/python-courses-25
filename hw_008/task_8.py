# Задача 8 - преобразование в camelCase.
# Напишите рекурсивную функцию, которая преобразует ключи словаря в
# camelCase нотацию. На вход подается словарь, где все ключи - это строки.
# Пример:
# to_camel_case_keys({'user_name': 'Alice'}) -> {'userName': 'Alice'}

testing_dict = {
    "user_name": "Andrej",
    "user_surname": "Vusik",
    "user_email": "andrejvusik@gmail.com",
    "status": "married",
    "children": {"first_child_name": "Ivan", "second_child_name": "Mikhail"},
    "city_of_residence": "minsk",
}


def to_camel_case_keys(u_dict):
    new_dict = dict()

    def key_to_camel(a):
        und_s_pos = a.find("_")
        el = a[und_s_pos + 1].upper()
        x, y = und_s_pos, und_s_pos + 2
        a = a[:x] + el + a[y:]
        if "_" in a:
            a = key_to_camel(a)
        return a

    for key, value in u_dict.items():
        new_key = key.lower()
        if "_" in new_key:
            new_key = key_to_camel(new_key)
        if isinstance(value, dict):
            value = to_camel_case_keys(value)
        new_dict[new_key] = value

    return new_dict


print(to_camel_case_keys(testing_dict))
