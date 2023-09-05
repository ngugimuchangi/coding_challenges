"""
Leetcode 88: Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""


from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    Time complexity: O(m + n)
    Space complexity: O(1)
    Algorithm:
        - Use three pointers, i, j, and k
        - i points to the last element in nums1
        - j points to the last element in nums2
        - k points to the last element in nums1 including the empty spaces
        - Compare nums1[i] and nums2[j] and place the greater element at nums1[k]
        - Decrement i, j, and k accordingly
    """
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
