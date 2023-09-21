"""
Leetcode 51:. N-Queens
https://leetcode.com/problems/n-queens/
- Approach: Backtracking
    - Use backtracking to find all possible paths
    - Check if the path is valid
        - Check if the column is valid
        - Check if the positive diagonal is valid
        - Check if the negative diagonal is valid
    - Continue if the path is valid until we reach the end of the board
    - Backtrack if the path is not valid and try another path
- Analysis:
    - Time: O(n!) - n is the number of queens
        - We have n choices for the first queen, n - 1 choices for the
          second queen,n - 2 choices for the third queen, etc.
    - Space: O(n^2) - n is the number of queens
"""
from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    res = []
    board = [['.'] * n for _ in range(n)]
    cols, positive_diagonals, negative_diagonals = set(), set(), set()

    def backtrack(row):
        if row == n:
            res.append([''.join(r) for r in board])
        for col in range(n):
            if col in cols or row + col in positive_diagonals or row - col in negative_diagonals:
                continue
            cols.add(col)
            positive_diagonals.add(row + col)
            negative_diagonals.add(row - col)
            board[row][col] = 'Q'
            backtrack(row + 1)

            cols.remove(col)
            positive_diagonals.remove(row + col)
            negative_diagonals.remove(row - col)
            board[row][col] = '.'
    backtrack(0)
    return res
