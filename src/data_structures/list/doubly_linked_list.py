"""
Doubly Linked List
"""
from typing import TypeVar, Generic

T = TypeVar('T')


class DLNode(Generic[T]):
    def __init__(self, data: T, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def set_data(self, data: T):
        self.data = data

    def get_data(self) -> T:
        return self.data

    def set_prev(self, node):
        self.prev = node

    def set_next(self, node):
        self.next = node


class DoublyLinkedList(Generic[T]):
    head: DLNode[T] = None
    tail: DLNode[T] = None
    size: int = 0

    def lpush(self, data: T):
        self.head = DLNode(data, None, self.head)

        if self.head.next is None:
            self.tail = self.head
        else:
            self.head.next.set_prev(self.head)

        self.size += 1

    def rpush(self, data: T):
        self.tail = DLNode(data, self.tail, None)

        if self.tail.prev is None:
            self.head = self.tail
        else:
            self.tail.prev.set_next(self.tail)

        self.size += 1

    def insert_at(self, current, data: T, prev: bool = False):
        if prev is True:
            node = DLNode(data, current.prev, current)
            current.set_prev(node)
            if node.prev is not None:
                node.prev.set_next(node)
        else:
            node = DLNode(data, current, current.next)
            current.set_next(node)
            if node.next is not None:
                node.next.set_prev(node)

        self.size += 1
        return node

    def lpop(self) -> T:
        return self.remove(self.head)

    def rpop(self) -> T:
        return self.remove(self.tail)

    def remove(self, node: DLNode) -> T:
        if node is None:
            return None

        current = node

        if current.prev is not None:
            current.prev.next = node.next
        else:
            self.head = node.next

        if current.next is not None:
            current.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1

        return node.data

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size is 0
