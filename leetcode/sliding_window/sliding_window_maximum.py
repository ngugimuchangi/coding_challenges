#!/usr/bin/env python3
"""
Leetcode 239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
"""

from collections import deque


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    - Sliding window problem
    - Valid window:
        1. Has k nums
    - Goal: find the maximum of each valid window
    - Time complexity: O(n) - where n is the length of nums
    - Space complexity: O(k) - where k is the length of the window
    - Approach:
        - Initialize a deque - monotonic decreasing
        - Initialize a result list
        - Initialize a left pointer
        - Iterate over nums:
            - While the deque is not empty and the last element in the deque is less than
                the current element, pop the last element
            - Append the current element to the deque
            - If the left pointer is greater than the index of the first element in the
                deque, pop the first element
            - If the right pointer is greater than or equal to k - 1, append the first
                element in the deque to the result
            - Increment the right pointer
        - Return the result
    """
    nums_dq = deque()
    res = []
    l = 0

    for r in range(len(nums)):
        num = nums[r]
        while nums_dq and nums[nums_dq[-1]] < num:
            nums_dq.pop()
        nums_dq.append(r)
        if l > nums_dq[0]:
            nums_dq.popleft()
        if r + 1 >= k:
            res.append(nums[nums_dq[0]])
            l += 1
    return res
