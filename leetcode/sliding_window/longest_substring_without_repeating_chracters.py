#!/usr/bin/env python3

def lengthOfLongestSubstring(s: str) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    Approach:
        - Add contiguous unique characters to a set until there's a duplicate
        - Compute max length by obtaining difference between left and right pointers
        - Remove leading characters upto the duplicate when encountered
    """
    max_length = 0
    len_s = len(s)
    l = 0
    char_set = set()
    for r in range(len(s)):
        c = s[r]
        while c in char_set:
            char_set.discard(s[l])
            l += 1
        char_set.add(c)
        max_length = max(max_length, r - l + 1)
    return max_length
