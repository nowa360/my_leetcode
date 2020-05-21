"""
May 20 Challenge - 230. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Constraints:
- The number of elements of the BST is between 1 to 10^4.
- You may assume k is always valid, 1<=k<= bst's total elements
"""


class KSmallestBst:

    def __init__(self):
        self.stack = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def do_dfs(node):
            if node and node.left:
                do_dfs(node.left)
            if node:
                self.stack.append(node.val)
            if node and node.right:
                do_dfs(node.right)

        do_dfs(root)
        return self.stack[k - 1]