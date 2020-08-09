"""
August 8 Challenge - Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class PathSumIII(object):

    def path_sum_helper(self, node, sum2):
        if not node:
            return 0
        return (1 if node.val == sum2 else 0) + self.path_sum_helper(node.left, sum2 - node.val) + self.path_sum_helper(
            node.right, sum2 - node.val)

    def pathSum(self, root, sum1):
        """
        :param sum1:
        :type root: TreeNode
        :type sum1: int
        :rtype: int
        """

        if not root:
            return 0
        return self.path_sum_helper(root, sum1) + self.pathSum(root.left, sum1) + self.pathSum(root.right, sum1)
