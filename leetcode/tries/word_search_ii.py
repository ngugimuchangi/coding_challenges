"""
Leetcode 212: Word Search II
https://leetcode.com/problems/word-search-ii/
"""

from typing import List


class TrieNode:
    """
    Trie node
    """

    def __init__(self):
        self.children = {}
        self.end = False

    def add_word(self, word: str):
        """
        Add word to the trie
        Args:
            word: word to add
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Find words in the board
    Args:
        board: 2D array of characters
        words: list of words
    Returns:
        list of words found in the board
    Algorithm:
        1. Create a prefix tree from the words
        2. For each cell in the board, search for words
            - Use DFS to search for words
            - If the current cell is not in the trie, return
            - If the current cell is in the trie, add the character to the word
            - If the current cell is the end of a word, add the word to the result
            - Mark the current cell as visited with a special character
            - Search the adjacent cells
            - Mark the current cell as unvisited
    """
    tree = TrieNode()
    res = []
    max_r, max_c = len(board), len(board[0])
    for w in words:
        tree.add_word(w)

    def search(node: TrieNode, r: int, c: int, max_r: int, max_c: int, word: int):
        """
        Search for words in the board
        Args:
            node: TrieNode
            r: current row index
            c: current column index
            max_r: max row index
            max_c: max column index
            word: word history 
        """
        if (r == max_r or c == max_c
            or r < 0 or c < 0
                or board[r][c] not in node.children):
            return

        char = board[r][c]
        word += char
        node = node.children[char]
        if node.end:
            res.append(word)
            node.end = False

        board[r][c] = '#'
        search(node, r + 1, c, max_r, max_c, word)
        search(node, r - 1, c, max_r, max_c, word)
        search(node, r, c + 1, max_r, max_c, word)
        search(node, r, c - 1, max_r, max_c, word)
        board[r][c] = char

    for r in range(max_r):
        for c in range(max_c):
            search(tree, r, c, max_r, max_c, '')
    return res
