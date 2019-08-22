"""
Fibonacci sequence problem
"""
from typing import List


class Fibonacci:
    fib_seq: List[int]

    def __init__(self, n: int):
        self.fib_seq = []

        if n > 2:
            self.fib_seq.append(0)
            self.fib_seq.append(1)
            for i in range(2, n + 1):
                self.fib_seq.append(self.fib_seq[i - 1] + self.fib_seq[i - 2])

    def get(self, sequence_no: int) -> List[int]:
        if 0 < sequence_no < len(self.fib_seq):
            return self.fib_seq[:sequence_no + 1]
        return []
