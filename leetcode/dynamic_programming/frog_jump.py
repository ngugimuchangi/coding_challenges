"""
Leetcode 403. Frog Jump
https://leetcode.com/problems/frog-jump/
"""
from typing import List


def canCross(stones: List[int]) -> bool:
    """
    - Dynamic programming problem
    - Time complexity: O(n^3) - n is the maximum number of stones
    - Space complexity: O(n)
    - Approach: Dynamic programming
        - Use a dictionary to store the possible jumps from each stone
        - The key is the stone and the value is a set of possible jumps
        - The possible jumps from a stone is the union of the possible jumps
            from the previous stones that can reach the current stone
    """
    stones_set = set(stones)
    visited = set()

    def canCrossNext(prev, k):
        stone = prev + k
        if not k or stone not in stones_set or (stone, k) in visited:
            return False
        visited.add((stone, k))
        if stone == stones[-1]:
            return True
        return canCrossNext(stone, k - 1) or canCrossNext(stone, k) or canCrossNext(stone, k + 1)

    return canCrossNext(stones[0], 1)


def canCrossNextTwo(stones: List[int]) -> bool:
    """
    - Dynamic programming problem
    - Time complexity: O(n^3) - n is the maximum number of stones
    - Space complexity: O(n)
    - Approach: Dynamic programming - Memoization
        - Use a dictionary to store the possible jumps from each stone
        - The key is the stone and the value is a set of possible jumps
        - The possible jumps from a stone is the union of the possible jumps
            from the previous stones that can reach the current stone
    """
    stones_set = set(stones)

    def canCrossNext(stone: int, k: int, memo: dict = {}):
        if (stone, k) in memo:
            return memo[(stone, k)]
        if not k or stone not in stones_set:
            return False
        if stone == stones[-1]:
            return True
        for i in range(k - 1, k + 2):
            can_cross = canCrossNext(stone + i, i, memo)
            if can_cross:
                memo[(stone, k)] = True
                return True
        memo[(stone, k)] = False
        return False

    return False if stones[1] - stones[0] > 1 else canCrossNext(stones[1], 1)
