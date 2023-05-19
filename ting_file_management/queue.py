from ting_file_management.abstract_queue import AbstractQueue
from ting_file_management.node import Node


class Queue(AbstractQueue):
    def __init__(self):
        self.head_value = None
        self.tail_value = None
        self.__length = 0

    def __len__(self):
        return self.__length

    def enqueue(self, value):
        last_value = Node(value)
        old_last = self.tail_value

        if (old_last):
            old_last.next = last_value
            last_value.previous = old_last
            self.tail_value = last_value
        else:
            self.head_value = last_value
            self.tail_value = last_value

        self.__length += 1

    def dequeue(self):
        old_first = self.head_value
        new_first = old_first.next
        if (self.__length > 1):
            new_first.previous = None

        self.head_value = new_first
        self.__length -= 1

        return old_first.value

    def search(self, index):
        if (index >= self.__length or index < 0):
            raise IndexError("Índice Inválido ou Inexistente")

        value = self.head_value
        while (index > 0):
            value = value.next
            index -= 1

        return value.value
