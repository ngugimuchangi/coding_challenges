"""
Leetcode 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
"""
from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    """
    Short and sweet solution
    Time complexity: O(n)
    Space complexity: O(n)
    Approach: Hash table
    """
    s_count = Counter(s)
    t_count = Counter(t)

    return s_count == t_count


def isValidAnagram(s: str, t: str) -> bool:
    """
    Longer solution
    Time complexity: O(n)
    Space complexity: O(n)
    Approach: Hash table
    """
    s_count = Counter(s)
    for c in t:
        if c not in s_count:
            return False
        s_count[c] -= 1

    return all(count == 0 for count in s_count.values())
