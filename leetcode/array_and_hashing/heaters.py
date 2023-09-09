"""
Leetcode 475: Heaters
https://leetcode.com/problems/heaters/
"""

from typing import List


def findRadius(houses: List[int], heaters: List[int]) -> int:
    """
    Time complexity: O(nlogn) - sorting
    Space complexity: O(1)
    Approach:
        1. Sort the houses and heaters
        2. For each house, find the closest heater on the left and right
        3. Return the maximum distance
    """
    radius = l = r = pos = 0
    len_heaters = len(heaters)
    houses.sort()
    heaters.sort()
    for house in houses:
        while pos < len_heaters - 1 and house >= heaters[pos]:
            pos += 1
        l = abs(house - (heaters[pos - 1] if pos > 0 else heaters[pos]))
        r = abs(house - heaters[pos])
        radius = max(radius, min(l, r))

    return radius
