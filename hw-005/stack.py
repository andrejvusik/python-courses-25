# Задача 1.
# Реализуйте структуру данных стек (Stack). Стек - это структура данных,
# коллекция, работающая по принципу "последним пришел - первым вышел"
# (LIFO - last in, first out). Это означает, что последний добавленный элемент
# будет извлечен из первым.
# Детали:
# 1. Определите класс Node с атрибутами data и next.
# 2. Определите класс Stack c атрибутами _top_node и _size
# 3. Stack использует Node для хранения своих элементов.
# 4. Один элемент стека - один объект класса Node.
# 5. Объекты класса Node связаны друг с другом через атрибут next.
# 6. Реализуйте следующие методы в классе Stack:
# - __init__() для инициализации стека.
# - push(item) для добавления элемента в верхнюю часть стека.
# - pop() для удаления и возврата верхнего элемента стека.
# - peek() для возврата верхнего элемента без его удаления.
# - is_empty() для проверки, пуст ли стек.
# - size() для возврата количества элементов в стеке.
# - display() для вывода стека от начала до конца
# Задача 4.
# Реализуйте прокол итерации для коллекций из предыдущих задач, чтобы
# можно было итерироваться по структурам данных в цикле for:
# 1. Методы __iter__ у коллекций для получения объекта-итератора
# 2. Сам объект-итератор StackIterator, QueueIterator, LinkedListIterator.
# 3. Методы __iter__, __next__ у объектов-итераторов для итерации по коллекции.


class StackIterator:
    def __init__(self, stack):
        self.stack = stack

    def __iter__(self):
        return self

    def __next__(self):
        node = self.stack.pop()
        if node is not None:
            return node
        else:
            raise StopIteration


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self._top_node = None
        self._size = 0

    def push(self, item):
        node = Node(item)
        node.next = self._top_node
        self._top_node = node
        self._size += 1

    def pop(self):
        if self._top_node is None:
            return None
        else:
            node = self._top_node
            self._top_node = self._top_node.next
            self._size -= 1
            return node.data

    def peek(self):
        if self._top_node is None:
            return None
        else:
            return self._top_node.data

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def display(self):
        if self._top_node is None:
            return
        else:
            while self._size:
                print(self.pop())

    def __iter__(self):
        return StackIterator(self)


# n_stack = Stack()
# n_stack.push(1)
# n_stack.push(2)
# n_stack.push(3)
#
# for item in n_stack:
#     print(item)
