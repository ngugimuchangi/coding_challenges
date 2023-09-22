"""
Leetcode 392: Is Subsequence
https://leetcode.com/problems/is-subsequence/
Approach: Two Pointers
    - Iterate through the string t
    - If the current character is equal to the current character in s, increment s_index
    - If s_index is equal to the length of s, return True
    - Return False
Analysis: Time: O(n) | Space: O(1) - n is the length of t
"""


def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return True
    s_index = 0
    for i in range(len(t)):
        if t[i] == s[s_index]:
            s_index += 1
        if s_index == len(s):
            return True
    return False
