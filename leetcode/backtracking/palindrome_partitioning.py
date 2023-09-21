"""
Leetcode 131: Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/
- Approach: Backtracking
    - Use backtracking to generate all possible substrings
    - Check if a substring is a palindrome
    - If it is, add it to the result
    - If not, backtrack
- Analysis:
    - Time: O(n^2) - n is the length of the string
    - Space: O(n ^ 2)
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    """ Driver function for backtracking """
    res, max_length = [], len(s)
    backtrack(s, 0, [], res, max_length)
    return res


def backtrack(s, start, sub_s, res, max_length):
    """ Backtracking function """
    if start >= max_length:
        res.append(sub_s)
        return
    for i in range(start, max_length):
        if is_palindrome(s, start, i):
            backtrack(s, i + 1, sub_s + [s[start: i + 1]], res, max_length)


def is_palindrome(s, l, r):
    """
    Helper function to check if a
    string is a palindrome
    """
    while l <= r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True
