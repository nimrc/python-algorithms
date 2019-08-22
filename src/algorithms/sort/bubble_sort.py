"""
Bubble Sort
T = O(n^2)
"""
from typing import List

from src.algorithms.common import swap, test_sorter


def bubble_sort(nums: List[int]):
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)


def main():
    test_sorter(bubble_sort)


if __name__ == '__main__':
    main()
