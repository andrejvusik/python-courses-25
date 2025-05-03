# Задача 3.
# Реализуйте структуру данных двусвязный список (LinkedList). Двусвязный
# список - это структура данных, коллекция, состоящая из последовательности
# узлов, где каждый узел содержит ссылку на следующий узел (или None), ссылку
# на предыдущий узел (или None), данные.
# Детали:
# 1. Определите класс Node с атрибутами data, next и prev.
# 2. Определите класс LinkedList, с атрибутами _head_node, _tail_node, _size.
# 3. LinkedList использует Node для хранения своих элементов.
# 4. Один элемент списка - один объект класса Node.
# 5. Объекты класса Node связаны друг с другом через атрибуты next и prev.
# 6. Реализуйте следующие методы в классе LinkedList:
# - __init__() для инициализации списка.
# - append(item) для добавления элемента в конец списка.
# - prepend(item) для добавления элемента в начало списка.
# - insert(item, i) для добавления элемента на позицию i.
# - delete(item) для удаления первого вхождения указанного элемента.
# - find(item) для возврата узла, содержащего элемент, или None,
#   если элемент не найден.
# - display(reverse=False) для вывода списка от начала до конца,
#   если reverse=False, или от конца до начала, если True.
# - __getitem__(i) для получения элемента списка на позиции i.
# https://docs.python.org/3/reference/datamodel.html#object.__getitem__
# Задача 4.
# Реализуйте прокол итерации для коллекций из предыдущих задач, чтобы
# можно было итерироваться по структурам данных в цикле for:
# 1. Методы __iter__ у коллекций для получения объекта-итератора
# 2. Сам объект-итератор StackIterator, QueueIterator, LinkedListIterator.
# 3. Методы __iter__, __next__ у объектов-итераторов для итерации по коллекции.


class LinkedListIterator:
    def __init__(self, linked_list):
        self._linked_list = linked_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index + 1 <= self._linked_list.size():
            data = self._linked_list.__getitem__(self._index)
            self._index += 1
            return data
        else:
            raise StopIteration


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None
        self._size = 0

    def append(self, item):
        node = Node(item)
        if self._head_node is None:
            self._head_node = self._tail_node = node
        else:
            node.prev = self._tail_node
            self._tail_node.next = node
            self._tail_node = node
        self._size += 1

    def prepend(self, item):
        node = Node(item)
        if self._head_node is None:
            self._head_node = self._tail_node = node
        else:
            node.next = self._head_node
            self._head_node.prev = node
            self._head_node = node
        self._size += 1

    def insert(self, item, i):
        node = Node(item)
        if not isinstance(i, int):
            raise TypeError("Index i must be an integer")
        elif i > self._size or i < -1 * (self._size + 1):
            raise IndexError(
                f"The index of the element being inserted is outside "
                f"the bounds of a doubly linked list. "
                f'The size of the list is "{self._size}".'
            )
        else:
            if self._head_node is None:
                self._head_node = self._tail_node = node
            else:
                if i < 0:
                    i = i + self._size + 1
                if i == 0:
                    self.prepend(item)
                    return
                elif i == self._size:
                    self.append(item)
                    return
                else:
                    pointer_node = self._head_node
                    for j in range(self._size):
                        if j == i:
                            node_prev = pointer_node.prev
                            node_prev.next = node
                            node.prev = node_prev
                            node.next = pointer_node
                            pointer_node.prev = node
                            self._size += 1
                            break
                        else:
                            pointer_node = pointer_node.next

    def delete(self, item):
        if self._head_node is None:
            return
        else:
            pointer_node = self._head_node
            for _ in range(self._size):
                if pointer_node.data == item:
                    node_prev = pointer_node.prev
                    node_next = pointer_node.next
                    node_prev.next = node_next
                    node_next.prev = node_prev
                    self._size -= 1
                    break
                else:
                    pointer_node = pointer_node.next
            return

    def find(self, item):
        if self._head_node is None:
            return None
        else:
            pointer_node = self._head_node
            for _ in range(self._size):
                if pointer_node.data == item:
                    item = pointer_node.data
                    node_prev = pointer_node.prev
                    node_next = pointer_node.next
                    node_prev.next = node_next
                    if node_next is not None:
                        node_next.prev = node_prev
                    self._size -= 1
                    return item
                else:
                    pointer_node = pointer_node.next
            return None

    def display(self, reverse=False):
        if self._head_node is None:
            return None
        else:
            for _ in range(self._size):
                if reverse:
                    print(self._tail_node.data)
                    self._tail_node = self._tail_node.prev
                    self._size -= 1
                else:
                    print(self._head_node.data)
                    self._head_node = self._head_node.next
                    self._size -= 1
            return None

    def __getitem__(self, i):
        if not isinstance(i, int):
            raise TypeError("Index i must be an integer")
        elif i > (self._size - 1) or i < -1 * (self._size + 1):
            raise IndexError(
                f"The index of the element being inserted is outside "
                f"the bounds of a doubly linked list. "
                f'The size of the list is "{self._size}".'
            )
        else:
            if i < 0:
                i = i + self._size + 1
            if i == 0:
                node = self._head_node
                if node is not None:
                    return node.data
                else:
                    return None
            elif i == self._size:
                node = self._tail_node
                return node.data
            else:
                node = Node(self)
                pointer_node = self._head_node
                for j in range(self._size):
                    if j == i:
                        node = pointer_node
                        break
                    else:
                        pointer_node = pointer_node.next
                return node.data

    def size(self):
        return self._size

    def __iter__(self):
        return LinkedListIterator(self)


# new_lili = LinkedList()
#
# new_lili.append(1)
# new_lili.append(2)
# new_lili.append(3)
# new_lili.append(4)
# new_lili.append(5)
# new_lili.insert(111, 0)
#
# print("")
# print(new_lili.__getitem__(0))
# print(new_lili.__getitem__(2))
# print(new_lili.__getitem__(5))
# print("")
#
# for item in new_lili:
#     print(item)
