#!/usr/bin/env python3
"""
Leetcode 242: Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
"""

from collections import defaultdict
from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """
    Time complexity: `O(n.m(log(m))`
        - `n `is the number of words in the list
        - `m` is the length of the longest string
        - Sorting the letters adds extra time complexity
    Space complexity: O(n)
        - Space grows linearly with the number of elements (words) since
          we allocated more memory for the anagrams

    """
    anagrams = defaultdict(list)
    # iterate over words
    for word in strs:
        # sort the word
        sorted_word = ''.join(sorted(word))
        # append the word to the list of similar
        # anagrams in the dictionary
        anagrams[sorted_word].append(word)
    return list(anagrams.values())


def groupAnagramsTwo(self, strs: List[str]) -> List[List[str]]:
    """
    Time complexity: O(26.n) = O(n) where 
        - n is the number of words
        - 26 is the number of letters in the alphabet
    Space complexity: O(n) where n is the number of words
        - space grows linearly with the number of words
          since we have to allocate more memory for the anagrams
    """
    anagrams = defaultdict(list)
    # iterate over the words
    for word in strs:
        # create an array representing the letters of the alphabet
        count = [0] * 26
        for char in word:
            # Get the count of each character
            count[ord(char) - ord('a')] += 1
        # update the word anagram list
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())
