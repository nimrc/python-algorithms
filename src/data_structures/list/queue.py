"""
Queue
First in first out
"""
from typing import TypeVar, Generic
from src.data_structures.list.doubly_linked_list import DoublyLinkedList

T = TypeVar('T')


class Queue(Generic[T]):
    queue: DoublyLinkedList[T]

    def __init__(self):
        self.queue = DoublyLinkedList()

    def enqueue(self, data: T):
        self.queue.lpush(data)

    def dequeue(self):
        return self.queue.rpop()

    def is_empty(self):
        return self.queue.is_empty()

    def get_size(self):
        return self.queue.get_size()
