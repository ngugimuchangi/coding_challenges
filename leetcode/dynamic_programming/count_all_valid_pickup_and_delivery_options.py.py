"""
Leetcode 1359: Count All Valid Pickup and Delivery Options
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
"""
MOD = 10 ** 9 + 7


def countOrders(n: int) -> int:
    """
    - Dynamic Programming - Combinatorics
    - Time Complexity: O(n)
    - Space Complexity: O(1)
    - Approach: Tabulation
        - Initialize the count to 1
        - Iterate from 2 to n + 1
            - Multiply the count by the current index, 2 * index - 1 and index
            - Mod the result by 10 ** 9 + 7
            - `2 * i - 1` because each order can pick up can go into `2 * i - 1` positions
              (minus 1 because the each the delivery can only occur after the pick up
              i.e. delivery would impossible if we place pickup at 2 * i)
            - `i` because each order can be delivered in i positions
        - Return the count
    """
    count = 1
    for i in range(2, n + 1):
        count = (count * (2 * i - 1) * i) % MOD
    return count


def countOrders(n: int, memo={}) -> int:
    """
    - Dynamic Programming - Combinatorics
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    - Approach: Memoization
        - Check if the current n is in the memo
            - If yes, return the result
        - If n is 1, return 1
        - Calculate the count by multiplying the result of the previous n by
          `(2 * n - 1) * n` (i.e. the number of ways to pick up and deliver the current order)
        - Mod the result by 10 ** 9 + 7
        - Add the result to the memo
        - Return the result
    """
    if n in memo:
        return memo[n]
    if n == 1:
        return 1

    count = (countOrders(n - 1) * (2 * n - 1) * n) % MOD
    memo[n] = count
    return count
