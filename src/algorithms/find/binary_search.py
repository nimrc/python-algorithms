"""
Binary Search
"""
from typing import List
from math import floor


def binary_search(nums: List[int], need: int) -> bool:
    """
    Binary search
    """
    length = len(nums)
    if length == 1:
        return nums[0] == need

    pivot = floor(length / 2)

    if nums[pivot] > need:
        return binary_search(nums[0:pivot], need)
    elif nums[pivot] < need:
        return binary_search(nums[pivot:], need)
    else:
        return True


def binary_search_non_rec(nums: List[int], need: int) -> bool:
    """
    Binary search non-recursion version
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = floor(left + (right - left + 1) / 2)
        if nums[mid] > need:
            right = mid - 1
        else:
            left = mid

    return nums[left] == need


def main():
    nums = [23, 26, 31, 41, 53, 58, 59, 93, 97]
    assert binary_search(nums, 53) is True
    assert binary_search_non_rec(nums, 53) is True


if __name__ == '__main__':
    main()
