#!/usr/bin/env python3
"""
Leetcode: 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    """
    - Binary search problem
    - Time: O(logn) - binary search
    - Space: O(1) - constant space
    - Algorithm:
        - Find mid
        - If mid is the target, return mid
        - If left is less than mid, then left to mid is sorted
            - If target is between left and mid, then search in left to mid
            - Else search in mid + 1 to right
        - Else right to mid is sorted
            - If target is between mid and right, then search in mid + 1 to right
            - Else search in left to mid
    - This forms the basis of Search in Rotated Sorted Array II
    """
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
