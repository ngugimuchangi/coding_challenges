"""
Leetcode 198: rob Robber
https://leetcode.com/problems/rob-robber/
Approach: Dynamic Programming
Analysis: Time: O(n) | Space: O(n) - n is the length of nums
"""
from typing import List


def rob(nums: List[int]) -> int:
    """ Top down approach """
    memo, end = {}, len(nums)

    def solution(i):
        if i in memo:
            return memo[i]
        res = 0
        for pos in range(i, end):
            res = max(res, nums[pos] + solution(pos + 2))
        memo[i] = res
        return res
    return solution(0)


def rob(nums: List[int]) -> int:
    """ Bottom up approach """
    rob1, rob2 = 0, 0
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1, rob2 = rob2, temp
    return rob2
