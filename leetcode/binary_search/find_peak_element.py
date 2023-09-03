#!/usr/bin/env python3
"""
Leetcode 162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
"""
from typing import List


def findPeakElement(nums: List[int]) -> int:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    Approach: Binary search
    - If the last element is greater than the second last element, then the last element is the peak
    - Otherwise, use binary search to find the peak
        - If the mid element is greater than the element to the left and right, then the mid element is the peak
        - If the mid element is less than the element to the left, then the peak is to the left (i.e the mid is a trough)
        - Otherwise, the peak is to the right(i.e the mid is a trough or a plateau with regards to the right)
    """
    len_nums = len(nums)
    l, r = 0, len_nums - 1

    if len_nums == 1:
        return 0
    if nums[len_nums - 1] > nums[len_nums - 2]:
        return len_nums - 1

    while l <= r:
        mid = l + (r - l) // 2
        peak, left, right = nums[mid], nums[mid - 1], nums[mid + 1]
        if peak > left and peak > right:
            return mid
        if peak < left:
            r = mid - 1
        else:
            l = mid + 1
