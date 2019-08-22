"""
Quick Sort
"""
from typing import List

from src.algorithms.common import swap, test_sorter


def sort(nums: List[int], low: int, high: int):
    if high <= low:
        return

    pivot = partition(nums, low, high)

    sort(nums, low, pivot - 1)
    sort(nums, pivot + 1, high)


def partition(nums: List[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            swap(nums, i, j)
    swap(nums, i + 1, high)
    return i + 1


def quick_sort(nums: List[int]):
    sort(nums, 0, len(nums) - 1)


def main():
    test_sorter(quick_sort)


if __name__ == '__main__':
    main()
