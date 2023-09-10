"""
Leetcode 139: Word Break
https://leetcode.com/problems/word-break/
For dp solution check `dynamic_programming/word_break.py`
"""
from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def add_word(self, word: str):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.end = True


class Solution:
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        """
        - Time Complexity: O(n*m) where n is the length of the string and m is
          the length of the wordDict
            - Not that creating the trie also take O(n * m) time in the worst case
        - Space Complexity: O(n^2) where n is the length of the string.
            - This is because of the memoization and copying the string in the recursive calls (slicing)
            - It can be reduced to O(n) if we track indices instead of copying the string
        - Approach: Trie + Memoization
            - Build a trie with all the words in the dictionary
            - Use memoization to store the result of the sub-problems
            - Check if the word is in the memo, if yes return the result
            - If the word is empty, return True
            - If the word is not in the trie, return False
            - If the word is in the trie, check if the node is the end of the word
                - If yes, check if the rest of the word is in the trie
                - If yes, return True
            - Else, check if the rest of the word is in the trie
            - Return the result
        """
        trie = Trie()
        memo = {}
        for word in wordDict:
            trie.add_word(word)

        def check_word(node: Trie, s: str, i: int, s_len: int):
            if s in memo:
                return memo[s]
            if s == '':
                return True
            if not node or i == s_len or s[i] not in node.children:
                memo[s] = False
                return memo[s]
            c = s[i]
            node = node.children[c]
            if node.end:
                t = s[i + 1:]
                memo[t] = check_word(trie, t, 0, s_len - i - 1)
                if memo[t]:
                    return memo[t]
            memo[s] = check_word(node, s, i + 1, s_len)
            return memo[s]

        return check_word(trie, s, 0, len(s))
