from typing import List, Optional
from tree_node import TreeNode


def isBalanced(root: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n) - n is the number of node
    Space complexity: O(h) - h is the height of the tree
        - maximum call stack is equal to the height of the tree (height of root)
    Approach: traverse through the nodes comparing the node
    """
    return dfs(root)[0]


def dfs(node: TreeNode) -> List[bool | int]:
    """
    Recursively check if a node is balance or not
    Approach:
        - Leaf nodes are balanced and have a height of 0
        - Internal nodes height is maximum height of its children plus one
        - If the lower subtrees is balance then check for the difference between the left
            and right subtrees heights
        - If difference between right and left node is less than or equal but
            equal to one then the current subtree is balance else return it is not
        - Return the balanced status of the trees and its height - the height is of a node is equal
            to maximum height of its subtree plus one.
    """
    if not node:
        return [True, -1]
    left, right = dfs(node.left), dfs(node.right)
    balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
    return [balanced, max(left[1], right[1]) + 1]
