"""
Leetcode 1721: Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""

from typing import Optional
from list_node import ListNode


def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: 3 pointers
        - fast pointer moves k steps ahead of slow pointer
        - when fast pointer reaches the end, slow pointer is at the kth node from the start
        - keep track of the previous node of the slow pointer
        - get the first node and the node before it
        - get the second node and the node before it
        - swap the two nodes
            - check if previous nodes are empty and adjust the head pointer
            - swap the nodes next values
    """
    slow = fast = head
    node1 = node1_prev = node2 = node2_prev = None

    # Get the first node and the node before it
    for nodes in range(1, k):
        node1_prev,  fast = fast, fast.next
    node1 = fast

    # Get the second node and the node before it
    while fast.next:
        fast, node2_prev, slow = fast.next, slow, slow.next
    node2 = slow

    # Swap the two nodes
    if node1_prev:
        node1_prev.next = node2
    else:
        head = node2

    if node2_prev:
        node2_prev.next = node1
    else:
        head = node1
    temp = node1.next
    node1.next = node2.next
    node2.next = temp

    return head
