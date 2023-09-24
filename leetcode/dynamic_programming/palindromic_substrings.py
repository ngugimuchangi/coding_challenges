"""
Leetcode 647: Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
"""


def countSubstrings(s: str) -> int:
    """
    Approach: Expand Around Center
        - For each character in the string, we will expand around
            it to find the longest palindrome
        - We will keep track of the number of palindromes we have
          found so far
        - There are two cases:
            + The length of the palindrome is odd
            + The length of the palindrome is even
    Analysis: Time O(n^2) | Space O(n) - n is the length of the string
    """
    res = 0
    len_s = len(s)

    def count_palindromes(left, right):
        count = 0
        l, r = left, right
        while l >= 0 and r < len_s and s[l] == s[r]:
            l, r = l - 1, r + 1
            count += 1
        return count

    for i in range(len_s):
        res += count_palindromes(i, i)
        res += count_palindromes(i, i + 1)
    return res
