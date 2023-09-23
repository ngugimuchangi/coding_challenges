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
    res = ''
    len_s, res_len = len(s), 0

    def check_and_update_res(mid, odd=True):
        nonlocal res, res_len
        l, r = mid, mid if odd else mid + 1
        while l >= 0 and r < len_s and s[l] == s[r]:
            l, r = l - 1, r + 1
        if r - l + 1 > res_len:
            res = s[l + 1: r]
            res_len = r - l + 1

    for i in range(len_s):
        check_and_update_res(i, odd=True)
        check_and_update_res(i, odd=False)

    return res
