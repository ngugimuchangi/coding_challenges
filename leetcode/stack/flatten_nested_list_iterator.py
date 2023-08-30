# /usr/bin/python3
"""
Leetcode 341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
#
"""

from collections import deque


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> ['NestedInteger']:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = self.build_queue(nestedList)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return bool(self.queue)

    def build_queue(self, nestedList: [NestedInteger]):
        queue = deque()
        for item in nestedList:
            if item.isInteger():
                queue.append(item.getInteger())
            else:
                queue.extend(self.build_queue(item.getList()))
        return queue


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
