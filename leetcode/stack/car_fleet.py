#!/usr/bin/env python3
"""
Leetcode 853. Car Fleet
https://leetcode.com/problems/car-fleet/
"""
from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    """
    - Stack problem
    - Time complexity: O(nlogn) - sorting takes O(nlogn) time
    - Space complexity: O(n) - n is the number of cars
    - Approach: Stack
        - Use a stack to store the time it takes for each car to reach the target
        - Sort the cars by their position in descending order
        - Iterate through the cars
            - Calculate the time it takes for the car to reach the target
            - If the stack is empty or the time is greater than the top of the
                stack, append the time to the stack (a new fleet is formed)
            - NB: if the time is less or equal to than the top of the stack, the car will
                catch up to the fleet else it will form a new fleet
        - Return the length of the stack
    """
    pos_speed = [(p, s) for p, s in zip(position, speed)]
    t_stack = []

    for p, s in sorted(pos_speed, reverse=True):
        time = (target - p) / s
        if not t_stack or (t_stack and time > t_stack[-1]):
            t_stack.append(time)

    return len(t_stack)
