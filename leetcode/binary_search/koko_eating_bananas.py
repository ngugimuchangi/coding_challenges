#!/usr/bin/env python3
"""
Leetcode 875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
"""

import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    - Binary search problem
    - Time: O(nlog(p)) - n is the number of piles, p is the max pile
    - Space: O(1)
    - Algorithm:
        - Max speed is the max pile
        - Use binary search to find the minimum speed
        - If the time taken to eat all the bananas with the current speed is less than
          or equal to h, then update the min speed and search for a lower speed by moving
          to the right half of the search space to look for an even lower speed
        - If the time taken to eat all the bananas with the current speed is greater than
          h, then move to the left half of the search space to look for a higher speed
          that can be used to eat all the bananas in h hours
        - At the end, return the min speed, when l > r
    """
    max_pile = max(piles)
    l, r, min_speed, = 1, max_pile, max_pile

    while l <= r:
        speed = (r + l) // 2
        time = 0
        for pile in piles:
            time += math.ceil(pile / speed)

        if time <= h:
            min_speed = min(min_speed, speed)
            r = speed - 1
        else:
            l = speed + 1
    return min_speed
