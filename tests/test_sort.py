import unittest

from typing import Callable

from src.algorithms.sort.bubble_sort import bubble_sort
from src.algorithms.sort.insertion_sort import insertion_sort
from src.algorithms.sort.quick_sort import quick_sort
from src.algorithms.sort.selection_sort import selection_sort


class TestSort(unittest.TestCase):
    def execute(self, sorter: Callable):
        nums = [31, 41, 59, 26, 53, 58, 97, 93, 23]
        ordered = [23, 26, 31, 41, 53, 58, 59, 93, 97]
        sorter(nums)
        self.assertEqual(nums, ordered)

    def test_bubble_sort(self):
        self.execute(bubble_sort)

    def test_insertion_sort(self):
        self.execute(insertion_sort)

    def test_quick_sort(self):
        self.execute(quick_sort)

    def test_selection_sort(self):
        self.execute(selection_sort)
