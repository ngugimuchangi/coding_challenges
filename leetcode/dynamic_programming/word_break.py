"""
Leetcode 139: Word Break
https://leetcode.com/problems/word-break/
For try solution check `tries/word_break.py`
"""
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    - Dynamic Programming using tabulation - Decision Problem
    - Time complexity(O(m.n^2)) - where m is the length of the wordDict and
      n is the length of the string
        - n ^ 2 because we iterate over the input string and also have to check
          if the substring is in the wordDict
    - Space complexity(O(n^2)) - where n is the length of the string
        - because of the table and the substrings splicing
    - Approach:
        - Create a table of size n + 1
        - Set the first element to True - base case where the string is empty
        - Iterate over the table
            - Iterate over the wordDict
                - Check if the current element in the table is True
                    - If yes, check if the substring is in the wordDict
                        - If yes, set the next element in the table to True
        - Return the last element in the table

    """
    len_s = len(s)
    table = [False] * (len_s + 1)
    table[0] = True
    for i in range(len_s + 1):
        for word in wordDict:
            if table[i]:
                len_word = len(word)
                if s[i: i + len_word] == word:
                    table[i + len_word] = True
    return table[len_s]
