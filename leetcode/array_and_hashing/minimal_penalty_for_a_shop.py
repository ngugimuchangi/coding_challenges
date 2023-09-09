"""
Leetcode 2483: Minimal Penalty for a Shop
https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
"""


def bestClosingTime(customers: str) -> int:
    """
    Prefix sum problem
    Time complexity: O(n)
    Space complexity: O(1)
    Approach: Prefix sum
        - Use a variable to store the penalty
        - Iterate through the customers
        - If the customer is Y, decrease the penalty by 1
        - If the customer is N, increase the penalty by 1
        - If the penalty is less than the current minimum penalty, update the
          minimum penalty and the best hour
        - Return the best hour
        - Note that the best hour is the hour after the current hour
        - For example, if the best hour is 1, the best closing time is 2
        - Space and time optimization is key to solving this problem
    """
    best_hr = 0
    # max penalty for closing early, i.e. closing at 0
    pen = max_pen = customers.count('Y')

    for i, c in enumerate(customers):
        # final penalty for closing at i, considering all customers before i
        pen = pen - 1 if c == 'Y' else pen + 1
        if pen < max_pen:
            max_pen = pen
            best_hr = i + 1
    return best_hr
