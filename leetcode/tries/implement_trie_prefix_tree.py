"""
Leetcode 208: Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class TrieNode:
    """
    Trie node
    """

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    """
    Trie
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert word to the trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Search for word in the trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Check for prefix in the trie
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
