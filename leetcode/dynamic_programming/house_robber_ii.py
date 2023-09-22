"""
Leetcode 213: House Robber II
https://leetcode.com/problems/house-robber-ii/
Approach: Dynamic Programming
    - Rob the first house, don't rob the last house
    - Don't rob the first house, rob the last house
    - Edge cases:
        - If there is only one house, rob it
Analysis: Time: O(n) | Space: O(1) - n is the length of nums
"""

from typing import List


def rob(nums: List[int]) -> int:
    houses = len(nums)

    def solution(start, end):
        rob1, rob2 = 0, 0
        for i in range(start, end):
            temp = max(nums[i] + rob1, rob2)
            rob1, rob2 = rob2, temp
        return rob2

    return max(nums[0], solution(0, houses - 1), solution(1, houses))
