"""
Leetcode 91: Decode Ways
https://leetcode.com/problems/decode-ways/
"""


def numDecodings(s: str) -> int:
    """
    Tabulation Approach
        - Iterate through the string, keeping track of the number of ways to decode
        - If previous number of ways is not 0, then add it to the current number
          of ways
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n)
    """
    ref = {str(i) for i in range(1, 27)}
    len_s = len(s)
    ways = [int(not i) for i in range(len_s + 1)]

    for left in range(len_s):
        prev_ways, right = ways[left], left + 1

        if prev_ways and s[left: right] in ref:
            ways[right] += prev_ways
        right += 1
        if right <= len_s and prev_ways and s[left: right] in ref:
            ways[right] += prev_ways
    return ways[len_s]


def numDecodings(s: str) -> int:
    """
    Recursive approach with memoization
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n)
    """
    ref = {str(i) for i in range(1, 27)}
    len_s = len(s)
    memo = {}

    def decode_ways(index: int) -> int:
        res = 0
        if index in memo:
            return memo[index]
        if index > len_s:
            return 0
        if index == len_s:
            return 1

        res += decode_ways(index + 1) if s[index: index + 1] in ref else 0
        res += decode_ways(index + 2) if s[index: index + 2] in ref else 0
        memo[index] = res
        return res
    return decode_ways(0)
