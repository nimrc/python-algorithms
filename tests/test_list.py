from unittest import TestCase

from src.data_structures.list.singly_linked_list import SinglyLinkedList
from src.data_structures.list.doubly_linked_list import DoublyLinkedList
from src.data_structures.list.queue import Queue
from src.data_structures.list.stack import Stack


class TestList(TestCase):
    def test_singly_linked_list(self):
        sl: SinglyLinkedList[int] = SinglyLinkedList()

        for i in [10, 5, 30]:
            sl.add(i)

        self.assertEqual(sl.get_size(), 3)
        self.assertTrue(sl.remove(30))
        self.assertEqual(sl.get_size(), 2)

        self.assertTrue(sl.search_node(5))
        self.assertTrue(sl.remove(5))
        self.assertFalse(sl.search_node(5))

    def test_doubly_linked_list(self):
        """
            31 <-> 41 <-> 59
        """
        dl: DoublyLinkedList[int] = DoublyLinkedList()

        self.assertEqual(dl.get_size(), 0)

        for i in [59, 31]:
            dl.lpush(i)

        self.assertEqual(dl.head.get_data(), 31)
        self.assertEqual(dl.tail.get_data(), 59)

        dl.insert_at(dl.head, 41)

        self.assertEqual(dl.get_size(), 3)
        self.assertEqual(dl.rpop(), 59)
        self.assertEqual(dl.tail.get_data(), 41)

    def test_queue(self):
        queue: Queue[int] = Queue()

        for i in [1, 3, 5]:
            queue.enqueue(i)

        self.assertEqual(queue.get_size(), 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 5)
        self.assertTrue(queue.is_empty())

    def test_stack(self):
        stack: Stack[int] = Stack()

        for i in [1, 3, 5]:
            stack.add(i)

        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.remove(), 5)
        self.assertEqual(stack.remove(), 3)
        self.assertEqual(stack.remove(), 1)
        self.assertTrue(stack.is_empty())
