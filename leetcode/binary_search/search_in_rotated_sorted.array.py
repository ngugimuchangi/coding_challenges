#!/usr/bin/env python3
"""
Leetcode: 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + (r - l) // 2
        val = nums[m]

        if val == target:
            return m
        if nums[l] <= val:
            if target > val or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < val or target > nums[r]:
                r = m - 1
            else:
                l = m + 1

    return -1
