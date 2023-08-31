#!/usr/bin/env python
"""
Leetcode 704. Binary Search
https://leetcode.com/problems/binary-search/
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Binary Search
    - Time: O(log(n))
    - Space: O(1)
    - Algorithm:
        - Initialize l and r to 0 and len(nums) - 1
        - While l <= r:
            - Calculate mid
            - If nums[mid] == target, then return mid
            - If nums[mid] < target, then move to the right half of the search space
            - If nums[mid] > target, then move to the left half of the search space
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
