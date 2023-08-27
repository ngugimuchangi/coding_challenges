#!/usr/bin/env python3
"""
Leetcode 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""

from collections import Counter


def minWindow(s: str, t: str) -> str:
    """
    - Sliding window problem
    - Viable window: contains all characters in t
    - Goal: find the smallest viable window
    - Time complexity: O(n + m) - where n is the length of s and m is the length of t
    - Space complexity: O(1) - considering the hash maps will have at most 26 characters
      leading to constant space complexity
    - Approach:
        - Get the count of characters in t
        - Get expected matches (number of unique characters in t)
        - Initialize matches to 0
        - Keep track of the minimum length of the viable window 
        - Iterate over s:
             - Increment the count of the current character
                - If the current character is in t and the count of the current character
                    is equal to the count of the current character in t, increment matches
                - While matches == expected:
                    - Update the minimum length of the viable window
                    - Update the result
                    - Decrement the count of the character at the left pointer
                    - If the character at the left pointer is in t and the count of the
                        character at the left pointer is less than the count of the
                        character at the left pointer in t, decrement matches
                    - Increment the left pointer
        - Return the result
    """
    char_count_s, char_count_t = {}, Counter(t)
    matches, expected = 0, len(char_count_t)
    res, min_len = [-1, -1], float("infinity")
    l = 0

    for r in range(len(s)):
        c = s[r]
        char_count_s[c] = char_count_s.get(c, 0) + 1
        if c in char_count_t and char_count_s[c] == char_count_t[c]:
            matches += 1
        while matches == expected:
            c = s[l]
            if r - l < min_len:
                res = [l, r]
                min_len = r - l
            if c in char_count_t and char_count_s[c] == char_count_t[c]:
                matches -= 1
            char_count_s[c] -= 1
            l += 1
    l, r = res
    return s[l: r + 1] if min_len != float("infinity") else ""
