"""
Leetcode 322: Coin Change
https://leetcode.com/problems/coin-change/
"""

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    """
    - Dynamic programming problem
    - Time complexity: O(n.m) - n is the amount and m is the number of coins
        - Reduced from O(n^m) because we memoize the results
    - Space complexity: O(n)
        - The space complexity of the memoization table is O(n)
    - Approach: Dynamic programming - Memoization
        - Use a dictionary to store the minimum number of coins to reach an amount
        - The key is the amount and the value is the minimum number of coins
        - The minimum number of coins to reach an amount is the minimum of
          the minimum number of coins to reach amount - coin for each coin
    """
    def solution(amount, memo: dict = {}):
        if amount in memo:
            return memo[amount]
        res = float('inf')
        if amount == 0:
            return 0
        if amount < 0:
            return res

        for coin in coins:
            res = min(res, 1 + solution(amount - coin, memo))
        memo[amount] = res
        return res

    res = solution(amount)
    return res if res != float('inf') else -1


def coinChangeTabulation(coins: List[int], amount: int) -> int:
    """
    - Dynamic programming problem
    - Time complexity: O(n.m) - n is the amount and m is the number of coins
    - Space complexity: O(n)
        - The space complexity of the memoization table is O(n)
    - Approach: Dynamic programming - Tabulation
        - Use a table to store the minimum number of coins to reach an amount
        - The minimum number of coins to reach an amount is the minimum of
          the minimum number of coins to reach amount - coin for each coin
    """
    table = [float('inf')] * (amount + 1)
    table[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            change = coin + i
            if change <= amount:
                table[change] = min(table[change], table[i] + 1)
    min_change = table[amount]
    return min_change if min_change != float('inf') else -1
