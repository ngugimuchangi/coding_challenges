#!/usr/bin/env python3
"""
Leetcode 395. Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""


def longestSubstring(s: str, k: int) -> int:
    """
    - Sliding window problem
    - Valid window:
        1. All characters should have a frequency of >= k
        2. All unique characters in the window should have a frequency of >= k
    - Divide and conquer approach:
        1. Find the character with the lowest frequency
        2. Split the string on that character
        3. Recursively call the function on each substring
        4. Return the max of the recursive calls
    - Time complexity: O(n^2) - O(n) for the for loop and O(n) for the split
    - Space complexity: O(n)
    """
    char_set = set(s)

    for c in char_set:
        if s.count(c) < k:
            return max((longestSubstring(sub_s, k) for sub_s in s.split(c)))
    return len(s)


def longestSubstring(s: str, k: int) -> int:
    """
    - Sliding window problem
    - Valid window:
        1. All characters should have a frequency of >= k 
        2. All unique characters in the window should have a frequency of >= k
    - Time complexity: O(n * m) - where m is the number of unique characters and
      n is the length of the string. Considering that the maximum number of unique
      characters is 26, the time complexity is O(n).
    - Space complexity: O(1) since we allocate maximum 26 characters for the
      char_count array
    - Sliding window approach:
        - Find the total number of unique characters in the string
        - For each window size from 1 to total number of unique characters:
            - Use a sliding window to find the longest substring with at least k
              repeating characters and with exactly window size unique characters
            - Update the result
    """
    char_set = set(s)
    total_unique = len(char_set)
    res = 0
    len_s = len(s)

    for window_unique in range(1, total_unique + 1):
        l = r = 0
        unique = at_least_k = 0
        char_count = [0] * 26

        while r < len_s:
            if unique <= window_unique:
                idx = ord(s[r]) - ord('a')
                if char_count[idx] == 0:
                    unique += 1
                char_count[idx] += 1
                if char_count[idx] == k:
                    at_least_k += 1
                r += 1
            else:
                idx = ord(s[l]) - ord('a')
                if char_count[idx] == k:
                    at_least_k -= 1
                char_count[idx] -= 1
                if char_count[idx] == 0:
                    unique -= 1
                l += 1
            if unique == window_unique and unique == at_least_k:
                res = max(res, r - l)
    return res
