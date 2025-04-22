# Задача 2.
# Реализуйте структуру данных очередь (Queue). Очередь - это структура
# данных, коллекция, работающая по принципу "первый пришел - первым вышел"
# (FIFO - first in, first out). Это означает, что первый добавленный элемент будет
# извлечен первым.
# Детали:
# 1. Определите класс Node с атрибутами data и next.
# 2. Определите класс Queue, с атрибутами _first_node, _last_node, _size.
# 3. Queue использует Node для хранения своих элементов.
# 4. Один элемент очереди - один объект класса Node.
# 5. Объекты класса Node связаны друг с другом через атрибут next.
# 6. Реализуйте следующие методы в классе Queue:
# - __init__() для инициализации очереди.
# - enqueue(item) для добавления элемента в конец очереди.
# - dequeue() для удаления и возврата элемента из начала очереди.
# - front() для возврата элемента из начала очереди без его удаления.
# - is_empty() для проверки, пуста ли очередь.
# - size() для возврата количества элементов в очереди.
# - display() для вывода очереди от начала до конца
# Задача 4.
# Реализуйте прокол итерации для коллекций из предыдущих задач, чтобы
# можно было итерироваться по структурам данных в цикле for:
# 1. Методы __iter__ у коллекций для получения объекта-итератора
# 2. Сам объект-итератор StackIterator, QueueIterator, LinkedListIterator.
# 3. Методы __iter__, __next__ у объектов-итераторов для итерации по коллекции.


class QueueIterator:
    def __init__(self, queue):
        self.queue = queue

    def __iter__(self):
        return self

    def __next__(self):
        node = self.queue.dequeue()
        if node is not None:
            return node
        else:
            raise StopIteration


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._first_node = None
        self._last_node = None
        self._size = 0

    def enqueue(self, item):
        node = Node(item)
        if self._first_node is None:
            self._first_node = self._last_node = node
        else:
            self._last_node.next = node
            self._last_node = node
        self._size += 1

    def dequeue(self):
        if self._first_node is None:
            return None
        else:
            node = self._first_node
            self._first_node = self._first_node.next
            self._size -= 1
            return node.data

    def front(self):
        if self._first_node is None:
            return None
        else:
            return self._first_node.data

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size

    def display(self):
        if self._first_node is None:
            return
        else:
            while self.size():
                print(self.dequeue())

    def __iter__(self):
        return QueueIterator(self)


# n_queue = Queue()
# n_queue.enqueue(1)
# n_queue.enqueue(2)
# n_queue.enqueue(3)
#
# for item in n_queue:
#     print(item)
