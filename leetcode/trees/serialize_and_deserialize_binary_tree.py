"""
Leetcode 297: Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""

import json
from collections import deque
from tree_node import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        data = []

        def dfs_serialize(root):
            if not root:
                data.append(None)
                return
            data.append(root.val)
            dfs_serialize(root.left)
            dfs_serialize(root.right)

        dfs_serialize(root)
        return json.dumps(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(json.loads(data))

        def dfs_deserialize():
            val = data.popleft()
            if val is None:
                return None
            root = TreeNode(val)
            root.left = dfs_deserialize()
            root.right = dfs_deserialize()
            return root
        return dfs_deserialize()
