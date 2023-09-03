#!/usr/bin/env python3
"""
Leetcode 125: Valid Palindrome
https://leetcode.com/problems/valid-palindrome/description/
"""

import re


def isPalindrome(s: str) -> bool:
    """
    Time complexity - O(n)
    Space complexity - O(n) - n is the number of characters in s
    Approach: Two pointers
        - Convert the string to lowercase
        - Replace all non alphanumeric characters
        - Use two pointers to track the letters from the beginning and from the end
        - If the letters are not the same, return False
    """
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    i, j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
