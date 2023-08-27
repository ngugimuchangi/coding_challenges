#!/urs/bin/env python3
"""
Leetcode: 567. Permutation in String
https://leetcode.com/problems/permutation-in-string/
"""
from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    """
    - Sliding window problem
    - Valid window:
        1. Must be equal to length of s1.
        2. Frequency of characters in the string must match that of s1 character.
    - Time complexity: O(m + n) - where  m is the number of unique characters in s1
      and n is the length of s2. Consider the maximum possible number of unique characters
      in s1 is 26, then the time complexity becomes O(26 + n) which is O(n)
    - Space complexity: O(n) - where n is the number of unique characters in s2.
    Approach:
        - Use a dictionary to store the frequency of characters in s1.
        - Use a dictionary to store the frequency of characters in the window.
        - Use two pointers l and r to represent the left and right of the window.
        - Increment the count of the character in s2.
        - If the count of the character in s2 is equal to the count of the character in s1
          then increment the matches count.
        - If the window size is greater than the length of s1 then remove the character from
          the left of the window and update left pointer.
        - If the count of the character in s2 is one less than the count of the character in s1
          then decrement the matches count. This ensures that the window is still valid
          and avoids decrementing the matches count for characters that are not in s1
        - If the window size is equal to the length of s1 and matches is equal to the number of
          unique characters in s1 then return True.

    """
    char_count = Counter(s1)
    char_count_s2 = {}
    l = 0
    len_s1 = len(s1)

    matches = 0
    expected_matches = len(char_count)

    for r in range(len(s2)):
        char_count_s2[s2[r]] = char_count_s2.get(s2[r], 0) + 1

        if char_count_s2[s2[r]] == char_count.get(s2[r]):
            matches += 1

        if (r - l + 1) > len_s1:
            char_count_s2[s2[l]] -= 1
            if char_count[s2[l]] - char_count_s2[s2[l]] == 1:
                matches -= 1
            l += 1
        if (r - l + 1) == len_s1 and matches == expected_matches:
            return True

    return False


def checkInclusionAlt(self, s1: str, s2: str) -> bool:
    """
    - Sliding window problem
    - Valid window:
        1. Must be equal to length of s1.
        2. Frequency of characters in the string must match that of s1 character.
    - Time complexity: O(n.m) - where n is the number characters in s2 and m is the number of
      unique characters in s1. Consider the maximum possible number of unique characters
      in s1 is 26, then the time complexity becomes O(26.n) which is O(n)

    - Difference from first approach:
        - Instead of using a matches counter, we check if the frequency of characters in the
          window is equal to the frequency of characters in s1. So we don't need to keep
          track of the matches count.
    """
    char_count = Counter(s1)
    char_count_s2 = {}
    l = 0
    len_s1 = len(s1)

    for r in range(len(s2)):
        char_count_s2[s2[r]] = char_count_s2.get(s2[r], 0) + 1
        while (r - l + 1) > len_s1:
            char_count_s2[s2[l]] -= 1
            l += 1
        if (r - l + 1) == len_s1:
            if all(char_count_s2.get(k) == v for k, v in char_count.items()):
                return True
    return False
