# Задача 6 - поиск файлов.
# Напишите рекурсивную функцию, которая находит все файлы с расширением
# extension. Для имитации дерева директорий используйте словарь TREE.
# Пример:
# TREE = {
#     'folder-1': ['file1.txt', 'file2.py'],
#     'folder-2': {
#         'subfolder': ['notes.txt', 'readme.md']
#     }
# }
# def find_files_by_ext(ext):
#     …
# find_files_by_ext(“txt”)

TREE = {
    "folder-1": ["file1.txt", "file2.py"],
    "folder-2": {"subfolder": ["notes.txt", "readme.md"]},
}

files_list = list()


def find_files_by_ext(files_tree: dict, ext: str):

    def check_file_ext(file_name: str):
        len_ext = len(ext)
        if file_name[-len_ext:] == ext:
            files_list.append(file_name)

    for value in files_tree.values():
        if isinstance(value, str):
            check_file_ext(value)
            continue
        elif isinstance(value, (list, tuple)):
            for el in value:
                check_file_ext(el)
            continue
        elif isinstance(value, dict):
            find_files_by_ext(value, ext)


find_files_by_ext(TREE, "txt")

print(files_list)
