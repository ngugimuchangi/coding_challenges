"""
Leetcode 146: LRU Cache
https://leetcode.com/problems/lru-cache/
"""


class Node:
    """
    Node class for doubly linked list
    """

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        """
        Cache class
        Props:
            cache: dictionary of key:node pairs
            capacity: capacity of cache
            count: number of nodes in cache
            left: leftmost node in cache (least recently used)
            right: rightmost node in cache (recently used)
        """
        self.cache = {}
        self.capacity = capacity
        self.count = 0
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node: Node) -> None:
        """
        Insert node in list
        """
        temp = self.right.prev
        self.right.prev, node.next = node, self.right
        node.prev, temp.next = temp, node

    def remove(self, node: Node) -> None:
        """
        Remove node from list
        """
        left, right = node.prev, node.next
        left.next, right.prev = right, left
        node.next = node.prev = None

    def get(self, key: int) -> int:
        """
        Get key from cache
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Add to or edit cache
        """
        if key not in self.cache:
            self.count += 1
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)

        if self.count > self.capacity:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)
            self.count -= 1
