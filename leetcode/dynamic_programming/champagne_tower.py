"""
Leetcode problem 799: Champagne Tower
https://leetcode.com/problems/champagne-tower/
Approach: Dynamic Programming
    - We will build the champagne tower row by row
    - We will keep track of the amount of champagne in each glass
    - For each row, we will calculate the amount of champagne that
      flows into each glass
    - We will then update the amount of champagne in each glass
    - We will repeat this process until we reach the query row
    - We will return the amount of champagne in the query glass
Analysis: Time O(n^2) | Space O(n) - n is the query row
"""


def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    prev = [poured]
    for row in range(1, query_row + 1):
        curr_row = [0] * (row + 1)
        for glass in range(row):
            extra = prev[glass] - 1
            if extra > 0:
                curr_row[glass] += (extra / 2)
                curr_row[glass + 1] += (extra / 2)
        prev = curr_row
    return min(1, prev[query_glass])
