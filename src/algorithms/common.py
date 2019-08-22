"""
Common utils
"""
from typing import List, Callable


def swap(nums: List[int], x: int, y: int):
    nums[x], nums[y] = nums[y], nums[x]


def ordered(nums: List[int]) -> bool:
    for i, _ in enumerate(nums[1:]):
        if nums[i] > nums[i + 1]:
            return False
    return True


def test_sorter(sorter: Callable):
    nums = [31, 41, 59, 26, 53, 58, 97, 93, 23]
    sorter(nums)
    assert ordered(nums)
