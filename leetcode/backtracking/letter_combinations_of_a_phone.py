"""
Leetcode 17: Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

from typing import List


def letterCombinations(digits: str) -> List[str]:
    """
    - Backtracking problem
    - Time complexity: O(3^n * 4^m) - n is the number of digits that maps to 3 letters
        and m is the number of digits that maps to 4 letters
        - This is because for each digit, we have to explore all possible
          combinations of letters that it maps to. For digits that map to
          3 letters, we have 3 choices, and for digits that map to 4 letters,
          we have 4 choices. Therefore, the total number of combinations
          is 3^n * 4^m.
    - Space complexity: O(3^n * 4^m)
    - Approach: Backtracking
        - Use a dictionary to store the mapping from digit to letters
        - Use a helper function to backtrack the possible combinations
    """
    lookup = {'2': 'abc', '3': 'def', '4': 'ghi',
              '5': 'jkl', '6': 'mno', '7': 'pqrs',
              '8': 'tuv', '9': 'wxyz'}
    res = []
    max_len = len(digits)

    def backtrack(s: str, digits: str, index: int):
        if index == max_len:
            res.append(s)
            return
        for d in lookup[digits[index]]:
            backtrack(s + d, digits, index + 1)
        return
    if digits:
        backtrack('', digits, 0)
    return res
