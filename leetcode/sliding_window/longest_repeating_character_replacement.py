#!/usr/bin/env python3
"""
Leetcode: 424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/
"""


def characterReplacement(self, s: str, k: int) -> int:
    """
    Sliding window problem.
    A viable window:
        - Window length - most frequent characters must be
        less than k i.e. replaceable characters
    Time complexity: O(n)
    Space complexity: O(k) where k is the number of unique characters
        - maximum size is limited to 26 due alphabetical letters
    Approach:
        - Use a dictionary to store the frequency of characters in the window.
        - Use two pointers l and r to represent the left and right of the window.
        - Increment the count of the character in s2. If the count of the character in s2
          is greater than the frequency of the most frequent character in the window then
          update the most frequent character.
        - If window size - most frequent character is greater than k then remove decrement
          the count of the character from the left of the window and update left pointer to
          restore window size validity.
        - Return the length of the window.
    """
    char_count = {}
    l = 0
    res = 0
    freq = 0

    for r in range(len(s)):

        char_count[s[r]] = char_count.get(s[r], 0) + 1
        freq = max(freq, char_count[s[r]])
        if (r - l + 1) - freq > k:
            char_count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res
