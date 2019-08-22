"""
Selection Sort
T = O(n^2)
"""
from typing import List

from src.algorithms.common import swap, test_sorter


def selection_sort(nums: List[int]):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        swap(nums, i, min_idx)


def main():
    test_sorter(selection_sort)


if __name__ == '__main__':
    main()
