"""
Leetcode 53: Maximum Subarray
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

"""
from typing import List


def maxSubArray(nums: List[int]) -> int:
    """
    Approach: Kadane's algorithm
    Analysis: Time: O(n) | Space: O(1) - n is the length of nums
    """
    max_sum = float('-inf')
    curr_sum = 0
    for n in nums:
        curr_sum = max(n, curr_sum + n)
        max_sum = max(curr_sum, max_sum)
    return max_sum
