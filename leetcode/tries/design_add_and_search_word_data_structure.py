"""
Leetcode: 211. Design Add and Search Words Data Structure
https://leetcode.com/problems/design-add-and-search-words-data-structure/
"""


class TrieNode:
    """
    Trie node
    """

    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    """
    Word dictionary
    """

    def __init__(self):
        self.start = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Add word to the tree
        """
        node = self.start
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Search for word in the tree
        """
        def _search(node: TrieNode, word: str, index: int, length: int) -> bool:
            if index == length:
                return node.end
            c = word[index]
            if c != '.':
                if c not in node.children:
                    return False
                else:
                    return _search(node.children[c], word, index + 1, length)
            else:
                for child in node.children.values():
                    if _search(child, word, index + 1, length):
                        return True
            return False
        return _search(self.start, word, 0, len(word))
