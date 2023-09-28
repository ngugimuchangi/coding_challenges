"""
Leetcode 5: Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
Approach: Expand Around Center
    - For each character in the string, we will expand around
      it to find the longest palindrome
    - There are two cases:
        + The length of the palindrome is odd
        + The length of the palindrome is even
Analysis: Time O(n^2) | Space O(n) - n is the length of the string
"""


def longestPalindrome(s: str) -> str:
    start, end = 0, 0
    len_s = len(s)

    def check_and_update_res(left, right):
        l, r = left, right
        while l >= 0 and r < len_s and s[l] == s[r]:
            l, r = l - 1, r + 1
        l += 1
        if r - l > end - start:
            return l, r
        return start, end

    for i in range(len_s):
        start, end = check_and_update_res(i, i)
        start, end = check_and_update_res(i, i + 1)

    return s[start: end]
