#!/usr/bin/env python3
"""
Leetcode 81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

from typing import List


def search(self, nums: List[int], target: int) -> bool:
    """
    - Binary search problem
    - Time: O(logn) - binary search
        - Worst case: O(n) - if all the elements are the same
    - Space: O(1) - constant space
    - Algorithm:
        - Bypass duplicates
        - Find mid
        - If mid is the target, return True
        - If left is less than mid, then left to mid is sorted
            - If target is between left and mid, then search in left to mid
            - Else search in mid + 1 to right
        - Else right to mid is sorted
            - If target is between mid and right, then search in mid + 1 to right
            - Else search in left to mid
        - Repeat until left is less than or equal to right
        - Return False if not found
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        # bypass duplicates
        while l < r and nums[l] == nums[l + 1]:
            l += 1
        while l < r and nums[r] == nums[r - 1]:
            r -= 1

        m = l + (r - l) // 2
        val = nums[m]

        if val == target:
            return True
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

    return False
