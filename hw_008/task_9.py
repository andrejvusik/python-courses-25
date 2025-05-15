# Задача 9 - преобразование HTML шаблонов.
# Напишите рекурсивную функцию render_template, которая заменяет
# плейсхолдеры в HTML шаблоне (структура приведена в примере) на значения
# из словаря (как render в Django).
# Пример:
# template = {
#     "tag": "div",
#     "attrs": {"class": "container"},
#     "children": [
#         {"tag": "h1", "content": "{{ title }}"},
#         {"tag": "p", "content": "{{ description }}"},
#         {
#             "tag": "ul",
#             "children": [
#                 {"tag": "li", "content": "{{ item1 }}"},
#                 {"tag": "li", "content": "{{ item2 }}"},
#             ]
#         }
#     ]
# }
# def render_template(template, context):
#   pass

template = {
    "tag": "div",
    "attrs": {"class": "container"},
    "children": [
        {"tag": "h1", "content": "{{ title }}"},
        {"tag": "p", "content": "{{ description }}"},
        {
            "tag": "ul",
            "children": [
                {"tag": "li", "content": "{{ item1 }}"},
                {"tag": "li", "content": "{{ item2 }}"},
            ],
        },
    ],
}

context = {
    "title": "Children",
    "description": "Our children",
    "item1": "Ivan",
    "item2": "Mikhail",
}


def render_template(templ, cont):
    new_template = dict()

    def replace_of_value(a):
        start = a.find("{{ ")
        end = a.find(" }}") + 3
        x = start + 3
        y = end - 3
        context_key = a[x:y]
        a = a[:start] + cont[context_key] + a[end:]
        if ("{{ " and " }}") in a:
            a = replace_of_value(a)
        return a

    for key, value in templ.items():
        if isinstance(value, str):
            if ("{{ " and " }}") in value:
                value = replace_of_value(value)
        elif isinstance(value, dict):
            value = render_template(value, cont)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                item = render_template(item, cont)
                value[i] = item
        new_template[key] = value

    return new_template


print(render_template(template, context))
