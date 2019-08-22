import unittest

from src.algorithms.find.binary_search import (
    binary_search,
    binary_search_non_rec
)


class TestFind(unittest.TestCase):
    def test_binary_search(self):
        nums = [23, 26, 31, 41, 53, 58, 59, 93, 97]

        self.assertTrue(binary_search(nums, 53))
        self.assertFalse(binary_search(nums, 54))

        self.assertTrue(binary_search_non_rec(nums, 53))
        self.assertFalse(binary_search_non_rec(nums, 54))
