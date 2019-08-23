"""
Stack
Last in first out
"""
from typing import TypeVar, Generic
from src.data_structures.list.doubly_linked_list import DoublyLinkedList

T = TypeVar('T')


class Stack(Generic[T]):
    stack: DoublyLinkedList[T]

    def __init__(self):
        self.stack = DoublyLinkedList()

    def add(self, data: T):
        self.stack.lpush(data)

    def remove(self):
        return self.stack.lpop()

    def is_empty(self):
        return self.stack.is_empty()

    def get_size(self):
        return self.stack.get_size()
