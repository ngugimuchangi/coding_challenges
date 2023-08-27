#!/usr/bin/env python3
"""
Leetcode 121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def maxProfit(prices: list[int]) -> int:
    """
    - Time complexity: O(n)
    - Space complexity: O(1)
    - Approach:
        - Track today and tomorrow's prices and
        - Adjust today's and tomorrow's pointer if the profit is less than max profit
        - Adjust tomorrow's pointer if profit is more than current profit and record the
            new max profit
    """
    l, r = 0, 1
    maxProfit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        else:
            l = r
        r += 1

    return maxProfit
