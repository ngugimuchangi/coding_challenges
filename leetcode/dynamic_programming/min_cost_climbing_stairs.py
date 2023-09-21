"""
Leetcode 746: Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
- Approach: Dynamic Programming
    - Recursion with memoization (top-down) or
    - tabulation (bottom-up)
- Analysis:
    - Time: O(n) - n is the number of stairs
        - Due to memoization, we only need to compute
          each subproblem once, when using recursion
    - Space: O(n) - n is the number of stairs
"""
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    """ Recursion with memoization """
    top = len(cost)
    memo = {}

    def solution(i):
        if i in memo:
            return memo[i]
        if i == top:
            return 0
        if i > top:
            return float('inf')
        memo[i] = cost[i] + min(solution(i + 1), solution(i + 2))
        return memo[i]
    solution(0)
    return min(memo[0], memo[1])


def minCostClimbingStairsTabulation(cost: List[int]) -> int:
    """ Tabulation """
    cost.append(0)
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])
