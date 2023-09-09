"""
Leetcode 403. Frog Jump
https://leetcode.com/problems/frog-jump/
"""
from typing import List


def canCross(stones: List[int]) -> bool:
    """
    - Dynamic programming problem
    - Time complexity: O(n^2) - n is the length of the stones
    - Space complexity: O(n^2) - n is the length of the stones
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
        # k == 0 is not allowed because the frog must jump forward
        # stone not in stones_set is not allowed because the frog must jump to a stone
        # (stone, k) in visited is not allowed because the frog must not visit the same stone with the same jump size
        # reduces the time complexity from O(n^3) to O(n^2)
        if not k or stone not in stones_set or (stone, k) in visited:
            return False
        visited.add((stone, k))
        if stone == stones[-1]:
            return True
        return canCrossNext(stone, k - 1) or canCrossNext(stone, k) or canCrossNext(stone, k + 1)

    return canCrossNext(stones[0], 1)
