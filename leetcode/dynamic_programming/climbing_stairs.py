"""
Leetcode 70: Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
Approach: Dynamic Programming
    - Recursion with memoization (top-down)
    - Or tabulation (bottom-up)
Analysis:
    - Time: O(n) - n is the number of stairs
        - Due to memoization, we only need to compute
          each subproblem once, when using recursion
    - Space: O(n) - n is the number of stairs
"""


def climbStairs(n: int) -> int:
    """ Recursion with memoization """
    def solution(n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        memo[n] = solution(n - 1, memo) + solution(n - 2, memo)
        return memo[n]
    return solution(n, {})


def climbStairsTabulation(n: int) -> int:
    """ Tabulation """
    table = [0] * (n + 1)
    table[0] = 1
    for i in range(n + 1):
        if i + 1 <= n:
            table[i + 1] += table[i]
        if i + 2 <= n:
            table[i + 2] += table[i]
    return table[n]
