"""
Leetcode 377: Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/
"""
from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    """
    Time complexity: O(n.m) - n is the target, m is the length of nums
    Space complexity: O(n) - n is the target
    Approach:
        1. Use memoization to store the number of ways to reach a target
        2. For each number in nums, find the number of ways to reach target - num
        3. Return the number of ways to reach target
    """

    def solution(nums: List[int], target: int, memo: dict) -> int:
        if target in memo:
            return memo[target]
        if target < 0:
            return 0
        if target == 0:
            return 1
        for num in nums:
            memo[target] = memo.get(target, 0) + \
                solution(nums, target - num, memo)
        return memo[target]
    return solution(nums, target, {})
