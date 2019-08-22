"""
Insertion Sort
"""
from typing import List

from src.algorithms.common import swap, test_sorter


def insertion_sort(nums: List[int]):
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            swap(nums, j, j - 1)
            j -= 1


def main():
    test_sorter(insertion_sort)


if __name__ == '__main__':
    main()
