"""
Leetcode problem: 14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class Trie:
    """
    Trie
    """

    def __init__(self):
        self.children = {}
        self.end = False

    def add_word(self, word):
        """
        Add word to the trie
        """
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.end = True


def longestCommonPrefix(strs: List[str]) -> str:
    """
    Find the longest common prefix
    Args:
        strs: list of strings
    Returns:
        longest common prefix
    Algorithm:
        1. Create a prefix tree from the strings
        2. While the current node has only one child and is not the end of a word
            - Add the character to the result
            - Move to the next node
        3. Return the result
    """
    res = ''
    tree = node = Trie()
    for s in strs:
        tree.add_word(s)

    while len(node.children) == 1 and not node.end:
        c = list(node.children.keys())[0]
        res += c
        node = node.children[c]
    return res
