#!/usr/bin/env python3
"""
Leetcode 153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

from typing import List


def findMin(nums: List[int]) -> int:
    """
    - Binary search problem
    - Time: O(log(n)) - n is the number of elements in the search space == len(nums)
    - Space: O(1)
    - Algorithm:
        - Initialize l and r to 0 and len(nums) - 1
        - While l <= r:
            - Calculate mid
            - if number at mid is less than the last number in the array, then move to the
              left half of the search space, i.e, the minimum is in the left half
            - else move to the right half of the search space, i.e, the minimum is in the
              right half
    """

    l, r = 0, len(nums) - 1
    res = float('inf')

    while l <= r:
        m = l + (r - l) // 2
        val = nums[m]
        res = min(res, val)
        if val < nums[-1]:
            r = m - 1
        else:
            l = m + 1
    return res
