"""
Dynamic programming test case
"""
import unittest

from src.dynamic_programming.fibonacci import Fibonacci


class TestDynamicTest(unittest.TestCase):
    def test_fibonacci(self):
        fib = Fibonacci(20)
        self.assertEqual(fib.get(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
