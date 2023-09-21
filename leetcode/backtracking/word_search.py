"""
Leetcode problem 79: Word Search
https://leetcode.com/problems/word-search/
- Approach: Backtracking
- Use backtracking to find all possible paths
- Check if the path is the word
- If it is, return True
- If not, backtrack
- Analysis:
    - Time: O(n * 4^k) - n is the number of cells (row * col), k is the length of the word
    - Space: O(k) - max length of the call stack is the length of the word
NB: Word Search II in tries/word_search_ii.py
"""
from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    row_len, col_len, word_len = len(board), len(board[0]), len(word),
    res = False

    def backtrack(index, row, col):
        if index >= word_len:
            return True
        if (row < 0 or row >= row_len
            or col < 0 or col >= col_len
                or board[row][col] != word[index]):
            return False

        temp = board[row][col]
        board[row][col] = '#'
        res = (backtrack(index + 1, row, col + 1)
               or backtrack(index + 1, row, col - 1)
               or backtrack(index + 1, row - 1, col)
               or backtrack(index + 1, row + 1, col))
        board[row][col] = temp
        return res

    for r in range(row_len):
        for c in range(col_len):
            res = backtrack(0, r, c)
            if res:
                return res
    return res
