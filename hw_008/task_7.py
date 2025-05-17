# Задача 7 - сериализация.
# Напишите рекурсивную функцию serialize, которая сериализует произвольную
# вложенную структуру (словари, списки, строки) в строку. Аналог json.dumps(),
# но вручную.


import numbers

testing_object = {
    "folder-1": [1111, "file2.py"],
    "folder-2": {"subfolder": ["notes.txt", "readme.md"]},
    67: {"56hhh": ["notes.txt", 78]},
}


def serialize(obj):
    result_string = str()

    def serialize_str(a):
        s = "'" + str(a) + "'"
        return s

    def serialize_number(a):
        s = str(a)
        return s

    if isinstance(obj, str):
        result_string += serialize_str(obj)
    elif isinstance(obj, numbers.Number):
        result_string += serialize_number(obj)
    elif isinstance(obj, list):
        result_string += "["
        for el in obj:
            if isinstance(el, str):
                result_string += serialize_str(el)
            elif isinstance(el, numbers.Number):
                result_string += serialize_number(el)
            else:
                result_string += serialize(el)
            result_string += ", "
        result_string = result_string[:-2] + "]"
    elif isinstance(obj, dict):
        result_string += "{"
        for key, value in obj.items():
            if isinstance(key, str):
                result_string += serialize_str(key)
            elif isinstance(key, numbers.Number):
                result_string += serialize_number(key)
            result_string += ": "
            if isinstance(value, str):
                result_string += serialize_str(value)
            elif isinstance(value, numbers.Number):
                result_string += serialize_number(value)
            else:
                result_string += serialize(value)
            result_string += ", "
        result_string = result_string[:-2] + "}"

    return result_string


print(serialize(testing_object))
