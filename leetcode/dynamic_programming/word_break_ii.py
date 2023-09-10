"""
Leetcode 140: Word Break II
https://leetcode.com/problems/word-break-ii/
"""
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    """
    - Dynamic Programming - Combinatorics
    - Time Complexity: O(m^n) where n is the length of the string and m is
      the length of the wordDict
      - We have to go through all the combinations of the words in the dictionary
    - Space Complexity: O(m^n) where n is the length of the string.
    - Approach: Tabulation
        - Create a table of size n + 1
        - Initialize the first element to an empty list
        - For each index in the table, check if the substring from the current index
            to the end of the string is in the wordDict
            - If yes, append the current word to the list of combinations
        - Return the last element in the table
    """
    len_s = len(s)
    table = [[] for _ in range(len_s + 1)]
    table[0] = ['']

    for i in range(len_s + 1):
        for word in wordDict:
            len_word = len(word)
            if s[i: i + len_word] == word:
                combinations = [f'{s} {word}' if s else word for s in table[i]]
                table[i + len_word] += combinations

    return table[len_s]


def wordBreakTwo(s: str, wordDict: List[str]) -> List[str]:
    """
    - Dynamic Programming - Combinatorics
    - Time Complexity: O(m^n) where n is the length of the string and m is
    the length of the wordDict
    - We have to go through all the combinations of the words in the dictionary
    - Space Complexity: O(m^n) where n is the length of the string.
    - Approach: Memoization
        - Create a memoization dictionary
        - Check if the string is in the memo
            - If yes, return the result
        - If the string is empty, return a list with an empty string
        - Iterate over the wordDict
            - Check if the current word is in the string
                - If yes, get the combinations of the rest of the string
                - Append the current word to the combinations
                - Add the combinations to the memo
        - Return the result
    """

    def solution(s: str, wordDict: List[str], memo: dict = {}) -> List[str]:
        if s in memo:
            return memo[s]
        if s == '':
            return ['']
        res = []
        for word in wordDict:
            len_word = len(word)
            if s[: len_word] == word:
                combinations = solution(s[len_word: len(s)], wordDict, memo)
                combinations = [
                    f'{word} {s}' if s else word for s in combinations]
                res.extend(combinations)
        memo[s] = res
        return res
    return solution(s, wordDict)
