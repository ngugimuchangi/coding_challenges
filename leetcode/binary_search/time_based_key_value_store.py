#!/usr/bin/env python3
"""
Leetcode 981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/
"""

from collections import defaultdict


class TimeMap:
    """
    Time-based key-value store
    """

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        - Binary search problem
        """
        res, vals = "", self.store.get(key) or []
        l, r = 0, len(vals) - 1

        while l <= r:
            m = l + (r - l) // 2
            t_stamp, val = vals[m]

            if t_stamp > timestamp:
                r = m - 1
            else:
                res = val
                l = m + 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
