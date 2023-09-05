
from typing import List, Optional
from list_node import ListNode


def mergeKListsOne(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time complexity: O(n.k)
    Space complexity: O(1)
    Algorithm: Iterative merge
      - merge two lists at a time
    """
    res, l1 = ListNode(), None

    for l2 in lists:
        res = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 or l2
        l1 = res.next
    return res.next


def mergeKListsTwo(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    More efficient than mergeKListsOne
    Time complexity: O(n.log(k)) - n is the total number of nodes in two lists,
        - k is the number of lists
    Space complexity: O(k) - space allocated depend on the number of lists i.e. k
    Algorithm: Divide and Conquer
        - merge two lists at a time
        - merge the merged lists
        - repeat until there is only one list
        - return the merged list
        - Similar to merge sort
    """

    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            merged_lists.append(merge(l1, l2))
        lists = merged_lists

    return lists[0]


def merge(list1: Optional[ListNode], list2: Optional[ListNode]):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    Algorithm: Iterative merge
      - merge two lists at a time
    """
    l1, l2 = list1, list2
    res = curr = ListNode()

    while l1 and l2:
        if l1.val < l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    curr.next = l1 or l2

    return res.next
