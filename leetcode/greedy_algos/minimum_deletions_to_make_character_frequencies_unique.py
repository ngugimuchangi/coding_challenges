"""
Leetcode 1647: Minimum Deletions to Make Character Frequencies Unique
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""
from collections import Counter


def minDeletions(s: str) -> int:
    """
    Time: O(n)
    Space: O(n)
    Approach: Use a set to keep track of the unique frequencies.
        - If the frequency is already in the set, decrement the frequency
          until it is not in the set.
        - Add the frequency to the set.
    """
    char_count = Counter(s)
    unique_freq = set()
    deletions = 0

    for count in char_count.values():
        while count and count in unique_freq:
            count -= 1
            deletions += 1
        unique_freq.add(count)
    return deletions
