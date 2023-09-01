#!/usr/bin/env python3
"""
Leetcode 4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    - Binary search problem
    - Time: O(log(min(m, n))) - binary search
    - Space: O(1) - constant space
    - Algorithm:
        - If the length of nums1 is greater than nums2, then swap them
        - Find the partition in nums1
        - Find the partition in nums2
        - If the left of nums1 is less than or equal to the right of nums2 and
            the left of nums2 is less than or equal to the right of nums1, then
            we have found the median
            - If the total number of elements is odd, then return the min of
              the right of nums1 and right of nums2
            - Else return the average of max of left of nums1 and left of nums2
                and min of right of nums1 and right of nums2
        - If the left of nums1 is greater than the right of nums2, then move
            the partition in nums1 to the left
        - Else move the partition in nums1 to the right
    - This forms the basis of Median of Two Sorted Arrays II
    """
    a, b = nums1, nums2
    len_a, len_b = len(a), len(b)
    n = len_a + len_b
    l, r, h = 0, len_a - 1,  n // 2

    if len_a > len_b:
        return findMedianSortedArrays(nums2, nums1)

    while True:
        end_a = l + (r - l) // 2
        end_b = h - end_a - 2

        left_a = a[end_a] if end_a >= 0 else float('-inf')
        left_b = b[end_b] if end_b >= 0 else float('-inf')
        right_a = a[end_a + 1] if end_a < len_a - 1 else float('inf')
        right_b = b[end_b + 1] if end_b < len_b - 1 else float('inf')

        if left_a <= right_b and left_b <= right_a:
            if n % 2:
                return min(right_a, right_b)
            return (max(left_a, left_b) + min(right_a, right_b)) / 2
        if left_a > right_b:
            r = end_a - 1
        else:
            l = end_a + 1
