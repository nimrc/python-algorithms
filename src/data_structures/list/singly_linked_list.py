"""
Singly Linked List
"""
from typing import TypeVar, Generic

T = TypeVar('T')


class Node:
    def __init__(self, data: T, next=None):
        self.data = data
        self.next = next

    def set_data(self, data: T):
        self.data = data

    def get_data(self) -> T:
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SinglyLinkedList(Generic[T]):
    head: Node = None
    size: int = 0

    def add(self, data: T):
        """
        Add element to list
        T=O(1)
        """
        self.head = Node(data, self.head)
        self.size += 1

    def search_node(self, data: T, remove: bool = False) -> bool:
        current = self.head
        previous = None

        while current:
            if current.data == data:
                break
            else:
                previous = current
                current = current.next

        if remove and current:
            if previous is None:
                self.head = current.next
            else:
                previous.set_next(current.next)
            self.size -= 1

        return current is not None

    def remove(self, data: T) -> bool:
        return self.search_node(data, True)

    def get_size(self) -> int:
        return self.size
