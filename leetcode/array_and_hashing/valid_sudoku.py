"""
Leetcode 36: Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/
"""

from typing import List
from collections import defaultdict


def isValidSudoku(self, board: List[List[str]]) -> bool:
    """
    Time complexity: O(n*m) - n is the number of rows, m is the number of columns
    Space complexity: O(n*m) - n is the number of rows, m is the number of columns
    Approach: Hash table
        - Use a hash table to store the numbers in each row, column, and square
        - Iterate through the board
        - If the number is '.', continue
        - Otherwise, check if the number is in the row, column, or square
        - If it is, return False
        - Otherwise, add the number to the row, column, and square
    """
    lookup = defaultdict(set)
    len_row = len(board)
    len_col = len(board[0])

    for row in range(len_row):
        for col in range(len_col):
            num = board[row][col]
            if num == '.':
                continue
            r, c, sq = f'r_{row}', f'c_{col}', f'sq_{row // 3}_{col // 3}'
            if num in lookup[r] or num in lookup[c] or num in lookup[sq]:
                return False
            lookup[r].add(num)
            lookup[c].add(num)
            lookup[sq].add(num)
    return True
