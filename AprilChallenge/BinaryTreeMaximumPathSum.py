"""
Leetcode Challenge Apr.29

124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


class BinaryTreeMaximumPathSum(object):
    def __init__(self):
        self.global_max = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(root):
            if not root:
                return 0

            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.global_max = max(self.global_max, left + right + root.val)
            return max(left, right) + root.val

        dfs(root)
        return self.global_max
