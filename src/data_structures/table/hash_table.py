"""
Hash Table
"""
from typing import List, Dict
from functools import reduce

from src.data_structures.list.singly_linked_list import SinglyLinkedList


class HashTable:
    defaultHashTableSize = 32
    buckets: List[SinglyLinkedList]
    keys: Dict

    def __init__(self, size: int = defaultHashTableSize):
        self.buckets = [SinglyLinkedList() for _ in range(size)]
        self.keys = {}
        pass

    def set(self, key: str, val):
        idx = self.__hash(key)
        self.keys[key] = idx
        self.buckets[idx].add((key, val))

    def get(self, key: str) -> str:
        if self.contains(key):
            idx = self.__hash(key)
            curr = self.buckets[idx].head
            if curr.data[0] != key:
                curr = curr.next

            return curr.data[1] if curr is not None else None

    def delete(self, key: str):
        if self.contains(key):
            idx = self.__hash(key)
            self.buckets[idx].remove((key, idx))
            del self.keys[key]

    def contains(self, key: str) -> bool:
        return self.keys.__contains__(key)

    def get_keys(self) -> Dict:
        return self.keys

    def __hash(self, key: str) -> int:
        """
        Times33 hash
        """
        return reduce(lambda s, c: s + ord(c) * 33, key, 0) % len(self.buckets)
